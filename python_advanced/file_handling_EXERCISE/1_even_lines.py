import re

PATH = 'text.txt'
PATTERN = r"[-,!?'.]"
REPLACEMENT = '@'


def replace_bad_chars(line):
    return re.sub(PATTERN, REPLACEMENT, line)


def get_even_lines(ll):
    return [ll[i].rstrip().split() for i in range(len(ll)) if i % 2 == 0]


def reverse_order(ll):
    return [line[::-1] for line in ll]


def print_output(ll):
    for line in ll:
        print(' '.join(line))


with open(PATH) as file:
    lines = [replace_bad_chars(l) for l in file.readlines()]
    even_lines = get_even_lines(lines)
    reversed_lines = reverse_order(even_lines)

print_output(reversed_lines)
