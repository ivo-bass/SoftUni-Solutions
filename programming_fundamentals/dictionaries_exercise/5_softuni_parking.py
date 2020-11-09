class DataBase:
	def __init__(self):
		self.db = {}

	def register(self, name, plate):
		if name in self.db.keys():
			print(f"ERROR: already registered with plate number {plate}")
			return
		self.db[name] = plate
		print(f"{name} registered {plate} successfully")

	def unregister(self, name):
		if not name in self.db.keys():
			print(f"ERROR: user {name} not found")
			return
		del self.db[name]
		print(f"{name} unregistered successfully")

	def print_data(self):
		for name, plate in self.db.items():
			print(f"{name} => {plate}")


def main():
	db = DataBase()
	commands = int(input())
	for _ in range(commands):
		command = input().split()
		action, name = command[0], command[1]
		if action == "register":
			plate = command[2]
			db.register(name, plate)
		elif action == "unregister":
			db.unregister(name)
	db.print_data()


if __name__ == '__main__':
	main()
