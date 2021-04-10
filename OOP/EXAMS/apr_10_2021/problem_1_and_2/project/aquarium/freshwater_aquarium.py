from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    init_capacity: int = 50
    water = 'Fresh'


    def __init__(self, name: str):
        super().__init__(name, self.init_capacity)
