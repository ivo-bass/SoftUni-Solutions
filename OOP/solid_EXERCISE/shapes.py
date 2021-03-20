from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calc_area(self):
        return 1 / 2 * self.b * self.h


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        return sum([shape.calc_area() for shape in self.shapes])


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
