class ExercisePlan:
    __id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):  # (in minutes)
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.set_id()

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def set_id(cls):
        cls.__id += 1
        return cls.__id

    @classmethod
    def get_next_id(cls):
        return cls.__id + 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)
