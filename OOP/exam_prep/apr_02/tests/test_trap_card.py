import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    name = 'Name'
    dp = 120
    hp = 5

    def setUp(self) -> None:
        self.card = TrapCard(self.name)

    def test_init(self):
        self.assertEqual(self.name, self.card.name)
        self.assertEqual(self.dp, self.card.damage_points)
        self.assertEqual(self.hp, self.card.health_points)

    def test_name__when_empty__should_raise(self):
        with self.assertRaises(ValueError) as exc:
            TrapCard('')
        msg = "Card's name cannot be an empty string."
        self.assertEqual(msg, str(exc.exception))

    def test_dp__when_negative_should_raise(self):
        with self.assertRaises(ValueError) as exc:
            self.card.damage_points = -1
        msg = "Card's damage points cannot be less than zero."
        self.assertEqual(msg, str(exc.exception))

    def test_hp__when_negative__should_raise(self):
        with self.assertRaises(ValueError) as exc:
            self.card.health_points = -1
        msg = "Card's HP cannot be less than zero."
        self.assertEqual(msg, str(exc.exception))


if __name__ == '__main__':
    unittest.main()
