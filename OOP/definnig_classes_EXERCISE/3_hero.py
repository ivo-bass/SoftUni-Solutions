class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage):
        if self.health <= damage:
            self.health = 0
            return self.is_defeat()
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def is_defeat(self):
        return f'{self.name} was defeated'

#
# hero = Hero("Peter", 100)
# print(hero.defend(50))
# hero.heal(50)
# print(hero.defend(99))
# print(hero.defend(1))
