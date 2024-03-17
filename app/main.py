from app import create_app
from flask import g, request
import sqlite3

app = create_app()


@app.before_request
def before_request():
    g.db = sqlite3.connect('../databases/bledo_databases.db')
    g.cursor = g.db.cursor()
    session = request.cookies.get('session')
    if session:
        from databases.database_config import get_image_path, return_user, get_user_name
        g.user_id = return_user(session)
        g.username = get_user_name(g.user_id)
        g.user_image = get_image_path(g.username)


@app.after_request
def after_request(response):
    if hasattr(g, 'db'):
        g.db.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)
