from abc import ABCMeta, abstractmethod
from typing import Sequence

from people.values import Person


class CreatePersonObserver(metaclass=ABCMeta):
    @abstractmethod
    def did_create_person(self, identifier: int):
        pass


class PresentPersonObserver(metaclass=ABCMeta):
    class InvalidIdentifier(Exception):
        pass

    @abstractmethod
    def did_present_person(self, person: Person):
        pass

    @abstractmethod
    def did_fail_to_present_person(self, identifier: int, error: Exception):
        pass


class PresentPeopleObserver(metaclass=ABCMeta):
    @abstractmethod
    def did_present_people(self, people: Sequence[Person]):
        pass


class DeletePersonObserver(metaclass=ABCMeta):
    class InvalidIdentifier(Exception):
        pass

    @abstractmethod
    def did_delete_person(self, person: Person):
        pass

    @abstractmethod
    def did_fail_to_delete_person(self, identifier: int, error: Exception):
        pass
