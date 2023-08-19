#!/usr/bin/env bash

function eval_in_virtual_environment {
    VIRTUALENV_NAME="env"

    if [ ! -d ${VIRTUALENV_NAME} ]; then
      python -m venv "${VIRTUALENV_NAME}"
    fi

    source ${VIRTUALENV_NAME}/bin/activate
    pip install -q --upgrade pip
    pip install -q --upgrade wheel
    pip install -q -r source-requirements.txt
    pip install -q -r requirements.txt
    deactivate
    source ${VIRTUALENV_NAME}/bin/activate
    PYTHONPATH=$PYTHONPATH:. alembic upgrade head
    echo "Running '$1' inside virtual environment…"
    $1
}
