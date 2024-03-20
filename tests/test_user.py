from .fixtures import *


def test_user_login(app):
    response = app.get("/login/")
    assert response.status_code == 200
    # działa o ile nie bedzie before i after request

    # response = app.post("/login/", data={'username': "John"})
    # assert response.status_code == 302

    """ 
    testy 
    - logowania
    - static folder 
    """
