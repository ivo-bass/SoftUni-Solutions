import unittest

from project.card.card_repository import CardRepository
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def test_init(self):
        c = Controller()
        self.assertIsInstance(c, Controller)

    def test_inti_card_repo(self):
        c = Controller()
        try:
            cr = c.card_repository
            self.assertIsInstance(cr, CardRepository)
        except AttributeError:
            self.assertRaises(AttributeError)

    def test_inti_player_repo(self):
        c = Controller()
        try:
            cr = c.player_repository
            self.assertIsInstance(cr, PlayerRepository)
        except AttributeError:
            self.assertRaises(AttributeError)

    def test_add_player(self):
        c = Controller()
        c.add_player('Beginner', 'b')
        res = c.player_repository.players[0]
        self.assertIsInstance(res, Beginner)

    def test_add_player_msg(self):
        c = Controller()
        res = c.add_player('Beginner', 'b')
        exp = "Successfully added player of type Beginner with username: b"
        self.assertEqual(res, exp)

    def test_add_card(self):
        c = Controller()
        c.add_card('Trap', 'b')
        res = c.card_repository.cards[0]
        self.assertIsInstance(res, TrapCard)

    def test_add_card_msg(self):
        c = Controller()
        res = c.add_card('Trap', 'b')
        exp = "Successfully added card of type TrapCard with name: b"
        self.assertEqual(res, exp)

    def test_add_player_card(self):
        c = Controller()
        c.add_player('Beginner', 'b')
        c.add_card('Trap', 't')
        c.add_player_card('b', 't')
        res = c.player_repository.players[0].card_repository.cards[0].name
        exp = 't'
        self.assertEqual(exp, res)

    def test_add_player_card_msg(self):
        c = Controller()
        c.add_player('Beginner', 'b')
        c.add_card('Trap', 't')
        res = c.add_player_card('b', 't')
        exp = "Successfully added card: t to user: b"
        self.assertEqual(exp, res)

    def test_fight(self):
        c = Controller()
        c.add_player('Beginner', 'b1')
        c.add_player('Beginner', 'b2')
        res = c.fight('b1', 'b2')
        exp = "Attack user health 90 - Enemy user health 90"
        self.assertEqual(res, exp)

    def test_report(self):
        c = Controller()
        c.add_player('Beginner', 'b1')
        c.add_player('Beginner', 'b2')
        c.add_card('Trap', 't1')
        c.add_card('Trap', 't2')
        c.add_player_card('b1', 't1')
        c.add_player_card('b2', 't2')
        res = c.report()
        exp = """Username: b1 - Health: 50 - Cards 1
### Card: t1 - Damage: 120
Username: b2 - Health: 50 - Cards 1
### Card: t2 - Damage: 120
"""
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
