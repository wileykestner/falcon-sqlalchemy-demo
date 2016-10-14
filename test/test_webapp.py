import json

from test.web_app_test_case import WebAppTestCase


# noinspection PyPep8Naming
class When_No_People_Have_Been_Created(WebAppTestCase):
    def test_people_should_return_empty_people_list(self):
        response = self.web_app.get('/people')
        response_string = response.body.decode('utf-8')
        response_json = json.loads(response_string)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json, {'data': [], 'type': 'people'})


# noinspection PyPep8Naming
class When_One_Person_Has_Been_Created(WebAppTestCase):
    def setUp(self):
        super().setUp()
        self.web_app.post_json('/people', {'name': 'Lionel Messi'})

    def test_should_return_one_element_people_list(self):
        response = self.web_app.get('/people')
        response_string = response.body.decode('utf-8')
        response_json = json.loads(response_string)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json, {'data': [{'id': 1, 'name': 'Lionel Messi'}], 'type': 'people'})
