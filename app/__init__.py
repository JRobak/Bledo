import os

from flask import Flask

from app.database_access import db
from routes import account, login, projects, errors, tasks


def create_app():
    db_path = os.path.join(os.environ['BLEDO_DATABASE_PATH'], 'bledo_databases.db')

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(account.account_)
    app.register_blueprint(login.login_)
    app.register_blueprint(projects.projects_)
    app.register_blueprint(errors.errors_)
    app.register_blueprint(tasks.tasks_)

    db.init_app(app)

    return app
