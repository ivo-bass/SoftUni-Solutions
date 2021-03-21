import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def test_init(self):
        pr = PlayerRepository()
        res = pr.players, pr.count
        exp = [], 0
        self.assertEqual(res, exp)

    def test_count_add_valid_player(self):
        pr = PlayerRepository()
        a = Advanced('asd')
        pr.add(a)
        res = pr.count
        exp = 1
        self.assertEqual(res, exp)

    def test_add_invalid_player(self):
        pr = PlayerRepository()
        a = Advanced('asd')
        pr.add(a)
        try:
            pr.add(a)
        except ValueError:
            self.assertRaises(ValueError)

    def test_find(self):
        pr = PlayerRepository()
        a = Advanced('asd')
        pr.add(a)
        res = pr.find('asd')
        exp = a
        self.assertEqual(res, exp)

    def test_remove_player(self):
        pr = PlayerRepository()
        a = Advanced('asd')
        pr.add(a)
        pr.remove('asd')
        res = pr.count
        exp = 0
        self.assertEqual(res, exp)

    def test_remove_invalid_player(self):
        pr = PlayerRepository()
        try:
            pr.remove('')
        except ValueError:
            self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
