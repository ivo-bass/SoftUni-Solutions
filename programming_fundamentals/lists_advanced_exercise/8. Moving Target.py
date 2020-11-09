def process_data(d):
	"""Takes the input and returns processed values
	for command, index and value."""
	com, i, v = d.split()
	return com, int(i), int(v)


def is_valid_index(index, t_list):
	"""Checks if the given index is in the range of the list."""
	if index in range(len(t_list)):
		return True


def shoot(index, power, t_list):
	"""Performs the 'shoot' command."""
	if is_valid_index(index, t_list):
		t_list[index] -= power
		if t_list[index] <= 0:
			t_list.pop(index)
	return t_list


def add(index, val, t_list):
	"""Performs the 'add' command."""
	if is_valid_index(index, t_list):
		t_list.insert(index, val)
	else:
		print("Invalid placement!")
	return t_list


def strike(index, radius, t_list):
	"""Performs the 'strike' command."""
	start = index - radius
	end = index + radius
	if start >= 0 and end < len(t_list):
		t_list = t_list[:start] + t_list[end + 1:]
	else:
		print("Strike missed!")
	return t_list


def end(t_list):
	"""Prints joined result list of mapped to string integers."""
	print("|".join(map(str, t_list)))


def main():
	targets = [int(s) for s in input().split()]
	data = input()
	while not data == "End":
		command, index, value = process_data(data)
		if command == "Shoot":
			targets = shoot(index, value, targets)
		elif command == "Add":
			targets = add(index, value, targets)
		elif command == "Strike":
			targets = strike(index, value, targets)
		data = input()
	end(targets)


if __name__ == '__main__':
	main()
