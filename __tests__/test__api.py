"""unittest."""
import unittest
from src.api import api


class TestingApi(unittest.TestCase):
    """test."""

    def test__api__type__string(self):
        """Testing type of date."""
        api__url = api.url
        self.assertEqual(type(api__url), str)

    def test__url__api(self):
        """Testing url."""
        api__url = api.url
        self.assertEqual(api__url, "https://pokeapi.co/api/v2/pokemon/")


if __name__ == '__main__':
    unittest.main()
