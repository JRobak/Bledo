from flask import render_template, Blueprint

account_ = Blueprint('account', __name__)


@account_.route('/account/<username>')
def account(username):
    title = 'Ustawienia konta'
    return render_template('account.html', title=title, username=username)