import numpy as np
from itertools import product
from random import shuffle, choices


class Board:
    def __init__(self):
        self.board = np.zeros([2, 3, 3])
        self.winner = 0

        self.play_game()

        self.array = self.board.flatten()
        self.truth = np.zeros(3)

    def generate_moves(self):
        moves = list(product(range(3), range(3)))
        shuffle(moves)
        return moves

    def play_game(self):
        for player, move in enumerate(self.generate_moves()):
            self.board[player % 2][move] = 1
            if self.game_has_winner(self.state()):
                break

    def calculate_col_sum(self):
        return np.max(np.sum(self.board, axis=1), axis=1)

    def calculate_row_sum(self):
        return np.max(np.sum(self.board, axis=2), axis=1)

    def calculate_diag_sum(self):
        main_diagonal = np.trace(self.board, axis1=1, axis2=2)
        flip_diagonal = np.trace(np.fliplr(self.board), axis1=1, axis2=2)
        return np.max(np.stack([main_diagonal, flip_diagonal]).T, axis=1)

    def state(self):
        return np.max(
            np.stack(
                [
                    self.calculate_col_sum(),
                    self.calculate_row_sum(),
                    self.calculate_diag_sum(),
                ]
            ),
            axis=0,
        )

    def game_has_winner(self, state):
        if (winner := np.where(state == 3)[0]).size:
            self.winner = winner[0] + 1
            return True
        return False

    def to_input_layer(self):
        self.array = self.board.flatten()
        self.truth[self.winner + 1] = 1


def create_sample(size=1000):
    samples = [Board() for _ in range(size * 30)]
    no_winner = choices([sample for sample in samples if sample.winner == 0], k=size)
    x_winner = choices([sample for sample in samples if sample.winner == 1], k=size)
    o_winner = choices([sample for sample in samples if sample.winner == 2], k=size)
    samples = x_winner + o_winner + no_winner
    shuffle(samples)
    return samples
