from flask import Blueprint, render_template

from lib.session import get_session_number

tasks_ = Blueprint('tasks', __name__)


@tasks_.route('/tasks/')
def get_tasks():
    session = get_session_number()

    title = "Zadania"
    return render_template('view_tasks.html', title=title)
