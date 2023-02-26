"""TEST."""
import unittest
import requests
from src.api import api


class GetPokemon(unittest.TestCase):
    """TEST.POKEMON"""

    def test_pokemon_data_type(self):
        """TYPE: DICT."""
        result = api.get_pokemon_data('lucario')
        self.assertIsInstance(result, dict)

    def test_pokemon_invalid_name(self):
        """ERROR."""
        with self.assertRaises(requests.exceptions.HTTPError):
            api.get_pokemon_data('invalid-pokemon-name')
