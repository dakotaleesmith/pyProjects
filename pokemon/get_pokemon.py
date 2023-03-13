import json

import duckdb
import typer
from rich import print

POKEDATA_FILEPATH = "data/pokedata.json"
TYPES_EFF_FILEPATH = "data/types_parsed_long.csv"

app = typer.Typer()


def _validate_pokemon(name: str) -> bool:
    with open(POKEDATA_FILEPATH, "r") as f:
        data = json.load(f)
    return name in [i.get("name") for i in data]


def _get_types_query(name: str) -> str:
    assert _validate_pokemon(name), "Pokemon name not found. Try checking the spelling."
    return f"""
    SELECT types
    FROM "{POKEDATA_FILEPATH}" 
    WHERE name = '{name}'
    ;
    """


def _get_type_effectiveness_query(types: list) -> str:
    if len(types) > 1:
        select_stmt = """
        SELECT
            type1.opposing_type
            , COALESCE(type1.effectiveness_multiplier * type2.effectiveness_multiplier, 0) AS effectiveness
        FROM type_eff AS type1
        INNER JOIN type_eff AS type2
            ON type1.opposing_type = type2.opposing_type
            AND type1.type != type2.type
        GROUP BY 1, 2
        HAVING effectiveness != 1.00
        ORDER BY effectiveness DESC, type1.opposing_type
        """
    else:
        select_stmt = """
        SELECT
            type1.opposing_type
            , COALESCE(type1.effectiveness_multiplier, 0) AS effectiveness
        FROM type_eff AS type1
        GROUP BY 1, 2
        HAVING effectiveness != 1.00
        ORDER BY effectiveness DESC, type1.opposing_type
        """
    return f"""
    WITH type_eff AS (
        SELECT * 
        FROM "{TYPES_EFF_FILEPATH}" 
        WHERE type IN {tuple(types)}
    )

    {select_stmt}
    ;
    """


def _get_pokemon_types(name: str) -> duckdb.DuckDBPyRelation:
    query = _get_types_query(name)
    return duckdb.sql(query).fetchone()[0]


def _get_pokemon_type_eff(types: list) -> list:
    query = _get_type_effectiveness_query(types)
    return duckdb.sql(query).fetchall()


def _format_results(type_eff: list) -> None:
    formatted_results = ""
    POKETYPE_ALIGNMENT = len(max([i[0] for i in type_eff], key=len))
    for i in type_eff:
        poketype, effectiveness = i[0], i[1]
        relationships = {
            "no_damage":"NO DAMAGE from",
            "resistant":"RESISTANT against",
            "weak":"WEAK to"
        }
        if effectiveness == 0.0:
            relationship = relationships["no_damage"]
        elif effectiveness < 1.0:
            relationship = relationships["resistant"]
        else:
            relationship = relationships["weak"]
        REL_ALIGNMENT = len(max(list(relationships.values()), key=len))
        formatted_results += f"{relationship:<{REL_ALIGNMENT}} {poketype.title():<{POKETYPE_ALIGNMENT}}: {effectiveness}\n"
    return formatted_results


@app.command()
def get_pokemon_type_effectiveness(name: str) -> None:
    types = _get_pokemon_types(name)
    type_eff = _get_pokemon_type_eff(types)
    results = _format_results(type_eff)
    print(f"\n{results}")


if __name__ == "__main__":
    app()
