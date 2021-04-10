import unittest

from project.card.card_repository import CardRepository
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_inti(self):
        self.assertIsInstance(self.controller.player_repository, PlayerRepository)
        self.assertIsInstance(self.controller.card_repository, CardRepository)


    def test_add_player(self):
        self.controller.add_player('Beginner', 'b')
        self.assertIsInstance(self.controller.player_repository.players[0], Beginner)

    def test_add_player_msg(self):
        exp = "Successfully added player of type Beginner with username: b"
        res = self.controller.add_player('Beginner', 'b')
        self.assertEqual(exp, res)

    def test_add_card(self):
        self.controller.add_card('Trap', 'b')
        res = self.controller.card_repository.cards[0]
        self.assertIsInstance(res, TrapCard)

    def test_add_card_msg(self):
        exp = "Successfully added card of type TrapCard with name: b"
        res = self.controller.add_card('Trap', 'b')
        self.assertEqual(exp, res)

    def test_add_player_card(self):
        self.controller.add_player('Beginner', 'b')
        self.controller.add_card('Trap', 't')
        self.controller.add_player_card('b', 't')
        res = self.controller.player_repository.players[0].card_repository.cards[0].name

        self.assertEqual('t', res)

    def test_add_player_card_msg(self):
        self.controller.add_player('Beginner', 'b')
        self.controller.add_card('Trap', 't')
        exp = "Successfully added card: t to user: b"
        res = self.controller.add_player_card('b', 't')

        self.assertEqual(exp, res)

    def test_fight(self):
        self.controller.add_player('Beginner', 'b1')
        self.controller.add_player('Beginner', 'b2')
        exp = "Attack user health 90 - Enemy user health 90"
        res = self.controller.fight('b1', 'b2')

        self.assertEqual(exp, res)

    def test_report(self):
        self.controller.add_player('Beginner', 'b1')
        self.controller.add_player('Beginner', 'b2')
        self.controller.add_card('Trap', 't1')
        self.controller.add_card('Trap', 't2')
        self.controller.add_player_card('b1', 't1')
        self.controller.add_player_card('b2', 't2')
        res = self.controller.report()
        exp = """Username: b1 - Health: 50 - Cards 1
### Card: t1 - Damage: 120
Username: b2 - Health: 50 - Cards 1
### Card: t2 - Damage: 120
"""
        self.assertEqual(exp, res)


if __name__ == '__main__':
    unittest.main()
