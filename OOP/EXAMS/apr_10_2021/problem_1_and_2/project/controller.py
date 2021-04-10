from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

VALID_AQUARIUM_TYPES = ('FreshwaterAquarium', 'SaltwaterAquarium')
VALID_DECORATION_TYPES = ('Ornament', 'Plant')
VALID_FISH_TYPES = ('FreshwaterFish', 'SaltwaterFish')


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def __is_valid_type(type_of_object, valid_types):
        return type_of_object in valid_types

    @staticmethod
    def __create_aquarium(aquarium_name, aquarium_type):
        aquarium = None
        if aquarium_type == 'FreshwaterAquarium':
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == 'SaltwaterAquarium':
            aquarium = SaltwaterAquarium(aquarium_name)
        return aquarium

    @staticmethod
    def __create_decoration(decoration_type):
        decoration = None
        if decoration_type == 'Ornament':
            decoration = Ornament()
        elif decoration_type == 'Plant':
            decoration = Plant()
        return decoration

    @staticmethod
    def __create_fish(fish_type, fish_name, fish_species, price):
        fish = None
        if fish_type == 'FreshwaterFish':
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == 'SaltwaterFish':
            fish = SaltwaterFish(fish_name, fish_species, price)
        return fish

    def __find_aquarium(self, aquarium_name):
        try:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        except IndexError:
            aquarium = None
        return aquarium

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if not self.__is_valid_type(aquarium_type, VALID_AQUARIUM_TYPES):
            return 'Invalid aquarium type.'
        aquarium = self.__create_aquarium(aquarium_name, aquarium_type)
        self.aquariums.append(aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        if not self.__is_valid_type(decoration_type, VALID_DECORATION_TYPES):
            return 'Invalid decoration type.'
        decoration = self.__create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__find_aquarium(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if aquarium is not None and not decoration == 'None':
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f'Successfully added {decoration_type} to {aquarium_name}.'
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if not self.__is_valid_type(fish_type, VALID_FISH_TYPES):
            return f"There isn't a fish of type {fish_type}."
        fish = self.__create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__find_aquarium(aquarium_name)
        if not fish.water == aquarium.water:
            return 'Water not suitable.'
        msg = aquarium.add_fish(fish)
        return msg

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        aquarium.feed()
        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        value = sum(f.price for f in aquarium.fish) + sum(dec.price for dec in aquarium.decorations)
        return f'The value of Aquarium {aquarium_name} is {value:.2f}.'

    def report(self):
        info = ''
        for aquarium in self.aquariums:
            info += aquarium.__str__()
        return info
