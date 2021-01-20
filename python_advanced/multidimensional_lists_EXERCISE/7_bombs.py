TEST_MATRIX = [
    [0, 0, 20],
    [0, 0, 0],
    [2, 1, -1],
]
TEST_CELLS = [(0, 2), (1, 2), (2, 1)]
ROW_MOVES = [-1, -1, -1, 0, 1, 1, 1, 0]
COL_MOVES = [-1,  0, 1, 1, 1, 0, -1, -1]
EMPTY = 0
LOCAL_TEST = False


def get_matrix(is_test=LOCAL_TEST):
    if is_test:
        matrix = TEST_MATRIX
    else:
        matrix = []
        size = int(input())
        for _ in range(size):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)
    return matrix


def get_exploding_cells(is_test=LOCAL_TEST):
    if is_test:
        exploding_cells = TEST_CELLS
    else:
        exploding_cells = []
        the_input = input().split(' ')
        for el in the_input:
            x, y = el.split(',')
            cell = (int(x), int(y))
            exploding_cells.append(cell)
    return exploding_cells


def is_valid_cell(m, r, c):
    size = len(m)
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def explode(mat, x, y):
    power = mat[x][y]
    if power <= 0:
        return mat
    mat[x][y] = 0
    for index in range(len(ROW_MOVES)):
        new_row = x + ROW_MOVES[index]
        new_col = y + COL_MOVES[index]
        if is_valid_cell(mat, new_row, new_col):
            value = mat[new_row][new_col]
            if value <= 0:
                continue
            else:
                mat[new_row][new_col] -= power
    return mat


def print_output(matrix):
    alive_cells = 0
    alive_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            val = matrix[r][c]
            if val > 0:
                alive_cells += 1
                alive_sum += val
    print(f'Alive cells: {alive_cells}')
    print(f'Sum: {alive_sum}')
    for row_index in range(size):
        print(' '.join(map(str, matrix[row_index])))


def main():
    matrix = get_matrix()
    exploding_cells = get_exploding_cells()
    for cell in exploding_cells:
        x, y = cell
        matrix = explode(matrix, x, y)
    print_output(matrix)


main()
