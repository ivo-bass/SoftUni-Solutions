arr_values_string = input()
array = [int(i) for i in arr_values_string.split(' ')]

while True:
	command_str = input()
	command = command_str.split(' ')
	operation = command[0]

	if operation == 'end':
		break
	elif operation == 'decrease':
		array = [i - 1 for i in array]
	else:
		index1 = int(command[1])
		index2 = int(command[2])
		if operation == 'swap':
			array[index1], array[index2] = array[index2], array[index1]
		if operation == 'multiply':
			array[index1] = array[index1] * array[index2]

print(', '.join(map(str, array)))
