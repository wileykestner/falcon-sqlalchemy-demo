#!/usr/bin/env bash

function eval_in_virtual_environment {
    VIRTUALENV_NAME=env

    if [ ! -d ${VIRTUALENV_NAME} ]; then
      virtualenv env -p python3
    fi

    source ${VIRTUALENV_NAME}/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    deactivate
    source ${VIRTUALENV_NAME}/bin/activate
    PYTHONPATH=$PYTHONPATH:. alembic upgrade head
    echo "Running '$1' inside virtual environment…"
    eval $1
}
