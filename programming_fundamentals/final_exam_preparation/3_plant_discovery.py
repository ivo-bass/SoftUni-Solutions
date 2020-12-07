def rate_plant(dic, pl, rat):
	if pl in dic:
		dic[pl]["ratings"].append(rat)
		return dic, False
	return dic, True


def update_plant(dic, pl, new_rarity):
	if pl in dic:
		dic[pl]["rarity"] = new_rarity
		return dic, False
	return dic, True


def reset_plant(dic, pl):
	if pl in dic:
		dic[pl]["ratings"] = []
		return dic, False
	return dic, True


def calculate_avrg_ratings(dic):
	for name, values in dic.items():
		if values["ratings"]:
			dic[name]["ratings"] = sum(values["ratings"]) / len(values["ratings"])
		else:
			dic[name]["ratings"] = 0
	return dic


def print_data(dic):
	dic = calculate_avrg_ratings(dic)
	dic = dict(sorted(dic.items(), key=lambda x: (-x[1]["rarity"], -x[1]["ratings"])))
	print("Plants for the exhibition:")
	for name, values in dic.items():
		print(f"- {name}; Rarity: {values['rarity']}; Rating: {values['ratings']:.2f}")


def get_input_data():
	collection = {}
	n = int(input())
	for _ in range(n):
		plant, rarity = input().split("<->")
		if plant in collection:
			collection[plant]["rarity"] += int(rarity)
		else:
			collection[plant] = {"rarity": int(rarity), "ratings": []}
	return collection


def main():
	collection = get_input_data()
	while True:
		command = input()
		if command == "Exhibition":
			print_data(collection)
			break
		action, data = command.split(": ")
		data = data.split(" - ")
		if action == "Rate":
			plant, rating = data[0], int(data[1])
			collection, is_invalid = rate_plant(collection, plant, rating)
		elif action == "Update":
			plant, rarity = data[0], int(data[1])
			collection, is_invalid = update_plant(collection, plant, rarity)
		elif action == "Reset":
			plant = data[0]
			collection, is_invalid = reset_plant(collection, plant)
		else:
			is_invalid = True
		if is_invalid:
			print("error")


main()
