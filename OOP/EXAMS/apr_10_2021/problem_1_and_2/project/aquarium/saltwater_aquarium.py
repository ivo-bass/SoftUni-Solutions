from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    init_capacity: int = 25
    water = 'Salty'

    def __init__(self, name: str):
        super().__init__(name, self.init_capacity)
