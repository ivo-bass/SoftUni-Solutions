from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = list()

    def add(self, card: Card):
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f'Card {card.name} already exists!')
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if not card:
            raise ValueError('Card cannot be an empty string!')
        card_found = list(filter(lambda x: x.name == card, self.cards))[0]
        self.cards.remove(card_found)
        self.count -= 1

    def find(self, name):
        return list(filter(lambda x: x.name == name, self.cards))[0]


from abc import ABC, abstractmethod


class Card(ABC):
    @abstractmethod
    def __init__(self, name: str, damage_points: int, health_points: int):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Card\'s name cannot be an empty string.')
        self.__name = name

    @property
    def damage_points(self):
        return self.__damage_points

    @damage_points.setter
    def damage_points(self, damage_points: int):
        if damage_points < 0:
            raise ValueError('Card\'s damage points cannot be less than zero.')
        self.__damage_points = damage_points

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, health_points):
        if health_points < 0:
            raise ValueError('Card\'s HP cannot be less than zero.')
        self.__health_points = health_points


from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name: str):
        super().__init__(name, 5, 80)


from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name: str):
        super().__init__(name, 120, 5)


from project.player.player import Player


class Advanced(Player):
    def __init__(self, username: str):
        super().__init__(username, 250)


from project.player.player import Player


class Beginner(Player):
    def __init__(self, username: str):
        super().__init__(username, 50)


from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = list()

    def add(self, player: Player):
        if any(p.username == player.username for p in self.players):
            raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if not player:
            raise ValueError('Player cannot be an empty string!')
        player_found = list(filter(lambda x: x.username == player, self.players))[0]
        self.players.remove(player_found)
        self.count -= 1

    def find(self, username):
        return list(filter(lambda x: x.username == username, self.players))[0]


from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, username: str, health: int):
        self.username = username
        self.card_repository = CardRepository()
        self.health = health

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        if username == "":
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = username

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health: int):
        if health < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.__health = health

    @property
    def is_dead(self):
        return self.health <= 0

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points


from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30
                enemy.health += card.health_points

        for card in attacker.card_repository.cards:
            attacker.health += card.health_points

        for card in enemy.card_repository.cards:
            enemy.health += card.health_points

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)


from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.battle_field import BattleField


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type, username):
        player = Beginner(username) if type == "Beginner" else Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        card = MagicCard(name) if type == "Magic" else TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = [x for x in self.player_repository.players if x.username == username][0]
        card = [x for x in self.card_repository.cards if x.name == card_name][0]
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attacker_name, enemy_name):
        attacker = [x for x in self.player_repository.players if x.username == attacker_name][0]
        enemy = [x for x in self.player_repository.players if x.username == enemy_name][0]
        battlefield = BattleField()
        battlefield.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for player in self.player_repository.players:
            result += f"Username: {player.username} - Health: {player.health} - Cards {len(player.card_repository.cards)}\n"
            for card in player.card_repository.cards:
                result += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return result
