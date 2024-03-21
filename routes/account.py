from flask import render_template, Blueprint, request, redirect, url_for
import os
from app.database_access import change_image_user, get_user_id_by_nr_session
from lib.session import get_session_number

account_ = Blueprint('account', __name__)


@account_.route('/account/')
def account():
    title = 'Ustawienia konta'
    error = request.args.get('error')

    nr_session = get_session_number()

    return render_template('account.html', title=title, error=error)


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
        user_id = get_user_id_by_nr_session(session)
        change_image_user(user_id, new_filename)
        return redirect(url_for('account.account'))

    return redirect(url_for('account.account', error="Cos poszlo nie tak"))


