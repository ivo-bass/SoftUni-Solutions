from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    init_size: int = 5
    increase_size: int = 2
    water = 'Salty'

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.init_size, price)
