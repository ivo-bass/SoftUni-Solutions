def get_row():
    return [int(s) for s in input().split(', ')]


def get_matrix():
    n = int(input())
    return [get_row() for _ in range(n)]


def extract_first_diagonal(m):
    size = len(m)
    return [m[r][r] for r in range(size)]


def extract_second_diagonal(m):
    size = len(m)
    return [m[r][size - r - 1] for r in range(size)]


def d_to_string(d):
    return ', '.join([str(n) for n in d])


matrix = get_matrix()
first_d = extract_first_diagonal(matrix)
second_d = extract_second_diagonal(matrix)
print(f'First diagonal: {d_to_string(first_d)}. Sum: {sum(first_d)}')
print(f'Second diagonal: {d_to_string(second_d)}. Sum: {sum(second_d)}')
