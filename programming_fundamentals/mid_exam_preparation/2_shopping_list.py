class ShoppingList:
	def __init__(self, initial_list):
		self.li = initial_list

	def __repr__(self):
		return ", ".join(self.li)

	def urgent(self, item):
		if item not in self.li:
			self.li.insert(0, item)

	def unnecessary(self, item):
		if item in self.li:
			self.li.remove(item)

	def correct(self, old, new):
		if old in self.li:
			index = self.li.index(old)
			self.li[index] = new

	def rearrange(self, item):
		if item in self.li:
			self.li.remove(item)
			self.li.append(item)


def main():
	shopping_list = ShoppingList(input().split("!"))

	while not (command := input()) == "Go Shopping!":
		command = command.split()
		command_type = command[0]
		item = command[1]
		if command_type == "Urgent":
			shopping_list.urgent(item)
		elif command_type == "Unnecessary":
			shopping_list.unnecessary(item)
		elif command_type == "Rearrange":
			shopping_list.rearrange(item)
		elif command_type == "Correct":
			new_item = command[2]
			shopping_list.correct(item, new_item)

	print(shopping_list)


if __name__ == '__main__':
	main()
