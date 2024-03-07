import sqlite3
from flask import g


def check_exists(name):
    query = f"SELECT name FROM users WHERE name = ?"
    g.cursor.execute(query, (name,))
    return g.cursor.fetchone() is not None


def add_data(name):
    g.cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    g.db.commit()


def get_user_id(name):
    query = f"SELECT id FROM users WHERE name = ?"
    g.cursor.execute(query, (name,))
    return g.cursor.fetchone()


# class Database_User:
#     def __init__(self, path):
#         self.path = path
#         self.connect = sqlite3.connect(path)
#         self.cursor = self.connect.cursor()
#
#     def check_exists(self, name):
#         query = f"SELECT name FROM users WHERE name = ?"
#         self.cursor.execute(query, (name,))
#         return self.cursor.fetchone() is not None
#
#     def add_data(self, name):
#         self.cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
#         self.connect.commit()
#
#     def get_user_id(self, name):
#         query = f"SELECT id FROM users WHERE name = ?"
#         self.cursor.execute(query, (name,))
#         return self.cursor.fetchone()

    # close connect


# db = Database_User('databases/bledo_databases.db')

# cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# rows = db.fetchall()
# for row in rows:
#     print(row)

# db.close_connection()
