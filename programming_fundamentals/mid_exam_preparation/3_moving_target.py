class Targets:
	def __init__(self, targets):
		self.targets = targets

	def __repr__(self):
		"""Returns joined result list of mapped to string integers."""
		return "|".join(map(str, self.targets))

	def is_valid_index(self, index):
		"""Checks if the given index is in the range of the list."""
		if index in range(len(self.targets)):
			return True

	def shoot(self, index, power):
		"""Performs the 'shoot' command."""
		if self.is_valid_index(index):
			self.targets[index] -= power
			if self.targets[index] <= 0:
				self.targets.pop(index)

	def add(self, index, val):
		"""Performs the 'add' command."""
		if self.is_valid_index(index):
			self.targets.insert(index, val)
		else:
			print("Invalid placement!")

	def strike(self, index, radius):
		"""Performs the 'strike' command."""
		start = index - radius
		end = index + radius
		if start >= 0 and end < len(self.targets):
			self.targets = self.targets[:start] + self.targets[end + 1:]
		else:
			print("Strike missed!")


def process_data(d):
	"""Takes the input and returns processed values
	for command, index and value."""
	com, i, v = d.split()
	return com, int(i), int(v)


def main():
	targets = Targets([int(s) for s in input().split()])
	data = input()
	while not data == "End":
		command, index, value = process_data(data)
		if command == "Shoot":
			targets.shoot(index, value)
		elif command == "Add":
			targets.add(index, value)
		elif command == "Strike":
			targets.strike(index, value)
		data = input()
	print(targets)


if __name__ == '__main__':
	main()
