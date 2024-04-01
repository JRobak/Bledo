from flask import render_template, Blueprint, request, redirect, url_for
from lib.session import get_session_number

user_search_ = Blueprint('user_search', __name__)


@user_search_.route('/user_search/')
def user_search():
    nr_session = get_session_number()

    return render_template('user_search.html')
