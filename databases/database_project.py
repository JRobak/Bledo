from flask import g


def add_new_project(name, user_id):
    pass


def check_exists(name, user_id):
    pass


def return_user_tables(user_id):
    pass

# db = sqlite3.connect('bledo_databases.db')
# cursor = db.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT, id_user INTEGER, FOREIGN KEY(id_user) REFERENCES users(id))''')
#
# # cursor.execute("INSERT INTO projects (name, id_user) VALUES ('p70', 2)")
# # db.commit()
#
# cursor.execute("SELECT projects.name, users.name FROM projects INNER JOIN users ON projects.id_user = users.id")
#
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# db.close()