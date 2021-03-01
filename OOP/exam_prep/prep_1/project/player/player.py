from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self, username: str, health: int):
        if username == "":
            raise ValueError("Player's username cannot be an empty string.")
        if health < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.username = username
        self.card_repository = CardRepository()
        self.health = health

    # @property
    # def username(self):
    #     return self.__username

    # @username.setter
    # def username(self, username: str):
    #     if username == "":
    #         raise ValueError("Player's username cannot be an empty string.")
    #     self.__username = username

    # @property
    # def health(self):
    #     return self.__health

    # @health.setter
    # def health(self, health: int):
    #     if health < 0:
    #         raise ValueError("Player's health bonus cannot be less than zero.")
    #     self.__health = health

    @property
    def is_dead(self):
        return self.health <= 0

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points