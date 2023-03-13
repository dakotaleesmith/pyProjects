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
        FROM types_eff AS type1
        INNER JOIN types_eff AS type2
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
        FROM types_eff AS type1
        GROUP BY 1, 2
        HAVING effectiveness != 1.00
        ORDER BY effectiveness DESC, type1.opposing_type
        """
    return f"""
    WITH types_eff AS (
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


def _get_pokemon_type_eff(types: list) -> duckdb.DuckDBPyRelation:
    query = _get_type_effectiveness_query(types)
    return duckdb.sql(query)


@app.command()
def get_pokemon_type_effectiveness(name: str):
    types = _get_pokemon_types(name)
    results = _get_pokemon_type_eff(types)
    print(results)


if __name__ == "__main__":
    app()
