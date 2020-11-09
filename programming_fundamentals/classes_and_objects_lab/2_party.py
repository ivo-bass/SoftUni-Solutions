class Person:
	def __init__(self, name):
		self.name = name


class Party:
	def __init__(self):
		self.people = []

	def attend(self, person):
		self.people.append(person)

	def going(self):
		return ", ".join([person.name for person in self.people])

	def total(self):
		return len(self.people)


def main():
	party = Party()
	command = input()
	while not command == "End":
		name = command
		person = Person(name)
		party.attend(person)
		command = input()
	print(f"Going: {party.going()}")
	print(f"Total: {party.total()}")


if __name__ == '__main__':
	main()
