import sqlite3
from sqlite3 import Error


def connect_db():
    conn = None
    try:
        conn = sqlite3.connect('test.db')
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_project(conn, project_data):
    sql = ''' INSERT INTO projects(name) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, project_data)
    conn.commit()

    return cur.lastrowid


def insert_location(conn, location_data):
    sql = ''' INSERT INTO locations(project_id, x, y, height, name) VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, location_data)
    conn.commit()

    return cur.lastrowid


if __name__ == '__main__':

    create_projects_sql = """
        CREATE TABLE IF NOT EXISTS projects (
            name TEXT PRIMARY KEY
        );
    """

    create_locations_sql = """
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            project_name TEXT NOT NULL,
            x TEXT NOT NULL,
            y TEXT NOT NULL,
            height TEXT NOT NULL,
            name TEXT NOT NULL,
            
            FOREIGN KEY (project_id) REFERENCES projects(name)
        );
    """

    conn = connect_db()

    if conn is not None:
        create_table(conn, create_projects_sql)
        create_table(conn, create_locations_sql)

        project_1 = ("Sandy Knowe", )
        location_1 = ("Sandy Knowe", "-4.231212", "56.32312", "149.9", "1")

        insert_location(conn, location_1)

    else:
        print("Error! Cannot create the database connection")
