from flask import Flask
from routes import account, login, projects


def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.register_blueprint(account.account_)
    app.register_blueprint(login.login_)
    app.register_blueprint(projects.projects_)

    return app
