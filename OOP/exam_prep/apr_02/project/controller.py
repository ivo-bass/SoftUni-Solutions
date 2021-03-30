from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            self.player_repository.add(Beginner(username=username))
            return f"Successfully added player of type {type} with username: {username}"
        elif type == 'Advanced':
            self.player_repository.add(Advanced(username=username))
            return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            self.card_repository.add(MagicCard(name=name))
            return f"Successfully added card of type {type}Card with name: {name}"
        elif type == "Trap":
            self.card_repository.add(TrapCard(name=name))
            return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        if player and card:
            player.card_repository.add(card)
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        bf = BattleField()
        bf.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        info = ''
        for pl in self.player_repository.players:
            info += f"Username: {pl.username} - Health: {pl.health} - Cards {pl.card_repository.count}\n"
            for c in pl.card_repository.cards:
                info += f"### Card: {c.name} - Damage: {c.damage_points}\n"
        return info
