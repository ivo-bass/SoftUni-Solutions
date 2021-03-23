class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        res = 0
        for arg in args:
            for el in arg:
                if el.__class__.__name__ == "Child":
                    res += el.cost * 30
                else:
                    res += el.get_monthly_expense()
        self.expenses = res
