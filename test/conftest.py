import pytest
from webtest import TestApp

from demo.application_provider import get_app
from test.helpers import set_up_test_database, tear_down_test_database


@pytest.fixture
def db():
    set_up_test_database()
    yield
    tear_down_test_database()


@pytest.fixture
def application():
    app = get_app()
    return TestApp(app)


# noinspection PyShadowingNames,PyUnusedLocal
@pytest.fixture
def get_people(db, application):
    return lambda: application.get('/people')


# noinspection PyShadowingNames,PyUnusedLocal
@pytest.fixture
def create_person(db, application):
    return lambda name: application.post_json('/people', {'name': name})
