SPACE = ' '
SYMBOL = '* '


def create_row(n, i):
    indent = SPACE * (n - i - 1)
    stars = SYMBOL * (i + 1)
    return indent + stars.rstrip()


def print_rhombus(n):
    for i in range(n):
        print(create_row(n, i))

    for i in range(n - 2, -1, -1):
        print(create_row(n, i))


print_rhombus(int(input()))
