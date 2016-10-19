from falcon import API

from falcon_web_demo.wsgi import app


def test_wsgi():
    assert isinstance(app, API)
