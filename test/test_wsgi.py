from falcon import App

from falcon_web_demo.wsgi import app


def test_wsgi():
    assert isinstance(app, App)
