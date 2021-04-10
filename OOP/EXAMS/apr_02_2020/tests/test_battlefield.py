import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        self.bf = BattleField()

    def test_fight__when_dead_player__should_raise(self):
        attacker = Advanced('a')
        enemy = Beginner('b')
        enemy.take_damage(50)
        with self.assertRaises(ValueError):
            self.bf.fight(attacker, enemy)

    def test_increase_beginner_health(self):
        attacker = Beginner('a')
        enemy = Beginner('e')
        self.bf.fight(attacker, enemy)
        self.assertEqual(90, attacker.health)

    def test_increase_dmg_points_for_cards(self):
        attacker = Beginner('a')
        card1 = MagicCard('mc1')
        card2 = MagicCard('mc2')
        attacker.card_repository.cards.append(card1)
        attacker.card_repository.cards.append(card2)
        enemy = Beginner('e')
        self.bf.fight(attacker, enemy)
        self.assertEqual(70, sum(card.damage_points for card in attacker.card_repository.cards))

    def test_get_bonus(self):
        attacker = Beginner('a')
        card1 = MagicCard('mc1')
        card2 = MagicCard('mc2')
        attacker.card_repository.cards.append(card1)
        attacker.card_repository.cards.append(card2)
        enemy = Beginner('e')
        self.bf.fight(attacker, enemy)
        self.assertEqual(250, attacker.health)

    def test_attack(self):
        attacker = Beginner('a')
        card1 = MagicCard('mc1')
        card2 = MagicCard('mc2')
        attacker.card_repository.cards.append(card1)
        attacker.card_repository.cards.append(card2)
        enemy = Beginner('b')
        self.bf.fight(attacker, enemy)
        self.assertEqual(20, enemy.health)


if __name__ == '__main__':
    unittest.main()
