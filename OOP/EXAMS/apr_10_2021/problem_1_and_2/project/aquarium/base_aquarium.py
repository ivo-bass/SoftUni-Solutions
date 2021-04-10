from abc import ABC, abstractmethod
from typing import Union

from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    def calculate_comfort(self):
        return sum(dec.comfort for dec in self.decorations)

    def add_fish(self, fish: Union[FreshwaterFish, SaltwaterFish]):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'
        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'

    def remove_fish(self, fish: Union[FreshwaterFish, SaltwaterFish]):
        self.fish.remove(fish)

    def add_decoration(self, decoration: Union[Ornament, Plant]):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        info = f"{self.name}:\n"
        if not self.fish:
            names = 'none'
        else:
            names = " ".join([f.name for f in self.fish])
        info += f'Fish: {names}\n'
        info += f'Decorations: {len(self.decorations)}\n'
        info += f'Comfort: {self.calculate_comfort()}\n'
        return info
