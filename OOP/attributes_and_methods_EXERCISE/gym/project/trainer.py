class Trainer:
    __id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.set_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @classmethod
    def set_id(cls):
        cls.__id = cls.get_next_id()

    @staticmethod
    def get_next_id():
        return Trainer.__id + 1
