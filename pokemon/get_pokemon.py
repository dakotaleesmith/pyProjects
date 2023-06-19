import json

import duckdb
import typer
from rich import print

POKEDATA_FILEPATH = "/Users/dakotaleesmith/pyProjects/pokemon/data/pokedata.json"
TYPES_EFF_FILEPATH = "/Users/dakotaleesmith/pyProjects/pokemon/data/types_parsed_long.csv"


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


def _get_pokemon_types(name: str) -> list:
    query = _get_types_query(name)
    return duckdb.sql(query).fetchone()[0]


def _get_pokemon_type_eff(types: list) -> list:
    query = _get_type_effectiveness_query(types)
    return duckdb.sql(query).fetchall()


def _format_results(type_eff: list) -> None:
    formatted_results = ""
    POKETYPE_ALIGNMENT = len(max([i[0] for i in type_eff], key=len))
    relationships = {
        "no_damage": "NO DAMAGE from",
        "resistant": "RESISTANT against",
        "weak": "WEAK to",
    }
    for i in type_eff:
        poketype, effectiveness = i[0], i[1]
        if effectiveness == 0.0:
            relationship = relationships["no_damage"]
        elif effectiveness < 1.0:
            relationship = relationships["resistant"]
        else:
            relationship = relationships["weak"]
        REL_ALIGNMENT = len(max(list(relationships.values()), key=len))
        formatted_results += f"{relationship:<{REL_ALIGNMENT}} {poketype.title():<{POKETYPE_ALIGNMENT}}: {effectiveness}\n"
    return formatted_results


def get_pokemon_type_effectiveness(
    name: str,
    tera: str = typer.Option("", help="Tera type of Pokemon, if terastallized.")
):
    if tera:
        query = f"""
        SELECT opposing_type, effectiveness_multiplier
        FROM "{TYPES_EFF_FILEPATH}"
        WHERE 
            type = '{tera}'
            AND effectiveness_multiplier != 1.00
        ORDER BY effectiveness_multiplier DESC, opposing_type
        ;
        """
        type_eff = duckdb.sql(query).fetchall()
    else:
        types = _get_pokemon_types(name)
        type_eff = _get_pokemon_type_eff(types)
    results = _format_results(type_eff)
    print(f"\n{results}")


if __name__ == "__main__":
    typer.run(get_pokemon_type_effectiveness)
