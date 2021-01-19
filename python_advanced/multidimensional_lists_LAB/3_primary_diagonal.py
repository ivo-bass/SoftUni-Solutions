MATRIX = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
]
LOCAL_TEST = False


def get_matrix_input(is_test=False):
    if is_test:
        matrix = MATRIX
    else:
        rows = int(input())
        matrix = []
        for row in range(rows):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)
    return matrix


def sum_matrix_elements(matrix):
    res = 0
    for r in range(len(matrix)):
        res += matrix[r][r]
    return res


matrix = get_matrix_input(LOCAL_TEST)
print(sum_matrix_elements(matrix))
