import os
import sqlite3
from sqlite3 import Error


def connect_db():
    conn = None
    try:
        conn = sqlite3.connect(create_db_file_path())
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        conn.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_project(conn, project_data):
    sql = ''' INSERT INTO projects (name, locations) SELECT ?, COUNT (*) FROM locations WHERE project_id = ? '''
    conn.execute(sql, project_data)
    conn.commit()
    curr = conn.cursor()

    return curr.lastrowid


def insert_location(conn, location_data):
    sql = ''' INSERT INTO locations (project_id, x, y, height, name) VALUES(?,?,?,?,?) '''
    conn.execute(sql, location_data)
    conn.commit()
    curr = conn.cursor()

    return curr.lastrowid


"""
Method to retrieve specified data from a specified table.  Column names are passed via args and kwarg accepts
'table ='.  If no args are declared the query will return all columns from the specified table.
"""


def get_data_from_table(*args, **kwargs):
    table = kwargs.get('table', '*')

    conn = connect_db()
    cur = conn.cursor()

    sql = f''' SELECT {','.join(args)} FROM {table} '''

    cur.execute(sql)
    rows = cur.fetchall()

    return rows


# Used to quickly find the database file
def create_db_file_path():
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(CURRENT_DIR, "../db/test.db")


if __name__ == '__main__':
    create_projects_sql = """
        CREATE TABLE IF NOT EXISTS projects (
            name TEXT PRIMARY KEY,
            locations INTEGER,
            folder TEXT
        );
    """

    create_locations_sql = """
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            project_id TEXT NOT NULL,
            x TEXT NOT NULL,
            y TEXT NOT NULL,
            height TEXT NOT NULL,
            name TEXT NOT NULL,
            
            FOREIGN KEY (project_id) REFERENCES projects(name)
        );
    """
