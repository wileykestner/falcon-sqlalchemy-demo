from typing import Sequence

from people.repositories import PeopleRepository
from people.values import Person


class InMemoryPeopleRepository(PeopleRepository):
    def __init__(self):
        super().__init__()
        self._people = set()
        self._next_identifier = 1

    def create_person(self, name: str) -> Person:
        next_identifier = self._next_identifier
        person = Person(identifier=next_identifier, name=name)
        self._next_identifier += 1
        self._people.add(person)

        return next_identifier

    def fetch_person(self, identifier) -> Person:
        try:
            return next((p for p in self._people if p.identifier == identifier))
        except StopIteration:
            raise PeopleRepository.NotFound()

    def fetch_people(self) -> Sequence[Person]:
        return [p for p in self._people]

    def delete_person(self, identifier) -> Person:
        person = next((p for p in self._people if p.identifier == identifier))
        self._people.clear()

        return person
