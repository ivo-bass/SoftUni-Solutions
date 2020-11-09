string = input()
beggars_count = int(input())

numbers = list(string.split(', '))
beggars_list = [0 for beggar in range(beggars_count)]

for _ in range(len(numbers)):
	for index in range(beggars_count):
		if numbers:
			beggars_list[index] += int(numbers.pop(0))

print(beggars_list)
