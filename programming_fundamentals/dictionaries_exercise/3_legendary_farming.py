from sys import stdin

legendary = {
	"shards": "Shadowmourne",
	"fragments": "Valanyr",
	"motes": "Dragonwrath"
}

required = {
	"shards": 250,
	"fragments": 250,
	"motes": 250
}

materials = {}


def sort_alpha_asc(dic):
	sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[0])}
	return sorted_dic


def sort_quantity_desc(dic):
	sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
	return sorted_dic


def is_completed(dic):
	for key, value in dic.items():
		if key in required.keys():
			if value >= required[key]:
				return key, value


def output(win, req, junk):
	print(f"{win} obtained!")
	for key, value in req.items():
		print(f"{key}: {value}")
	for key, value in junk.items():
		print(f"{key}: {value}")


lines = stdin.read().split()

for index in range(0, len(lines) - 1, 2):
	material = lines[index + 1].lower()
	quantity = int(lines[index])
	if material not in materials.keys():
		materials[material] = quantity
	else:
		materials[material] += quantity
	if is_completed(materials):
		break


win_material, win_quantity = is_completed(materials)
winner = legendary[win_material]

for key, value in required.items():
	if materials.get(key):
		required[key] = materials[key]

for key, value in required.items():
	if value >= 250:
		required[key] -= 250

for key in required.keys():
	if key in materials.keys():
		del materials[key]

required = sort_alpha_asc(required)
required = sort_quantity_desc(required)

materials = sort_alpha_asc(materials)

output(winner, required, materials)
