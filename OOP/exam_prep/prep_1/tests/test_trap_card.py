import unittest

from OOP.exam_prep.prep_1.project.card.trap_card import TrapCard


class TrapCardTest(unittest.TestCase):
    def test_init_name(self):
        card = TrapCard('a')
        act = card.name
        exp = 'a'
        self.assertEqual(act, exp)

    def test_init_dmg_points_120(self):
        card = TrapCard('a')
        act = card.damage_points
        exp = 120
        self.assertEqual(act, exp)

    def test_init_health_points_5(self):
        card = TrapCard('a')
        act = card.health_points
        exp = 5
        self.assertEqual(act, exp)

    def test_init_with_empty_name(self):
        try:
            card = TrapCard('')
        except:
            self.assertRaises(ValueError)

    def test_init_with_negative_dmg_points(self):
        try:
            card = TrapCard(name='a', damage_points=-1)
        except:
            self.assertRaises(ValueError)

    def test_init_with_negative_HP(self):
        try:
            card = TrapCard(name='a', damage_points=5, health_points=-1)
        except:
            self.assertRaises(ValueError)
