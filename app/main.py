from app import create_app
from flask import g
import sqlite3

app = create_app()


@app.before_request
def before_request():
    g.db = sqlite3.connect('../databases/bledo_databases.db')
    g.cursor = g.db.cursor()


# @app.after_request
# def after_request():
#     g.db.close()


if __name__ == '__main__':
    app.run(debug=True)