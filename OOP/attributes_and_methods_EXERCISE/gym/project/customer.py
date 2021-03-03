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
        cls.__id += 1
        return cls.__id

    @classmethod
    def get_next_id(cls):
        return cls.__id + 1
