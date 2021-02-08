QUEEN = 'Q'
KING = 'K'
SIZE = 8
SAFE_KING_MSG = 'The king is safe!'


def plus(a, b): return a + b


def minus(a, b): return a - b


DIRECTIONS = [
    (None, plus),  # right
    (None, minus),  # left
    (plus, None),  # up
    (minus, None),  # down
    (plus, plus),  # down right
    (minus, plus),  # up right
    (plus, minus),  # down left
    (minus, minus),  # up left
]


def get_input():
    return [input().split(' ') for _ in range(SIZE)]


def locate_king(mat):
    for row_i in range(SIZE):
        for col_i in range(SIZE):
            if mat[row_i][col_i] == KING:
                return row_i, col_i


def is_valid(m, r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE and m[r][c] == QUEEN


def search_direction(mat, x, y, x_operator=None, y_operator=None):
    for i in range(1, SIZE):
        row = x_operator(x, i) if x_operator else x
        col = y_operator(y, i) if y_operator else y
        if is_valid(mat, row, col):
            return [row, col]


def search_for_queens(mat, x, y):
    results = [search_direction(mat, x, y, x_op, y_op) for (x_op, y_op) in DIRECTIONS]
    return list(filter(lambda q: q, results))


def print_queens(queens):
    if queens:
        [print(queen) for queen in queens]
    else:
        print(SAFE_KING_MSG)


matrix = get_input()
king_x, king_y = locate_king(matrix)
killer_queens = search_for_queens(matrix, king_x, king_y)
print_queens(killer_queens)
