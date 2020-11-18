class Trip:
	def __init__(self, stops):
		self.stops = stops

	def add_stop(self, index, new):
		if index in range(len(self.stops)):
			self.stops = self.stops[:index] + new + self.stops[index:]

	def remove_stop(self, start, end):
		if start in range(len(self.stops)) and end in range(len(self.stops)):
			self.stops = self.stops[:start] + self.stops[end+1:]

	def switch(self, old, new):
		if old in self.stops:
			self.stops = self.stops.replace(old, new)


trip_1 = Trip(input())
data = input()
while not data == "Travel":
	action, value_1, value_2 = data.split(':')
	if action == "Add Stop":
		index = int(value_1)
		trip_1.add_stop(index, value_2)
		print(trip_1.stops)
	elif action == "Remove Stop":
		start, end = int(value_1), int(value_2)
		trip_1.remove_stop(start, end)
		print(trip_1.stops)
	elif action == "Switch":
		trip_1.switch(value_1, value_2)
		print(trip_1.stops)
	data = input()
print(f"Ready for world tour! Planned stops: {trip_1.stops}")
