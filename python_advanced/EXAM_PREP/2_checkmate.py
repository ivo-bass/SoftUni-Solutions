QUEEN = 'Q'
KING = 'K'
SIZE = 8
SAFE_KING_MSG = 'The king is safe!'

DELTAS = [
    (0, -1),  # left
    (-1, -1),  # up left
    (1, 0),  # up
    (-1, 1),  # up right
    (0, 1),  # right
    (1, 1),  # down right
    (-1, 0),  # down
    (1, -1),  # down left
]


def get_input():
    return [input().split(' ') for _ in range(SIZE)]


def locate_king(mat):
    for row_i in range(SIZE):
        for col_i in range(SIZE):
            if mat[row_i][col_i] == KING:
                return row_i, col_i


def is_valid(value):
    return 0 <= value < SIZE


def search_for_delta(mat, x, y, delta):
    delta_x, delta_y = delta
    while True:
        if not is_valid(x) or not is_valid(y):
            return None
        if mat[x][y] == QUEEN:
            return [x, y]
        x += delta_x
        y += delta_y


def search_for_queens(mat, x, y):
    results = [search_for_delta(mat, x, y, delta) for delta in DELTAS]
    return list(filter(lambda q: q, results))


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print(SAFE_KING_MSG)


matrix = get_input()
king_x, king_y = locate_king(matrix)
killer_queens = search_for_queens(matrix, king_x, king_y)
print_result(killer_queens)
