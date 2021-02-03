#!/usr/bin/env python3

from python_advanced.modules_LAB.fibonacci.sequence import create_seq, locate

END_COMMAND = 'Stop'
CREATE = 'Create'
LOCATE = 'Locate'


while True:
    command = input().split()
    action = command[0]
    if action == END_COMMAND:
        break
    number = int(command[-1])
    if action == CREATE:
        seq = create_seq(number)
        print(' '.join(map(str, seq)))
    elif action == LOCATE:
        print(locate(number))
