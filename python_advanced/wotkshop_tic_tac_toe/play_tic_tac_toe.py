from python_advanced.wotkshop_tic_tac_toe.modules.play import play
from python_advanced.wotkshop_tic_tac_toe.modules.setup import setup


def main():
    pl_1, pl_2, board = setup()
    play(board, pl_1, pl_2)


if __name__ == '__main__':
    main()
