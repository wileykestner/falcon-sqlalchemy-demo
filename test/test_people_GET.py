from test.utils.assertions import assert_header_value, assert_json_response

from test.utils.helpers import get_json_from_response, get_identifier_for_created_person


# noinspection PyPep8Naming,PyShadowingNames
class Test_When_No_People_Exist(object):
    def test_status_code(self, get_people):
        assert get_people().status_code == 200

    def test_header_content_type(self, get_people):
        assert_header_value('content-type',
                            'application/json',
                            get_people().headers)

    def test_body(self, get_people):
        assert_json_response({'data': [], 'type': 'person_list'}, get_people())


# noinspection PyPep8Naming,PyShadowingNames,PyUnusedLocal
class Test_When_One_Person_Exists(object):
    def test_body_should_contain_one_person(self, create_person, get_people):
        response = create_person('Frank Stella')
        person_id = get_identifier_for_created_person(response)
        people = get_json_from_response(get_people())

        assert people == {'data': [{'name': 'Frank Stella', 'id': person_id}], 'type': 'person_list'}
