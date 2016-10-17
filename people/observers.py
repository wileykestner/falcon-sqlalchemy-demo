from abc import ABCMeta, abstractmethod
from typing import Sequence

from people.values import Person


class CreatePersonObserver(metaclass=ABCMeta):
    @abstractmethod
    def did_create_person(self, person: Person):
        pass


class PresentPeopleObserver(metaclass=ABCMeta):
    @abstractmethod
    def did_present_people(self, people: Sequence[Person]):
        pass


class DeletePersonObserver(metaclass=ABCMeta):
    @abstractmethod
    def did_delete_person(self, person: Person):
        pass