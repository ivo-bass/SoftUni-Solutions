class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []  # list of dvd instances

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has " \
               f"{len(self.rented_dvds)} rented DVD's " \
               f"({', '.join([dvd.name for dvd in self.rented_dvds])})"
