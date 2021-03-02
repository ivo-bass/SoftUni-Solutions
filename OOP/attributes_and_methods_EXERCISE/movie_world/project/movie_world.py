class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []  # list of customers objects
        self.dvds = []  # list of dvd objects

    def __repr__(self):
        rep = ''
        for customer in self.customers:
            rep += f'{customer}\n'
        for dvd in self.dvds:
            rep += f'{dvd}\n'
        return rep

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def can_add(count, capacity):
        return count < capacity

    @staticmethod
    def find_object(obj_id, collection):
        for obj in collection:
            if obj.id == obj_id:
                return obj

    def add_customer(self, customer):
        if self.can_add(len(self.customers), self.customer_capacity()):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.can_add(len(self.dvds), self.dvd_capacity()):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_object(customer_id, self.customers)
        dvd = self.find_object(dvd_id, self.dvds)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_object(customer_id, self.customers)
        dvd = self.find_object(dvd_id, self.dvds)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"
