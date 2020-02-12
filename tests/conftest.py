import pytest
from app import create_app, db
from config import TestingConfig


@pytest.fixture(scope="session")
def app():
    flask_app = create_app(TestingConfig)

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield flask_app

    ctx.pop()


@pytest.fixture(scope="session")
def client(app):
    testing_client = app.test_client()
    yield testing_client


@pytest.fixture(scope="session")
def create_db(app):
    db.create_all()
    yield db
    db.drop_all()
