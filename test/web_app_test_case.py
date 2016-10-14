from webtest import TestApp

from demo.application_provider import get_app
from test.database_test_case import DatabaseTestCase


class WebAppTestCase(DatabaseTestCase):
    def setUp(self):
        super().setUp()
        self.web_app = TestApp(get_app())
