from flask import render_template, Blueprint, request, redirect, url_for, make_response
import os
from databases.database_config import change_image_user, check_expiration_date, check_exists_number_session, delete_session, return_user, extend_date_of_session

account_ = Blueprint('account', __name__)


@account_.route('/account/')
def account():
    title = 'Ustawienia konta'
    error = request.args.get('error')

    nr_session = request.cookies.get('session')
    if nr_session and check_exists_number_session(nr_session):
        if check_expiration_date(nr_session):
            extend_date_of_session(nr_session)
            return render_template('account.html', title=title, error=error)
        else:
            delete_session(nr_session)

    response = make_response(redirect(url_for('login.login')))
    response.delete_cookie('session')
    return response


@account_.route('/change_image/', methods=["POST"])
def change_image():

    if request.method == "POST":
        if 'image_file' not in request.files:
            return redirect(url_for('account.account', error="Nie wstawiono pliku 2"))

        image = request.files['image_file']

        if not image:
            return redirect(url_for('account.account', error="Nie wstawiono pliku"))

        allowed_extensions = {'png', 'jpg', 'gif'}
        if not image.filename[-3:].lower() in allowed_extensions:
            return redirect(url_for('account.account', error="Nieprawidlowy format. Dozwolone: PNG, JPG, GIF"))

        # sprawdzanie czy plik o takiej nazwie istnieje, jeśli tak to zmienia nazwę
        file_path = os.path.join('../static/image/', image.filename)
        new_filename = image.filename
        i = 0
        while os.path.exists(file_path):
            i += 1
            filename, extension = os.path.splitext(image.filename)
            new_filename = f"{filename}_{i}{extension}"
            file_path = os.path.join('../static/image/', new_filename)

        try:
            image.save(file_path)
        except Exception as e:
            return redirect(url_for('account.account', error="Blad przy zapisie pliku, sprobuj ponownie"))

        session = request.cookies.get('session')
        user_id = return_user(session)
        change_image_user(user_id, new_filename)
        return redirect(url_for('account.account'))

    return redirect(url_for('account.account', error="Cos poszlo nie tak"))




