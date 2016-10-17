import pytest

from people.repositories import PeopleRepository


# noinspection PyMethodMayBeStatic
class PeopleRepositoryContract(object):
    @pytest.fixture
    def a_people_repository(self, *args):
        raise NotImplementedError('Not Implemented Yet')

    def test_starts_out_empty(self, a_people_repository):
        assert a_people_repository.fetch_people() == []

    def test_can_create_a_fetchable_person(self, a_people_repository):
        identifier = a_people_repository.create_person(name='Adriana')
        person = a_people_repository.fetch_person(identifier=identifier)

        assert person.name == 'Adriana'

    def test_creates_people_with_unique_identifiers(self, a_people_repository):
        identifier_1 = a_people_repository.create_person(name='Adriana')
        identifier_2 = a_people_repository.create_person(name='Mary')

        assert identifier_1 != identifier_2

    def test_can_create_fetchable_people(self, a_people_repository):
        a_people_repository.create_person(name='Adriana')
        people = a_people_repository.fetch_people()

        assert len(people) == 1
        assert people[0].name == 'Adriana'

    def test_can_delete_a_person(self, a_people_repository):
        identifier = a_people_repository.create_person(name='Adriana')
        a_people_repository.delete_person(identifier=identifier)
        with pytest.raises(PeopleRepository.NotFound):
            a_people_repository.fetch_person(identifier=identifier)
