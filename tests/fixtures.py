import sqlite3

from pytest import fixture


# @fixture()
# def database():
#     base = sqlite3.connect("test.db")
#     cursor = base.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
#     return base

@fixture()
def app():
    from app.main import app
    return app.test_client()
