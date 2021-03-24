class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


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
