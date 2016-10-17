from people.people_application import PresentPeopleObserver, DeletePersonObserver
from people.observers import CreatePersonObserver, PresentPeopleObserver, DeletePersonObserver
from people.values import Person


class PresentObserver(PresentPeopleObserver):
    def __init__(self):
        self.people = None

    def did_present_people(self, people):
        self.people = people


class CreateObserver(CreatePersonObserver):
    def __init__(self):
        self.person = None

    def did_create_person(self, person: Person):
        self.person = person


class DeleteObserver(DeletePersonObserver):
    def __init__(self):
        self.deleted_person = None

    def did_delete_person(self, person: Person):
        self.deleted_person = person


