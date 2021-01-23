def get_dimensions():
    return [int(s) for s in input().split()]


def get_alphabet():
    return [chr(n) for n in range(97, 123)]


def generate_element(r, c, alpha):
    return f'{alpha[r]}{alpha[r+c]}{alpha[r]}'


def generate_row(y, r, alpha):
    return [generate_element(r, c, alpha) for c in range(y)]


def generate_matrix(x, y, alpha):
    return [generate_row(y, r, alpha) for r in range(x)]


def print_row(m, r):
    print(' '.join(m[r]))


def print_matrix(m):
    [print_row(m, row) for row in range(len(m))]


x, y = get_dimensions()
alpha = get_alphabet()
matrix = generate_matrix(x, y, alpha)
print_matrix(matrix)
