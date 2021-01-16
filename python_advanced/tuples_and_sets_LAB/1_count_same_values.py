list_of_numbers = map(float, input().split(' '))

value_count = {}
for num in list_of_numbers:
    if not num in value_count:
        value_count[num] = 0
    value_count[num] += 1

for num, count in value_count.items():
    print(f'{num} - {count} times')
