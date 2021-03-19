class Animal:
    sound = ''

    def make_sound(self):
        return self.sound


class Cat(Animal):
    sound = 'meow'


class Dog(Animal):
    sound = 'bark'


class Lion(Animal):
    sound = 'roar'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Lion()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
