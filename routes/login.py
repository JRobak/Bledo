from flask import render_template, request, redirect, url_for, Blueprint, make_response
from databases.database_config import check_exists_user, add_data, get_user_id, check_expiration_date, check_exists_number_session, create_new_session, return_session_number, delete_session

login_ = Blueprint('login', __name__)


@login_.route('/login/', methods=['GET', 'POST'])
def login():
    title = 'Zaloguj się'

    nr_session = request.cookies.get('session')
    if nr_session and check_exists_number_session(nr_session):
        if check_expiration_date(nr_session):
            return redirect(url_for('account.account'))
        else:
            delete_session(nr_session)

    if request.method == "POST":
        username = request.form.get('username')
        username = username.strip()

        if not username:
            response = make_response(render_template('login.html', title=title, error="Nazwa nie może byc pusta"))
            response.delete_cookie('session')
            response.delete_cookie('user_name')
            return response

        if not check_exists_user(username):
            add_data(username)

        db_user_id = str(get_user_id(username))[1:-2]

        nr_session = str(return_session_number(db_user_id))[2:-3]
        if nr_session and check_exists_number_session(nr_session):
            if check_expiration_date(nr_session):
                response = make_response(redirect(url_for('account.account')))
                response.set_cookie('session', nr_session)
                response.set_cookie('user_name', username)
                return response
            else:
                delete_session(nr_session)

        create_new_session(db_user_id)
        session_number = str(return_session_number(db_user_id))[2:-3]
        response = make_response(redirect(url_for('account.account')))
        response.set_cookie('session', session_number)
        response.set_cookie('user_name', username)
        return response

    response = make_response(render_template('login.html', title=title))
    response.delete_cookie('session')
    response.delete_cookie('user_name')
    return response


@login_.route('/logout/')
def logout():
    delete_session(request.cookies.get('session'))

    response = make_response(redirect(url_for('login.login')))
    response.delete_cookie('session')
    response.delete_cookie('user_name')
    return response
