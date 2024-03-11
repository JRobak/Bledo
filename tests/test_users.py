
def test_user_login(app):
    response = app.get("/login/")

    data = response.data

    assert data.decode("utf-8").find("login_box") >= 0

    response = app.post("/login/")
