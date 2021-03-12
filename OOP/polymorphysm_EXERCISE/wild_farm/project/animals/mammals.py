from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 0.1)


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 0.4)


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 0.3)


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 1.0)
