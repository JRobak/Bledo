from .fixtures import *


def test_user_login(app):
    response = app.get("/login/")
    assert response.status_code == 200
    assert response.data.decode("utf-8").find("login_box") > 0
    assert response.data.decode("utf-8").find('id="error"') <= 0

    response = app.post("/login/", data={'username': "Tester"})
    assert response.status_code == 302
    assert response.location == "/account/"

    response = app.get("/logout/")
    assert response.status_code == 302
    assert response.location == "/login/"

    response = app.post("/login/", data={'username': " "})
    assert response.status_code == 200
    assert response.data.decode("utf-8").find("error") > 0

    # cookies = [response.headers.get('Set-Cookie').split(';')]


def test_access_for_user_not_logged_in(app):
    response = app.get("/projects/")
    assert response.location == "/login/"

    response = app.get("/project/e/")
    assert response.location == "/login/"


def test_user_project(app):
    app.post("/login/", data={'username': "Tester"})
    response = app.get("/projects/")
    assert response.status_code == 200
    assert response.data.decode("utf-8").find('<input type="text" name="new_project_name" placeholder="Wpisz nazwę projektu">') > 0

    app.post("/add_new_project/", data={'new_project_name': 'projekt'})
    response = app.get("/project/projekt/")
    assert response.data.decode("utf-8").find('<h2>projekt</h2>') > 0


def test_static_folder(app):
    # response = app.post('/change_image/', data={'image_file': 'test_image.png'})
    # print(response.status_code)
    response = app.get("/static/image/RnaZtle.png")
    assert response.status_code == 200

    response = app.get("/static/image/1njkzvi.gif")
    assert response.status_code == 404
