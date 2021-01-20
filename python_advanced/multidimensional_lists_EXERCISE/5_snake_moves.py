from collections import deque


TEST_MATRIX = [
    ['*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*'],
]
TEST_STRING = 'SoftUni'
LOCAL_TEST = False


def get_input(is_test=LOCAL_TEST):
    if is_test:
        matrix = TEST_MATRIX
        snake = deque([x for x in TEST_STRING])
    else:
        rows, cols = [int(x) for x in input().split(' ')]
        matrix = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append('*')
            matrix.append(row)

        snake = deque([x for x in input()])
    return matrix, snake


# __________________________________________


def place_snake_on_matrix(matrix, snake):
    is_right_direction = True
    moving_snake = snake.copy()
    for r_index in range(len(matrix)):
        if is_right_direction:
            for c_index in range(len(matrix[0])):
                if not moving_snake:
                    moving_snake = snake.copy()
                char = moving_snake.popleft()
                matrix[r_index][c_index] = char
            is_right_direction = False
        else:
            for c_index in range(len(matrix[0])-1, -1, -1):
                if not moving_snake:
                    moving_snake = snake.copy()
                char = moving_snake.popleft()
                matrix[r_index][c_index] = char
            is_right_direction = True
    return matrix


# __________________________________________


def print_matrix(matrix):
    for row_index in range(len(matrix)):
        print(''.join(matrix[row_index]))


def main():
    matrix, snake = get_input()
    matrix = place_snake_on_matrix(matrix, snake)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
