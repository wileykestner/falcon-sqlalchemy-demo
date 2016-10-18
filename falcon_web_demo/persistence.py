import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_url():
    database_url = os.getenv("DATABASE_URL", "sqlite:///development.db")
    if database_url is None:
        raise ValueError("Could not find DATABASE_URL in the local environment.")

    return database_url


class SessionScope(object):
    def __init__(self):
        super().__init__()
        self.engine = create_engine(get_url())
        self._session_provider = sessionmaker(self.engine)

    @contextmanager
    def __call__(self, commit_on_exit=True, *args, **kwargs):
        session = self._session_provider()
        try:
            yield session
        except:
            session.rollback()  # untested
            raise
        else:
            if commit_on_exit:
                session.commit()
        finally:
            session.close()  # untested
