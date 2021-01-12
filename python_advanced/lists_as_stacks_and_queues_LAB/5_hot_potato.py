from collections import deque

q = deque(input().split(' '))
n_toss = int(input())

while len(q) > 1:
    for _ in range(n_toss-1):
        q.append(q.popleft())
    print(f'Removed {q.popleft()}')

print(f'Last is {q.popleft()}')
