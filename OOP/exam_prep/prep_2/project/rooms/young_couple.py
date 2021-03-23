from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count  # ???
        self.calculate_expenses(self.appliances)

# c = YoungCouple('asd', 150, 250)
# for ap in c.appliances:
#     print(ap)
# print(c.expenses)