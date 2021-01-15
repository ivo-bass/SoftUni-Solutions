from collections import deque

cups_queue = deque([int(s) for s in input().split(' ')])
bottles_queue = deque([int(s) for s in input().split(' ')])

wasted_watter = 0

while bottles_queue:
    if cups_queue:
        bottle = bottles_queue.pop()
        cup_capacity = cups_queue[0]
        if cup_capacity > bottle:
            cups_queue[0] -= bottle
            continue
        else:
            cup = cups_queue.popleft()
            wasted_watter += bottle - cup
    else:
        break

if not cups_queue:
    bottles = ''
    while bottles_queue:
        b = bottles_queue.pop()
        bottles += f' {b}'
    print(f'Bottles: {bottles.strip()}')
else:
    cups = ''
    while cups_queue:
        c = cups_queue.popleft()
        cups += f' {c}'
    print(f'Cups: {cups.strip()}')

print(f'Wasted litters of water: {wasted_watter}')
