from flask import render_template, Blueprint, request, redirect, url_for, jsonify
import os
from lib.query_models import change_image_user, get_user_by_nr_session, change_position_user_by_nr_session, \
    change_description_user_by_nr_session, get_user_data_in_json_by_name
from lib.session import get_session_number

account_ = Blueprint('account', __name__)


@account_.route('/account/')
def account():
    title = 'Ustawienia konta'
    error = request.args.get('error')

    nr_session = get_session_number()
    user = get_user_by_nr_session(nr_session)

    return render_template('account.html', title=title, error=error, user=user)


@account_.route('/get_user_info/<user_name>/')
def get_user_info(user_name):
    nr_session = get_session_number()

    user_info_in_json = get_user_data_in_json_by_name(user_name)
    print(user_info_in_json)
    return jsonify(user_info_in_json)


@account_.route('/change_image/', methods=["POST"])
def change_image():

    nr_session = get_session_number()

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

        user = get_user_by_nr_session(nr_session)
        change_image_user(user.id, new_filename)
        return redirect(url_for('account.account'))

    return redirect(url_for('account.account', error="Cos poszlo nie tak"))


@account_.route('/change_job_position/', methods=["POST"])
def change_job_position():
    nr_session = get_session_number()

    if request.method == "POST":
        position_text = request.form.get('position_text')
        change_position_user_by_nr_session(nr_session, position_text)

        return redirect(url_for('account.account'))


@account_.route('/change_description_user/', methods=["POST"])
def change_description_user():
    nr_session = get_session_number()

    if request.method == "POST":
        description_text = request.form.get('description_text')
        change_description_user_by_nr_session(nr_session, description_text)

        return redirect(url_for('account.account'))

