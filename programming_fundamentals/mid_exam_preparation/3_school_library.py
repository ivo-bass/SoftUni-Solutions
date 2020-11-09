class Library:
	def __init__(self, books):
		self.collection = books

	def add(self, name):
		if name not in self.collection:
			self.collection.insert(0, name)

	def take(self, name):
		if name in self.collection:
			self.collection.remove(name)

	def swap(self, name1, name2):
		if name1 in self.collection and name2 in self.collection:
			i1, i2 = self.collection.index(name1), self.collection.index(name2)
			self.collection[i1], self.collection[i2] = self.collection[i2], self.collection[i1]

	def insert(self, name):
		self.collection.append(name)

	def check(self, index):
		if index in range(len(self.collection)):
			print(self.collection[index])

	def print_lib(self):
		print(", ".join(self.collection))


def main():
	lib = Library(input().split("&"))
	command = input()
	while not command == "Done":
		action, book = command.split(" | ", maxsplit=1)
		if action == "Add Book":
			lib.add(book)
		elif action == "Take Book":
			lib.take(book)
		elif action == "Swap Books":
			book1, book2 = book.split(" | ")
			lib.swap(book1, book2)
		elif action == "Insert Book":
			lib.insert(book)
		elif action == "Check Book":
			index = int(book)
			lib.check(index)
		command = input()
	lib.print_lib()


if __name__ == '__main__':
	main()
