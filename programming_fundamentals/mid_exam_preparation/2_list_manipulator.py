class FriendList:
	def __init__(self, fr):
		self.friends = fr

	def __repr__(self):
		return " ".join(self.friends)

	def blacklist(self, name):
		if name not in self.friends:
			print(f"{name} was not found.")
		else:
			index = self.friends.index(name)
			self.friends[index] = "Blacklisted"
			print(f"{name} was blacklisted.")

	def error(self, index):
		if index in range(len(self.friends)):
			name = self.friends[index]
			if not name == "Blacklisted" and not name == "Lost":
				self.friends[index] = "Lost"
				print(f"{name} was lost due to an error.")

	def change(self, index, new_name):
		if index in range(len(self.friends)):
			currant_name = self.friends[index]
			self.friends[index] = new_name
			print(f"{currant_name} changed his username to {new_name}.")

	def report(self):
		print(f"Blacklisted names: {self.friends.count('Blacklisted')}")
		print(f"Lost names: {self.friends.count('Lost')}")
		print(self)


def main():
	fr_list = FriendList(input().split(", "))
	while True:
		command = input()
		if command == "Report":
			fr_list.report()
			break
		action, *data = command.split()
		if action == "Blacklist":
			name = data[0]
			fr_list.blacklist(name)
		elif action == "Error":
			index = int(data[0])
			fr_list.error(index)
		elif action == "Change":
			index, new_name = int(data[0]), data[1]
			fr_list.change(index, new_name)


if __name__ == '__main__':
	main()
