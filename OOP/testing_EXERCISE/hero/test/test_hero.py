import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    username = 'username'
    level = 2
    health = 100.0
    damage = 10.0

    def setUp(self) -> None:
        self.hero = Hero(
            username=self.username,
            level=self.level,
            health=self.health,
            damage=self.damage
        )

    def test_hero_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertEqual(self.level, self.hero.level)

    def test_hero_string_representation(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"
        actual = self.hero.__str__()
        self.assertEqual(expected, actual)

    def test_battle__when_self_fight__should_raise_exception(self):
        enemy = self.hero
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy)
        msg = "You cannot fight yourself"
        self.assertEqual(msg, str(exc.exception))

    def test_battle__when_hero_health_is_0__should_raise_value_error(self):
        enemy = Hero('enemy', 1, 100.0, 10.0)
        self.hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        msg = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(msg, str(exc.exception))

    def test_battle__when_hero_health_is_negative__should_raise_value_error(self):
        enemy = Hero('enemy', 1, 100.0, 10.0)
        self.hero.health = -1
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        msg = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(msg, str(exc.exception))

    def test_battle__when_enemy_health_is_0__should_raise_value_error(self):
        enemy = Hero('enemy', 1, 0.0, 10.0)
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        msg = f"You cannot fight {enemy.username}. He needs to rest"
        self.assertEqual(msg, str(exc.exception))

    def test_battle__when_enemy_health_is_negative__should_raise_value_error(self):
        enemy = Hero('enemy', 1, -1.0, 10.0)
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        msg = f"You cannot fight {enemy.username}. He needs to rest"
        self.assertEqual(msg, str(exc.exception))

    def test_battle__hero_health_is_reduced_by_enemy_dmg(self):
        enemy = Hero(username='enemy', level=2, health=100.0, damage=10.0)
        self.hero.battle(enemy)
        self.assertEqual(80.0, self.hero.health)

    def test_battle__enemy_health_is_reduced_by_hero_dmg(self):
        enemy = Hero(username='enemy', level=2, health=100.0, damage=10.0)
        self.hero.battle(enemy)
        self.assertEqual(85.0, enemy.health)

    def test_battle__when_health_is_negative__should_return_draw(self):
        self.hero.damage = 100
        enemy = Hero(username='enemy', level=2, health=100.0, damage=100.0)
        expected = 'Draw'
        actual = self.hero.battle(enemy)
        self.assertEqual(expected, actual)

    def test_battle__when_health_is_0__should_return_draw(self):
        self.hero.damage = 50
        enemy = Hero(username='enemy', level=2, health=100.0, damage=50.0)
        expected = 'Draw'
        actual = self.hero.battle(enemy)
        self.assertEqual(expected, actual)

    def test_battle__when_hero_health_is_less_than_enemy__should_return_lose(self):
        enemy = Hero(username='enemy', level=2, health=100.0, damage=50.0)
        expected = 'You lose'
        actual = self.hero.battle(enemy)
        self.assertEqual(expected, actual)

    def test_battle__when_enemy_health_is_0__should_return_win(self):
        enemy = Hero(username='enemy', level=1, health=20.0, damage=10.0)
        expected = 'You win'
        actual = self.hero.battle(enemy)
        self.assertEqual(expected, actual)

    def test_battle__when_enemy_health_is_negative__should_return_win(self):
        enemy = Hero(username='enemy', level=1, health=10.0, damage=10.0)
        expected = 'You win'
        actual = self.hero.battle(enemy)
        self.assertEqual(expected, actual)

    def test_battle__when_win__should_increase_hero_stats(self):
        enemy = Hero(username='enemy', level=1, health=10.0, damage=0.0)
        self.hero.battle(enemy)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(105.0, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)

    def test_battle__when_lose__should_increase_enemy_stats(self):
        enemy = Hero(username='enemy', level=10, health=100.0, damage=100.0)
        self.hero.battle(enemy)
        self.assertEqual(11, enemy.level)
        self.assertEqual(85.0, enemy.health)
        self.assertEqual(105.0, enemy.damage)


if __name__ == '__main__':
    unittest.main()
