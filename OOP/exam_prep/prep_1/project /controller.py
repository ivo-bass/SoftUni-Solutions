# from OOP.exam_prep.prep_1.project.battle_field import BattleField
# from OOP.exam_prep.prep_1.project.card.card_repository import CardRepository
# from OOP.exam_prep.prep_1.project.card.magic_card import MagicCard
# from OOP.exam_prep.prep_1.project.card.trap_card import TrapCard
# from OOP.exam_prep.prep_1.project.player.advanced import Advanced
# from OOP.exam_prep.prep_1.project.player.beginner import Beginner
# from OOP.exam_prep.prep_1.project.player.player_repository import PlayerRepository


from .battle_field import BattleField
from .card.card_repository import CardRepository
from .card.magic_card import MagicCard
from .card.trap_card import TrapCard
from .player.advanced import Advanced
from .player.beginner import Beginner
from .player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_card(self, type_: str, name: str):
        card = None
        if type_ == 'Magic':
            card = MagicCard(name)
        elif type_ == 'Trap':
            card = TrapCard(name)
        if card:
            self.card_repository.add(card)
        return f"Successfully added card of type {type_}Card with name: {name}"

    def add_player(self, type_: str, username: str):
        pl = None
        if type_ == 'Beginner':
            pl = Beginner(username)
        elif type_ == 'Advanced':
            pl = Advanced(username)
        if pl:
            self.player_repository.add(pl)
        return f"Successfully added player of type {type_} with username: {username}"

    def add_player_card(self, username: str, card_name: str):
        card = self.card_repository.find(card_name)
        player = self.player_repository.find(username)
        if card and player:
            player.card_repository.add(card)
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        bf = BattleField()
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        if attacker and enemy:
            bf.fight(attacker, enemy)
            return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        info = ''
        for player in self.player_repository.players:
            cards_info = ''
            for card in player.card_repository.Cards:
                cards_info += f'### Card: {card.name} - Damage: {card.damage_points}\n'
            info += f"Username: {player.username} - Health: {player.health} - Cards {player.card_repository.Count}\n" + cards_info
        return info


c = Controller()
print(c.add_card('Magic', 'Spell'))
print(c.add_player('Beginner', 'Ivo'))
print(c.add_player('Beginner', 'Vesi'))
c.add_player_card('Ivo', 'Spell')
c.add_player_card('Vesi', 'Spell')
print(c.fight('Ivo', 'Vesi'))
print(c.report())
a = 5
