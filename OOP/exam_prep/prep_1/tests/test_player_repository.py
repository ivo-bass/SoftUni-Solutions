import unittest

from OOP.exam_prep.prep_1.project.player.beginner import Beginner
from OOP.exam_prep.prep_1.project.player.player_repository import PlayerRepository


class PlayerRepositoryTest(unittest.TestCase):
    def test_init_count_is_0(self):
        repo = PlayerRepository()
        act = repo.count
        exp = 0
        self.assertEqual(act, exp)

    def test_init_players_is_empty_list(self):
        repo = PlayerRepository()
        act = repo.players
        exp = []
        self.assertEqual(act, exp)

    def test_count_when_added_player(self):
        repo = PlayerRepository()
        repo.add(Beginner('a'))
        act = repo.count
        exp = 1
        self.assertEqual(act, exp)

    def test_players_when_added_player(self):
        repo = PlayerRepository()
        repo.add(Beginner('a'))
        act = repo.players[0].username
        exp = 'a'
        self.assertEqual(act, exp)

    def test_add_existing_player(self):
        repo = PlayerRepository()
        repo.add(Beginner('a'))
        try:
            repo.add(Beginner('a'))
        except:
            self.assertRaises(ValueError)
