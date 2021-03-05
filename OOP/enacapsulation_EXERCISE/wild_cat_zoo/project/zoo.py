# from project.caretaker import Caretaker
# from project.cheetah import Cheetah
# from project.keeper import Keeper
# from project.lion import Lion
# from project.tiger import Tiger
# from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.type} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.position} hired successfully"

    def fire_worker(self, worker_name: str):
        worker = None
        workers_found = list(filter(lambda x: x.name == worker_name, self.workers))
        if workers_found:
            worker = workers_found[0]
        if not worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum([x.salary for x in self.workers])
        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needs = sum([x.get_needs() for x in self.animals])
        if self.__budget < needs:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda x: x.type == 'Lion', self.animals))
        tigers = list(filter(lambda x: x.type == 'Tiger', self.animals))
        cheetahs = list(filter(lambda x: x.type == 'Cheetah', self.animals))
        info = f"You have {len(self.animals)} animals\n"
        info += f"----- {len(lions)} Lions:\n"
        for l in lions:
            info += str(l) + '\n'
        info += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            info += str(t) + '\n'
        info += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            info += str(c) + '\n'
        return info.rstrip('\n')

    def workers_status(self):
        keepers = [x for x in self.workers if x.position == 'Keeper']
        caretakers = [x for x in self.workers if x.position == 'Caretaker']
        vets = [x for x in self.workers if x.position == 'Vet']
        info = f"You have {len(self.workers)} workers\n"
        info += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            info += str(k) + '\n'
        info += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            info += str(c) + '\n'
        info += f"----- {len(vets)} Vets:\n"
        for v in vets:
            info += str(v) + '\n'
        return info.rstrip('\n')


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())