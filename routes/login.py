from flask import render_template, request, redirect, url_for, Blueprint, make_response
from lib.query_models import check_exists_user, add_new_user, create_new_session, get_user_by_name

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

        # if not check_exists_user(username):
        #     add_new_user(username)
        #
        # user_id = get_user_id_by_name(username)
        user = get_user_by_name(username)
        if not user:
            user = add_new_user(username)

        nr_session = create_new_session(user.id)
        response = make_response(redirect(url_for('account.account')))
        response.set_cookie('session', nr_session)
        return response

    response = make_response(render_template('login.html', title=title))
    return response


@login_.route('/logout/')
def logout():
    # delete_session(request.cookies.get('session'))

    response = make_response(redirect(url_for('login.login')))
    response.delete_cookie('session')
    return response
