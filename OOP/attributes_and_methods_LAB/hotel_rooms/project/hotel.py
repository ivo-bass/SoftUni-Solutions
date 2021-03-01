from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = list()
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        found_room = list(filter(lambda x: x.number == room_number, self.rooms))[0]
        if Room.take_room(found_room, people) is None:
            self.guests += people

    def free_room(self, room_number: int):
        found_room = list(filter(lambda x: x.number == room_number, self.rooms))[0]
        people = found_room.guests
        if Room.free_room(found_room) is None:
            self.guests -= people

    def print_status(self):
        free_rooms = list(filter(lambda x: not x.is_taken, self.rooms))
        free_numbers = [str(r.number) for r in free_rooms]
        taken_rooms = list(filter(lambda x: x.is_taken, self.rooms))
        taken_numbers = [str(r.number) for r in taken_rooms]
        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f'Free rooms: {", ".join(free_numbers)}')
        print(f'Taken rooms: {", ".join(taken_numbers)}')
