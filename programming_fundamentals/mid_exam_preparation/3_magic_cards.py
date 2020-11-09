class Deck:
	def __init__(self, deck):
		self.available = deck
		self.new_deck = []

	def __repr__(self):
		return " ".join(self.new_deck)

	def add_card(self, name):
		if name not in self.available:
			print("Card not found.")
			return
		self.new_deck.append(name)

	def insert_card(self, name, index):
		if name not in self.available or index not in range(len(self.new_deck)):
			print("Error!")
			return
		self.new_deck.insert(index, name)

	def remove_card(self, name):
		if name not in self.new_deck:
			print("Card not found.")
			return
		self.new_deck.remove(name)

	def swap_cards(self, name1, name2):
		i1, i2 = self.new_deck.index(name1), self.new_deck.index(name2)
		self.new_deck[i1], self.new_deck[i2] = self.new_deck[i2], self.new_deck[i1]

	def shuffle(self):
		self.new_deck = list(reversed(self.new_deck))


def main():
	deck = Deck(input().split(":"))

	data = input()
	while not data == "Ready":
		command = data.split()
		action = command[0]
		if action == "Add":
			name = command[1]
			deck.add_card(name)
		elif action == "Insert":
			name, index = command[1], command[2]
			index = int(index)
			deck.insert_card(name, index)
		elif action == "Remove":
			name = command[1]
			deck.remove_card(name)
		elif action == "Swap":
			name1, name2 = command[1], command[2]
			deck.swap_cards(name1, name2)
		elif action == "Shuffle":
			deck.shuffle()
		data = input()

	print(deck)


if __name__ == '__main__':
	main()
