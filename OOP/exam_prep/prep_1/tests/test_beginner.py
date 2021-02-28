import unittest

from OOP.exam_prep.prep_1.project.player.beginner import Beginner


class BeginnerPlayerTest(unittest.TestCase):
    def test_init_health(self):
        player = Beginner('Ivo')
        hp = player.health
        expected = 50
        self.assertEqual(hp, expected)

    def test_init_with_valid_username(self):
        player = Beginner('Ivo')
        username = player.username
        expected = 'Ivo'
        self.assertEqual(username, expected)

    def test_is_dead_init(self):
        player = Beginner('A')
        actual = player.is_dead
        expected = False
        self.assertEqual(actual, expected)

    def test_take_damage_25(self):
        player = Beginner('A')
        player.take_damage(25)
        actual = player.health
        expected = 25
        self.assertEqual(actual, expected)

    def test_init_without_username(self):
        try:
            player = Beginner()
        except:
            self.assertRaises(TypeError)

    def test_init_empty_string_username(self):
        try:
            player = Beginner('')
        except:
            self.assertRaises(ValueError)
