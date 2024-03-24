from flask import Flask
from routes import account, login, projects, errors, tasks


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    app.register_blueprint(account.account_)
    app.register_blueprint(login.login_)
    app.register_blueprint(projects.projects_)
    app.register_blueprint(errors.errors_)
    app.register_blueprint(tasks.tasks_)

    return app
