"""Search for element's COORDINATES until element is found from given POSITION in SQUARE matrix"""
QUEEN = 'Q'
KING = 'K'
SIZE_OF_MATRIX = 8

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


def is_valid(value, max_value):
    return 0 <= value < max_value


def search_for_delta(mat, x, y, delta):
    delta_x, delta_y = delta
    while True:
        if not is_valid(x, SIZE_OF_MATRIX) or not is_valid(y, SIZE_OF_MATRIX):
            return None
        if mat[x][y] == QUEEN:
            return x, y
        x += delta_x
        y += delta_y


def search_for_cell_from_given_position(mat, x, y):
    results = [search_for_delta(mat, x, y, delta) for delta in DELTAS]
    return list(filter(lambda q: q, results))
