import unittest

from OOP.exam_prep.prep_1.project.player.advanced import Advanced


class AdvancedPlayerTest(unittest.TestCase):
    def test_init_health(self):
        player = Advanced('Ivo')
        hp = player.health
        expected = 250
        self.assertEqual(hp, expected)

    def test_init_with_valid_username(self):
        player = Advanced('Ivo')
        username = player.username
        expected = 'Ivo'
        self.assertEqual(username, expected)

    def test_is_dead_init(self):
        player = Advanced('A')
        actual = player.is_dead
        expected = False
        self.assertEqual(actual, expected)

    def test_take_damage_50(self):
        player = Advanced('A')
        player.take_damage(50)
        actual = player.health
        expected = 200
        self.assertEqual(actual, expected)

    def test_init_without_username(self):
        try:
            player = Advanced()
        except:
            self.assertRaises(TypeError)

    def test_init_empty_string_username(self):
        try:
            player = Advanced('')
        except:
            self.assertRaises(ValueError)
