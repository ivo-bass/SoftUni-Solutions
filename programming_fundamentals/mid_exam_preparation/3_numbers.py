sequence_string = input()

sequence = [int(i) for i in sequence_string.split(' ')]
average_value = sum(sequence) / len(sequence)
greatest_reverse_sorted = sorted([i for i in sequence if i > average_value], reverse=True)

result = None
if greatest_reverse_sorted:
	result = ' '.join(map(str, greatest_reverse_sorted[:5]))
else:
	result = "No"

print(result)
