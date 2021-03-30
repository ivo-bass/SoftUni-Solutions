import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_init_valid_name(self):
        a = MagicCard('a')
        res = a.name
        exp = 'a'
        self.assertEqual(res, exp)

    def test_init_invalid_name(self):
        try:
            a = MagicCard('')
        except ValueError:
            self.assertRaises(ValueError)

    def test_valid_health_points(self):
        a = MagicCard('a')
        res = a.health_points
        exp = 80
        self.assertEqual(res, exp)

    def test_invalid_health_points(self):
        try:
            a = MagicCard('a', -50)
        except TypeError:
            self.assertRaises(TypeError)

    def test_valid_dmg_points(self):
        a = MagicCard('a')
        res = a.damage_points
        exp = 5
        self.assertEqual(res, exp)

    def test_invalid_dmg_points(self):
        try:
            a = MagicCard('a', -50)
        except TypeError:
            self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
