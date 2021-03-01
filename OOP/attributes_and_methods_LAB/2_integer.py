class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) is not float:
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(value):
            if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if type(value) is not str:
            return 'wrong type'
        return cls(int(value))

    def add(self, integer):
        if type(integer) is not Integer:
            return 'number should be an Integer instance'
        return self.value + integer.value


import unittest


class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")

    def test_add_success(self):
        first_integer = Integer(10)
        second_integer = Integer(12)
        result = first_integer.add(second_integer)
        self.assertEqual(result, 22)

    def test_add_error(self):
        first_integer = Integer(10)
        second_integer = 12
        result = first_integer.add(second_integer)
        self.assertEqual(result, "number should be an Integer instance")


if __name__ == "__main__":
    unittest.main()
