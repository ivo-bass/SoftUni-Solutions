def get_for_input(count):
    """Takes input with for loop in given range.
    Returns list of the inputs."""
    return [input() for _ in range(count)]


def get_while_input(endword):
    """Takes input with no given range but with keyword.
    Returns list of the inputs."""
    the_input = []
    while True:
        text = input()
        if text == endword:
            return the_input
        the_input.append(text)


# __________________________________________
MATRIX = []
LOCAL_TEST = False


def get_matrix_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = MATRIX
    else:
        rows, _ = map(int, input().split(' '))
        matrix = []
        for row in range(rows):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)
    return matrix


def print_matrix(m):
    for r in range(len(m)):
        print(*m[r])
