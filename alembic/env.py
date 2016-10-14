from __future__ import with_statement

from logging.config import fileConfig

from sqlalchemy import create_engine

from alembic import context
from demo.persistence import get_url

config = context.config
fileConfig(config.config_file_name)
target_metadata = None


def run_migrations_offline():
    url = get_url()
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    url = get_url()
    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
