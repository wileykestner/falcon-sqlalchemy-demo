from typing import Sequence

from people.repositories import PeopleRepository
from people.values import Person
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PostgresPerson(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class PostgresPeopleRepository(PeopleRepository):
    def __init__(self, session_scope):
        super().__init__()
        self.session_scope = session_scope

    def delete_person(self, identifier: int) -> Person:
        with self.session_scope() as session:
            identifier = int(identifier)
            postgres_person = session.get(PostgresPerson, identifier)
            if postgres_person is None:
                raise PeopleRepository.NotFound()
            session.delete(postgres_person)
            identifier = postgres_person.id
            name = postgres_person.name
            return Person(identifier=identifier, name=name)

    def fetch_person(self, identifier: int) -> Person:
        with self.session_scope() as session:
            identifier = int(identifier)
            postgres_person = session.get(PostgresPerson, identifier)
            if postgres_person is None:
                raise PeopleRepository.NotFound()
            identifier = postgres_person.id
            name = postgres_person.name
            return Person(identifier=identifier, name=name)

    def create_person(self, name: str) -> int:
        with self.session_scope(commit_on_exit=False) as session:
            postgres_person = PostgresPerson(name=name)
            session.add(postgres_person)
            session.commit()
            return postgres_person.id

    def fetch_people(self) -> Sequence[Person]:
        with self.session_scope() as session:
            return [Person(identifier=p.id, name=p.name)
                    for p in session.query(PostgresPerson,
                                           PostgresPerson.id,
                                           PostgresPerson.name).all()]
