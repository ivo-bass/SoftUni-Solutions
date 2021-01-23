def get_row():
    return [int(x) for x in input().split(', ')]


def get_matrix(n):
    return [get_row() for _ in range(n)]


def is_valid(el):
    return el % 2 == 0


def get_even_row(m, i):
    return [el for el in m[i] if is_valid(el)]


def get_even_matrix(matrix):
    return [get_even_row(matrix, i) for i in range(len(matrix))]


n = int(input())
matrix = get_matrix(n)
even_matrix = get_even_matrix(matrix)
print(even_matrix)
