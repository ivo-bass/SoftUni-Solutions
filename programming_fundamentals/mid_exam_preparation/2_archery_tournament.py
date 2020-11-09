class Field:
	def __init__(self, field):
		self.field = field
		self.player_points = 0

	def shoot(self, target, index):
		if index in range(len(self.field)):
			if self.field[target] < 5:
				self.player_points += self.field[target]
				self.field[target] = 0
			else:
				self.player_points += 5
				self.field[target] -= 5

	def shoot_left(self, index, length):
		target_index = (index - length) % len(self.field)
		self.shoot(target_index, index)

	def shoot_right(self, index, length):
		target_index = (index + length) % len(self.field)
		self.shoot(target_index, index)

	def reverse(self):
		self.field = self.field[::-1]

	def game_over(self):
		print(" - ".join(map(str, self.field)))
		print(f"Iskren finished the archery tournament with {self.player_points} points!")


def main():
	field = Field([int(i) for i in input().split("|")])
	data = input()
	while not data == "Game over":
		command = data.split()
		type_command = command[0]
		if type_command == "Shoot":
			direction, index, length = command[1].split("@")
			index, length = int(index), int(length)
			if direction == "Left":
				field.shoot_left(index, length)
			elif direction == "Right":
				field.shoot_right(index, length)
		elif type_command == "Reverse":
			field.reverse()
		data = input()
	field.game_over()


if __name__ == '__main__':
	main()
