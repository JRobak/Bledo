import sqlite3
from flask import g


def add_new_project(name, user_id):
    g.cursor.execute("INSERT INTO projects (name, id_user) VALUES (?, ?)", (name, user_id))
    g.db.commit()


def check_exists(name, user_id):
    query = f"SELECT name FROM projects WHERE name = ? AND id_user = ?"
    g.cursor.execute(query, (name, user_id))
    return g.cursor.fetchone() is not None


def return_user_tables(user_id):
    query = f"SELECT name FROM projects WHERE id_user = ?"
    g.cursor.execute(query, (user_id,))
    return g.cursor.fetchall()

# db = sqlite3.connect('bledo_databases.db')
# cursor = db.cursor()
#
# # cursor.execute('''CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT, id_user INTEGER, FOREIGN KEY(id_user) REFERENCES users(id))''')
#
# cursor.execute("INSERT INTO projects (name, id_user) VALUES ('p9', 1)")
# cursor.execute("INSERT INTO projects (name, id_user) VALUES ('p0', 1)")
# cursor.execute("INSERT INTO projects (name, id_user) VALUES ('projec1', 1)")
# db.commit()
#
# # cursor.execute("SELECT projects.name, users.name FROM projects INNER JOIN users ON projects.id_user = users.id")
# #
# # rows = cursor.fetchall()
# # for row in rows:
# #     print(row)
#
# db.close()