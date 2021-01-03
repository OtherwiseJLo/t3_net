import numpy as np


class Board:
    def __init__(self, state: str):
        self.state = state
        self.board = np.array([int(i) for i in state], dtype=np.uint8)
        self.board.reshape((2, 3, 3))
        self.label = self._calculate_label()

    def _calculate_label(self):
        return "NULL"

    def _is_invalid(self) -> bool:
        if self.board.sum() < 5 or self.board > 9:
            return True
        return False
