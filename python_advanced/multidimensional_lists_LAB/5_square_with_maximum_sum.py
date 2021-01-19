MATRIX = [
    [7, 1, 3, 3, 2, 1],
    [1, 3, 9, 8, 5, 6],
    [4, 6, 7, 9, 1, 0],
]
LOCAL_TEST = False


def get_matrix_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = MATRIX
    else:
        rows, _ = map(int, input().split(', '))
        matrix = []
        for row in range(rows):
            row = [int(x) for x in input().split(', ')]
            matrix.append(row)
    return matrix


def init_first_submatrix_sum(matrix):
    f_sum = matrix[0][0] + matrix[0][1] + \
        matrix[1][0] + matrix[1][1]
    return f_sum


def best_submatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrix = None
    best_sum = init_first_submatrix_sum(matrix)
    for r in range(rows-1):
        for c in range(cols-1):
            current_sum = matrix[r][c] + matrix[r][c+1] + \
                matrix[r+1][c] + matrix[r+1][c+1]
            if current_sum > best_sum:
                best_sum = current_sum
                submatrix = [[matrix[r][c], matrix[r][c+1]],
                             [matrix[r+1][c], matrix[r+1][c+1]]]
    return submatrix, best_sum


def print_matrix(matrix):
    for row in range(len(matrix)):
        string = ' '.join(map(str, matrix[row]))
        print(string)


matrix = get_matrix_input()
submatrix, best_sum = best_submatrix(matrix)
print_matrix(submatrix)
print(best_sum)
