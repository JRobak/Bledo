from .fixtures import *


def test_user_login(app):
    response = app.post("/login/", data={'username': "John"})
    assert response.status_code == 302
    assert response.location == '/account/'

    """ 
    testy 
    - logowania
    - static folder 
    """
