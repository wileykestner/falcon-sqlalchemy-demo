#!/usr/bin/env bash

source ./setup.sh

function test_with_flake8_and_coverage {
    coverage erase
    flake8 falcon_web_demo
    FLAKE_STATUS=$?
    coverage erase
    py.test --quiet --cov-report=term:skip-covered --cov=falcon_web_demo test
    TEST_STATUS=$?

    if [[ ( ${FLAKE_STATUS} == 0 ) && ( ${TEST_STATUS} == 0 ) ]] ; then
        exit 0
    else
        exit 1
    fi
}

eval_in_virtual_environment test_with_flake8_and_coverage