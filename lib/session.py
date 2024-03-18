from flask import request, redirect, url_for

from databases.database_config import check_exists_number_session, check_expiration_date, extend_date_of_session, \
    delete_session


def get_session_number():
    nr_session = request.cookies.get('session')
    if nr_session and check_exists_number_session(nr_session):
        if check_expiration_date(nr_session):
            extend_date_of_session(nr_session)
            return nr_session
        else:
            delete_session(nr_session)
    return None
