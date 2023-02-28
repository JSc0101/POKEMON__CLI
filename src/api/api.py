"""API."""
import requests
from PIL import Image
import os
import time
import ascii_magic
from message import stats_pokemon

URL_API = 'https://pokeapi.co/api/v2/pokemon/'
IMAGE_FILE = 'pokemon.png'


def get_pokemon_data(name: str) -> dict:
    """GET /"""
    try:
        url = f'{URL_API}{name.lower()}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, ValueError) as error_request:
        print(
            f'error de la solicitud a la ruta: {url}: error: {error_request}')
        return None


def pokemon_image(pokemon__data):
    """image pokemon."""
    try:
        sprites__url = pokemon__data["sprites"]["front_default"]
        response = requests.get(sprites__url, timeout=10)
        with open(IMAGE_FILE, 'wb') as file:
            file.write(response.content)
        os.chmod(IMAGE_FILE, 0o755)
        time.sleep(0.5)
    except (requests.exceptions.RequestException, IOError) as error_image:
        print(f"error al cafgar la imagen {error_image}")


def show_pokemon_ascii(pokemon_data):
    try:
        with Image.open(IMAGE_FILE) as image:
            ascii_pokemon = ascii_magic.from_image(IMAGE_FILE)
            # terminal image
            ascii_pokemon.to_terminal(columns=120, with_ratio=3)
            stats_pokemon(pokemon_data)
    except Exception as e:
        print(f"error loading image {e}")
