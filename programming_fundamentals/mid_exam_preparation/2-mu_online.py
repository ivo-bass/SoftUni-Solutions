class Player:
	def __init__(self):
		self.health = 100
		self.coins = 0
		self.is_alive = True

	def get_potion(self, value):
		if value + self.health > 100:
			value = 100 - self.health
		self.health += value

		print(f"You healed for {value} hp.")
		print(f"Current health: {self.health} hp.")

	def get_chest(self, amount):
		self.coins += amount
		print(f"You found {amount} bitcoins.")

	def fight_monster(self, monster, attack):
		self.health -= attack
		if self.health > 0:
			print(f"You slayed {monster}.")
		else:
			print(f"You died! Killed by {monster}.")
			self.is_alive = False


class PlayGame:
	def __init__(self, player, commands):
		self.player = player
		self.commands = commands
		self.room_number = 0

	def play(self):
		for command in self.commands:
			self.room_number += 1
			action, value = command.split()
			value = int(value)
			if action == "potion":
				self.player.get_potion(value)
			elif action == "chest":
				self.player.get_chest(value)
			else:
				self.player.fight_monster(action, value)
				if not self.player.is_alive:
					break

	def over(self):
		if self.player.is_alive:
			print(f"You've made it!")
			print(f"Bitcoins: {self.player.coins}")
			print(f"Health: {self.player.health}")
		else:
			print(f"Best room: {self.room_number}")


def main():
	commands = input().split("|")
	player = Player()
	game = PlayGame(player, commands)
	game.play()
	game.over()


if __name__ == '__main__':
	main()
