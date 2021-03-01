import unittest

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.player.beginner import Beginner


class BattleFieldTest(unittest.TestCase):
    def test_fight_user_is_dead(self):
        bf = BattleField()
        p1 = Beginner('1')
        card = TrapCard('c')
        p1.card_repository.add(card)
        p2 = Beginner('2')
        bf.fight(p1, p2)
        try:
            bf.check_for_dead(p2)
        except:
            self.assertRaises(ValueError)

    def test_increase_health_of_beginner_player_with_40(self):
        bf = BattleField()
        p1 = Beginner('1')
        bf.check_for_beginner(p1)
        act = p1.health
        exp = 90
        self.assertEqual(exp, act)

    def test_increase_dmg_points_of_beginner_cards_with_30(self):
        bf = BattleField()
        p1 = Beginner('1')
        card = TrapCard('c')
        p1.card_repository.add(card)
        bf.check_for_beginner(p1)
        act = p1.card_repository.cards[0].damage_points
        exp = 150
        self.assertEqual(exp, act)

    def test_get_bonus_for_2_Trap_cards(self):
        bf = BattleField()
        p1 = Beginner('1')
        p2 = Beginner('2')
        card = TrapCard('c')
        card2 = TrapCard('a')
        p1.card_repository.add(card)
        p2.card_repository.add(card)
        p1.card_repository.add(card2)
        p2.card_repository.add(card2)
        bf.get_bonus_hp(p1)
        bf.get_bonus_hp(p2)
        act = p1.health, p2.health
        exp = (60, 60)
        self.assertEqual(exp, act)

    def test_attacker_attacks(self):
        bf = BattleField()
        p1 = Beginner('1')
        p2 = Beginner('2')
        card = TrapCard('c')
        p1.card_repository.add(card)
        bf.attack(p1, p2)
        act = p2.health
        exp = -70
        self.assertEqual(exp, act)
