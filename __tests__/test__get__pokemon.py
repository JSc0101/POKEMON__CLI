import unittest
import requests
from src.api import api


class GetPokemon(unittest.TestCase):

    def test__pokemon__data__type(self):
        """TYPE: DICT."""
        result = api.get__pokemon__data('lucario')
        self.assertIsInstance(result, dict)

    def test__pokemon__invalid__name(self):
        """ERROR."""
        with self.assertRaises(requests.exceptions.HTTPError):
            api.get__pokemon__data('invalid-pokemon-name')
                
