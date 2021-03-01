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