from itertools import cycle

from python_advanced.wotkshop_tic_tac_toe.modules.setup import clean_board
from python_advanced.wotkshop_tic_tac_toe.modules.utils import *


def ask_for_position(board, name):
    """Ask for player's choice until it is valid."""
    while True:
        position = input(f'{name} choose a free position [1-9]: ')
        if is_valid_position(board, position):
            return position
        print_invalid_position_msg(position)


def get_coordinates(position):
    return LEGAL_MOVES[position]


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


def play(board, pl1, pl2):
    board = clean_board(board)
    print_start_msg()
    show_board(board)
    players = cycle([pl1, pl2])
    for player in players:
        position = ask_for_position(board, player.name)
        row, col = get_coordinates(position)
        board = draw_position_on_board(board, row, col, player.symbol)
        show_board(board)
        if is_winner(board, row, col, player.symbol):
            print_winner(player.name)
            player.wins += 1
            break
        if is_full_board(board):
            print_tie(pl1.name, pl2.name)
            break
