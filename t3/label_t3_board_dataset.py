import numpy as np
import sqlite3
from t3.board import Board


def label_board(state: str) -> str:
    return Board(state).label
