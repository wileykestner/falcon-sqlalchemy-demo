import pytest

from falcon_web_demo.persistence import SessionProvider
from falcon_web_demo.postgres_people_repository import PostgresPeopleRepository
from test.test_people.people_repository_contract import PeopleRepositoryContract


class TestPostgresPeopleRepository(PeopleRepositoryContract):
    @pytest.fixture
    def a_people_repository(self, db):
        _session_provider = SessionProvider()
        return PostgresPeopleRepository(session_provider=_session_provider)
