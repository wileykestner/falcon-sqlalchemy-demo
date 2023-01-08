import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_url():
    return os.getenv("DATABASE_URL", "sqlite:///development.db")


class SessionScope(object):
    def __init__(self):
        super().__init__()
        self._engine = create_engine(get_url())
        self._session_provider = sessionmaker(self._engine)

    @contextmanager
    def __call__(self, commit_on_exit=True, *args, **kwargs):
        session = self._session_provider()
        try:
            yield session
        except Exception as e:
            session.rollback()  # untested
            raise e
        else:
            if commit_on_exit:
                session.commit()
        finally:
            session.close()  # untested
