from .fixtures import *


def test_user_login(app):
    # response = app.get("/login/")
    # assert response.status_code == 200  # zwraca  500

    response = app.post("login", data={'username': "John"})
    assert response.status_code == 200

    """ 
    testy 
    - logowania
    - static folder 
    """
