def contains(raw_str, substring):
	if substring in raw_str:
		return f"{raw_str} contains {substring}"
	return "Substring not found!"


def flip_str(raw_str, direction, start_i, end_i):
	if direction == "Upper":
		changed = raw_str[start_i:end_i].upper()
	else:
		changed = raw_str[start_i:end_i].lower()
	return raw_str[:start_i] + changed + raw_str[end_i:]


def slice_str(raw_str, start_i, end_i):
	return raw_str[:start_i] + raw_str[end_i:]


def main():
	raw_key = input()
	while True:
		command = input().split(">>>")
		action = command[0]
		if action == "Generate":
			print(f"Your activation key is: {raw_key}")
			break
		if action == "Contains":
			substring = command[1]
			print(contains(raw_key, substring))
		elif action == "Flip":
			direction, start_i, end_i = command[1], int(command[2]), int(command[3])
			raw_key = flip_str(raw_key, direction, start_i, end_i)
			print(raw_key)
		elif action == "Slice":
			start_i, end_i = int(command[1]), int(command[2])
			raw_key = slice_str(raw_key, start_i, end_i)
			print(raw_key)


main()
