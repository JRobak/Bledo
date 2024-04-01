import os
from flask import Flask
from routes import account, login, projects, errors, tasks, user_search


def create_app(db, migrate):
    dir_db_path = os.environ['BLEDO_DATABASE_PATH']
    db_path = os.path.join(dir_db_path, 'bledo_databases.db')
    os.makedirs(dir_db_path, exist_ok=True)
    if not os.path.exists(db_path):
        with open(db_path, 'w') as f:
            f.close()

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    app.register_blueprint(account.account_)
    app.register_blueprint(login.login_)
    app.register_blueprint(projects.projects_)
    app.register_blueprint(errors.errors_)
    app.register_blueprint(tasks.tasks_)
    app.register_blueprint(user_search.user_search_)

    return app
