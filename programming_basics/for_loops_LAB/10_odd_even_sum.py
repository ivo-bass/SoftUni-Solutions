n = int(input())

even_sum = 0
odd_sum = 0

for index, _ in enumerate(range(n), 1):
    number = int(input())
    if index % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

difference = abs(even_sum - odd_sum)
if difference == 0:
    print(f"Yes\nSum = {even_sum}")
else:
    print(f"No\nDiff = {difference}")
