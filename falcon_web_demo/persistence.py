import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_url():
    return os.getenv("DATABASE_URL", "sqlite:///development.db")


class SessionScope(object):

    @contextmanager
    def __call__(self, commit_on_exit=True, *args, **kwargs):
        engine = create_engine(get_url())
        session_provider = sessionmaker(engine)
        session = session_provider()
        try:
            yield session
        except Exception as e:
            session.rollback()
            raise e
        else:
            if commit_on_exit:
                session.commit()
        finally:
            session.close()
            engine.dispose()
