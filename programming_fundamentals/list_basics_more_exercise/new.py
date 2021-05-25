DOT = "."
DASH = "-"
DIRECTIONS = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)

TEST_MATRIX = [
    ["-", ".", "-", ".", ".", "-"],
    [".", "-", ".", ".", "-", "."],
    [".", "-", "-", "-", "-", "-"],
    ["-", "-", "-", ".", "-", "-"],
]


def get_matrix():
    matrix = []
    row_count = int(input())
    for row_index in range(row_count):
        row = input().split()
        matrix.append(row)
    return matrix


def is_valid_position(mat, r, c):
    return 0 <= r < len(mat) and 0 <= c < len(mat[0])


def count_in_neighbours(matrix, row, col):
    if not is_valid_position(matrix, row, col):
        return 0

    if matrix[row][col] == DASH:
        return 0

    count = 1
    matrix[row][col] = DASH

    for d in DIRECTIONS:
        new_row = row + d[0]
        new_col = col + d[1]
        count += count_in_neighbours(matrix, new_row, new_col)
    return count


def max_connected_dots(matrix):
    max_count = 0

    for row_i, row in enumerate(matrix):
        for col_i, value in enumerate(row):
            if value == DOT:
                current_count = count_in_neighbours(matrix, row_i, col_i)
                max_count = max(max_count, current_count)
    return max_count


# matrix = get_matrix()
matrix = TEST_MATRIX
result = max_connected_dots(matrix)
print(result)
