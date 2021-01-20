TEST_MATRIX = [
    ['K', '0', 'K'],
    ['0', '0', '0'],
    ['0', 'K', '0'],
]
ROW_MOVES = [-2, -2, 2, 2, -1, -1, 1, 1]
COL_MOVES = [-1, 1, -1, 1, -2, 2, -2, 2]
EMPTY = '0'
KNIGHT = 'K'
LOCAL_TEST = False


def get_matrix(is_test=LOCAL_TEST):
    if is_test:
        matrix = TEST_MATRIX
    else:
        matrix = []
        size = int(input())
        for _ in range(size):
            row = [x for x in input()]
            matrix.append(row)
    return matrix


def is_valid(m, r_i, c_i):
    size = len(m)
    if 0 <= r_i < size and 0 <= c_i < size:
        return True
    return False


def calculate_kills(m, r, c):
    kills = 0
    change_row = ROW_MOVES
    change_col = COL_MOVES
    for i in range(len(change_row)):
        new_row = r + change_row[i]
        new_col = c + change_col[i]
        if is_valid(m, new_row, new_col):
            position = m[new_row][new_col]
            if position == KNIGHT:
                kills += 1
    return kills


def find_best_knight(matrix):
    most_kills = 0
    best_knight = None
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix)):
            if matrix[row_index][col_index] == KNIGHT:
                current_kills = calculate_kills(matrix, row_index, col_index)
                if current_kills > most_kills:
                    most_kills = current_kills
                    best_knight = (row_index, col_index)
    return best_knight


def remove_best_knight(matrix, best_knight):
    matrix[best_knight[0]][best_knight[1]] = EMPTY
    return matrix


def main():
    matrix = get_matrix()
    count = 0
    while True:
        best_knight = find_best_knight(matrix)
        if not best_knight:
            break
        matrix = remove_best_knight(matrix, best_knight)
        count += 1
    print(count)


if __name__ == '__main__':
    main()
