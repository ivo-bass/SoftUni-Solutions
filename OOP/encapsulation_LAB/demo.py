class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def __repr__(self):
        return str(self.__age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


p = Person('az', 13)  # init
print(p)
p.__age = 25  # does not change the age
print(p)
p.age = 25  # changes the age
print(p)
