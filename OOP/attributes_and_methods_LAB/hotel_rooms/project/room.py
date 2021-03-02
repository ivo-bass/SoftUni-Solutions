class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def can_take_room(self, people):
        return not self.is_taken and self.capacity >= people

    def take_room(self, people: int):
        if not self.can_take_room(people):
            return f"Room number {self.number} cannot be taken"
        self.guests = people
        self.is_taken = True

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0
