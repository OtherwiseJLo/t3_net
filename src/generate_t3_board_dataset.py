import sqlite3


def to_binary_string(num: int) -> str:
    return bin(num)[2:].zfill(18)


def main():
    conn = sqlite3.connect("t3.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS t3(
        BOARD TEXT PRIMARY KEY NOT NULL,
        LABEL TEXT);
        """
    )
    for state in map(to_binary_string, range(2 ** 19)):
        insert_values = f"{state}, NULL"
        insert_statement = f"INSERT INTO t3 VALUES({insert_values});"
        cur.execute(insert_statement)
    conn.commit()


if __name__ == "__main__":
    main()
