from sqlite3 import connect


def create_connect():
    conn = connect('bubble.sqlite3')
    return conn


if __name__ == '__main__':
    conn = create_connect()
    cur = conn.cursor()
    with open('DB/create_db.sql', 'r') as f:
        text = f.read()

    cur.executescript(text)
    conn.close()
