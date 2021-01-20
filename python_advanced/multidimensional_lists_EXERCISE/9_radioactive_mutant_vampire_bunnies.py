"""___RMVB___"""

# ___TEST_DATA___
TEST_MATRIX = [
    ['.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.', 'B', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'B', '.', '.', 'B'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'P', '.', '.', '.', '.', '.'],
]
TEST_COMMANDS = ['U', 'L', 'L', 'L']

# ________________
BUNNY_NEW_ROW = [-1, 0, 1, 0]
BUNNY_NEW_COL = [0, 1, 0, -1]
# ___DIRECTIONS___
UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'
# ___CELL_TYPES___
REGULAR_CELL = '.'
BUNNY_CELL = 'B'
PLAYER_CELL = 'P'
# ___STATUS___
PLAY = 0
GAME_OVER = -1
WIN = 1
# ___MESSAGES___
GAME_OVER_MSG = 'dead:'
WIN_MSG = 'won:'
# ___TEST_CONDITION___
LOCAL_TEST = False


def get_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = TEST_MATRIX
        commands = TEST_COMMANDS
    else:
        matrix = []
        rows_count, _ = [int(x) for x in input().split()]
        for _ in range(rows_count):
            row_input = [x for x in input()]
            matrix.append(row_input)
        commands = [x for x in input()]
    return matrix, commands


def get_starting_position(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == PLAYER_CELL:
                return r, c


def calc_new_position(x, y, com):
    n_x, n_y = x, y
    if com == UP:
        n_x -= 1
    elif com == DOWN:
        n_x += 1
    elif com == LEFT:
        n_y -= 1
    elif com == RIGHT:
        n_y += 1
    return n_x, n_y


def is_valid_cell(m, r, c):
    row_size = len(m)
    col_size = len(m[0])
    return 0 <= r < row_size and 0 <= c < col_size


def move_player(mat, pos, stat, comm):
    x, y = pos
    new_x, new_y = calc_new_position(x, y, comm)
    if is_valid_cell(mat, new_x, new_y):
        pos = new_x, new_y
        cell = mat[new_x][new_y]
        if cell == BUNNY_CELL:
            stat = GAME_OVER
            mat[x][y] = REGULAR_CELL
            return mat, pos, stat
        if cell == REGULAR_CELL:
            mat[new_x][new_y] = PLAYER_CELL
            mat[x][y] = REGULAR_CELL
    else:
        mat[x][y] = REGULAR_CELL
        stat = WIN
    return mat, pos, stat


def find_all_bunnies(matrix):
    bunnies = set()
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            cell = matrix[r][c]
            if cell == BUNNY_CELL:
                bunnies.add((r, c))
    return bunnies


def new_bunnies_positions(matrix, x, y):
    new_cells = set()
    for r in range(len(BUNNY_NEW_ROW)):
        new_row = x + BUNNY_NEW_ROW[r]
        new_col = y + BUNNY_NEW_COL[r]
        if is_valid_cell(matrix, new_row, new_col):
            new_cell = (new_row, new_col)
            new_cells.add(new_cell)
    return new_cells


def visualize_new_bunnies(matrix, new_bunnies, status, position):
    for new_bunny_cell in new_bunnies:
        x, y = new_bunny_cell
        if matrix[x][y] == PLAYER_CELL:
            status = GAME_OVER
        elif matrix[x][y] == BUNNY_CELL:
            continue
        matrix[x][y] = BUNNY_CELL
    return matrix, status


def multiply_bunnies(matrix, status, position, all_bunnies):
    new_bunnies = set()
    if all_bunnies:
        for bunny in all_bunnies:
            x, y = bunny
            new_bunnies.update(new_bunnies_positions(matrix, x, y))

        matrix, status = visualize_new_bunnies(
            matrix, new_bunnies, status, position)
        all_bunnies.update(new_bunnies)
    return matrix, status, all_bunnies


def print_output(matrix, position, status):
    for r in range(len(matrix)):
        print(''.join(matrix[r]))
    if position:
        row, col = position
        if status == GAME_OVER:
            print(f'{GAME_OVER_MSG} {row} {col}')
        elif status == WIN:
            print(f'{WIN_MSG} {row} {col}')


matrix, commands = get_input()
position = get_starting_position(matrix)
all_bunnies = find_all_bunnies(matrix)
status = PLAY
for command in commands:
    if position:
        matrix, position, status = move_player(
            matrix, position, status, command)
    if all_bunnies:
        matrix, status, all_bunnies = multiply_bunnies(
            matrix, status, position, all_bunnies)
    if not status == PLAY:
        break
print_output(matrix, position, status)
