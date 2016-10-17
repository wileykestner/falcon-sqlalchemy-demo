from people.observers import CreatePersonObserver, PresentPeopleObserver, DeletePersonObserver
from people.repositories import PeopleRepository


class PeopleApplication(object):
    def __init__(self, people_repository: PeopleRepository):
        super().__init__()
        self._people_repository = people_repository

    def present_people(self, observer: PresentPeopleObserver):
        people = self._people_repository.fetch_people()
        observer.did_present_people(people=people)

    def create_person(self, name: str, observer: CreatePersonObserver):
        person = self._people_repository.create_person(name=name)
        observer.did_create_person(person=person)

    def delete_person(self, identfier, observer: DeletePersonObserver):
        deleted_person = self._people_repository.delete_person(identifier=identfier)
        observer.did_delete_person(person=deleted_person)