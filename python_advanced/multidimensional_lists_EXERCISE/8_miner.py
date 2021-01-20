"""___Miner Game___"""

# ___TEST_DATA___
TEST_MATRIX = [
    ['*', '*', '*', 'c', '*'],
    ['*', '*', '*', 'e', '*'],
    ['*', '*', 'c', '*', '*'],
    ['s', '*', '*', 'c', '*'],
    ['*', '*', 'c', '*', '*'],
]
TEST_COMMANDS = ['up', 'right', 'right', 'up', 'right']

# ________________
SPLITTER = ' '
# ___DIRECTIONS___
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
# ___CELL_TYPES___
REGULAR_CELL = '*'
END_ROUTE = 'e'
COAL_CELL = 'c'
START_CELL = 's'
# ___STATUS___
PLAY = 0
GAME_OVER = -1
WIN = 1
# ___MESSAGES___
GAME_OVER_MSG = 'Game over!'
WIN_MSG = 'You collected all coals!'
TIE_MSG = 'coals left.'
# ___TEST_CONDITION___
LOCAL_TEST = False


def get_input(is_test=LOCAL_TEST):
    """If not local test is active
    gets the user input to initialize
    game field and move commands"""
    if is_test:
        matrix = TEST_MATRIX
        commands = TEST_COMMANDS
    else:
        matrix = []
        size = int(input())
        commands = input().split(SPLITTER)
        for _ in range(size):
            row = [x for x in input().split(SPLITTER)]
            matrix.append(row)
    return matrix, commands


def get_starting_position(m):
    """Finds starting cell coordinates"""
    for r in range(len(m)):
        for c in range(len(m)):
            if m[r][c] == START_CELL:
                return r, c


def calc_new_position(x, y, com):
    """Calculate coordinates after 1 step move"""
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
    """Check if the given coordinates are in the range of matrix"""
    size = len(m)
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def move(mat, pos, stat, comm):
    """Perform 1 step movement.
    Returns the updated matrix, new position
    and current status"""
    x, y = pos
    new_x, new_y = calc_new_position(x, y, comm)
    if is_valid_cell(mat, new_x, new_y):
        pos = new_x, new_y
        cell = mat[new_x][new_y]
        if cell == END_ROUTE:
            stat = GAME_OVER
            return mat, pos, stat
        if cell == COAL_CELL:
            mat[new_x][new_y] = REGULAR_CELL
    return mat, pos, stat


def check_status(mat, stat):
    """Checks what is the current status and
    returns new status if needed."""
    if stat == GAME_OVER:
        return GAME_OVER
    for r in range(len(mat)):
        if COAL_CELL in mat[r]:
            return PLAY
    return WIN


def print_output(matrix, position, status):
    """Prints the output message with the current coordinates"""
    if status == GAME_OVER:
        print(f'{GAME_OVER_MSG} {position}')
    elif status == WIN:
        print(f'{WIN_MSG} {position}')
    else:
        coals_left = 0
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if matrix[r][c] == COAL_CELL:
                    coals_left += 1
        print(f'{coals_left} {TIE_MSG} {position}')


def main():
    """No strings in logic and functions!:)"""
    matrix, commands = get_input()
    position = get_starting_position(matrix)
    status = PLAY
    for command in commands:
        matrix, position, status = move(
            matrix, position, status, command)
        status = check_status(matrix, status)
        if not status == PLAY:
            break
    print_output(matrix, position, status)


main()
