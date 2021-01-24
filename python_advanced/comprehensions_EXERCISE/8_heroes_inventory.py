END_COMMAND = 'End'


def get_input():
    return {name: {} for name in input().split(', ')}


def print_output(dd):
    for name, items in dd.items():
        count = len(items)
        costs = sum(items.values())
        print(f'{name} -> Items: {count}, Cost: {costs}')


heroes = get_input()

while True:
    command = input()
    if command == END_COMMAND:
        break
    name, item, cost = command.split('-')
    cost = int(cost)
    if item not in heroes[name].keys():
        heroes[name][item] = cost

print_output(heroes)
