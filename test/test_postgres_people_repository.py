import pytest

from falcon_web_demo.persistence import SessionScope
from falcon_web_demo.postgres_people_repository import PostgresPeopleRepository
from test_people.people_repository_contract import PeopleRepositoryContract


class TestPostgresPeopleRepository(PeopleRepositoryContract):
    @pytest.fixture
    def a_people_repository(self, db):
        session_scope = SessionScope()
        return PostgresPeopleRepository(session_scope=session_scope)
