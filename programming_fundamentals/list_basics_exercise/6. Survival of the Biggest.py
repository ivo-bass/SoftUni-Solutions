string = input()
count = int(input())

numbers = [int(i) for i in string.split()]
smallest = sorted(numbers)[:count]

for num in smallest:
	numbers.remove(num)

print(numbers)
