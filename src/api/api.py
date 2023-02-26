import requests

url = 'https://pokeapi.co/api/v2/pokemon/'


def get__pokemon__data(name: str):
    """GET /"""
    response = requests.get(f'{url}{name.lower()}')
    response.raise_for_status()
    return response.json()


