from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from lib.__init__ import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    img_path = db.Column(db.String, default="default.png")
    position = db.Column(db.String, default='Brak stanowiska')
    description = db.Column(db.String, default='Brak Opisu')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.id} {self.name} {self.img_path} {self.position}"


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id_creator = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, user_id_creator):
        self.name = name
        self.user_id_creator = user_id_creator

    def __repr__(self):
        return f"{self.id} {self.name} {self.user_id_creator}"


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    session_number = db.Column(db.String(255), unique=True, nullable=False)
    date_of_creation = db.Column(db.String(8), nullable=False, default=datetime.utcnow().strftime('%d-%m-%Y'))
    expiration_date = db.Column(db.String(8), nullable=False)

    def __init__(self, user_id, session_number, date_of_creation, expiration_date):
        self.user_id = user_id
        self.session_number = session_number
        self.date_of_creation = date_of_creation
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"{self.id} {self.user_id} {self.session_number} {self.date_of_creation} {self.expiration_date}"


class Access_project(db.Model):
    __tablename__ = 'access_projects'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    description = db.Column(db.String, nullable=True)

    def __init__(self, user_id, project_id, description):
        self.user_id = user_id
        self.project_id = project_id
        self.description = description

    def __repr__(self):
        return f"{self.id} {self.user_id} {self.project_id} {self.description}"


def create_all():
    db.Model.metadata.create_all(bind=db.engine, checkfirst=True)
