from abc import ABCMeta, abstractmethod
from typing import Sequence

from people.values import Person


class PeopleRepository(metaclass=ABCMeta):
    class NotFound(Exception):
        pass

    @abstractmethod
    def create_person(self, name: str) -> int:
        pass

    @abstractmethod
    def fetch_person(self, identifier: int) -> Person:
        pass

    @abstractmethod
    def fetch_people(self) -> Sequence[Person]:
        pass

    @abstractmethod
    def delete_person(self, identifier: int) -> Person:
        pass
