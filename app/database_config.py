import sqlite3
import os

dir_db_path = os.environ['BLEDO_DATABASE_PATH']
db_path = os.path.join(dir_db_path, 'bledo_databases.db')


def create_database_file():
    os.makedirs(dir_db_path, exist_ok=True)
    with open(db_path, 'w') as f:
        f.close()


def create_tables():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, img_path TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY, id_user INTEGER, session_number TEXT, date_of_creation TEXT, expiration_date TEXT, FOREIGN KEY (id_user) REFERENCES users(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT, id_user INTEGER, FOREIGN KEY (id_user) REFERENCES users(id))''')

    conn.close()