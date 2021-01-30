#!/usr/bin/python3

import os

F_PATH = 'numbers.txt'

if os.path.exists(F_PATH):
    with open(F_PATH) as file:
        lines = file.readlines()
        numbers = [int(el[:-1]) for el in lines]
        print(sum(numbers))
