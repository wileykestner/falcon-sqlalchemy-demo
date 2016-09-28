import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

__engine = None
__session_provider = None


def get_url():
    database_url = os.getenv("DATABASE_URL", None)
    if database_url is None:
        raise ValueError("Could not find DATABASE_URL in the local environment.")

    return database_url


def get_engine():
    global __engine
    if __engine is not None:
        return __engine
    __engine = create_engine(get_url())
    return __engine


def get_session():
    global __session_provider
    if __session_provider is not None:
        return __session_provider()
    __session_provider = sessionmaker(bind=get_engine())
    return __session_provider()


@contextmanager
def session_scope():
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
