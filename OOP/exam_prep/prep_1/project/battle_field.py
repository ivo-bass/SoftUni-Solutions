from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        self.validate_player_alive(attacker)
        self.validate_player_alive(enemy)
        self.check_for_beginner(attacker)
        self.check_for_beginner(enemy)
        self.get_bonus(attacker)
        self.get_bonus(enemy)
        self.attack(attacker, enemy)
        self.attack(enemy, attacker)

    @staticmethod
    def validate_player_alive(player):
        if player.is_dead:
            raise ValueError("Player is dead!")

    def check_for_beginner(self, player):
        if not isinstance(player, Beginner):
            return
        self.increase_health(player)
        self.increase_cards_damage(player)

    @staticmethod
    def increase_health(player):
        player.health += 40

    @staticmethod
    def increase_cards_damage(player):
        for card in player.card_repository.cards:
            card.damage_points += 30

    @staticmethod
    def get_bonus(player):
        player.health += sum([card.health_points for card in player.card_repository.cards])

    @staticmethod
    def attack(att: Player, en: Player):
        for card in att.card_repository.cards:
            en.take_damage(card.damage_points)
