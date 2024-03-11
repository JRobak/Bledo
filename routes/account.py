from flask import render_template, Blueprint, request, redirect, url_for

from databases.database_project import get_user_thumbnail

account_ = Blueprint('account', __name__)


@account_.route('/account/')
def account():
    title = 'Ustawienia konta'

    user_id = request.cookies.get('user_id')
    thumbnail = get_user_thumbnail(user_id)
    if user_id:
        return render_template('account.html', title=title, user_account_photo=url_for("static", filename=thumbnail))

    return redirect(url_for('login.login'))
