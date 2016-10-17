from typing import Any

from people.observers import CreatePersonObserver, PresentPeopleObserver, DeletePersonObserver, PresentPersonObserver
from people.values import Person


class PresentOnePersonObserver(PresentPersonObserver):
    def __init__(self):
        self.person = None

    def did_present_person(self, person):
        self.person = person


class PresentManyPeopleObserver(PresentPeopleObserver):
    def __init__(self):
        self.people = None

    def did_present_people(self, people):
        self.people = people


class CreateObserver(CreatePersonObserver):
    def __init__(self):
        self.identifier = None

    def did_create_person(self, identifier: Any):
        self.identifier = identifier


class DeleteObserver(DeletePersonObserver):
    def __init__(self):
        self.deleted_person = None

    def did_delete_person(self, person: Person):
        self.deleted_person = person
