class Vet:
    animals = []
    space = 5
    space_taken = 0

    @staticmethod
    def get_free_space():
        return Vet.space - Vet.space_taken

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.get_free_space() == 0:
            return "Not enough space"
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        Vet.space_taken += 1
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        try:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            Vet.space_taken -= 1
            return f"{animal_name} unregistered successfully"
        except ValueError:
            return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.get_free_space()} space left in clinic"

# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())
