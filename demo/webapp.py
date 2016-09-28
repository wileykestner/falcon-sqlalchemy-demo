import json

import falcon

from .persistence import session_scope
from .person import Person


class PeopleResource(object):
    @staticmethod
    def on_get(req, resp):
        with session_scope() as session:
            resp.data = json.dumps({
                "type": "people",
                "data": [{"id": p.id, "name": p.name} for p in session.query(Person, Person.id, Person.name).all()],
            }).encode("utf-8")

    @staticmethod
    def on_post(req, resp):
        post_body = json.loads(req.stream.read().decode("utf-8"))
        name = post_body.get("name")
        with session_scope() as session:
            person = Person(name=name)
            session.add(person)

        resp.status = falcon.HTTP_201


class PersonResource(object):
    @staticmethod
    def on_get(req, resp, identifier):
        with session_scope() as session:
            person = session.query(Person).get(int(identifier))

            resp.data = json.dumps({
                "type": "person",
                "data": {"id": person.id, "name": person.name},
            }).encode("utf-8")

    @staticmethod
    def on_delete(req, resp, identifier):
        with session_scope() as session:
            person = session.query(Person).get(int(identifier))
            session.delete(person)

        resp.status = falcon.HTTP_204


people_resource = PeopleResource()

app = falcon.API()
app.add_route("/people", people_resource)
app.add_route('/people/{identifier}', PersonResource())
