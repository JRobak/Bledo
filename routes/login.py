from flask import render_template, request, redirect, url_for, Blueprint, make_response
from databases.databases_config import check_exists, add_data, get_user_id

login_ = Blueprint('login', __name__)


@login_.route('/login/', methods=['GET', 'POST'])
def login():
    title = 'Zaloguj się'

    user_id = request.cookies.get('user_id')
    if user_id:
        return redirect(url_for('account.account'))

    if request.method == "POST":
        username = request.form.get('username')
        username = username.strip()
        if not username:
            return render_template('login.html', title=title, error="Nazwa nie może byc pusta")

        if not check_exists(username):
            add_data(username)

        db_user_id = str(get_user_id(username))[1:-2]  # zwraca (1,) dlatego ustawione na [1:-2]
        response = make_response(redirect(url_for('account.account')))
        response.set_cookie('user_id', db_user_id)
        response.set_cookie('user_name', username)
        return response

    return render_template('login.html', title=title)


@login_.route('/logout/')
def logout():
    response = make_response(redirect(url_for('login.login')))
    response.delete_cookie('user_id')
    return response
