PLAYER_CELL = 'P'
EMPTY_CELL = '-'
COMMANDS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def get_matrix_input():
    size = int(input())
    matrix = []
    for row in range(size):
        row = [x for x in input()]
        matrix.append(row)
    return matrix


def get_position(m):
    size = len(m)
    for row in range(size):
        for col in range(size):
            if m[row][col] == PLAYER_CELL:
                return row, col


def calc_next_cell(p, mov):
    x = p[0] + mov[0]
    y = p[1] + mov[1]
    return x, y


def is_valid_cell(m, c):
    x, y = c
    return 0 <= x < len(m) and 0 <= y < len(m)


def punishment(string):
    if string:
        string = string[:-1]
    return string


def make_move(m, n_cell, pos, string):
    pos_x, pos_y = pos
    x, y = n_cell
    if not m[x][y] == EMPTY_CELL:
        string += m[x][y]
    pos = n_cell
    m[pos_x][pos_y] = EMPTY_CELL
    m[x][y] = PLAYER_CELL
    return m, pos, string


def print_output(string, m):
    print(string)
    for r in range(len(m)):
        print(''.join(m[r]))


init_string = input()
matrix = get_matrix_input()
position = get_position(matrix)
count_of_commands = int(input())
for _ in range(count_of_commands):
    command = input()
    move_coordinates = COMMANDS[command]
    next_cell = calc_next_cell(position, move_coordinates)
    if not is_valid_cell(matrix, next_cell):
        init_string = punishment(init_string)
        continue
    matrix, position, init_string = make_move(
        matrix, next_cell, position, init_string)

print_output(init_string, matrix)
