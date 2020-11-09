class Sequence:
	def __init__(self, seq):
		self.seq = seq

	def __repr__(self):
		return " ".join(map(str, self.seq))

	def add_cube(self, value):
		self.seq.append(value)

	def remove_cube(self, value):
		self.seq.remove(value)

	def replace_cube(self, old, new):
		index = self.seq.index(old)
		self.seq[index] = new

	def collapse_cube(self, value):
		self.seq = list(filter(lambda x: x >= value, self.seq))

	def mort(self):
		print(self)


def main():
	seq = Sequence([int(s) for s in input().split()])
	data = input()
	while not data == "Mort":
		command = data.split()
		action = command[0]
		if action == "Add":
			value = int(command[1])
			seq.add_cube(value)
		if action == "Remove":
			value = int(command[1])
			seq.remove_cube(value)
		if action == "Replace":
			old, new = int(command[1]), int(command[2])
			seq.replace_cube(old, new)
		if action == "Collapse":
			value = int(command[1])
			seq.collapse_cube(value)
		data = input()
	seq.mort()


if __name__ == '__main__':
	main()
