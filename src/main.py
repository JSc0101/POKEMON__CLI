"""MESSAGE"""
import requests
from api import api

EXIT = 'exit'
LIST = 'all'

# manejamos que esto se ejecute como modulo princiapll de la aplicacion
if __name__ == '__main__':
    # mantemos un entorno de ejecucion activo
    while True:
        pokemon_name = input("Ingresa el nombre de un pokemon: ").lower().strip()
        # validamos si el usuario no quiere mantener ese servidor activo
        if pokemon_name == EXIT:
            break
        # si desea ver toda la lista de los pokemon
        elif pokemon_name == LIST:
          api.show_all_pokemon()
          print()
          continue
        # aqui hacemos la petición
        response = requests.get(api.URL_API + pokemon_name, timeout=10)
        # les pasamos la respuesta mas el nombre de la petición
        if api.check_response_pokemon(response, pokemon_name):
            print()
            pokemon_data = api.get_pokemon_data(pokemon_name)
            api.pokemon_image(pokemon_data)
            api.show_pokemon_ascii(pokemon_data)