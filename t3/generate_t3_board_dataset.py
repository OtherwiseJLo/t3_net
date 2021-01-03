import sqlite3
from typing import Tuple

from t3.board import Board


def calculate_board_state_label(num: str) -> Board:
    _board_state = bin(num)[2:].zfill(18)
    return Board(_board_state)


def main():
    conn = sqlite3.connect("t3.db")
    cur = conn.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS t3;
        CREATE TABLE IF NOT EXISTS t3(
        STATE TEXT PRIMARY KEY NOT NULL,
        LABEL TEXT);
        """
    )
    for board in map(calculate_board_state_label, range(2 ** 19)):
        insert_values = f"{board.state}, {board.label}"
        insert_statement = f"INSERT INTO t3 VALUES({insert_values});"
        cur.execute(insert_statement)
    conn.commit()


if __name__ == "__main__":
    main()
