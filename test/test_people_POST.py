from test.utils.assertions import assert_header_value

from test.utils.helpers import get_header_value


# noinspection PyPep8Naming
class Test_When_No_People_Exist(object):
    def test_status_code(self, create_person):
        response = create_person("Batman")

        assert response.status_code == 201

    def test_json_response_in_utf_8(self, create_person):
        response = create_person("Robin")
        assert_header_value("content-type", "application/json", response.headers)

    def test_should_put_the_url_of_the_newly_created_resource_in_the_location_header(
        self, create_person, application
    ):
        response = create_person("Batgirl")
        location = get_header_value("location", response.headers)
        response = application.get(location)

        assert response.status_code == 200
