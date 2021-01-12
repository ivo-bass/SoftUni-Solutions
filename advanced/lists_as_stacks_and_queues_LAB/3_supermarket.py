from collections import deque

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'

q = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f'{len(q)} people remaining.')
        break
    elif command == PAID_COMMAND:
        while q:
            print(q.popleft())
    else:
        q.append(command)
