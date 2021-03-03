class Equipment:
    __id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.set_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @classmethod
    def set_id(cls):
        cls.__id = cls.get_next_id()
        return cls.__id

    @staticmethod
    def get_next_id():
        return Equipment.__id + 1
