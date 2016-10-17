from typing import Sequence

from people.repositories import PeopleRepository
from people.values import Person


class InMemoryPeopleRepository(PeopleRepository):
    def __init__(self):
        super().__init__()
        self._people = set()

    def create_person(self, name: str) -> Person:
        person = Person(identifier=1, name=name)
        self._people.add(person)

        return person

    def fetch_people(self) -> Sequence[Person]:
        return [p for p in self._people]

    def delete_person(self, identifier) -> Person:
        person = next((p for p in self._people if p.identifier == identifier))
        self._people.clear()

        return person
