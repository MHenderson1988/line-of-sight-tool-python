import sqlite3


def connect_db():
    return sqlite3.connect('test.db')


def create_development_table(conn):
    conn.execute('''
    CREATE TABLE if not exists developments(
    development_id INTEGER PRIMARY KEY UNIQUE,
    name CHAR(50) NOT NULL UNIQUE
    );
    ''')


def create_location_table(conn):
    conn.execute('''
    CREATE TABLE if not exists location(
    id INTEGER PRIMARY KEY,
    development_id INT NOT NULL,
    name CHAR(50) NOT NULL UNIQUE,
    x CHAR(20) NOT NULL,
    y CHAR(20) NOT NULL,
    height CHAR(10) NOT NULL,
    
    FOREIGN KEY(development_id)
        REFERENCES development(id)
    );
    ''')


def insert_to_developments_table(conn, value):
    curr = conn.cursor()
    curr.execute('''INSERT INTO developments(name) VALUES (?)''', (value,))


if __name__ == '__main__':
    conn = connect_db()
    create_location_table(conn)
    create_development_table(conn)
    
    curr = conn.cursor()
    curr.execute('''
    SELECT * FROM developments
    ''')

    rows = curr.fetchall()

    for row in rows:
        print(row)
