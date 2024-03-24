import sqlite3
import os

dir_db_path = os.environ['BLEDO_DATABASE_PATH']
db_path = os.path.join(dir_db_path, 'bledo_databases.db')


def create_database_file():
    os.makedirs(dir_db_path, exist_ok=True)
    if not os.path.exists(db_path):
        with open(db_path, 'w') as f:
            f.close()


def create_tables():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, img_path TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY, user_id INTEGER, session_number TEXT, date_of_creation TEXT, expiration_date TEXT, FOREIGN KEY (user_id) REFERENCES users(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT, user_id_creator INTEGER, FOREIGN KEY (user_id_creator) REFERENCES users(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS access_projects (id INTEGER PRIMARY KEY, project_id TEXT, user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (project_id) REFERENCES projects(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT, user_id INTEGER, user_id_creator INTEGER, project_name TEXT, description TEXT, date_of_creation TEXT, date_of_end TEXT, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (user_id_creator) REFERENCES users(id))''')
    conn.close()
