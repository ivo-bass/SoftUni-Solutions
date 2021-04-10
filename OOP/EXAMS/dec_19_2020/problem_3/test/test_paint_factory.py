from unittest import TestCase, main


from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    name = 'name'
    capacity = 10

    def setUp(self) -> None:
        self.pf = PaintFactory(
            name=self.name,
            capacity=self.capacity
        )

    def test_inherits_from_factory(self):
        self.assertIsInstance(self.pf, PaintFactory)
        self.assertIsInstance(self.pf, Factory)
        self.assertTrue(issubclass(PaintFactory, Factory))

    def test_init(self):
        self.assertEqual(self.name, self.pf.name)
        self.assertEqual(self.capacity, self.pf.capacity)
        self.assertDictEqual({}, self.pf.ingredients)
        # self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)
        self.assertEqual(self.pf.ingredients, self.pf.products)

    def test_add__with_valid_new(self):
        self.pf.add_ingredient('white', 1)
        self.assertDictEqual({'white': 1}, self.pf.ingredients)

    def test_add__with_valid_existing(self):
        self.pf.add_ingredient('white', 1)
        self.pf.add_ingredient('white', 1)
        self.assertDictEqual({'white': 2}, self.pf.ingredients)

    def test_add__with_invalid_name(self):
        with self.assertRaises(TypeError) as exc:
            self.pf.add_ingredient('sth', 1)
        # msg = "Ingredient of type sth not allowed in PaintFactory"
        # self.assertEqual(msg, str(exc.exception))

    def test_add__with_invalid_quantity(self):
        with self.assertRaises(ValueError) as exc:
            self.pf.add_ingredient('white', 100)
        # msg = "Not enough space in factory"
        # self.assertEqual(msg, str(exc.exception))

    def test_remove__with_valid_less_than_owned(self):
        self.pf.add_ingredient('white', 1)
        self.pf.add_ingredient('white', 1)
        self.pf.remove_ingredient('white', 1)
        self.assertDictEqual({'white': 1}, self.pf.ingredients)

    def test_remove__with_valid_all_quantity(self):
        self.pf.add_ingredient('white', 1)
        self.pf.add_ingredient('white', 1)
        self.pf.remove_ingredient('white', 2)
        self.assertDictEqual({'white': 0}, self.pf.ingredients)

    def test_remove__with_invalid_type(self):
        self.pf.add_ingredient('white', 1)
        with self.assertRaises(KeyError) as exc:
            self.pf.remove_ingredient('sth', 1)
        # msg = "'No such product in the factory'"
        # self.assertEqual(msg, str(exc.exception))

    def test_remove__with_invalid_quantity(self):
        self.pf.add_ingredient('white', 1)
        with self.assertRaises(ValueError) as exc:
            self.pf.remove_ingredient('white', 100)
        # msg = "Ingredient quantity cannot be less than zero"
        # self.assertEqual(msg, str(exc.exception))

    def test_can_add__with_value_result_less_than_0(self):
        self.pf.add_ingredient('white', 1)
        self.assertTrue(self.pf.can_add(8))

    def test_can_add__with_value_result_equal_to_0(self):
        self.pf.add_ingredient('white', 1)
        self.assertTrue(self.pf.can_add(9))

    def test_can_add__with_value_result_more_than_0(self):
        self.pf.add_ingredient('white', 1)
        self.assertFalse(self.pf.can_add(10))



if __name__ == '__main__':
    main()
