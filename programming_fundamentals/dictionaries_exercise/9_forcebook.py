class ForceBook:
	def __init__(self):
		self.sides = {}
		self.all_users = []

	def add_user(self, side, user):
		if side not in self.sides:
			self.sides[side] = [user]
			self.all_users.append(user)
		else:
			if user not in self.all_users:
				self.all_users.append(user)
				self.sides[side].append(user)

	def change_side(self, side, user):
		for key, value in self.sides.items():
			if user in value and not side == key:
				self.sides[key].remove(user)
				if side not in self.sides:
					self.sides[side] = [user]
				else:
					self.sides[side].append(user)
				break

	def sort_sides(self):
		self.sides = dict(sorted(self.sides.items(), key=lambda x: x[0]))
		self.sides = dict(sorted(self.sides.items(), key=lambda x: len(x[1]), reverse=True))

	def get_info(self):
		self.sort_sides()
		for side, users in self.sides.items():
			count = len(users)
			if count > 0:
				print(f"Side: {side}, Members: {count}")
				users = list(sorted(users))
				for user in users:
					print(f"! {user}")


def main():
	f_b = ForceBook()
	data = input()
	while not data == "Lumpawaroo":
		if " | " in data:
			command = data.split(" | ")
			side, user = command[0], command[1]
			if user not in f_b.all_users:
				f_b.add_user(side, user)
		elif " -> " in data:
			command = data.split(" -> ")
			user, side = command[0], command[1]
			if user in f_b.all_users:
				f_b.change_side(side, user)
			elif user not in f_b.all_users:
				f_b.add_user(side, user)
			print(f"{user} joins the {side} side!")
		data = input()
	f_b.get_info()


if __name__ == '__main__':
	main()
