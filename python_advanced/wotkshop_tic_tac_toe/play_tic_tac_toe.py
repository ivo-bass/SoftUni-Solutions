from itertools import cycle

PLAYERS_COUNT = ('one', 'two')
PLAYERS_SYMBOLS = ('X', 'O')
EMPTY_CELL = ' '
BOARD_SIZE = 3
LEGAL_MOVES = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
}
DIAGONAL_CELLS = ((0, 0), (0, 2), (1, 1), (2, 0), (2, 2))


class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = ''


def create_players(turns=PLAYERS_COUNT):
    return [Player(input(f'Player {turn} name: ')) for turn in turns]


def is_valid_symbol(symbol, symbols=PLAYERS_SYMBOLS):
    return symbol in symbols


def assign_players_symbols(*pls, symbols=PLAYERS_SYMBOLS):
    while True:
        symbol = input(f'{pls[0].name} would you like to play with "X" or "O"?').upper()
        if is_valid_symbol(symbol):
            pls[0].symbol = symbol
            pls[1].symbol = symbols[1] if pls[0].symbol == symbols[0] else symbols[0]
            break
        else:
            print('Try again.')


def create_board(size=BOARD_SIZE):
    """Create board with cell numbers 1-9"""
    cell = 1
    board = []
    for row_i in range(size):
        row = []
        for col_i in range(size):
            row.append(str(cell))
            cell += 1
        board.append(row)
    return board


def show_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')


def show_board_numbers(board):
    print('This is the numeration of the board:')
    show_board(board)


def clean_board(board):
    return [[EMPTY_CELL for _ in range(len(board))] for _ in range(len(board))]


def setup():
    pl_1, pl_2 = create_players()
    assign_players_symbols(pl_1, pl_2)
    board = create_board()
    show_board_numbers(board)
    board = clean_board(board)
    return pl_1, pl_2, board


def is_valid_position(board, position):
    """First check if is legal matrix choice,
    than check if the cell is empty."""
    if position in LEGAL_MOVES:
        row, col = LEGAL_MOVES[position]
        return board[row][col] == EMPTY_CELL


def ask_for_position(board, name):
    """Ask for player's choice until it is valid."""
    while True:
        pos = input(f'{name} choose a free position [1-9]: ')
        if is_valid_position(board, pos):
            return pos
        print('Invalid position.')


def draw_position_on_board(board, x, y, symbol):
    board[x][y] = symbol
    return board


def is_winner(board, row, col, symbol):
    """We need to check only the row and col for the current position.
    If current position is on diagonal only then diagonal check is needed."""
    check_current_row = all([board[row][c] == symbol for c in range(len(board))])
    check_current_col = all([board[r][col] == symbol for r in range(len(board))])
    if (row, col) in DIAGONAL_CELLS:
        check_main_diagonal = all([board[d][d] == symbol for d in range(len(board))])
        check_second_diagonal = all([board[d][len(board) - d - 1] == symbol for d in range(len(board))])
        return any((check_current_row, check_current_col, check_main_diagonal, check_second_diagonal))
    return any((check_current_row, check_current_col))


def print_winner(name):
    print(f'{name} won!')


def is_full_board(board):
    for row in board:
        if EMPTY_CELL in row:
            return False
    return True


def print_tie(name1, name2):
    print(f'{name1} and {name2} it\'s tie')


def get_coordinates(position):
    return LEGAL_MOVES[position]


def play(board, pl1, pl2):
    players = cycle([pl1, pl2])
    for player in players:
        position = ask_for_position(board, player.name)
        row, col = get_coordinates(position)
        board = draw_position_on_board(board, row, col, player.symbol)
        show_board(board)
        if is_winner(board, row, col, player.symbol):
            print_winner(player.name)
            break
        if is_full_board(board):
            print_tie(pl1.name, pl2.name)
            break


def main():
    pl_1, pl_2, board = setup()
    play(board, pl_1, pl_2)


if __name__ == '__main__':
    main()
