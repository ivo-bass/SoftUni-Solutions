n = int(input())

numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)

print(f'Max number: {max(numbers)}')
print(f'Min number: {min(numbers)}')
