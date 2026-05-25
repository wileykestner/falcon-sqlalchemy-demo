#!/usr/bin/env bash

function eval_in_virtual_environment {
    VIRTUALENV_NAME="env"
    PYTHON_BINARY="python3"

    if [ ! -d ${VIRTUALENV_NAME} ]; then
      "${PYTHON_BINARY}" -m venv "${VIRTUALENV_NAME}"
    fi

    source ${VIRTUALENV_NAME}/bin/activate
    "${PYTHON_BINARY}" -m pip install --upgrade pip
    "${PYTHON_BINARY}" -m pip install --upgrade wheel
    "${PYTHON_BINARY}" -m pip install -r source-requirements.txt
    "${PYTHON_BINARY}" -m pip install -r requirements.txt
    deactivate
    source ${VIRTUALENV_NAME}/bin/activate
    PYTHONPATH=$PYTHONPATH:. alembic upgrade head
    echo "Running '$1' inside virtual environment…"
    $1
}
