#!/usr/bin/env bash

function eval_in_virtual_environment {
    VIRTUALENV_NAME=env

    if [ ! -d ${VIRTUALENV_NAME} ]; then
      python -m venv env
    fi

    source ${VIRTUALENV_NAME}/bin/activate
    pip install --upgrade pip
    pip install --upgrade wheel
    pip install -r source-requirements.txt
    pip install -r requirements.txt
    deactivate
    source ${VIRTUALENV_NAME}/bin/activate
    PYTHONPATH=$PYTHONPATH:. alembic upgrade head
    echo "Running '$1' inside virtual environment…"
    $1
}
