from __future__ import with_statement

import logging
from logging.config import fileConfig

from sqlalchemy import create_engine

from alembic import context
from falcon_web_demo.persistence import get_url

config = context.config
fileConfig(config.config_file_name)
logging_preference = context.get_x_argument(as_dictionary=True).get('loggingPreference')
if logging_preference:
    logging.getLogger('alembic').setLevel(logging_preference)


def run_migrations_offline():
    url = get_url()
    context.configure(url=url, target_metadata=None, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(get_url())

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=None
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
