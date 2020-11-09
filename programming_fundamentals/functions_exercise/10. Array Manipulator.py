"""Trifon has finally become a junior developer and has received his first task. It's about manipulating an array of
integers. He is not quite happy about it, since he hates manipulating arrays. They are going to pay him a lot of
money, though, and he is willing to give somebody half of it if to help him do his job. You, on the other hand,
love arrays (and money) so you decide to try your luck. """

# THIS IS INSANELY STUPID EXERCISE!


def exchange(arr, index):
	"""Splits the array after the given index, and exchanges the places of the two resulting sub-arrays.
	E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]"""
	if index <= -1 or index >= len(arr):
		print("Invalid index")
		return arr
	arr = arr[index + 1:] + arr[:index + 1]
	return arr


def max_even(arr):
	"""returns the INDEX of the max even element -> [1, 4, 8, 2, 3] -> max even -> print 2
	If there are two or more equal min/max elements, return the index of the rightmost one
	If a min/max even/odd element cannot be found, print "No matches" """
	found = False
	index = None
	max_even_num = 0
	for i in range(len(arr)):
		if arr[i] % 2 == 0:
			found = True
			if arr[i] >= max_even_num:
				max_even_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def max_odd(arr):
	"""returns the INDEX of the max odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
	If there are two or more equal min/max elements, return the index of the rightmost one
	If a min/max even/odd element cannot be found, print "No matches" """
	found = False
	index = None
	max_odd_num = 0
	for i in range(len(arr)):
		if arr[i] % 2 != 0:
			found = True
			if arr[i] >= max_odd_num:
				max_odd_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def min_even(arr):
	"""returns the INDEX of the min even element -> [1, 4, 8, 2, 3] -> min even > print 3
	If there are two or more equal min/max elements, return the index of the rightmost one
	If a min/max even/odd element cannot be found, print "No matches" """
	found = False
	index = None
	min_even_num = 1001
	for i in range(len(arr)):
		if arr[i] % 2 == 0:
			found = True
			if arr[i] <= min_even_num:
				min_even_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def min_odd(arr):
	"""returns the INDEX of the min odd element -> [1, 4, 8, 2, 3] -> min even > print 0
	If there are two or more equal min/max elements, return the index of the rightmost one
	If a min/max even/odd element cannot be found, print "No matches" """
	found = False
	index = None
	min_odd_num = 1001
	for i in range(len(arr)):
		if arr[i] % 2 != 0:
			found = True
			if arr[i] <= min_odd_num:
				min_odd_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def first_even(arr, count):
	"""returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
	If the count is greater than the array length, print "Invalid count"
	If there are not enough elements to satisfy the count, print as many as you can.
	If there are zero even/odd elements, print an empty array "[]" """
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for num in arr:
		if num % 2 == 0 and count > 0:
			result.append(num)
			count -= 1
	return result


def first_odd(arr, count):
	"""returns the first {count} elements -> [1, 8, 2, 3] -> first 2 odd -> print [1, 3]
	If the count is greater than the array length, print "Invalid count"
	If there are not enough elements to satisfy the count, print as many as you can.
	If there are zero even/odd elements, print an empty array "[]" """
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for num in arr:
		if num % 2 != 0 and count > 0:
			result.append(num)
			count -= 1
	return result


def last_even(arr, count):
	"""returns the last {count} elements -> [1, 8, 2, 3] -> last 2 even -> print [8, 2]
	If the count is greater than the array length, print "Invalid count"
	If there are not enough elements to satisfy the count, print as many as you can.
	If there are zero even/odd elements, print an empty array "[]" """
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for index in range(len(arr) - 1, -1, -1):
		if arr[index] % 2 == 0 and count > 0:
			result.append(arr[index])
			count -= 1
	result = result[::-1]
	return result


def last_odd(arr, count):
	"""returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
	If the count is greater than the array length, print "Invalid count"
	If there are not enough elements to satisfy the count, print as many as you can.
	If there are zero even/odd elements, print an empty array "[]" """
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for index in range(len(arr) - 1, -1, -1):
		if arr[index] % 2 != 0 and count > 0:
			result.append(arr[index])
			count -= 1
	result = result[::-1]
	return result


def array_manipulator():
	"""The array may be manipulated by commands.
	The input data should be read from the console.
	On the first line, the initial array is received as a line of integers, separated by a single space
	On the next lines, until the command "end" is received, you will receive the array manipulation commands
	The input data will always be valid. There is no need to check it explicitly."""
	array_string = input()
	array = [int(n) for n in array_string.split()]

	while True:
		command = input().split()
		if command[0] == "end":
			print(array)
			break
		elif command[0] == "exchange":
			array = exchange(array, int(command[1]))
		elif command[0] == "max":
			if command[1] == "even":
				print(max_even(array))
			elif command[1] == "odd":
				print(max_odd(array))
		elif command[0] == "min":
			if command[1] == "even":
				print(min_even(array))
			elif command[1] == "odd":
				print(min_odd(array))
		elif command[0] == "first":
			if command[2] == "even":
				print(first_even(array, int(command[1])))
			elif command[2] == "odd":
				print(first_odd(array, int(command[1])))
		elif command[0] == "last":
			if command[2] == "even":
				print(last_even(array, int(command[1])))
			elif command[2] == "odd":
				print(last_odd(array, int(command[1])))


array_manipulator()
