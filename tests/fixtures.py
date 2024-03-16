from pytest import fixture


@fixture()
def app():
    from app.main import app
    return app.test_client()