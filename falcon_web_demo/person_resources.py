import json
from typing import Sequence

import falcon

from people.people_application import PeopleApplication, CreatePersonObserver, PresentPeopleObserver, \
    PresentPersonObserver, DeletePersonObserver
from people.values import Person


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


class WebCreatePersonObserver(CreatePersonObserver):
    def __init__(self, request, response):
        super().__init__()
        self.request = request
        self.response = response

    def did_create_person(self, identifier: int):
        self.response.set_header('location', "{}/{}".format(self.request.uri, identifier))
        self.response.status = falcon.HTTP_201


class WebPresentPeopleObserver(PresentPeopleObserver):
    def __init__(self, response):
        super().__init__()
        self.response = response

    def did_present_people(self, people: Sequence[Person]):
        self.response.data = json.dumps({
            'type': 'person_list',
            'data': [{'id': p.identifier, 'name': p.name} for p in people],
        }).encode('utf-8')


class WebPresentPersonObserver(PresentPersonObserver):
    def __init__(self, response):
        super().__init__()
        self.response = response

    def did_present_person(self, person: Person):
        self.response.data = json.dumps({
            'type': 'person',
            'data': {'id': person.identifier, 'name': person.name},
        }).encode('utf-8')

    def did_fail_to_present_person(self, identifier: int, error: Exception):
        self.response.status = falcon.HTTP_404


class WebDeletePersonObserver(DeletePersonObserver):
    def __init__(self, response):
        super().__init__()
        self.response = response

    def did_delete_person(self, person: Person):
        self.response.status = falcon.HTTP_204

    def did_fail_to_delete_person(self, identifier: int, error: Exception):
        self.response.status = falcon.HTTP_404
