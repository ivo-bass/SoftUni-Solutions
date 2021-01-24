END_COMMAND = 'END'
ADD_COMMAND = 'Add'
SUB_COMMAND = 'Subtract'


def get_input():
    size = int(input())
    return [[int(x) for x in input().split(' ')] for r in range(size)]


def is_valid_coordinates(m, x, y):
    size = len(m)
    return 0 <= x < size and 0 <= y < size


def err_msg():
    print('Invalid coordinates')


def add_value(m, r, c, val):
    m[r][c] += val
    return m


def subtract_value(m, r, c, val):
    m[r][c] -= val
    return m


def print_matrix(m):
    for row in range(len(m)):
        print(' '.join([str(x) for x in m[row]]))


matrix = get_input()

while True:
    command = input()
    if command == END_COMMAND:
        break
    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if not is_valid_coordinates(matrix, row, col):
        err_msg()
        continue
    if action == ADD_COMMAND:
        matrix = add_value(matrix, row, col, value)
    elif action == SUB_COMMAND:
        matrix = subtract_value(matrix, row, col, value)

print_matrix(matrix)
