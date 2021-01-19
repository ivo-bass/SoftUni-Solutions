END_COMMAND = 'END'
MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
]
LOCAL_TEST = True  # set as get_matrix parameter


def get_matrix(is_test=False):
    if is_test:
        matrix = MATRIX
    else:
        matrix = []
        row, _ = [int(x) for x in input().split(' ')]
        for _ in range(row):
            line = [x for x in input().split(' ')]
            matrix.append(line)
    return matrix


def validate_command(comm, mat):
    split_command = command.split()
    if not len(split_command) == 5:
        return False
    if not split_command[0] == 'swap':
        return False
    x1, y1, x2, y2 = [int(s) for s in split_command[1:]]
    if not x1 in range(len(mat)) or not x2 in range(len(mat)):
        return False
    if not y1 in range(len(mat[0])) or not y2 in range(len(mat[0])):
        return False
    return x1, y1, x2, y2


def perform_swap(m, x1, y1, x2, y2):
    # value_1 = m[x1][y1]
    # value_2 = m[x2][y2]
    # m[x1][y1] = value_2
    # m[x2][y2] = value_1
    m[x1][y1], m[x2][y2] = m[x2][y2], m[x1][y1]
    return m


def print_matrix(m):
    for row in range(len(m)):
        print(' '.join(map(str, m[row])))


matrix = get_matrix()
while True:
    command = input()
    if command == END_COMMAND:
        break
    is_valid = validate_command(command, matrix)
    if is_valid:
        x1, y1, x2, y2 = is_valid
        matrix = perform_swap(matrix, x1, y1, x2, y2)
        print_matrix(matrix)
    else:
        print('Invalid input!')
