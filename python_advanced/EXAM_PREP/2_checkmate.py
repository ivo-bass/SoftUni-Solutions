QUEEN = 'Q'
KING = 'K'
SAFE_MSG = 'The king is safe!'


def get_input():
    size = 8
    return [input().split(' ') for _ in range(size)]


def locate_king(mat):
    for row_i in range(len(mat)):
        for col_i in range(len(mat)):
            if mat[row_i][col_i] == KING:
                return row_i, col_i


def search_left(mat, x, y):
    for c in range(y - 1, -1, -1):
        if mat[x][c] == QUEEN:
            return [x, c]


def search_right(mat, x, y):
    for c in range(y + 1, len(mat)):
        if mat[x][c] == QUEEN:
            return [x, c]


def search_up(mat, x, y):
    for r in range(x - 1, -1, -1):
        if mat[r][y] == QUEEN:
            return [r, y]


def search_down(mat, x, y):
    for r in range(x + 1, len(mat)):
        if mat[r][y] == QUEEN:
            return [r, y]


def search_up_left(mat, x, y):
    for r in range(x - 1, -1, -1):
        y -= 1
        if y < 0:
            break
        if mat[r][y] == QUEEN:
            return [r, y]


def search_up_right(mat, x, y):
    for r in range(x - 1, -1, -1):
        y += 1
        if y == len(mat):
            break
        if mat[r][y] == QUEEN:
            return [r, y]


def search_down_left(mat, x, y):
    for r in range(x + 1, len(mat)):
        y -= 1
        if y < 0:
            break
        if mat[r][y] == QUEEN:
            return [r, y]


def search_down_right(mat, x, y):
    for r in range(x + 1, len(mat)):
        y += 1
        if y == len(mat):
            break
        if mat[r][y] == QUEEN:
            return [r, y]


def search_for_queen(mat, x, y):
    return [search_left(mat, x, y),
            search_right(mat, x, y),
            search_up(mat, x, y),
            search_down(mat, x, y),
            search_up_left(mat, x, y),
            search_up_right(mat, x, y),
            search_down_left(mat, x, y),
            search_down_right(mat, x, y)]


def print_queens(ll):
    queens = list(filter(lambda x: x is not None, ll))
    if queens:
        [print(queen) for queen in queens]
    else:
        print(SAFE_MSG)


matrix = get_input()
king_x, king_y = locate_king(matrix)
killer_queens = search_for_queen(matrix, king_x, king_y)
print_queens(killer_queens)
