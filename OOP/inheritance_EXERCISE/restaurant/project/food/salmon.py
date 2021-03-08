from project.food.main_dish import MainDish


class Salmon(MainDish):
    __GRAMS = 22

    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)

    @property
    def grams(self):
        return self.__GRAMS
