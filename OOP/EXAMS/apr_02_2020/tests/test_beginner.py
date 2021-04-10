import unittest

from project.card.card_repository import CardRepository
from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    name = 'Name'

    def setUp(self) -> None:
        self.pl = Beginner(self.name)

    def test_valid_init(self):
        self.assertEqual(self.name, self.pl.username)
        self.assertEqual(50, self.pl.health)
        self.assertIsInstance(self.pl.card_repository, CardRepository)  # Could be issue
        self.assertFalse(self.pl.is_dead)

    def test_username__when_empty__should_raise(self):
        with self.assertRaises(ValueError) as exc:
            Beginner('')
        msg = "Player's username cannot be an empty string."  # Could be issue
        self.assertEqual(msg, str(exc.exception))

    def test_health__when_negative__should_raise(self):
        with self.assertRaises(ValueError) as exc:
            self.pl.health = -1
        msg = "Player's health bonus cannot be less than zero."  # Could be issue
        self.assertEqual(msg, str(exc.exception))

    def test_is_dead__when_health_is_0__should_set_to_true(self):
        self.pl.take_damage(50)
        self.assertTrue(self.pl.is_dead)

    # def test_is_dead__when_health_is_negative__should_set_to_true(self):
    #     self.pl.take_damage(251)
    #     self.assertTrue(self.pl.is_dead)

    def test_take_dmg__when_1__should_decrease_health_by_1(self):
        self.pl.take_damage(1)
        self.assertEqual(49, self.pl.health)

    def test_take_dmg__when_negative__should_raise(self):
        with self.assertRaises(ValueError) as exc:
            self.pl.take_damage(-1)
        msg = "Damage points cannot be less than zero."
        self.assertEqual(msg, str(exc.exception))


if __name__ == '__main__':
    unittest.main()
