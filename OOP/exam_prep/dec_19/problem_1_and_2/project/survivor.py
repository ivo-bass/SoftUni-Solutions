class Survivor:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100

    @property
    def needs_sustenance(self):
        return 0 <= self.needs < 100

    @property
    def needs_healing(self):
        return 0 <= self.health < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        self.__health = value
        if self.__health > 100:
            self.__health = 100

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        self.__needs = value
        if self.__needs > 100:
            self.__needs = 100


# from unittest import TestCase, main
#
#
# class TestSurvivor(TestCase):
#     def setUp(self) -> None:
#         self.s = Survivor('name', 11)
#
#     def test_init(self):
#         self.assertEqual('name', self.s.name)
#         self.assertEqual(11, self.s.age)
#         self.assertEqual(100, self.s.health)
#         self.assertEqual(100, self.s.needs)
#         self.assertFalse(self.s.needs_healing)
#         self.assertFalse(self.s.needs_sustenance)
#
#     def test_invalid_init(self):
#         with self.assertRaises(ValueError) as exc:
#             Survivor('', 11)
#         self.assertEqual("Name not valid!", str(exc.exception))
#
#         with self.assertRaises(ValueError) as exc:
#             Survivor('asd', -1)
#         self.assertEqual("Age not valid!", str(exc.exception))
#
#         with self.assertRaises(ValueError) as exc:
#             s = Survivor('asd', 11)
#             s.health = -1
#         self.assertEqual("Health not valid!", str(exc.exception))
#
#         s.health = 110
#         self.assertEqual(100, s.health)
#
#         with self.assertRaises(ValueError) as exc:
#             s = Survivor('asd', 11)
#             s.needs = -1
#         self.assertEqual("Needs not valid!", str(exc.exception))
#
#         s.needs = 110
#         self.assertEqual(100, s.needs)
#
#         with self.assertRaises(ValueError) as exc:
#             Survivor('', 11)
#         self.assertEqual("Name not valid!", str(exc.exception))
#
#     def test_needs_sustenance(self):
#         self.s.needs = 99
#         self.assertTrue(self.s.needs_sustenance)
#
#     def test_needs_healing(self):
#         self.s.health = 99
#         self.assertTrue(self.s.needs_healing)
#
#
# if __name__ == '__main__':
#     main()