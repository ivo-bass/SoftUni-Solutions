QUEEN = 'Q'
KING = 'K'
PLUS = '+'
MINUS = '-'
SAFE_KING_MSG = 'The king is safe!'
SIZE = 8


def get_input():
    return [input().split(' ') for _ in range(SIZE)]


def locate_king(mat):
    for row_i in range(SIZE):
        for col_i in range(SIZE):
            if mat[row_i][col_i] == KING:
                return row_i, col_i


def is_valid(m, r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE and m[r][c] == QUEEN


def search_direction(mat, x, y, x_sign=None, y_sign=None):
    for i in range(1, SIZE):
        row = eval(f'{x} {x_sign} {i}') if x_sign else x
        col = eval(f'{y} {y_sign} {i}') if y_sign else y
        if is_valid(mat, row, col):
            return [row, col]


def search_for_queen(mat, x, y):
    results = [search_direction(mat, x, y, y_sign=PLUS),  # right
               search_direction(mat, x, y, y_sign=MINUS),  # left
               search_direction(mat, x, y, x_sign=PLUS),  # up
               search_direction(mat, x, y, x_sign=MINUS),  # down
               search_direction(mat, x, y, x_sign=PLUS, y_sign=PLUS),  # down right
               search_direction(mat, x, y, x_sign=MINUS, y_sign=PLUS),  # up right
               search_direction(mat, x, y, x_sign=PLUS, y_sign=MINUS),  # down left
               search_direction(mat, x, y, x_sign=MINUS, y_sign=MINUS)]  # up left
    return list(filter(lambda q: q, results))


def print_queens(queens):
    if queens:
        [print(queen) for queen in queens]
    else:
        print(SAFE_KING_MSG)


matrix = get_input()
king_x, king_y = locate_king(matrix)
killer_queens = search_for_queen(matrix, king_x, king_y)
print_queens(killer_queens)
