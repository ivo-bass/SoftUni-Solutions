from python_advanced.wotkshop_tic_tac_toe.modules.utils import *


class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = ''
        self.wins = 0


def create_players(turns=PLAYERS_COUNT):
    return [Player(input(f'Player {turn} name: ')) for turn in turns]


def assign_players_symbols(*pls, symbols=PLAYERS_SYMBOLS):
    while True:
        symbol = input(f'{pls[0].name} would you like to play with "X" or "O"?').upper()
        if is_valid_symbol(symbol):
            pls[0].symbol = symbol
            pls[1].symbol = symbols[1] if pls[0].symbol == symbols[0] else symbols[0]
            break
        else:
            print_invalid_symbol_msg(symbol)


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


def show_board_numbers(board):
    print_show_board_numbers_msg()
    show_board(board)


def clean_board(board):
    return [[EMPTY_CELL for _ in range(len(board))] for _ in range(len(board))]


def setup():
    pl_1, pl_2 = create_players()
    assign_players_symbols(pl_1, pl_2)
    board = create_board()
    show_board_numbers(board)
    return pl_1, pl_2, board
