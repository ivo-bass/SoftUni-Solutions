def get_for_input(count):
    """Takes input with for loop in given range.
    Returns list of the inputs."""
    lines = []
    for _ in range(count):
        text = input()
        lines.append(text)
    return lines


IN_COMMAND = 'IN'
OUT_COMMAND = 'OUT'

n = int(input())
commands = get_for_input(n)

parking_lot = set()

for command in commands:
    direction, number = command.split(', ')
    if direction == IN_COMMAND:
        parking_lot.add(number)
    elif direction == OUT_COMMAND:
        parking_lot.remove(number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print('Parking Lot is Empty')
