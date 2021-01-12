from collections import deque

START_COMMAND = 'Start'
END_COMMAND = 'End'

names = deque()
quantity = int(input())

while True:
    command = input()
    if command == START_COMMAND:
        break
    names.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        break
    if command.startswith('refill'):
        liters = int(command.split()[-1])
        quantity += liters
    else:
        person = names.popleft()
        wanted_liters = int(command)
        if wanted_liters <= quantity:
            quantity -= wanted_liters
            print(f'{person} got water')
        else:
            print(f'{person} must wait')

print(f'{quantity} liters left')
