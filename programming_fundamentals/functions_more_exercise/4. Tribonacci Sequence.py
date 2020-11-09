given_num = int(input())


def tribonacci_sequence(el_count):
	sequence = [1]
	previous_3 = [0, 0, 1]
	for _ in range(given_num - 1):
		new_number = sum(previous_3)
		sequence.append(new_number)
		previous_3.pop(0)
		previous_3.append(new_number)
	return sequence


print(*tribonacci_sequence(given_num))
