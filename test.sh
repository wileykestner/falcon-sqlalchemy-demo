#!/usr/bin/env bash

source ./setup.sh

function test_with_flake8_and_coverage {
    pip install -r requirements-dev.txt -q
    coverage erase
    flake8 falcon_web_demo
    FLAKE_STATUS=$?
    coverage erase
    py.test --quiet --cov=term:skip-covered --cov=falcon_web_demo test
    TEST_STATUS=$?

    if [[ ( ${FLAKE_STATUS} == 0 ) && ( ${TEST_STATUS} == 0 ) ]] ; then
        echo "All tests pass, application is PEP8 compliant, and 100% of the production code is covered by test."
        exit 0
    else
        exit 1
    fi
}

eval_in_virtual_environment test_with_flake8_and_coverage
