import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_init_valid_name(self):
        a = TrapCard('a')
        res = a.name
        exp = 'a'
        self.assertEqual(res, exp)

    def test_init_invalid_name(self):
        try:
            a = TrapCard('')
        except ValueError:
            self.assertRaises(ValueError)

    def test_valid_health_points(self):
        a = TrapCard('a')
        res = a.health_points
        exp = 5
        self.assertEqual(res, exp)

    def test_invalid_health_points(self):
        try:
            a = TrapCard('a', -50)
        except TypeError:
            self.assertRaises(TypeError)

    def test_valid_dmg_points(self):
        a = TrapCard('a')
        res = a.damage_points
        exp = 120
        self.assertEqual(res, exp)

    def test_invalid_dmg_points(self):
        try:
            a = TrapCard('a', -50)
        except TypeError:
            self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
