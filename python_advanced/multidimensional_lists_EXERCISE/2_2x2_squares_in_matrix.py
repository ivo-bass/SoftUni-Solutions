MATRIX = [
    ['A', 'B', 'B', 'D'],
    ['E', 'B', 'B', 'B'],
    ['I', 'J', 'B', 'B'],
]
LOCAL_TEST = False


def get_matrix_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = MATRIX
    else:
        matrix = []
        row, _ = [int(x) for x in input().split(' ')]
        for _ in range(row):
            row = [x for x in input().split(' ')]
            matrix.append(row)
    return matrix


def find_valid_submatrix(m):
    count = 0
    row = len(m)
    col = len(m[0])
    for r in range(row-1):
        for c in range(col-1):
            if m[r][c] == m[r][c+1] == m[r+1][c] == m[r+1][c+1]:
                count += 1
    return count


matrix = get_matrix_input()
print(find_valid_submatrix(matrix))
