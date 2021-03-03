class Customer:
    __id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.set_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @classmethod
    def set_id(cls):
        cls.__id = cls.get_next_id()
        return cls.__id

    @staticmethod  # should be class method but that's how it is described in problem description
    def get_next_id():
        return Customer.__id + 1
