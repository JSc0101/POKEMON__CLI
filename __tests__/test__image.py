"""TEST."""
import os
import unittest
from src.api import api

IMAGE_FILE = 'pokemon.png'


class GetImagePokemon(unittest.TestCase):
    """.IMAGE"""

    def setUp(self):
        self.pokemon__data = {
            "sprites": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png"
            }
        }

    def test_image_download(self):
        """Validate image"""
        api.pokemon_image(self.pokemon__data)
        self.assertTrue(os.path.exists(IMAGE_FILE))

    def tearDown(self):
        if os.path.exists(IMAGE_FILE):
            os.remove(IMAGE_FILE)
