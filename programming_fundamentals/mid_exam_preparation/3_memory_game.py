sequence_input = input()

sequence = sequence_input.strip().split(' ')
moves = 0


def invalid(seq, move):
	print("Invalid input! Adding additional elements to the board")
	midpoint = len(seq) // 2
	add = f'-{move}a'
	seq = seq[0:midpoint] + [add] * 2 + seq[midpoint:]
	return seq


def match(seq, element1, element2):
	print(f"Congrats! You have found matching elements - {element1}!")
	seq.remove(element1)
	seq.remove(element2)


while True:
	command_input = input()
	if command_input == "end":
		print(f"Sorry you lose :(\n{' '.join(map(str, sequence))}")
		break
	moves += 1
	index_1, index_2 = [int(i) for i in command_input.split(' ')]
	i1_not_in_range = index_1 not in range(len(sequence))
	i2_not_in_range = index_2 not in range(len(sequence))
	if index_1 == index_2 or i1_not_in_range or i2_not_in_range:
		sequence = invalid(sequence, moves)
	else:
		if not sequence:
			print(f"You have won in {moves} turns!")
			break
		if sequence[index_1] == sequence[index_2]:
			match(sequence, sequence[index_1], sequence[index_2])
		elif not sequence[index_1] == sequence[index_2]:
			print("Try again!")
