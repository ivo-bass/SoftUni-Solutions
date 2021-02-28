import unittest

from OOP.exam_prep.prep_1.project.card.card_repository import CardRepository
from OOP.exam_prep.prep_1.project.card.trap_card import TrapCard
from OOP.exam_prep.prep_1.project.controller import Controller
from OOP.exam_prep.prep_1.project.player.beginner import Beginner
from OOP.exam_prep.prep_1.project.player.player_repository import PlayerRepository


class ControllerTest(unittest.TestCase):
    def test_init_player_repository_exists(self):
        c = Controller()
        act = type(c.player_repository) is PlayerRepository
        self.assertTrue(act)

    def test_init_card_repository_exists(self):
        c = Controller()
        act = type(c.card_repository) is CardRepository
        self.assertTrue(act)

    def test_add_player_message(self):
        c = Controller()
        act = c.add_player('Beginner', 'a')
        exp = "Successfully added player of type Beginner with username: a"
        self.assertEqual(exp, act)

    def test_add_player_type(self):
        c = Controller()
        c.add_player('Beginner', 'a')
        act = type(c.player_repository.players[0])
        exp = Beginner
        self.assertEqual(exp, act)

    def test_add_player_name(self):
        c = Controller()
        c.add_player('Beginner', 'a')
        act = c.player_repository.players[0].username
        exp = 'a'
        self.assertEqual(exp, act)

    def test_add_card_message(self):
        c = Controller()
        act = c.add_card('Trap', 'a')
        exp = "Successfully added card of type TrapCard with name: a"
        self.assertEqual(exp, act)

    def test_add_card_type(self):
        c = Controller()
        c.add_card('Trap', 'a')
        act = type(c.card_repository.Cards[0])
        exp = TrapCard
        self.assertEqual(exp, act)

    def test_add_card_name(self):
        c = Controller()
        c.add_card('Trap', 'a')
        act = c.card_repository.Cards[0].name
        exp = 'a'
        self.assertEqual(exp, act)

    def test_add_player_card_message(self):
        c = Controller()
        c.add_player('Beginner', 'beginner')
        c.add_card('Trap', 'trap')
        act = c.add_player_card('beginner', 'trap')
        exp = "Successfully added card: trap to user: beginner"
        self.assertEqual(exp, act)

    def test_player_repo_when_added_player_card(self):
        c = Controller()
        c.add_player('Beginner', 'beginner')
        c.add_card('Trap', 'trap')
        c.add_player_card('beginner', 'trap')
        act = c.player_repository.players[0].card_repository.Cards[0].name
        exp = 'trap'
        self.assertEqual(exp, act)

    def test_fight_message(self):
        c = Controller()
        c.add_player('Advanced', 'a')
        c.add_card('Trap', 't')
        c.add_player_card('a', 't')
        c.add_player('Beginner', 'b')
        c.add_card('Magic', 'm')
        c.add_player_card('b', 'm')
        act = c.fight('a', 'b')
        exp = "Attack user health 220 - Enemy user health 50"
        self.assertEqual(exp, act)

    def test_report(self):
        c = Controller()
        c.add_player('Advanced', 'a')
        c.add_card('Trap', 't')
        c.add_player_card('a', 't')
        c.add_player('Beginner', 'b')
        c.add_card('Magic', 'm')
        c.add_player_card('b', 'm')
        c.fight('a', 'b')
        act = c.report()
        exp = "Username: a - Health: 220 - Cards 1\n" \
              "### Card: t - Damage: 120\n" \
              "Username: b - Health: 50 - Cards 1\n" \
              "### Card: m - Damage: 35\n"
        self.assertEqual(exp, act)
