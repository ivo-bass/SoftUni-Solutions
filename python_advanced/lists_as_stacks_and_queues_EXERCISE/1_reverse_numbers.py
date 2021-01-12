numbers = input().split(' ')
stack = []

for number in numbers:
    stack.append(number)

while stack:
    print(stack.pop(), end=' ')
