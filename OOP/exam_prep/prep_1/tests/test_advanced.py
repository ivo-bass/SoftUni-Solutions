import unittest

from project.card.card_repository import CardRepository
from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def test_init_valid_username(self):
        a = Advanced('a')
        res = a.username
        exp = 'a'
        self.assertEqual(res, exp)

    def test_init_invalid_username(self):
        try:
            a = Advanced('')
        except ValueError:
            self.assertRaises(ValueError, msg="Player's username cannot be an empty string. ")

    def test_valid_health(self):
        a = Advanced('a')
        res = a.health
        exp = 250
        self.assertEqual(res, exp)

    def test_invalid_health(self):
        try:
            a = Advanced('a', -50)
        except TypeError:
            self.assertRaises(TypeError)

    def test_card_repository(self):
        a = Advanced('a')
        res = a.card_repository
        self.assertIsInstance(res, CardRepository)

    def test_is_dead_not_dead(self):
        a = Advanced('a')
        res = a.is_dead
        exp = False
        self.assertEqual(res, exp)

    def test_is_dead_is_dead(self):
        a = Advanced('a')
        a.take_damage(250)
        res = a.is_dead
        exp = True
        self.assertEqual(res, exp)

    def test_is_dead_is_dead_with_negative_left(self):
        a = Advanced('a')
        try:
            a.take_damage(300)
        except ValueError:
            self.assertRaises(ValueError)

    def test_take_valid_dmg(self):
        a = Advanced('a')
        a.take_damage(50)
        res = a.health
        exp = 200
        self.assertEqual(res, exp)

    def test_invalid_dmg(self):
        a = Advanced('a')
        try:
            a.take_damage(-50)
        except ValueError:
            self.assertRaises(ValueError, msg="Damage points cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()
