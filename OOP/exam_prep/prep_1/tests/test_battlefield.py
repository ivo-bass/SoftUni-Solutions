import unittest

from OOP.exam_prep.prep_1.project.battle_field import BattleField
from OOP.exam_prep.prep_1.project.card.trap_card import TrapCard
from OOP.exam_prep.prep_1.project.player.beginner import Beginner


class BattleFieldTest(unittest.TestCase):
    def test_fight_user_is_dead(self):
        bf = BattleField()
        p1 = Beginner('1')
        card = TrapCard('c')
        p1.card_repository.add(card)
        p2 = Beginner('2', health=5)
        bf.fight(p1, p2)
        try:
            bf.check_for_dead(p2)
        except:
            self.assertRaises(ValueError)

    def test_increase_health_of_beginner_player_with_40(self):
        bf = BattleField()
        p1 = Beginner('1', health=10)
        bf.check_for_beginner(p1)
        act = p1.health
        exp = 50
        self.assertEqual(act, exp)

    def test_increase_dmg_points_of_beginner_cards_with_30(self):
        bf = BattleField()
        p1 = Beginner('1')
        card = TrapCard('c', damage_points=100)
        p1.card_repository.add(card)
        bf.check_for_beginner(p1)
        act = p1.card_repository.Cards[0].damage_points
        exp = 130
        self.assertEqual(act, exp)

    def test_get_bonus_for_2_Trap_cards(self):
        bf = BattleField()
        p1 = Beginner('1', health=10)
        p2 = Beginner('2', health=10)
        card = TrapCard('c', health_points=10)
        card2 = TrapCard('a', health_points=20)
        p1.card_repository.add(card)
        p2.card_repository.add(card)
        p1.card_repository.add(card2)
        p2.card_repository.add(card2)
        bf.get_bonus_hp(p1)
        bf.get_bonus_hp(p2)
        act = p1.health, p2.health
        exp = (40, 40)
        self.assertEqual(exp, act)

    def test_attacker_attacks(self):
        bf = BattleField()
        p1 = Beginner('1')
        p2 = Beginner('2', health=100)
        card = TrapCard('c', damage_points=100)
        p1.card_repository.add(card)
        bf.attack(p1, p2)
        act = p2.health
        exp = 0
        self.assertEqual(exp, act)
