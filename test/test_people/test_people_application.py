from people.people_application import PeopleApplication
from test.test_people.test_observers import PresentObserver, CreateObserver, DeleteObserver
from test.test_people.test_repositories import InMemoryPeopleRepository


# noinspection PyPep8Naming,PyUnusedLocal,PyShadowingNames
class Test_People_Application(object):
    def test_present_people(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)

        present_observer = PresentObserver()
        people_application.present_people(observer=present_observer)

        assert present_observer.people == []

    def test_create_person(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)

        create_observer = CreateObserver()
        people_application.create_person(name='Mary', observer=create_observer)

        present_observer = PresentObserver()
        people_application.present_people(observer=present_observer)

        assert len(present_observer.people) == 1
        assert present_observer.people[0].name == 'Mary'

    def test_delete_person(self):
        people_repository = InMemoryPeopleRepository()
        people_application = PeopleApplication(people_repository=people_repository)

        create_observer = CreateObserver()
        people_application.create_person(name='Mary', observer=create_observer)

        delete_observer = DeleteObserver()
        people_application.delete_person(identfier=create_observer.person.identifier,
                                         observer=delete_observer)

        assert delete_observer.deleted_person.name == 'Mary'

        present_observer = PresentObserver()
        people_application.present_people(observer=present_observer)

        assert present_observer.people == []
