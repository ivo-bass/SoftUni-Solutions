import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    name = 'name'
    mammal_type = 'type'
    sound = 'sound'
    kingdom = 'animals'

    def setUp(self) -> None:
        self.m = Mammal(self.name, self.mammal_type, self.sound)

    def test_mammal_init(self):
        self.assertEqual(self.name, self.m.name)
        self.assertEqual(self.mammal_type, self.m.type)
        self.assertEqual(self.sound, self.m.sound)
        self.assertEqual(self.kingdom, self.m._Mammal__kingdom)

    def test_make_sound__should_return_sound_string(self):
        expected = "name makes sound"
        actual = self.m.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom__returns_animals(self):
        expected = "animals"
        actual = self.m.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info__should_return_valid_text(self):
        expected = "name is of type type"
        actual = self.m.info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
