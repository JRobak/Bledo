from flask import render_template, request, redirect, url_for, Blueprint, make_response
from databases_config import check_exists, add_data, get_user_id

login_ = Blueprint('login', __name__)


@login_.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Zaloguj się'

    user_id = request.cookies.get('user_id')
    if user_id:
        return redirect(url_for('account'))

    if request.method == "POST":
        username = request.form.get('username')
        if not username:
            return render_template('login.html', title=title, error="Nazwa nie może by")

        if not check_exists(username):
            add_data(username)

        db_user_id = get_user_id(username)
        response = make_response(redirect(url_for('account')))
        response.set_cookie('user_id', str(db_user_id))
        return response

    return render_template('login.html', title=title)
