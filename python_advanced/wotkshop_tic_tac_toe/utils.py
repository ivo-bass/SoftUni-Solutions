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


# ____Validations____

def is_valid_symbol(symbol, symbols=PLAYERS_SYMBOLS):
    return symbol in symbols


def is_valid_position(board, position):
    """First check if is legal matrix choice,
    than check if the cell is empty."""
    if position in LEGAL_MOVES:
        row, col = LEGAL_MOVES[position]
        return board[row][col] == EMPTY_CELL


def is_full_board(board):
    for row in board:
        if EMPTY_CELL in row:
            return False
    return True


# ____Print functions_____

def print_tie(name1, name2):
    print(f'{name1} and {name2} it\'s tie')


def print_winner(name):
    print(f'{name} won!')


def show_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')


def print_invalid_symbol_msg(s):
    print(f'"{s}" is invalid symbol.')


def print_show_board_numbers_msg():
    print('This is the numeration of the board:')


def print_invalid_position_msg(p):
    print(f'"{p}" is invalid position.')
