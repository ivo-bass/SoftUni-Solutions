def get_row():
    return [int(x) for x in input().split(', ')]


def get_matrix(n):
    return [get_row() for _ in range(n)]


def flat_matrix(m):
    return [num for row in m for num in row]


n = int(input())
matrix = get_matrix(n)
flat = flat_matrix(matrix)
print(flat)
