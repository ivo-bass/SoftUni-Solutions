class Trainer:
    __id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.set_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @classmethod
    def set_id(cls):
        cls.__id += 1
        return cls.__id

    @classmethod
    def get_next_id(cls):
        return cls.__id + 1
