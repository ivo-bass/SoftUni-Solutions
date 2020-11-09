class Inventory:
	def __init__(self, data):
		self.inventory = data

	def __repr__(self):
		return ", ".join(self.inventory)

	def collect(self, item):
		if item not in self.inventory:
			self.inventory.append(item)

	def drop(self, item):
		if item in self.inventory:
			self.inventory.remove(item)

	def combine_items(self, items):
		old, new = items.split(":")
		if old in self.inventory:
			self.inventory.insert(self.inventory.index(old) + 1, new)

	def renew(self, item):
		if item in self.inventory:
			self.inventory.remove(item)
			self.inventory.append(item)


def main():
	data = input().split(", ")
	inventory = Inventory(data)
	command = input()
	while not command == "Craft!":
		action, item = command.split(" - ")
		if action == "Collect":
			inventory.collect(item)
		elif action == "Drop":
			inventory.drop(item)
		elif action == "Combine Items":
			inventory.combine_items(item)
		elif action == "Renew":
			inventory.renew(item)
		command = input()
	print(inventory)


if __name__ == '__main__':
	main()
