from rich import print
import typer
import json

app = typer.Typer()

def _get_pokemon(name: str) -> dict:
    fp = '/Users/dakotaleesmith/pyProjects/pokemon/production_pokedata.json'
    with open(fp, 'r') as f:
        data = json.load(f)
        pokemon = [i for i in data if i.get('name') == name]
        return pokemon[0]

@app.command()
def get_pokemon_type_effectiveness(name: str):
    pokemon_data = _get_pokemon(name)
    types = pokemon_data.get('types')
    types_data_fp = '/Users/dakotaleesmith/pyProjects/pokemon/types_parsed.json'
    with open(types_data_fp, 'r') as f:
        types_data = json.load(f)

    print(f'\nPOKEDATA TYPE EFFECTIVENESS FOR: {name.title()}')
    print(f'TYPES: {[t.title() for t in types]}')
    for type in types:
        effectiveness = types_data.get(type)
        print(f'\n{type.upper()}')
        for k, v in effectiveness.items():
            damage_relation = k.replace('_', ' ').title()
            print(f'\t{damage_relation}:')
            print(f'\t{[t.title() for t in v]}')
        


if __name__ == '__main__':
    app()