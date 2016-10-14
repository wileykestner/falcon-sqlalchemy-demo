import json
import os

TEST_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_DATABASE_NAME = "test.db"
MIGRATIONS_DIRECTORY_PATH = os.path.join(TEST_FILE_PATH, "..")
TEST_DATABASE_URL = "sqlite:///{}".format(TEST_DATABASE_NAME)


def set_up_test_database():
    try:
        os.remove(TEST_DATABASE_NAME)
    except FileNotFoundError:
        pass
    os.chdir(MIGRATIONS_DIRECTORY_PATH)
    os.environ["DATABASE_URL"] = TEST_DATABASE_URL

    import alembic.config
    alembic_args = [
        '-xloggingPreference=CRITICAL',
        '--raiseerr',
        'upgrade',
        'head'
    ]

    alembic.config.main(argv=alembic_args)


def tear_down_test_database():
    del os.environ["DATABASE_URL"]
    try:
        os.remove(TEST_DATABASE_NAME)
    except FileNotFoundError:
        pass


def get_json_from_response(response):
    response_string = response.body.decode('utf-8')

    return json.loads(response_string)


def get_header_value(header_key, response_headers):
    try:
        return next(h[1] for h in response_headers.items() if h[0] == header_key)
    except StopIteration:
        return None
