class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.status() < milliliters:
            return
        self.quantity += milliliters

    def status(self):
        return self.size - self.quantity

# cup = Cup(100, 50)
# cup.fill(10)
# cup.fill(50)
# print(cup.status())
