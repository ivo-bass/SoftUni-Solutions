class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def get_free_space(self):
        return Glass.capacity - self.content

    def is_enough_space(self, ml):
        return self.get_free_space() >= ml

    def fill(self, ml):
        if not self.is_enough_space(ml):
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{self.get_free_space()} ml left"

# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())
