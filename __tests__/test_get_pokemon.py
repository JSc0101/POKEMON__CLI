"""TEST."""
from src.api import api
import unittest


class GetPokemon(unittest.TestCase):
    """TEST.POKEMON"""

    def test_pokemon_data_type(self):
        """TYPE: DICT."""
        result = api.get_pokemon_data('lucario')
        self.assertIsInstance(result, dict)