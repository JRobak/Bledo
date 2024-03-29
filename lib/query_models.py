from datetime import datetime, timedelta
from flask import g
from .models import User, Project, Session


# users
def check_exists_user(name):
    return User.query.filter_by(name=name).first()


def add_new_user(name):
    user = User(name)
    g.session.add(user)
    g.session.commit()
    return user


def get_user_by_name(name):
    return User.query.filter_by(name=name).first()


# projects
def add_new_project(name, user_id):
    project = Project(name, user_id)
    g.session.add(project)
    g.session.commit()


def check_exists_project(name, user_id):
    return Project.query.filter_by(name=name, user_id=user_id).first()


def get_project_id(name, user_id):
    pass


def get_user_tables_by_user_id(user_id):
    pass


def get_users_in_project_by_project_id(project_id):
    pass


def get_user_host_project_by_project_id(project_id):
    pass


# image
def change_image_user(user_id, path_to_image):
    user = User.query.filter_by(user_id=user_id).first()
    user.image_path = path_to_image
    g.session.commit()


def get_image_path_by_user_name(user_name):
    pass


# sessions
def check_exists_number_session(nr):
    return Session.query.filter_by(session_number=nr).first()


def get_session_number_by_user_id(user_id):
    pass


def get_user_id_by_nr_session(nr_session):
    pass


def create_new_session(user_id):
    from app.sessions import create_session_number, LENGTH
    new_session_number = create_session_number(LENGTH)
    while check_exists_number_session(new_session_number):
        new_session_number = create_session_number(LENGTH)

    date_of_creation = datetime.now().strftime("%d-%m-%Y")
    expiration_date = (datetime.now() + timedelta(days=4)).strftime("%d-%m-%Y")

    new_session = Session(user_id, new_session_number, date_of_creation, expiration_date)
    g.session.add(new_session)
    g.session.commit()

    return new_session_number


def check_expiration_date(nr):
    session = Session.query.filter_by(session_number=nr).first()
    expiration_date = datetime.strptime(session.expiration_date, "%d-%m-%Y")
    current_datetime = datetime.now()
    return (expiration_date - current_datetime).days >= 0


def extend_date_of_session(nr):
    expiration_date = (datetime.now() + timedelta(days=4)).strftime("%d-%m-%Y")
    session = Session.query.filter_by(session_number=nr).first()
    session.expiration_date = expiration_date
    g.session.commit()


def delete_session(nr):
    session = Session.query.filter_by(session_number=nr).first()
    g.session.delete(session)
