from app import create_app
from flask import g, request
import sqlite3
import os


app = create_app()
app.static_folder = os.path.expandvars(os.path.dirname(__file__) + "\\..\\static")
print(app.static_folder)

@app.before_request
def before_request():
    g.username = request.cookies.get('user_name')
    g.db = sqlite3.connect('databases/bledo_databases.db')
    g.cursor = g.db.cursor()


@app.after_request
def after_request(response):
    if hasattr(g, 'db'):
        g.db.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)