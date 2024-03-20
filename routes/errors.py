from flask import Blueprint, redirect, url_for

errors_ = Blueprint('errors', __name__)


@errors_.app_errorhandler(401)
def unauthorized(error):
    response = redirect(url_for('login.login'))
    response.delete_cookie('session')
    return response
