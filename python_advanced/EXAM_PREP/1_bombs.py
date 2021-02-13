from collections import deque

BOMBS_TABLE = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}

bombs_counts = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0,
}


def is_pouch_full(b_count):
    for _, count in b_count.items():
        if count < 3:
            return False
    return True


def print_results(pouch, effects, casings, counts):
    if pouch:
        print('Bene! You have successfully filled the bomb pouch!')
    else:
        print('You don\'t have enough materials to fill the bomb pouch.')
    if not effects:
        print('Bomb Effects: empty')
    else:
        print(f'Bomb Effects: {", ".join(map(str, effects))}')
    if not casings:
        print('Bomb Casings: empty')
    else:
        print(f'Bomb Casings: {", ".join(map(str, casings))}')
    for name, count in counts.items():
        print(f'{name}: {count}')


def main():
    bomb_effects = deque(map(int, input().split(', ')))
    bomb_casings = list(map(int, input().split(', ')))
    check_pouch = False
    while bomb_effects and bomb_casings:
        current_effect = bomb_effects[0]
        current_casing = bomb_casings[-1]
        current_sum = current_effect + current_casing
        if current_sum in BOMBS_TABLE.keys():
            bomb_effects.popleft()
            bomb_casings.pop()
            bombs_counts[BOMBS_TABLE[current_sum]] += 1
        else:
            bomb_casings[-1] -= 5
        check_pouch = is_pouch_full(bombs_counts)
        if check_pouch:
            break

    print_results(check_pouch, bomb_effects, bomb_casings, bombs_counts)


if __name__ == '__main__':
    main()
