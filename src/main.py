"""MESSAGE"""
import requests
from api import api

EXIT = 'exit'
LIST = 'all'

if __name__ == '__main__':
    while True:
        pokemon_name = input("Ingresa el nombre de un pokemon: ").lower().strip()
        if pokemon_name == EXIT:
            break
        elif pokemon_name == LIST:
          api.show_all_pokemon()
          print()
          continue
        response = requests.get(api.URL_API + pokemon_name, timeout=10)
        if api.check_response_pokemon(response, pokemon_name):
            print()
            pokemon_data = api.get_pokemon_data(pokemon_name)
            api.pokemon_image(pokemon_data)
            api.show_pokemon_ascii(pokemon_data)