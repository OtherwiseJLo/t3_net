import itertools as it
import TicTacToe

move_list = list(it.product(range(3), range(3)))

all_moves = list(it.permutations(move_list, len(move_list)))
all_boards = [TicTacToe.Board(move) for move in all_moves]
