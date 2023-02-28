"""Message."""
from colorama import Fore


def stats_pokemon(pokemon_data):
    # Stast pokemon
    print(f"name: {pokemon_data['name']}")
    print(f"HP: {pokemon_data['stats'][0]['base_stat']}")
    print(f"type: {pokemon_data['types'][0]['type']['name']}")
    for ability in pokemon_data["abilities"]:
        print("", ability["ability"]["name"])