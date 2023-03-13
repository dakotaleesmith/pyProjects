import duckdb
from rich import print
import typer

app = typer.Typer()


def _get_types_query(name: str) -> str:
    return f"""
    SELECT types
    FROM "data/pokedata.json" 
    WHERE name = '{name}'
    ;
    """


def _get_type_effectiveness_query(types: list) -> str:
    if len(types) > 1:
        select_stmt = """
        SELECT
            protag.opposing_type
            , COALESCE(protag.effectiveness_multiplier * antag.effectiveness_multiplier, 0) AS effectiveness
        FROM types_eff AS protag
        INNER JOIN types_eff AS antag
            ON protag.opposing_type = antag.opposing_type
            AND protag.type != antag.type
        GROUP BY 1, 2
        HAVING effectiveness != 1.00
        ORDER BY effectiveness DESC, protag.opposing_type
        """
    else:
        select_stmt = """
        SELECT
            protag.opposing_type
            , COALESCE(protag.effectiveness_multiplier, 0) AS effectiveness
        FROM types_eff AS protag
        GROUP BY 1, 2
        HAVING effectiveness != 1.00
        ORDER BY effectiveness DESC, protag.opposing_type
        """

    return f"""
    WITH types_eff AS (
        SELECT * 
        FROM "data/types_parsed_long.csv" 
        WHERE type IN {tuple(types)}
    )

    {select_stmt}
    ;
    """


@app.command()
def get_pokemon_type_effectiveness(name: str):
    types_query = _get_types_query(name)
    types = duckdb.sql(types_query).fetchone()[0]

    type_effectiveness_query = _get_type_effectiveness_query(types)
    type_effectiveness = duckdb.sql(type_effectiveness_query)

    print(type_effectiveness)


if __name__ == "__main__":
    app()
