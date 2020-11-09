class Battle:
	def __init__(self, status_pirate, status_war, max_health):
		self.pirate_ship = status_pirate
		self.war_ship = status_war
		self.max_health = max_health

	def fire(self, index, dmg):
		if index in range(len(self.war_ship)):
			self.war_ship[index] -= dmg
			if self.war_ship[index] <= 0:
				print("You won! The enemy ship has sunken.")
				exit(1)

	def defend(self, start_i, end_i, dmg):
		if start_i in range(len(self.pirate_ship)) and end_i in range(len(self.pirate_ship)):
			for section in range(start_i, end_i + 1):
				self.pirate_ship[section] -= dmg
				if self.pirate_ship[section] <= 0:
					print("You lost! The pirate ship has sunken.")
					exit(2)

	def repair(self, index, health):
		if index in range(len(self.pirate_ship)):
			self.pirate_ship[index] += health
			if self.pirate_ship[index] > self.max_health:
				self.pirate_ship[index] = self.max_health

	def status(self):
		count_for_repair = 0
		for section in self.pirate_ship:
			if section < self.max_health * 0.2:
				count_for_repair += 1
		print(f"{count_for_repair} sections need repair.")

	def stalemate(self):
		pirate_ship_sum, war_ship_sum = sum(self.pirate_ship), sum(self.war_ship)
		print(f"Pirate ship status: {pirate_ship_sum}")
		print(f"Warship status: {war_ship_sum}")


def main():
	status_pirate_ship = [int(s) for s in input().split('>')]
	status_war_ship = [int(s) for s in input().split('>')]
	maximum_health = int(input())

	battle = Battle(status_pirate_ship, status_war_ship, maximum_health)

	data = input()
	while not data == "Retire":
		command = data.split()
		action = command[0]
		if action == "Fire":
			index, damage = command[1], command[2]
			index, damage = int(index), int(damage)
			battle.fire(index, damage)
		elif action == "Defend":
			start, end, damage = command[1], command[2], command[3]
			start, end, damage = int(start), int(end), int(damage)
			battle.defend(start, end, damage)
		elif action == "Repair":
			index, health = command[1], command[2]
			index, health = int(index), int(health)
			battle.repair(index, health)
		elif action == "Status":
			battle.status()
		data = input()
	battle.stalemate()


if __name__ == '__main__':
	main()
