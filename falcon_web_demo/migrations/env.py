from __future__ import with_statement

import logging
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

from falcon_web_demo.persistence import get_url

config = context.config
fileConfig(config.config_file_name)
kwargs = {'as_dictionary': True}
pref = 'loggingPreference'
logging_preference = context.get_x_argument(**kwargs).get(pref)
if logging_preference:
    logging.getLogger('alembic').setLevel(logging_preference)

connectable = create_engine(get_url())

with connectable.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=None
    )

    with context.begin_transaction():
        context.run_migrations()
