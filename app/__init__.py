from flask import Flask
from routes import account, login
from flask import g
import sqlite3


def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.register_blueprint(account.account_)
    app.register_blueprint(login.login_)

    @app.before_request
    def before_request():
        g.db = sqlite3.connect('../databases/bledo_databases.db')
        g.cursor = g.db.cursor()

    @app.after_request
    def after_request(response):
        if hasattr(g, 'db'):
            g.db.close()
        return response

    return app