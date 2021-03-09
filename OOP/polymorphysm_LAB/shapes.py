from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        # raise NotImplementedError('Subclass must Implement')
        pass

    @abstractmethod
    def calculate_perimeter(self):
        # raise NotImplementedError('Subclass must Implement')
        pass


class Circle(Shape):
    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        return pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, h, w):
        self.__height = h
        self.__width = w

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * self.__width + 2 * self.__height


# test circle
import unittest


class ShapesTests(unittest.TestCase):
    def test(self):
        c = Circle(5)
        self.assertEqual(c.calculate_area(), 78.53981633974483)
        self.assertEqual(c.calculate_perimeter(), 31.41592653589793)


if __name__ == "__main__":
    unittest.main()
