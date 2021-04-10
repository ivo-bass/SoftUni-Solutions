from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    init_size: int = 3
    increase_size: int = 3
    water = 'Fresh'

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.init_size, price)
