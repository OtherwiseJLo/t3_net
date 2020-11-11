import numpy as np
from itertools import product
from random import shuffle, choices


class Board:
    def __init__(self):
        self.board = np.zeros([3, 3])
        self.winner = 0
        moves = list(product(range(3), range(3)))
        shuffle(moves)
        player = 1
        for move in moves:
            self.board[move] = player
            player *= -1
            if self.game_has_winner():
                break
        self.array = self.board.flatten()
        self.truth = np.zeros(3)
        self.truth[self.winner+1] = 1

    def game_has_winner(self):
        result = np.sum(self.board, axis=0)
        result = np.append(result, np.sum(self.board, axis=1))
        result = np.append(
            result, [np.diag(np.fliplr(self.board)), np.diag(self.board)]
        )
        if 3 in result:
            self.winner = 1
            return True
        elif -3 in result:
            self.winner = -1
            return True
        return False


def create_sample(size=1000):
    samples = [Board() for _ in range(size * 30)]
    x_winner = choices([sample for sample in samples if sample.winner == 1], k=size)
    o_winner = choices([sample for sample in samples if sample.winner == -1], k=size)
    no_winner = choices([sample for sample in samples if sample.winner == 0], k=size)
    samples = x_winner + o_winner + no_winner
    shuffle(samples)
    return samples
