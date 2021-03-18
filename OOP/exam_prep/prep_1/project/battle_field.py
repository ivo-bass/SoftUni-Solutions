from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        self.validate_players_alive(attacker, enemy)
        self.check_for_beginners(attacker, enemy)
        self.get_bonus(attacker, enemy)
        self.attack(attacker, enemy)
        self.attack(enemy, attacker)

    @staticmethod
    def validate_players_alive(*players):
        for player in players:
            if player.is_dead:
                raise ValueError("Player is dead!")

    def check_for_beginners(self, *players):
        for player in players:
            if player.__class__.__name__ == 'Beginner':
                self.increase_health(player)
                self.increase_cards_damage(player)

    @staticmethod
    def increase_health(player):
        player.health += 40

    @staticmethod
    def increase_cards_damage(player):
        for card in player.card_repository:
            card.damage_points += 30

    @staticmethod
    def get_bonus(*players):
        for player in players:
            player.health += sum([card.health_points for card in player.card_repository])

    @staticmethod
    def attack(att: Player, en: Player):
        for card in att.card_repository:
            en.take_damage(card.damage_points)
