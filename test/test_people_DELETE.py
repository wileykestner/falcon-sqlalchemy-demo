from test.utils.helpers import get_header_value, get_identifier_for_created_person


# noinspection PyPep8Naming
class Test_Deleting_People(object):
    def test_status_code(self, create_person, delete_person):
        create_response = create_person("Batman")
        person_id = get_identifier_for_created_person(create_response)
        delete_response = delete_person(person_id)

        assert delete_response.status_code == 204

    def test_getting_after_deleting(self, create_person, application, delete_person):
        create_response = create_person("Batgirl")
        location = get_header_value('location', create_response.headers)
        person_id = get_identifier_for_created_person(create_response)
        delete_person(person_id)

        response = application.get(location, status=404)

        assert response.status_code == 404
