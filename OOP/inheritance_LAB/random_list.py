from random import randint


class RandomList(list):
    def get_random_element(self):
        return self.pop(randint(0, len(self) - 1))
