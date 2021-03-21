import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def test_init(self):
        bf = BattleField()
        self.assertIsInstance(bf, BattleField)

    def test_fight_with_dead_player(self):
        bf = BattleField()
        att = Advanced('a')
        en = Beginner('b')
        en.take_damage(50)
        try:
            bf.fight(att, en)
        except ValueError:
            self.assertRaises(ValueError)

    def test_increase_beginner_health(self):
        bf = BattleField()
        att = Beginner('a')
        en = Beginner('b')
        bf.fight(att, en)
        res = att.health
        exp = 90
        self.assertEqual(res, exp)

    def test_increase_dmg_points_for_cards(self):
        bf = BattleField()
        att = Beginner('a')
        card1 = MagicCard('mc1')
        card2 = MagicCard('mc2')
        att.card_repository.cards.append(card1)
        att.card_repository.cards.append(card2)
        en = Beginner('b')
        bf.fight(att, en)
        res = sum(card.damage_points for card in att.card_repository.cards)
        exp = 70
        self.assertEqual(res, exp)

    def test_get_bonus(self):
        bf = BattleField()
        att = Beginner('a')
        card1 = MagicCard('mc1')
        card2 = MagicCard('mc2')
        att.card_repository.cards.append(card1)
        att.card_repository.cards.append(card2)
        en = Beginner('b')
        bf.fight(att, en)
        res = att.health
        exp = 250
        self.assertEqual(res, exp)

    def test_attack(self):
        bf = BattleField()
        att = Beginner('a')
        card1 = MagicCard('mc1')
        card2 = MagicCard('mc2')
        att.card_repository.cards.append(card1)
        att.card_repository.cards.append(card2)
        en = Beginner('b')
        bf.fight(att, en)
        res = en.health
        exp = 20
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
