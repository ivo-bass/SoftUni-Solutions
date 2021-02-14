from collections import deque


def make_firework(dd, key, effs, pows):
    dd[key] += 1
    effs.popleft()
    pows.pop()


def is_enough(_count):
    for _, count in _count.items():
        if count < 3:
            return False
    return True


def print_results(enough, effects, powers, counts):
    if enough:
        print('Congrats! You made the perfect firework show!')
    else:
        print("Sorry. You can’t make the perfect firework show.")
    if effects:
        print(f'Firework Effects left: {", ".join(map(str, effects))}')
    if powers:
        print(f'Explosive Power left: {", ".join(map(str, powers))}')
    for name, count in counts.items():
        print(f'{name}: {count}')


fireworks_count = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

effects = deque([int(x) for x in input().split(', ')])
powers = [int(x) for x in input().split(', ')]

check_enough = False
while effects and powers:
    current_effect = effects[0]
    current_power = powers[-1]
    current_sum = current_effect + current_power
    if current_effect <= 0:
        effects.popleft()
        continue
    if current_power <= 0:
        powers.pop()
        continue
    if current_sum % 3 == 0 and current_sum % 5 != 0:
        make_firework(fireworks_count, 'Palm Fireworks', effects, powers)
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        make_firework(fireworks_count, 'Willow Fireworks', effects, powers)
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        make_firework(fireworks_count, 'Crossette Fireworks', effects, powers)
    else:
        effects[0] -= 1
        cur_ef = effects.popleft()
        effects.append(cur_ef)

    check_enough = is_enough(fireworks_count)
    if check_enough:
        break

print_results(check_enough, effects, powers, fireworks_count)
