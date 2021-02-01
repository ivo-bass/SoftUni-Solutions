#!/usr/bin/env python3


def print_line(n):
    ll = []
    for i in range(1, n+1):
        ll.append(i)
    print(' '.join(map(str, ll)))


def print_triangle(size):
    for row in range(1, size + 2):
        print_line(row)
    for row in range(size, 0, -1):
        print_line(row)
