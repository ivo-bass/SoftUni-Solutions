import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = PlayerRepository()
        self.pl = Advanced('name')

    def test_init(self):
        self.assertEqual(0, self.repo.count)
        self.assertListEqual([], self.repo.players)

    def test_add__when_valid__should_add_to_players(self):
        self.repo.add(self.pl)
        self.assertIn(self.pl, self.repo.players)

    def test_add__when_valid__should_increase_count(self):
        self.repo.add(self.pl)
        self.assertEqual(1, self.repo.count)

    def test_add__when_player_exists__should_raise(self):
        self.repo.add(self.pl)
        new_pl = Advanced('name')
        with self.assertRaises(ValueError) as exc:
            self.repo.add(new_pl)
        msg = f"Player {new_pl.username} already exists!"
        self.assertEqual(msg, str(exc.exception))

    def test_remove__when_valid__should_remove(self):
        self.repo.add(self.pl)
        self.repo.remove('name')
        self.assertNotIn(self.pl, self.repo.players)

    def test_remove__when_valid__should_decrease_count(self):
        self.repo.add(self.pl)
        self.repo.remove('name')
        self.assertEqual(0, self.repo.count)

    def test_remove__when_empty_name__should_raise(self):
        self.repo.add(self.pl)
        with self.assertRaises(ValueError) as exc:
            self.repo.remove('')
        msg = "Player cannot be an empty string!"
        self.assertEqual(msg, str(exc.exception))

    def test_find__should_return_player(self):
        self.repo.add(self.pl)
        res = self.repo.find('name')
        self.assertEqual(self.pl, res)


if __name__ == '__main__':
    unittest.main()
