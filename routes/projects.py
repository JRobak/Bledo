from flask import Blueprint, request

projects_ = Blueprint('projects', __name__)


@projects_.route('/project/<project_name>/')
def view_project(project_name):
    user_id = request.cookies.get('user_id')