from typing import Any

from people.observers import CreatePersonObserver, PresentPeopleObserver, DeletePersonObserver, PresentPersonObserver
from people.repositories import PeopleRepository


class PeopleApplication(object):
    def __init__(self, people_repository: PeopleRepository):
        super().__init__()
        self._people_repository = people_repository

    def present_people(self, observer: PresentPeopleObserver):
        people = self._people_repository.fetch_people()
        observer.did_present_people(people=people)

    def create_person(self, name: str, observer: CreatePersonObserver):
        identifier = self._people_repository.create_person(name=name)
        observer.did_create_person(identifier=identifier)

    def delete_person(self, identifier: int, observer: DeletePersonObserver):
        try:
            deleted_person = self._people_repository.delete_person(identifier=identifier)
            observer.did_delete_person(person=deleted_person)
        except PeopleRepository.NotFound:
            invalid_identifier = DeletePersonObserver.InvalidIdentifier()
            observer.did_fail_to_delete_person(identifier=identifier, error=invalid_identifier)

    def present_person(self, identifier: Any, observer: PresentPersonObserver):
        try:
            person = self._people_repository.fetch_person(identifier=identifier)
            observer.did_present_person(person=person)
        except PeopleRepository.NotFound:
            error = PresentPersonObserver.InvalidIdentifier()
            observer.did_fail_to_present_person(identifier=identifier, error=error)
