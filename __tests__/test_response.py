""".test"""
from unittest import mock, TestCase
from src.api import api


class TestResponsePokemon(TestCase):
    """Function"""

    def test_validate_status_error(self):
        """.status fail"""
        response = mock.Mock(status_code=404)
        pokemon_name = 'mewtwo'
        self.assertFalse(api.check_response_pokemon(response, pokemon_name))

    def test_validate_status_good(self):
        """status.validate"""
        response = mock.Mock(status_code=200)
        pokemon_name = 'mew'
        self.assertTrue(api.check_response_pokemon(response, pokemon_name))
