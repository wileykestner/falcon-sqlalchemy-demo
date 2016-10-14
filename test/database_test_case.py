import os
import unittest

TEST_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_DATABASE_NAME = "test.db"
MIGRATIONS_DIRECTORY_PATH = os.path.join(TEST_FILE_PATH, "..")
TEST_DATABASE_URL = "sqlite:///{}".format(TEST_DATABASE_NAME)


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self._clear_database()
        os.chdir(MIGRATIONS_DIRECTORY_PATH)
        os.environ["DATABASE_URL"] = TEST_DATABASE_URL
        import alembic.config
        alembicArgs = [
            '--raiseerr',
            'upgrade',
            'head',
        ]
        alembic.config.main(argv=alembicArgs)

    def tearDown(self):
        super().tearDown()
        del os.environ["DATABASE_URL"]
        self._clear_database()

    @staticmethod
    def _clear_database():
        try:
            os.remove(TEST_DATABASE_NAME)
        except FileNotFoundError:
            pass
