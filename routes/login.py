from flask import render_template, request, redirect, url_for, Blueprint, make_response
from app.database_access import check_exists_user, add_data, get_user_id, create_new_session, delete_session

login_ = Blueprint('login', __name__)


@login_.route('/login/', methods=['GET', 'POST'])
def login():
    title = 'Zaloguj się'

    if 'session' in request.cookies:
        return make_response(redirect(url_for('account.account')))

    if request.method == "POST":
        username = request.form.get('username').strip()

        if not username:
            return make_response(render_template('login.html', title=title, error="Field can't be empty"))

        if not check_exists_user(username):
            add_data(username)

        db_user_id = get_user_id(username)

        # nr_session = return_session_number(db_user_id)
        # if nr_session and check_exists_number_session(nr_session):
        #     if check_expiration_date(nr_session):
        #         response = make_response(redirect(url_for('account.account')))
        #         response.set_cookie('session', nr_session)
        #         return response
        #     else:
        #         delete_session(nr_session)

        nr_session = create_new_session(db_user_id)
        response = make_response(redirect(url_for('account.account')))
        response.set_cookie('session', nr_session)
        return response

    response = make_response(render_template('login.html', title=title))
    return response


@login_.route('/logout/')
def logout():
    delete_session(request.cookies.get('session'))

    response = make_response(redirect(url_for('login.login')))
    response.delete_cookie('session')
    return response
