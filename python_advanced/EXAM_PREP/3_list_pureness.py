from collections import deque


def best_list_pureness(*args):
    numbers, k = args
    numbers = deque(numbers)
    best_rotation = 0
    best_pureness = 0
    for rotation in range(k + 1):
        pureness = sum([n * i for i, n in enumerate(numbers)])
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        num = numbers.pop()
        numbers.appendleft(num)
    return f'Best pureness {best_pureness} after {best_rotation} rotations'
