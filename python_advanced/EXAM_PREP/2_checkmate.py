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


def search_direction(mat, x, y, x_operator=None, y_operator=None):
    for i in range(1, SIZE):
        row = eval(f'{x} {x_operator} {i}') if x_operator else x
        col = eval(f'{y} {y_operator} {i}') if y_operator else y
        if is_valid(mat, row, col):
            return [row, col]


def search_for_queens(mat, x, y):
    results = [
        search_direction(mat, x, y, y_operator=PLUS),  # right
        search_direction(mat, x, y, y_operator=MINUS),  # left
        search_direction(mat, x, y, x_operator=PLUS),  # up
        search_direction(mat, x, y, x_operator=MINUS),  # down
        search_direction(mat, x, y, x_operator=PLUS, y_operator=PLUS),  # down right
        search_direction(mat, x, y, x_operator=MINUS, y_operator=PLUS),  # up right
        search_direction(mat, x, y, x_operator=PLUS, y_operator=MINUS),  # down left
        search_direction(mat, x, y, x_operator=MINUS, y_operator=MINUS)  # up left
    ]
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
