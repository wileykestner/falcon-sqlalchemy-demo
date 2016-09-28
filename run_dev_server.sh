#!/usr/bin/env bash

VIRTUALENV_NAME=env
DEVELOPMENT_ENVIRONMENT_FILENAME=.env
DEVELOPMENT_DATABASE_URL=.env

if [ ! -d ${VIRTUALENV_NAME} ]; then
  virtualenv env -p python3
fi

if [ ! -f ${DEVELOPMENT_ENVIRONMENT_FILENAME} ]; then
  touch ${DEVELOPMENT_ENVIRONMENT_FILENAME}
  echo "export DATABASE_URL=sqlite:///development.db" >> ${DEVELOPMENT_ENVIRONMENT_FILENAME}
fi

source ${VIRTUALENV_NAME}/bin/activate
pip install -r requirements.txt
source ${DEVELOPMENT_ENVIRONMENT_FILENAME}

PYTHONPATH=$PYTHONPATH:. alembic upgrade head
gunicorn demo.webapp:app
