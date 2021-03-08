from project.food.dessert import Dessert


class Cake(Dessert):
    __GRAMS = 250
    __CALORIES = 1000
    __PRICE = 5

    @property
    def calories(self):
        return self.__CALORIES

    @property
    def price(self):
        return self.__PRICE

    @property
    def grams(self):
        return self.__GRAMS
