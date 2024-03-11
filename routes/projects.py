from flask import Blueprint, request, render_template, redirect, url_for
from databases.database_project import return_user_tables, check_exists, add_new_project as aaad_new_project

projects_ = Blueprint('projects', __name__)


# WYSWIETLA WSZYSTKIE PROJEKTY
@projects_.route('/projects/')
def view_projects():
    title = "Projekty"

    user_id = request.cookies.get('user_id')
    if user_id:
        projects_list = return_user_tables(user_id)
        return render_template('view_projects.html', title=title, projects_list=projects_list)

    return redirect(url_for('login.login'))


# POST - DODAJE NOWY PROJEKT
@projects_.route('/add_new_project/', methods=["POST"])
def add_new_project():
    if request.method == "POST":
        user_id = request.cookies.get('user_id')
        new_project_name = request.form.get('new_project_name')
        if check_exists(new_project_name, user_id):
            return view_project(new_project_name)
        else:
            aaad_new_project(new_project_name, user_id)
            return view_project(new_project_name)

    return redirect(url_for('account.account'))


# WYSWIETLA PROJEKT O DANEJ NAZWIE
@projects_.route('/project/<project_name>/')
def view_project(project_name):
    user_id = request.cookies.get('user_id')
    if check_exists(project_name, user_id):
        return render_template('view_project.html', project_name=project_name)

    return redirect(url_for('account.account'))
