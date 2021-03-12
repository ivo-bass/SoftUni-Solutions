from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 0.25)


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        self.eat(food, 0.35)
