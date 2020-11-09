class Circle:
	def __init__(self, diameter):
		self.diameter = diameter
		self.radius = diameter / 2
		self.pi = 3.14

	def calculate_circumference(self):
		return self.pi * self.diameter

	def calculate_area(self):
		return self.pi * self.radius ** 2

	def calculate_area_of_sector(self, angle):
		return (angle / 360) * self.calculate_area()
