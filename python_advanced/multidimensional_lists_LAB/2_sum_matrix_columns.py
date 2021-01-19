MATRIX = [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
LOCAL_TEST = False


def get_matrix_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = MATRIX
    else:
        rows, _ = map(int, input().split(', '))
        matrix = []
        for row in range(rows):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)
    return matrix


def sum_matrix_columns(matrix):
    res = []
    rows = len(matrix)
    cols = len(matrix[0])
    for c in range(cols):
        col_sum = 0
        for r in range(rows):
            col_sum += matrix[r][c]
        res.append(col_sum)
    return res


matrix = get_matrix_input()
result = sum_matrix_columns(matrix)
[print(x) for x in result]
