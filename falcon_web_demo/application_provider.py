import json

import falcon

from falcon_web_demo.observers import WebPresentPeopleObserver, WebCreatePersonObserver, WebPresentPersonObserver, \
    WebDeletePersonObserver
from people.people_application import PeopleApplication
from .persistence import SessionProvider
from .postgres_people_repository import PostgresPeopleRepository


class PersonListResource(object):
    def __init__(self, people_application: PeopleApplication):
        super().__init__()
        self._people_application = people_application

    def on_get(self, req, resp):
        observer = WebPresentPeopleObserver(response=resp)
        self._people_application.present_people(observer=observer)

    def on_post(self, req, resp):
        post_body = json.loads(req.stream.read().decode('utf-8'))
        name = post_body.get('name')
        observer = WebCreatePersonObserver(request=req, response=resp)
        self._people_application.create_person(name=name, observer=observer)


class PersonResource(object):
    def __init__(self, people_application):
        super().__init__()
        self._people_application = people_application

    def on_get(self, req, resp, identifier):
        observer = WebPresentPersonObserver(response=resp)
        self._people_application.present_person(identifier=int(identifier), observer=observer)

    def on_delete(self, req, resp, identifier):
        observer = WebDeletePersonObserver(response=resp)
        self._people_application.delete_person(identifier=int(identifier), observer=observer)


def get_app():
    session_provider = SessionProvider()
    people_repository = PostgresPeopleRepository(session_provider=session_provider)
    people_application = PeopleApplication(people_repository=people_repository)
    person_list_resource = PersonListResource(people_application=people_application)
    person_resource = PersonResource(people_application=people_application)

    _app = falcon.API()
    _app.add_route('/people', person_list_resource)
    _app.add_route("/people/{identifier}", person_resource)

    return _app
