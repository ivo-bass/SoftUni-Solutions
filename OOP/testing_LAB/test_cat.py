class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    name = 'CatName'

    def setUp(self) -> None:
        self.cat = Cat(self.name)

    def test_initialize(self):
        self.assertEqual(self.name, self.cat.name)

    def test_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_raises_error_when_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        msg = 'Already fed.'
        self.assertEqual(msg, str(exc.exception))

    def test_becomes_sleepy_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_raises_exception_if_not_fed_when_trying_to_sleep(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        msg = 'Cannot sleep while hungry'
        self.assertEqual(msg, str(exc.exception))

    def test_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
