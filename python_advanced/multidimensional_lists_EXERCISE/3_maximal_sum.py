from sys import maxsize

MATRIX = [
    [1, 5, 5, 2, 4],
    [2, 1, 4, 14, 3],
    [3, 7, 11, 2, 8],
    [4, 8, 12, 16, 4],
]
LOCAL_TEST = True  # place as argument in get_matrix_input() to test locally
SIZE = 3


def get_matrix_input(is_test=False):
    if is_test:
        matrix = MATRIX
    else:
        matrix = []
        row, _ = [int(x) for x in input().split(' ')]
        for _ in range(row):
            row = [int(x) for x in input().split(' ') if x.isnumeric()]
            matrix.append(row)
    return matrix


def calc_sum_of_submatrix(submatrix):
    the_sum = 0
    size = len(submatrix)
    for row in range(size):
        the_sum += sum(submatrix[row])
    return the_sum


def find_best_submatrix(m, size):
    best_sum = -maxsize
    best_submatrix = []
    r_size = len(m)
    c_size = len(m[0])
    for r in range(0, r_size - size + 1):
        for c in range(0, c_size - size + 1):
            submatrix = [
                [m[r][c], m[r][c+1], m[r][c+2]],
                [m[r+1][c], m[r+1][c+1], m[r+1][c+2]],
                [m[r+2][c], m[r+2][c+1], m[r+2][c+2]],
            ]
            current_sum = calc_sum_of_submatrix(submatrix)
            if current_sum > best_sum:
                best_sum = current_sum
                best_submatrix = submatrix
    return best_sum, best_submatrix


def print_output(b_sum, b_submatrix):
    print(f'Sum = {b_sum}')
    for r in range(len(b_submatrix)):
        line = ' '.join(map(str, b_submatrix[r]))
        print(line)


matrix = get_matrix_input()
best_sum, best_submatrix = find_best_submatrix(matrix, SIZE)
print_output(best_sum, best_submatrix)
