import TicTacToe
import sys
from itertools import combinations, combinations_with_replacement
import numpy as np

from progress.bar import Bar
from multiprocessing import Pool
from tqdm import *

non_unique = []


def check_if_unique(trial):
    board_sum = trial[0].board + trial[1].board
    if 1 not in np.unique(board_sum):
        non_unique.append(trial)
        sys.exit(sum([b.board for b in non_unique[0]]))
        return 1
    return 0


samples = TicTacToe.create_sample(1000)
trials = list(combinations(samples, 2))

with Pool() as p:
    with tqdm(total=len(trials)) as pbar:
        for i, _ in enumerate(p.imap_unordered(check_if_unique, trials)):
            pbar.update()
