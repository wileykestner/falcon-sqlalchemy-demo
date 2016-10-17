import pytest

from test.test_people.people_repository_contract import PeopleRepositoryContract
from test.test_people.reference_repositories import InMemoryPeopleRepository


class TestInMemoryPeopleRepository(PeopleRepositoryContract):
    @pytest.fixture
    def a_people_repository(self):
        return InMemoryPeopleRepository()
