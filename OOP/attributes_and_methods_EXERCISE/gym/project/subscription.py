class Subscription:
    __id = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.set_id()

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @classmethod
    def set_id(cls):
        cls.__id = cls.get_next_id()
        return cls.__id

    @staticmethod
    def get_next_id():
        return Subscription.__id + 1
