from test.utils.helpers import get_json_from_response, get_identifier_for_created_person


# noinspection PyPep8Naming,PyShadowingNames
class Test_When_No_People_Exist(object):
    def test_status_code(self, get_person):
        assert get_person(identifier=1234, status=404).status_code == 404


# noinspection PyPep8Naming,PyShadowingNames,PyUnusedLocal
class Test_When_One_Person_Exists(object):
    def test_body_should_contain_one_person(self, create_person, get_person):
        response = create_person("Frank Stella")
        person_id = get_identifier_for_created_person(response)
        person = get_json_from_response(get_person(identifier=person_id))

        assert person == {
            "data": {"name": "Frank Stella", "id": person_id},
            "type": "person",
        }
