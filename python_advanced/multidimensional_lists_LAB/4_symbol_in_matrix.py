MATRIX = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['X', '!', '@'],
]
LOCAL_TEST = False


def get_matrix_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = MATRIX
    else:
        rows = int(input())
        matrix = []
        for _ in range(rows):
            row = [x for x in input()]
            matrix.append(row)
    return matrix


def find_symbol_in_matrix(matrix, symbol):
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            if symbol == matrix[r][c]:
                return (r, c)
    return f'{symbol} does not occur in the matrix'


matrix = get_matrix_input()
symbol = input()
result = find_symbol_in_matrix(matrix, symbol)
print(result)
