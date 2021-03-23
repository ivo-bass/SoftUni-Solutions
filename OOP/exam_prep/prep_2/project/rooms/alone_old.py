from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name: str, pension: float):
        super().__init__(name=family_name, budget=pension, members_count=1)
        self.room_cost = 10
