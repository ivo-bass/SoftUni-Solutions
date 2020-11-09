def shoot(seq, i):
	target = seq[i]
	for ind in range(len(seq)):
		if seq[ind] > target and not seq[ind] == -1:
			seq[ind] -= target
		elif seq[ind] <= target and not seq[ind] == -1:
			seq[ind] += target
	seq[i] = -1


sequence = [int(s) for s in input().split()]

while True:
	command = input()
	if command == "End":
		count = sequence.count(-1)
		print(f"Shot targets: {count} -> {' '.join(map(str, sequence))}")
		break
	index = int(command)
	if index in range(len(sequence)):
		shoot(sequence, index)
