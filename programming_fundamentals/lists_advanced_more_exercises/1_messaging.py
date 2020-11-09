def calculate_sum_of_digits(el):
	result = sum([int(s) for s in el])
	return result


def get_valid_index(i, s):
	if i > len(s):
		i -= len(s)
		get_valid_index(i, s)
	return i


def process_string(li, s):
	list_of_indexes = [calculate_sum_of_digits(el) for el in li]
	result = []
	for i in list_of_indexes:
		i = get_valid_index(i, s)
		ch = string.pop(i)
		result.append(ch)
	return "".join(result)


list_of_numbers = input().split()
string = [ch for ch in input()]

print(process_string(list_of_numbers, string))
