from flask import Blueprint, request, render_template, redirect, url_for
from lib.query_models import add_new_project as add_new_project_db, check_exists_project, \
    get_users_in_project_by_project_id, get_access_project_by_id, get_host_project, get_project_by_id
from lib.query_models import get_user_by_nr_session, get_user_projects_name_by_user_id, get_project_by_name_and_user, add_new_user_by_project_id_and_user_name
from lib.session import get_session_number

projects_ = Blueprint('projects', __name__)


# WYSWIETLA WSZYSTKIE PROJEKTY
@projects_.route('/projects/')
def view_projects():
    title = "Projekty"

    nr_session = get_session_number()

    user = get_user_by_nr_session(nr_session)
    projects_list = get_user_projects_name_by_user_id(user.id)
    access_projects_list = get_access_project_by_id(user.id)
    return render_template('view_projects.html', title=title, projects_list=projects_list, access_projects_list=access_projects_list)


# POST - DODAJE NOWY PROJEKT
@projects_.route('/add_new_project/', methods=["POST"])
def add_new_project():
    if request.method == "POST":
        session = request.cookies.get('session')
        user = get_user_by_nr_session(session)
        new_project_name = request.form.get('new_project_name')

        if not check_exists_project(new_project_name, user.id):
            add_new_project_db(new_project_name, user.id)

        return redirect(f'/project/{new_project_name}/')

    return redirect(url_for('account.account'))


# WYSWIETLA PROJEKT O DANEJ NAZWIE
@projects_.route('/project/<project_name>/')
def view_project(project_name):
    nr_session = get_session_number()
    error = request.args.get('error')

    user = get_user_by_nr_session(nr_session)
    project = get_project_by_name_and_user(project_name, user.id)

    if not project:
        return redirect(url_for('account.account'))

    users = get_users_in_project_by_project_id(project.id)
    host = get_host_project(project.id)
    users.insert(0, [host.name, host.img_path, 'Creator'])

    return render_template('view_project.html', project_name=project.name, users=users, project_id=project.id, error=error)


# DODAJE NOWEGO UZYTKOWNIKA DO PROJEKTU
@projects_.route('/add_new_user/', methods=["POST"])
def add_new_user():
    if request.method == "POST":
        user_name = request.form.get('new-user-name')
        project_id = request.form.get('project_id')
        error = ''
        project_name = get_project_by_id(project_id)

        if not add_new_user_by_project_id_and_user_name(project_id, user_name):
            error = 'User not found or already added'

        return redirect(url_for('projects.view_project', project_name=project_name, error=error))




