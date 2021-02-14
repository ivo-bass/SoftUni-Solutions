PLAYER = 'P'
WALL = 'X'
GAME_OVER = -1
WIN = +1

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coins = 0
        self.status = 0
        self.path = []


def get_field():
    size = int(input())
    return [input().split(' ') for _ in range(size)]


def locate_element(matrix, element):
    for row in range(len(matrix)):
        if element in matrix[row]:
            col = matrix[row].index(element)
            return row, col


def is_valid_index(v, max_v):
    return 0 <= v < max_v


def made_wrong_move():
    player.status = GAME_OVER
    player.coins //= 2


def collect_coins(board, new_x, new_y):
    number = int(board[new_x][new_y])
    player.x = new_x
    player.y = new_y
    player.path.append([new_x, new_y])
    player.coins += number
    if player.coins >= 100:
        player.status = WIN


def make_move(board, new_x, new_y):
    new_cell = board[new_x][new_y]
    if new_cell == WALL:
        made_wrong_move()
        return
    collect_coins(board, new_x, new_y)


def move_player(board, n_x, n_y):
    new_x = player.x + n_x
    new_y = player.y + n_y
    if not is_valid_index(new_x, len(board)) or not is_valid_index(new_y, len(board)):
        made_wrong_move()
        return
    make_move(board, new_x, new_y)


def print_path():
    print('Your path:')
    [print(x) for x in player.path]


def print_game_over():
    print(f'Game over! You\'ve collected {player.coins} coins.')
    print_path()


def print_win():
    print(f'You won! You\'ve collected {player.coins} coins.')
    print_path()


field = get_field()
pl_x, pl_y = locate_element(field, PLAYER)
player = Player(pl_x, pl_y)
while True:
    command = input()
    if command not in DIRECTIONS.keys():
        continue
    next_x, next_y = DIRECTIONS[command]
    move_player(field, next_x, next_y)
    if player.status == GAME_OVER:
        print_game_over()
        break
    if player.status == WIN:
        print_win()
        break
