import unittest

from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    fuel = 50.0
    horse_power = 100.0

    def setUp(self) -> None:
        self.v = Vehicle(self.fuel, self.horse_power)

    def test_vehicle_init(self):
        self.assertEqual(self.fuel, self.v.fuel)
        self.assertEqual(self.v.fuel, self.v.capacity)
        self.assertEqual(self.horse_power, self.v.horse_power)
        self.assertEqual(1.25, self.v.fuel_consumption)

    def test_drive_1_km__when_enough_fuel__should_decrement_fuel(self):
        self.v.drive(1)
        expected = self.fuel - 1.25
        self.assertEqual(expected, self.v.fuel)

    def test_drive_100_km__when_not_enough_fuel__should_raise_exception(self):
        with self.assertRaises(Exception) as exc:
            self.v.drive(100)
        msg = "Not enough fuel"
        self.assertEqual(msg, str(exc.exception))

    def test_refuel__with_valid_fuel_10(self):
        self.v.fuel = 10
        self.v.refuel(10)
        self.assertEqual(20, self.v.fuel)

    def test_refuel_with_more_fuel_than_capacity(self):
        with self.assertRaises(Exception) as exc:
            self.v.refuel(100)
        msg = "Too much fuel"
        self.assertEqual(msg, str(exc.exception))

    def test_vehicle_string_representation(self):
        expected = "The vehicle has 100.0 horse power with 50.0 fuel left and 1.25 fuel consumption"
        actual = self.v.__str__()
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
