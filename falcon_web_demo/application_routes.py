import falcon
from falcon import API

from falcon_web_demo.person_resources import PersonListResource, PersonResource
from people.people_application import PeopleApplication
from .persistence import SessionScope
from .postgres_people_repository import PostgresPeopleRepository


def get_app() -> API:
    session_scope = SessionScope()
    people_repository = PostgresPeopleRepository(session_scope=session_scope)
    people_application = PeopleApplication(people_repository=people_repository)
    person_list_resource = PersonListResource(
        people_application=people_application)
    person_resource = PersonResource(people_application=people_application)

    _app = falcon.App()
    _app.add_route('/people', person_list_resource)
    _app.add_route('/people/{identifier}', person_resource)

    return _app
