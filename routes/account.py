from flask import render_template, Blueprint, request, redirect, url_for
import os
from databases.database_config import change_image_user

account_ = Blueprint('account', __name__)


@account_.route('/account/')
def account():
    title = 'Ustawienia konta'
    error = request.args.get('error')

    user_id = request.cookies.get('user_id')
    if user_id:
        return render_template('account.html', title=title, error=error)

    return redirect(url_for('login.login'))


@account_.route('/change_image/', methods=["POST"])
def change_image():
    title = 'Ustawienia konta'

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

        change_image_user(request.cookies.get('user_id'), new_filename)
        return redirect(url_for('account.account'))

    return redirect(url_for('account.account', error="Cos poszlo nie tak"))




