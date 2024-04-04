from pytest import fixture
import os


@fixture()
def app(tmpdir):
    test_db_path = os.path.join(str(tmpdir))
    os.environ["BLEDO_DATABASE_PATH"] = test_db_path

    from app.wsgi import app
    client = app.test_client()

    from lib.models import create_all
    create_all()
    return client
