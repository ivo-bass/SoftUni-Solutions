EMPTY_CELL = ' '
MINE_CELL = '*'
NEIGHBOUR_CELLS_DISTANCE = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def get_user_input():
    size = int(input())
    count_of_bombs = int(input())
    matrix = [[' ' for _ in range(size)] for _ in range(size)]
    for _ in range(count_of_bombs):
        x, y = [int(s) for s in input().lstrip('(').rstrip(')').split(', ')]
        matrix[x][y] = '*'
    return matrix


def is_in_range(index, size):
    return 0 <= index < size


def check_for_mine(board, row, col):
    cell_to_observe = board[row][col]
    if cell_to_observe == MINE_CELL:
        return 1
    return 0


def count_neighbours_mines(board, size, row_index, col_index):
    count_mines = 0
    for neighbour_distance in NEIGHBOUR_CELLS_DISTANCE:
        row_distance, col_distance = neighbour_distance
        observed_row = row_index + row_distance
        observed_col = col_index + col_distance
        if is_in_range(observed_row, size) and is_in_range(observed_col, size):
            count_mines += check_for_mine(board, observed_row, observed_col)
    return count_mines


def draw_numbers_on_board(board, size, row_i, col_i):
    number = count_neighbours_mines(board, size, row_i, col_i)
    board[row_i][col_i] = number
    return board


def add_numbers_to_board(size, board):
    for row_i in range(size):
        for col_i in range(size):
            current_cell = board[row_i][col_i]
            if current_cell == EMPTY_CELL:
                board = draw_numbers_on_board(board, size, row_i, col_i)
    return board


def show_board(size, matrix):
    for row_i in range(size):
        print(' '.join(map(str, matrix[row_i])))


def main():
    board = get_user_input()
    size = len(board)
    board = add_numbers_to_board(size, board)
    show_board(size, board)


main()
