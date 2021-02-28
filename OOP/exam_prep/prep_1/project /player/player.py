from abc import ABC

from ..card.card_repository import CardRepository


# from OOP.exam_prep.prep_1.project.card.card_repository import CardRepository


class Player(ABC):
    def __init__(self, username: str, health: int):
        if not username:
            raise ValueError("Player's username cannot be an empty string. ")
        if health < 0:
            raise ValueError("Player's health bonus cannot be less than zero. ")
        self.username = username
        self.health = health
        self.card_repository = CardRepository()
        self.is_dead = self.calc_is_dead()

    def calc_is_dead(self):
        return self.health <= 0

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points
