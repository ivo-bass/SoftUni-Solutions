from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.calculate_expenses(self.appliances, self.children)


# child_one = Child(5, 1, 2, 1)
# child_two = Child(3, 2)
# a = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)
#
# print(a.expenses)
# for ap in a.appliances:
#     print(ap)
#     print(ap.cost)
#     print(ap.get_monthly_expense())
#     print()