from flask import Flask
from . import account, login


def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.register_blueprint(account.account_)
    app.register_blueprint(login.login_)

    return app