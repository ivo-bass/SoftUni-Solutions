from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    __MILLILITERS = 50
    __PRICE = 3.50

    def __init__(self, name: str, price: float, milliliters: float, caffeine: float):
        super().__init__(name, price, milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @property
    def price(self):
        return self.__PRICE

    @property
    def milliliters(self):
        return self.__MILLILITERS
