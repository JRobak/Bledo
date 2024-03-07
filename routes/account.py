from flask import render_template, Blueprint, request, redirect, url_for

account_ = Blueprint('account', __name__)


@account_.route('/account/')
def account():
    title = 'Ustawienia konta'

    user_id = request.cookies.get('user_id')
    if user_id:
        return render_template('account.html', title=title)

    return redirect(url_for('login.login'))