from flask import render_template, request, redirect, url_for, Blueprint, make_response
from databases.database_config import check_exists_user, add_data, get_user_id, check_expiration_date, check_exists_number_session, create_new_session, return_session_number, delete_session, extend_date_of_session
from lib.session import get_session_number

login_ = Blueprint('login', __name__)


@login_.route('/login/', methods=['GET', 'POST'])
def login():
    title = 'Zaloguj się'

    # if not get_session_number():
    #     return redirect(url_for("account.account"))

    if request.method == "POST":
        username = request.form.get('username')
        username = username.strip()

        if not username:
            response = make_response(render_template('login.html', title=title, error="Nazwa nie może byc pusta"))
            response.delete_cookie('session')
            return response

        if not check_exists_user(username):
            add_data(username)

        db_user_id = get_user_id(username)

        nr_session = return_session_number(db_user_id)
        if nr_session and check_exists_number_session(nr_session):
            if check_expiration_date(nr_session):
                response = make_response(redirect(url_for('account.account')))
                response.set_cookie('session', nr_session)
                return response
            else:
                delete_session(nr_session)

        session_number = create_new_session(db_user_id)
        # session_number = return_session_number(db_user_id)
        response = make_response(redirect(url_for('account.account')))
        response.set_cookie('session', session_number)
        return response

    response = make_response(render_template('login.html', title=title))
    response.delete_cookie('session')
    return response


@login_.route('/logout/')
def logout():
    delete_session(request.cookies.get('session'))

    response = make_response(redirect(url_for('login.login')))
    response.delete_cookie('session')
    return response
