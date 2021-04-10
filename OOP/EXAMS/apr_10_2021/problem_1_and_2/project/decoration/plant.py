from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    def_comfort: int = 5
    def_price: int = 10

    def __init__(self):
        super().__init__(self.def_comfort, self.def_price)
