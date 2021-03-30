import unittest

from project.card.card_repository import CardRepository
from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def test_init_valid_username(self):
        a = Beginner('a')
        res = a.username
        exp = 'a'
        self.assertEqual(res, exp)

    def test_init_invalid_username(self):
        try:
            a = Beginner('')
        except ValueError:
            self.assertRaises(ValueError, msg="Player's username cannot be an empty string. ")

    def test_valid_health(self):
        a = Beginner('a')
        res = a.health
        exp = 50
        self.assertEqual(res, exp)

    def test_invalid_health(self):
        try:
            a = Beginner('a', -50)
        except TypeError:
            self.assertRaises(TypeError)

    def test_card_repository(self):
        a = Beginner('a')
        res = a.card_repository
        self.assertIsInstance(res, CardRepository)

    def test_is_dead_not_dead(self):
        a = Beginner('a')
        res = a.is_dead
        exp = False
        self.assertEqual(res, exp)

    def test_is_dead_is_dead_with_0_left(self):
        a = Beginner('a')
        a.take_damage(50)
        res = a.is_dead
        exp = True
        self.assertEqual(res, exp)

    def test_is_dead_is_dead_with_negative_left(self):
        a = Beginner('a')
        try:
            a.take_damage(250)
        except ValueError:
            self.assertRaises(ValueError)

    def test_take_valid_dmg(self):
        a = Beginner('a')
        a.take_damage(10)
        res = a.health
        exp = 40
        self.assertEqual(res, exp)

    def test_invalid_dmg(self):
        a = Beginner('a')
        try:
            a.take_damage(-50)
        except ValueError:
            self.assertRaises(ValueError, msg="Damage points cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()
