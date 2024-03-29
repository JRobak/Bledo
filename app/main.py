from flask import g
from app import create_app
from lib.__init__ import db
from lib.session import get_session_number

app = create_app(db)


@app.before_request
def before_request():
    nr_session = get_session_number()
    if nr_session:
        from lib.query_models import get_user_by_nr_session
        user = get_user_by_nr_session(nr_session)
        if user:
            g.username = user.name
            g.user_image = user.img_path


if __name__ == '__main__':
    app.run(debug=True)