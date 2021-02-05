from python_advanced.wotkshop_tic_tac_toe.modules.play import play, print_result
from python_advanced.wotkshop_tic_tac_toe.modules.setup import setup
from python_advanced.wotkshop_tic_tac_toe.modules.utils import POSITIVE_ANSWERS, print_goodbye_msg


def main():
    pl_1, pl_2, board = setup()
    while True:
        play(board, pl_1, pl_2)
        print_result(pl_1.name, pl_2.name, pl_1.wins, pl_2.wins)
        new_game_prompt = input("Play another game? [y/n]: ").lower()
        if new_game_prompt not in POSITIVE_ANSWERS:
            print_goodbye_msg()
            break


if __name__ == '__main__':
    main()
