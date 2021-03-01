import unittest

from project.card.magic_card import MagicCard


class MagicCardTest(unittest.TestCase):
    def test_init_name(self):
        card = MagicCard('a')
        act = card.name
        exp = 'a'
        self.assertEqual(exp, act)

    def test_init_dmg_points_5(self):
        card = MagicCard('a')
        act = card.damage_points
        exp = 5
        self.assertEqual(exp, act)

    def test_init_health_points_80(self):
        card = MagicCard('a')
        act = card.health_points
        exp = 80
        self.assertEqual(exp, act)

    def test_init_with_empty_name(self):
        try:
            card = MagicCard('')
        except:
            self.assertRaises(ValueError)

    def test_init_with_negative_dmg_points(self):
        try:
            card = MagicCard(name='a')
        except:
            self.assertRaises(ValueError)

    def test_init_with_negative_HP(self):
        try:
            card = MagicCard(name='a')
        except:
            self.assertRaises(ValueError)
