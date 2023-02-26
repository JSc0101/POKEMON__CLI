"""unittest."""
import unittest
from src.api import api


class TestingApi(unittest.TestCase):
    """test."""

    def test_api_type_string(self):
        """Testing type of date."""
        api__url = api.url
        self.assertEqual(type(api__url), str)

    def test_url_api(self):
        """Testing url."""
        api__url = api.url
        self.assertEqual(api__url, "https://pokeapi.co/api/v2/pokemon/")
