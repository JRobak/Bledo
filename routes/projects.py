from flask import Blueprint, request, render_template, redirect, url_for
from databases.database_config import return_user_tables, add_new_project as add_new_project_db, check_exists_project, return_user

projects_ = Blueprint('projects', __name__)


# WYSWIETLA WSZYSTKIE PROJEKTY
@projects_.route('/projects/')
def view_projects():
    title = "Projekty"

    session = request.cookies.get('session')
    user_id = return_user(session)
    if user_id:
        projects_list = return_user_tables(user_id)
        return render_template('view_projects.html', title=title, projects_list=projects_list)

    return redirect(url_for('login.login'))


# POST - DODAJE NOWY PROJEKT
@projects_.route('/add_new_project/', methods=["POST"])
def add_new_project():
    if request.method == "POST":
        session = request.cookies.get('session')
        user_id = return_user(session)
        new_project_name = request.form.get('new_project_name')
        if check_exists_project(new_project_name, user_id):
            return view_project(new_project_name)
        else:
            add_new_project_db(new_project_name, user_id)
            return view_project(new_project_name)

    return redirect(url_for('account.account'))


# WYSWIETLA PROJEKT O DANEJ NAZWIE
@projects_.route('/project/<project_name>/')
def view_project(project_name):
    session = request.cookies.get('session')
    user_id = return_user(session)
    if check_exists_project(project_name, user_id):
        return render_template('view_project.html', project_name=project_name)

    return redirect(url_for('account.account'))
