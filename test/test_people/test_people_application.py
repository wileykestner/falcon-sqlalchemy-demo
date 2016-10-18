from people.observers import DeletePersonObserver
from people.people_application import PeopleApplication
from test.test_people.reference_repositories import InMemoryPeopleRepository
from test.test_people.test_observers import PresentManyPeopleObserver, CreateObserver, DeleteObserver, \
    PresentOnePersonObserver


# noinspection PyPep8Naming,PyUnusedLocal,PyShadowingNames
class Test_People_Application(object):
    def test_present_people(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)

        present_observer = PresentManyPeopleObserver()
        people_application.present_people(observer=present_observer)

        assert present_observer.people == []

    def test_present_person(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)

        create_observer = CreateObserver()
        people_application.create_person(name='Aaron', observer=create_observer)

        identifier = create_observer.identifier

        present_observer = PresentOnePersonObserver()
        people_application.present_person(identifier=identifier, observer=present_observer)

        assert present_observer.person.identifier == identifier
        assert present_observer.person.name == 'Aaron'

    def test_create_person(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)

        create_observer = CreateObserver()
        people_application.create_person(name='Mary', observer=create_observer)

        present_observer = PresentManyPeopleObserver()
        people_application.present_people(observer=present_observer)

        assert len(present_observer.people) == 1
        assert present_observer.people[0].name == 'Mary'

    def test_delete_person(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)

        create_observer = CreateObserver()
        people_application.create_person(name='Mary', observer=create_observer)

        delete_observer = DeleteObserver()
        people_application.delete_person(identifier=create_observer.identifier,
                                         observer=delete_observer)

        assert delete_observer.deleted_person.name == 'Mary'

        present_observer = PresentManyPeopleObserver()
        people_application.present_people(observer=present_observer)

        assert present_observer.people == []

    def test_delete_person_with_invalid_identifier(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)
        delete_observer = DeleteObserver()
        people_application.delete_person(identifier=1234,
                                         observer=delete_observer)

        assert type(delete_observer.error) == DeletePersonObserver.InvalidIdentifier
        assert delete_observer.identifier == 1234
