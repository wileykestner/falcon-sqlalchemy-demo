import json

import falcon

from .persistence import session_scope, SessionProvider
from .postgres_people_repository import PostgresPerson


class PersonListResource(object):
    def __init__(self, session_provider):
        super().__init__()
        self.session_provider = session_provider

    def on_get(self, req, resp):
        session = self.session_provider.get_session()
        with session_scope(session):
            resp.data = json.dumps({
                'type': 'person_list',
                'data': [{'id': p.id, 'name': p.name} for p in session.query(PostgresPerson, PostgresPerson.id, PostgresPerson.name).all()],
            }).encode('utf-8')

    def on_post(self, req, resp):
        post_body = json.loads(req.stream.read().decode('utf-8'))
        name = post_body.get('name')

        session = self.session_provider.get_session()
        try:
            person = PostgresPerson(name=name)
            session.add(person)

            session.commit()

            resp.set_header('location', "{}/{}".format(req.uri, person.id))
            resp.status = falcon.HTTP_201
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


class PersonResource(object):
    def __init__(self, session_provider):
        super().__init__()
        self.session_provider = session_provider

    def on_get(self, req, resp, identifier):
        session = self.session_provider.get_session()
        with session_scope(session):
            person = session.query(PostgresPerson).get(int(identifier))
            if person is not None:
                resp.data = json.dumps({
                    'type': 'person',
                    'data': {'id': person.id, 'name': person.name},
                }).encode('utf-8')
            else:
                resp.status = falcon.HTTP_404

    def on_delete(self, req, resp, identifier):
        session = self.session_provider.get_session()
        with session_scope(session):
            person = session.query(PostgresPerson).get(int(identifier))
            session.delete(person)

            resp.status = falcon.HTTP_204


def get_app():
    _session_provider = SessionProvider()
    person_list_resource = PersonListResource(session_provider=_session_provider)
    person_resource = PersonResource(session_provider=_session_provider)

    _app = falcon.API()
    _app.add_route('/people', person_list_resource)
    _app.add_route("/people/{identifier}", person_resource)

    return _app
