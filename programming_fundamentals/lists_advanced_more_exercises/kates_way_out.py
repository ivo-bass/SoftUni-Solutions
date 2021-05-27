# TODO: NOT WORKING PROPERLY

test_maze = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', '#', ' ', ' ', 'k', '#'],
    ['#', '#', ' ', '#', '#', '#'],
    ['#', '#', ' ', '#', '#', '#'],
]

# test_maze = [
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '#', ' ', ' ', 'k', '#'],
#     ['#', '#', ' ', '#', '#', '#'],
#     ['#', '#', '#', '#', '#', '#'],
#     ['#', '#', ' ', '#', '#', '#'],
# ]

WALL_CELL = "#"
EMPTY_CELL = " "
KATE = "k"
DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


def get_maze(is_test=False):
    if is_test:
        return test_maze
    ll = []
    rows = int(input())
    for _ in range(rows):
        ll.append(list(input()))
    return ll


def find_kate_position(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == KATE:
                return row, col


def is_in_the_maze(maze, row, col):
    max_row = len(maze)
    max_col = len(maze[0])
    return 0 <= row < max_row and 0 <= col < max_col


def find_the_way_out(maze, position, moves=0):
    row, col = position
    if not is_in_the_maze(maze, row, col):
        return moves

    value = maze[row][col]
    if value == WALL_CELL:
        return 0
    if value == EMPTY_CELL:
        maze[row][col] = KATE
        return 1

    for direction in DIRECTIONS:
        delta_row, delta_col = direction
        new_row, new_col = delta_row + row, delta_col + col

        moves += find_the_way_out(maze, (new_row, new_col), moves)
    return moves


def kate_way_out():
    maze = get_maze(True)
    kate_position = find_kate_position(maze)
    moves = find_the_way_out(maze, kate_position)
    if moves:
        print(f"Kate got out in {moves} moves")
    else:
        print("Kate cannot get out")


kate_way_out()
