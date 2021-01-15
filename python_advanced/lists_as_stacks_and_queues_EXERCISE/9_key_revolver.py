from collections import deque

bullet_price = int(input())
size_of_barrel = int(input())
bullets_stack = [int(s) for s in input().split(' ')]
locks_queue = deque([int(s) for s in input().split(' ')])
value_of_inteligence = int(input())

shots = 0

success = False
while bullets_stack:
    if locks_queue:
        bullet = bullets_stack.pop()
        shots += 1

        if bullet <= locks_queue[0]:
            print('Bang!')
            locks_queue.popleft()
        else:
            print('Ping!')

        if bullets_stack:
            if shots % size_of_barrel == 0:
                print('Reloading!')

    else:
        break

if locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else:
    earned = value_of_inteligence - shots * bullet_price
    print(f'{len(bullets_stack)} bullets left. Earned ${earned}')
