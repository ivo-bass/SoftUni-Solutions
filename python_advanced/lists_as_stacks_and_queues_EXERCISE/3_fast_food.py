from collections import deque

BIGGEST_ORDER = 0
MIN_OREDER = 0

food_quantity = int(input())
orders_input = [int(s) for s in input().split(' ')]
orders = deque(orders_input)

if orders:
    orders_copy = orders.copy()
    best = MIN_OREDER
    while orders_copy:
        el = orders_copy.popleft()
        if el >= best:
            best = el
    print(best)

while orders:
    current = orders.popleft()
    if current > food_quantity:
        orders.appendleft(current)
        break
    food_quantity -= current

if orders:
    orders_left = " ".join(map(str, orders))
    print(f'Orders left: {orders_left}')
else:
    print('Orders complete')
