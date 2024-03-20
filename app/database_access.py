from datetime import datetime, timedelta
from flask import g


# users
def check_exists_user(name):
    query = f"SELECT name FROM users WHERE name = ?"
    g.cursor.execute(query, (name,))
    return g.cursor.fetchone() is not None


def add_data(name):
    g.cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    g.db.commit()


def get_user_id(name):
    query = f"SELECT id FROM users WHERE name = ?"
    g.cursor.execute(query, (name,))
    return str(g.cursor.fetchone())[1:-2]


def get_user_name(id):
    query = f"SELECT name FROM users WHERE id = ?"
    g.cursor.execute(query, (id,))
    return str(g.cursor.fetchone())[2:-3]


# projects
def add_new_project(name, user_id):
    g.cursor.execute("INSERT INTO projects (name, id_user) VALUES (?, ?)", (name, user_id))
    g.db.commit()


def check_exists_project(name, user_id):
    query = f"SELECT name FROM projects WHERE name = ? AND id_user = ?"
    g.cursor.execute(query, (name, user_id))
    return g.cursor.fetchone() is not None


def return_user_tables(user_id):
    query = f"SELECT name FROM projects WHERE id_user = ?"
    g.cursor.execute(query, (user_id,))
    return g.cursor.fetchall()


# image
def change_image_user(user_id, path_to_image):
    g.cursor.execute("UPDATE users SET img_path = ? WHERE id = ?", (path_to_image, user_id))
    g.db.commit()


def get_image_path(user_name):
    query = f"SELECT img_path FROM users WHERE name = ?"
    g.cursor.execute(query, (user_name,))
    return str(g.cursor.fetchone())[2:-3]


# sessions
def check_exists_number_session(nr):
    query = f"SELECT session_number FROM sessions WHERE session_number = ?"
    g.cursor.execute(query, (nr,))
    return g.cursor.fetchone() is not None


def return_session_number(user_id):
    query = f"SELECT session_number FROM sessions WHERE id_user = ?"
    g.cursor.execute(query, (user_id,))
    return str(g.cursor.fetchone())[2:-3]


def return_user(nr_session):
    query = f"SELECT id_user FROM sessions WHERE session_number = ?"
    g.cursor.execute(query, (nr_session,))
    return str(g.cursor.fetchone())[1:-2]


def create_new_session(user_id):
    from app.sessions import create_session_number, LENGTH
    new_session_number = create_session_number(LENGTH)
    while check_exists_number_session(new_session_number):
        new_session_number = create_session_number(LENGTH)

    date_of_creation = datetime.now().strftime("%d-%m-%Y")
    expiration_date = (datetime.now() + timedelta(days=4)).strftime("%d-%m-%Y")

    g.cursor.execute("INSERT INTO sessions (id_user, session_number, date_of_creation, expiration_date) VALUES (?, ?, ?, ?)", (user_id, new_session_number, date_of_creation, expiration_date))
    g.db.commit()

    return new_session_number


def check_expiration_date(nr):
    query = f"SELECT expiration_date FROM sessions WHERE session_number = ?"
    g.cursor.execute(query, (nr,))
    date_str = g.cursor.fetchone()[0]
    expiration_date = datetime.strptime(date_str, "%d-%m-%Y")
    current_datetime = datetime.now()
    return (expiration_date - current_datetime).days >= 0


def extend_date_of_session(nr):
    expiration_date = (datetime.now() + timedelta(days=4)).strftime("%d-%m-%Y")
    g.cursor.execute("UPDATE sessions SET expiration_date = ? WHERE session_number = ?", (expiration_date, nr))
    g.db.commit()


def delete_session(nr):
    query = "DELETE FROM sessions WHERE session_number = ?"
    g.cursor.execute(query, (nr,))
    g.db.commit()
