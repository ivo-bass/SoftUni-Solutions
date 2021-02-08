"""Search for element's COORDINATES until element is found from given POSITION in SQUARE matrix"""
SEARCHED_ELEMENT = 'Q'
SIZE_OF_MATRIX = 8
PLUS = '+'
MINUS = '-'


def is_valid(m, r, c):
    return 0 <= r < SIZE_OF_MATRIX and 0 <= c < SIZE_OF_MATRIX and m[r][c] == SEARCHED_ELEMENT


def search(mat, x, y, x_operator=None, y_operator=None):
    for i in range(1, SIZE_OF_MATRIX):
        row = eval(f'{x} {x_operator} {i}') if x_operator else x
        col = eval(f'{y} {y_operator} {i}') if y_operator else y
        if is_valid(mat, row, col):
            return [row, col]


def search_for_element_from_given_location_in_matrix(mat, x, y):
    results = [search(mat, x, y, y_operator=PLUS),  # right
               search(mat, x, y, y_operator=MINUS),  # left
               search(mat, x, y, x_operator=PLUS),  # up
               search(mat, x, y, x_operator=MINUS),  # down
               search(mat, x, y, x_operator=PLUS, y_operator=PLUS),  # down right
               search(mat, x, y, x_operator=MINUS, y_operator=PLUS),  # up right
               search(mat, x, y, x_operator=PLUS, y_operator=MINUS),  # down left
               search(mat, x, y, x_operator=MINUS, y_operator=MINUS)]  # up left
    return list(filter(lambda q: q, results))
