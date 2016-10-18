import pytest
from webtest import TestApp

from falcon_web_demo.application_routes import get_app
from test.utils.helpers import set_up_test_database, tear_down_test_database


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


# noinspection PyShadowingNames,PyUnusedLocal
@pytest.fixture
def get_person(db, application):
    def _get_person(identifier, status=None):
        kwargs = {}
        if status is not None:
            kwargs['status'] = status
        return application.get('/people/{}'.format(identifier), **kwargs)

    return _get_person


# noinspection PyShadowingNames,PyUnusedLocal
@pytest.fixture
def delete_person(db, application):
    def _delete(identifier, status=None):
        kwargs = {}
        if status is not None:
            kwargs['status'] = status
        return application.delete('/people/{}'.format(identifier), **kwargs)

    return _delete
