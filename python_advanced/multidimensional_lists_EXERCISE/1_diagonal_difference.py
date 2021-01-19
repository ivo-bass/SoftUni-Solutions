MATRIX = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
]
LOCAL_TEST = False


def get_matrix_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = MATRIX
    else:
        matrix = []
        size = int(input())
        for _ in range(size):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)
    return matrix


def calc_primary_diagonal(matrix):
    d_sum = 0
    size = len(matrix)
    for r in range(size):
        d_sum += matrix[r][r]
    return d_sum


def calc_secondary_diagonal(matrix):
    d_sum = 0
    size = len(matrix)
    for r in range(size):
        d_sum += matrix[r][size - r - 1]
    return d_sum


def calc_absolute_difference(x, y):
    diff = x - y
    return abs(diff)


matrix = get_matrix_input()
d_1 = calc_primary_diagonal(matrix)
d_2 = calc_secondary_diagonal(matrix)
print(calc_absolute_difference(d_1, d_2))
