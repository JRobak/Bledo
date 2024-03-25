from pytest import fixture
import os


@fixture()
def app(tmpdir):
    test_db_path = os.path.join(str(tmpdir), "test_db.db")
    print(test_db_path)
    os.environ["BLEDO_DATABASE_PATH"] = test_db_path
    from app.database_config import create_tables
    create_tables()
    from app.main import app
    return app.test_client()
