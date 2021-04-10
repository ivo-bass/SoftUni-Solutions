from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    def_comfort: int = 1
    def_price: int = 5

    def __init__(self):
        super().__init__(self.def_comfort, self.def_price)
