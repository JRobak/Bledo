from flask import Blueprint, request, render_template, redirect, url_for
from lib.query_models import  add_new_project as add_new_project_db, check_exists_project, \
    get_user_id_by_nr_session, get_users_in_project_by_project_id, get_user_host_project_by_project_id, \
    get_image_path_by_user_name
from lib.query_models import get_user_by_nr_session, get_user_projects_name_by_user_id, get_project_by_name_and_user
from lib.session import get_session_number

projects_ = Blueprint('projects', __name__)


# WYSWIETLA WSZYSTKIE PROJEKTY
@projects_.route('/projects/')
def view_projects():
    title = "Projekty"

    nr_session = get_session_number()

    user = get_user_by_nr_session(nr_session)
    projects_list = get_user_projects_name_by_user_id(user.id)
    return render_template('view_projects.html', title=title, projects_list=projects_list)


# POST - DODAJE NOWY PROJEKT
@projects_.route('/add_new_project/', methods=["POST"])
def add_new_project():
    if request.method == "POST":
        session = request.cookies.get('session')
        user_id = get_user_id_by_nr_session(session)
        new_project_name = request.form.get('new_project_name')

        if not check_exists_project(new_project_name, user_id):
            add_new_project_db(new_project_name, user_id)

        return redirect(f'/project/{new_project_name}/')

    return redirect(url_for('account.account'))


# WYSWIETLA PROJEKT O DANEJ NAZWIE
@projects_.route('/project/<project_name>/')
def view_project(project_name):
    nr_session = get_session_number()

    user = get_user_by_nr_session(nr_session)
    project = get_project_by_name_and_user(project_name, user.id)

    if not project:
        return redirect(url_for('account.account'))

    users = get_users_in_project_by_project_id(project.id)

        # host_id = get_user_host_project_by_project_id(project_id)
        # users_id = get_users_in_project_by_project_id(project_id)
        #
        # host = get_user_name_by_id(host_id)
        # users = [get_user_name_by_id(str(x)[1:-2]) for x in users_id]
        # users_and_images = {}
        # users_and_images[host] = get_image_path_by_user_name(host)
        # for user in users:
        #     if user not in users_and_images:
        #         users_and_images[user] = get_image_path_by_user_name(user)

        # return render_template('view_project.html', project_name=project_name, users_and_images=users_and_images)



# DODAJE NOWEGO UZYTKOWNIKA DO PROJEKTU
@projects_.route('/add_new_user/', methods=["POST"])
def add_new_user():
    if request.method == "POST":
        user = request.form.get('new-user-name')
