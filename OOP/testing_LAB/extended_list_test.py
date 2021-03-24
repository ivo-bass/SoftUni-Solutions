import unittest


class IntegerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = IntegerList([])

    def test_add(self):
        self.assertEqual(self.obj.add(42), [42])

    def test_add_string_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.obj.add('42')
        self.assertEqual(str(exc.exception), "Element is not Integer")

    def test_remove_index(self):
        self.obj.add(42)
        self.assertEqual(self.obj.remove_index(0), 42)

    def test_remove_invalid_index_raises_exception(self):
        self.obj.add(42)
        with self.assertRaises(IndexError) as exc:
            self.obj.remove_index(1)
        self.assertEqual(str(exc.exception), "Index is out of range")

    def test_init_takes_only_integers(self):
        ll = IntegerList('42', 42)
        self.assertEqual(ll.get_data(), [42])

    def test_get(self):
        self.obj.add(42)
        self.assertEqual(self.obj.get(0), 42)

    def test_get_with_invalid_index_raises_exception(self):
        self.obj.add(42)
        with self.assertRaises(IndexError) as exc:
            self.obj.get(1)
        self.assertEqual(str(exc.exception), "Index is out of range")

    def test_insert(self):
        self.obj.add(42)
        self.obj.insert(0, 100)
        self.assertEqual(self.obj.get(0), 100)

    def test_insert_raises_index_error(self):
        with self.assertRaises(IndexError) as exc:
            self.obj.insert(0, 42)
        self.assertEqual(str(exc.exception), "Index is out of range")

    def test_insert_raises_value_error(self):
        self.obj.add(42)
        with self.assertRaises(ValueError) as exc:
            self.obj.insert(0, '42')
        self.assertEqual(str(exc.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.obj.add(42)
        self.obj.add(43)
        self.assertEqual(self.obj.get_biggest(), 43)

    def test_get_index(self):
        self.obj.add(42)
        self.assertEqual(self.obj.get_index(42), 0)


if __name__ == '__main__':
    unittest.main()
