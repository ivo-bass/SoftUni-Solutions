def plunder(dic, city, people, gold):
	dic[city]["population"] -= people
	dic[city]["gold"] -= gold
	print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
	if dic[city]["population"] <= 0 or dic[city]["gold"] <= 0:
		print(f"{city} has been wiped off the map!")
		del dic[city]
	return dic


def prosper(dic, city, gold):
	if gold < 0:
		print("Gold added cannot be a negative number!")
		return dic
	dic[city]["gold"] += gold
	print(f"{gold} gold added to the city treasury. {city} now has {dic[city]['gold']} gold.")
	return dic


def get_data(dic):
	if not dic:
		print("Ahoy, Captain! All targets have been plundered and destroyed!")
		return
	a = 5
	dic = dict(sorted(dic.items(), key=lambda x: (-x[1]['gold'], x[0])))
	print(f"Ahoy, Captain! There are {len(dic)} wealthy settlements to go to:")
	for town, values in dic.items():
		print(f"{town} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")
	return


def main():
	towns = {}
	while True:
		data = input().split("||")
		if data[0] == "Sail":
			break
		name, population, gold = data[0], int(data[1]), int(data[2])
		if name not in towns:
			towns[name] = {"population": population, "gold": gold}
		else:
			towns[name]["population"] += population
			towns[name]["gold"] += gold

	while True:
		command = input().split("=>")
		if command[0] == "End":
			break
		action, town = command[0], command[1]
		if action == "Plunder":
			people, gold = int(command[2]), int(command[3])
			towns = plunder(towns, town, people, gold)
		elif action == "Prosper":
			gold = int(command[2])
			towns = prosper(towns, town, gold)
	get_data(towns)


main()
