from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    name = 'Name'
    capacity = 2
    passenger = 'passenger'

    def setUp(self) -> None:
        self.train = Train(self.name, self.capacity)

    def test_init(self):
        self.assertEqual(self.name, self.train.name)
        self.assertEqual(self.capacity, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test_add__when_all_valid__expect_append_and_return_msg(self):
        expected = f"Added passenger {self.passenger}"
        actual = self.train.add(self.passenger)
        self.assertListEqual([self.passenger], self.train.passengers)
        self.assertEqual(expected, actual)

    def test_add__when_train_is_full__expect_raise_value_error(self):
        self.train.add(self.passenger)
        self.train.add('new1')
        with self.assertRaises(ValueError) as context:
            self.train.add('new2')
        expected = "Train is full"
        self.assertEqual(expected, str(context.exception))

    def test_add__when_passenger_already_in_train__expect_raise_value_error(self):
        self.train.add(self.passenger)
        with self.assertRaises(ValueError) as context:
            self.train.add(self.passenger)
        expected = f"Passenger {self.passenger} Exists"
        self.assertEqual(expected, str(context.exception))

    def test_remove__when_all_valid__expect_remove_and_return_msg(self):
        self.train.add(self.passenger)
        expected = f"Removed {self.passenger}"
        actual = self.train.remove(self.passenger)
        self.assertListEqual([], self.train.passengers)
        self.assertEqual(expected, actual)

    def test_remove__when_passenger_not_in_train__expect_raise_value_error(self):
        self.train.add(self.passenger)
        with self.assertRaises(ValueError) as context:
            self.train.remove('new')
        expected = "Passenger Not Found"
        self.assertEqual(expected, str(context.exception))


if __name__ == '__main__':
    main()
