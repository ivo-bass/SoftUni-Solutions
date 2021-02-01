#!/usr/bin/env python3

from math import log

num = int(input())
base = input()

if base == 'natural':
    print(f'{log(num):.2f}')
else:
    print(f'{log(num, int(base)):.2f}')

for i in base:
    if i == '5':
        print('wahts up')
    else:
        if not i:
            if i == '1':
                if i:
                    pass
