class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Car(
            make='ford',
            model='ka',
            fuel_consumption=10,
            fuel_capacity=100
        )

    def test_init(self):
        self.assertEqual(self.c.make, 'ford')
        self.assertEqual(self.c.model, 'ka')
        self.assertEqual(self.c.fuel_consumption, 10)
        self.assertEqual(self.c.fuel_capacity, 100)
        self.assertEqual(self.c.fuel_amount, 0)

    def test_make_setter(self):
        self.c.make = 'asd'
        self.assertEqual(self.c.make, 'asd')

    def test_make_invalid_setter(self):
        with self.assertRaises(Exception) as exc:
            self.c.make = ''
        msg = "Make cannot be null or empty!"
        self.assertEqual(msg, str(exc.exception))

    def test_model_setter(self):
        self.c.model = 'asd'
        self.assertEqual(self.c.model, 'asd')

    def test_model_invalid_setter(self):
        with self.assertRaises(Exception) as exc:
            self.c.model = ''
        msg = "Model cannot be null or empty!"
        self.assertEqual(msg, str(exc.exception))

    def test_fuel_consumption_setter(self):
        self.c.fuel_consumption = 20
        self.assertEqual(self.c.fuel_consumption, 20)

    def test_fuel_consumption_invalid_setter_0(self):
        with self.assertRaises(Exception) as exc:
            self.c.fuel_consumption = 0
        msg = "Fuel consumption cannot be zero or negative!"
        self.assertEqual(msg, str(exc.exception))

    def test_fuel_consumption_invalid_setter_negative(self):
        with self.assertRaises(Exception) as exc:
            self.c.fuel_consumption = -1
        msg = "Fuel consumption cannot be zero or negative!"
        self.assertEqual(msg, str(exc.exception))

    def test_fuel_capacity_setter(self):
        self.c.fuel_capacity = 20
        self.assertEqual(self.c.fuel_capacity, 20)

    def test_fuel_capacity_invalid_setter_0(self):
        with self.assertRaises(Exception) as exc:
            self.c.fuel_capacity = 0
        msg = "Fuel capacity cannot be zero or negative!"
        self.assertEqual(msg, str(exc.exception))

    def test_fuel_capacity_invalid_setter_negative(self):
        with self.assertRaises(Exception) as exc:
            self.c.fuel_capacity = -1
        msg = "Fuel capacity cannot be zero or negative!"
        self.assertEqual(msg, str(exc.exception))

    def test_fuel_amount_setter(self):
        self.c.fuel_amount = 20
        self.assertEqual(self.c.fuel_amount, 20)

    def test_fuel_amount_setter_0_is_valid(self):
        self.c.fuel_amount = 0
        self.assertEqual(self.c.fuel_amount, 0)

    def test_fuel_amount_invalid_setter_negative(self):
        with self.assertRaises(Exception) as exc:
            self.c.fuel_amount = -1
        msg = "Fuel amount cannot be negative!"
        self.assertEqual(msg, str(exc.exception))

    def test_refuel(self):
        self.c.refuel(10)
        self.assertEqual(self.c.fuel_amount, 10)

    def test_refuel_with_more_than_capacity(self):
        self.c.fuel_amount = 99
        self.c.refuel(2)
        self.assertEqual(self.c.fuel_amount, 100)

    def test_refuel_with_0_fill(self):
        with self.assertRaises(Exception) as exc:
            self.c.refuel(0)
        msg = "Fuel amount cannot be zero or negative!"
        self.assertEqual(msg, str(exc.exception))

    def test_refuel_with_negative_fill(self):
        with self.assertRaises(Exception) as exc:
            self.c.refuel(-1)
        msg = "Fuel amount cannot be zero or negative!"
        self.assertEqual(msg, str(exc.exception))

    def test_drive(self):
        self.c.refuel(10)
        self.c.drive(100)
        self.assertEqual(self.c.fuel_amount, 0)

    def test_drive_not_enough_fuel(self):
        self.c.refuel(1)
        with self.assertRaises(Exception) as exc:
            self.c.drive(100)
        msg = "You don't have enough fuel to drive!"
        self.assertEqual(msg, str(exc.exception))


if __name__ == '__main__':
    unittest.main()
