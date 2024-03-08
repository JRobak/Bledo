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


# db = Database_User('databases/bledo_databases.db')

# cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# rows = db.fetchall()
# for row in rows:
#     print(row)

# db.close_connection()
