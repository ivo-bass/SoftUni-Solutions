data = input().strip().split()
ALPHABET = [chr(x) for x in range(65, 91)]


def calc_sum(el):
	result = 0
	first, number, last = el[0], int(el[1:-1]), el[-1]
	position_first = ALPHABET.index(first.upper()) + 1
	position_last = ALPHABET.index(last.upper()) + 1
	if first.isupper():
		result = number / position_first
	elif first.islower():
		result = number * position_first
	if last.isupper():
		result -= position_last
	elif last.islower():
		result += position_last
	return result


for index, element in enumerate(data):
	data[index] = calc_sum(element)
print(f"{sum(data):.2f}")
