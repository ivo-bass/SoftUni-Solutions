def split_input_by_pipe():
    return [str(x) for x in input().split('|')]


def create_matrix(ll):
    return [ll[i].split() for i in range(len(ll)-1, -1, -1)]


def flat_matrix(m):
    return [num for row in m for num in row]


def print_output(ll):
    print(' '.join([str(x) for x in ll]))


big_list = split_input_by_pipe()
matrix = create_matrix(big_list)
flat = flat_matrix(matrix)
print_output(flat)
