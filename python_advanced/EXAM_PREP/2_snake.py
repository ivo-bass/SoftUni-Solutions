SNAKE = 'S'
BURROW = 'B'
FOOD = '*'
TRAIL = '.'
EMPTY = '-'
GAME_OVER = -1
WIN = +1
DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.food = 0
        self.status = 0


def get_board():
    size = int(input())
    return [list(input()) for _ in range(size)]


def locate_element(matrix, element):
    for row in range(len(matrix)):
        if element in matrix[row]:
            col = matrix[row].index(element)
            return row, col


def is_valid_index(v, max_v):
    return 0 <= v < max_v


def enter_burrow(board, snake, new_x, new_y):
    burrow_x, burrow_y = locate_element(board, BURROW)
    board[new_x][new_y] = TRAIL
    board[burrow_x][burrow_y] = SNAKE
    snake.x = burrow_x
    snake.y = burrow_y


def eat_food(snake):
    snake.food += 1
    if snake.food == 10:
        snake.status = WIN


def make_move(board, snake, new_x, new_y):
    new_cell = board[new_x][new_y]
    board[snake.x][snake.y] = TRAIL
    board[new_x][new_y] = SNAKE
    snake.x = new_x
    snake.y = new_y
    if new_cell == FOOD:
        eat_food(snake)
    if new_cell == BURROW:
        enter_burrow(board, snake, new_x, new_y)


def move_snake(board, snake, n_x, n_y):
    new_x = snake.x + n_x
    new_y = snake.y + n_y
    if not is_valid_index(new_x, len(board)) or not is_valid_index(new_y, len(board)):
        board[snake.x][snake.y] = TRAIL
        snake.status = -1
        return
    make_move(board, snake, new_x, new_y)


def print_end(matrix, snake):
    print(f'Food eaten: {snake.food}')
    [print(''.join(row)) for row in matrix]


def print_game_over(matrix, snake):
    print('Game over!')
    print_end(matrix, snake)


def print_win(matrix, snake):
    print('You won! You fed the snake.')
    print_end(matrix, snake)


def main():
    board = get_board()
    x, y = locate_element(board, SNAKE)
    snake = Snake(x, y)
    while True:
        command = input()
        next_x, next_y = DIRECTIONS[command]
        move_snake(board, snake, next_x, next_y)
        if snake.status == GAME_OVER:
            print_game_over(board, snake)
            break
        if snake.status == WIN:
            print_win(board, snake)
            break


if __name__ == '__main__':
    main()
