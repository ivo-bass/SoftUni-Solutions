def get_magic_triangle(n, triangle=[[1], [1, 1]]):
    if n == len(triangle):
        return triangle
    triangle.append(generate_row(triangle))
    triangle = get_magic_triangle(n, triangle)
    return triangle


def generate_row(ll):
    next_row = []
    prev_row = ll[-1]
    for i in range(len(prev_row)+1):
        if i - 1 < 0:
            left_num = 0
        else:
            left_num = prev_row[i - 1]
        if i == len(prev_row):
            right_num = 0
        else:
            right_num = prev_row[i]
        next_row.append(left_num + right_num)
    return next_row
