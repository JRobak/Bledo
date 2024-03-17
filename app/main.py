from app import create_app
from flask import g, request
import sqlite3

app = create_app()


@app.before_request
def before_request():
    g.username = request.cookies.get('user_name')
    g.db = sqlite3.connect('../databases/bledo_databases.db')
    g.cursor = g.db.cursor()
    from databases.database_config import get_image_path
    g.user_image = get_image_path(g.username)


@app.after_request
def after_request(response):
    if hasattr(g, 'db'):
        g.db.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)