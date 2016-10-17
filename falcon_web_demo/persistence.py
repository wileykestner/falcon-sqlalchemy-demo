import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


def get_url():
    database_url = os.getenv("DATABASE_URL", "sqlite:///development.db")
    if database_url is None:
        raise ValueError("Could not find DATABASE_URL in the local environment.")

    return database_url


class SessionProvider(object):
    def __init__(self):
        super().__init__()
        self.engine = create_engine(get_url())
        self._session_provider = sessionmaker(self.engine)

    def get_session(self):
        return self._session_provider()


@contextmanager
def session_scope(session):
    try:
        yield
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
