import json

import pytest

from test.helpers import get_header_value, get_json_from_response


def assert_header_value(header_key, expected_value, response_headers):
    header_value = get_header_value(header_key, response_headers)
    if header_value is not None:
        assert header_value == expected_value
    else:
        pytest.fail("The response headers do not contain the key: '{}'".format(header_key))


def assert_json_response(expected_json_body, response):
    assert get_json_from_response(response) == expected_json_body
