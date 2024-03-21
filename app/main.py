from app import create_app
from flask import g, request
import sqlite3
from app.database_config import create_database_file, create_tables, db_path

app = create_app()


@app.before_request
def before_request():
    g.db = sqlite3.connect(db_path)
    g.cursor = g.db.cursor()

    session = request.cookies.get('session')
    if session:
        from app.database_access import get_image_path_by_user_name, get_user_id_by_nr_session, get_user_name_by_id
        g.user_id = get_user_id_by_nr_session(session)
        g.username = get_user_name_by_id(g.user_id)
        g.user_image = get_image_path_by_user_name(g.username)


@app.after_request
def after_request(response):
    if hasattr(g, 'db'):
        g.db.close()
    return response


if __name__ == '__main__':
    create_database_file()
    create_tables()
    app.run(debug=True)
