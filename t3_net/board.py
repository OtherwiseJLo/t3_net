import numpy as np


class Board:
    def __init__(self, state: str):
        self.state = _validate_state(state)
        self.board = np.array([int(i) for i in state], dtype=np.uint8)
        self.board.reshape((2, 3, 3))
        self.label = self._calculate_label()

    def _validate_state(self, state: str) -> str:
        assert len(state) == 18
        return state

    def _calculate_label(self):
        if self._is_invalid():
            return "INVALID"
        elif self._is_incomplete():
            return "INCOMPLETE"
        elif self._is_draw():
            return "DRAW"
        elif self._is_x_victory():
            return "X"
        elif self._is_o_victory():
            return "O"
        else:
            return "NULL"

    def _is_invalid(self) -> bool:
        # TODO:
        return False

    def _is_incomplete(self) -> bool:
        # TODO:
        return False

    def _is_draw(self) -> bool:
        # TODO:
        return False

    def _is_x_victory(self) -> bool:
        # TODO:
        return False

    def _is_o_victory(self) -> bool:
        # TODO:
        return False
