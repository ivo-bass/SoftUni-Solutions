data = input()
resources = {}
all_input_list = []
while not data == "stop":
	all_input_list.append(data)
	data = input()

for index in range(0, len(all_input_list), 2):
	key = all_input_list[index]
	value = all_input_list[index + 1]
	if key not in resources.keys():
		resources[key] = int(value)
	else:
		resources[key] += int(value)

for item in resources.items():
	key, value = item
	print(f"{key} -> {value}")
