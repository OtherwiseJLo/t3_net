import itertools as it
import TicTacToe
from tqdm import *
from multiprocessing import Pool

move_list = list(it.product(range(3), range(3)))

all_moves = list(it.permutations(move_list, len(move_list)))
all_boards = []


def create_all_boards(move):
    return TicTacToe.Board(move)


def main():
    pool = Pool()
    return pool.map(create_all_boards, all_moves)


def test():
    with Pool() as pool:
        with tqdm(total=len(all_moves)) as progress_bar:
            for i, board in enumerate(pool.imap(create_all_boards, all_moves)):
                all_boards.append(board)
                progress_bar.update()


if __name__ == "__main__":
    test()
