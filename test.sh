#!/usr/bin/env bash

source ./setup.sh

_print_success() {
  local -r green='\033[0;32m'
  >&2 echo -e "${green}${1}"
}

_print_failure() {
  local -r red='\033[0;31m'
  >&2 echo -e "${red}${1}"
}

test_with_flake8_coverage_and_black() {
    pip install -r requirements-dev.txt -q

    local -r application_source_directory="falcon_web_demo"

    local -r test_source_directory="test"

    coverage erase
    flake8 "${application_source_directory}"
    local flake8_status=$?

    coverage erase
    py.test --quiet --cov=term:skip-covered --cov="${application_source_directory}" "${test_source_directory}"
    local pytest_status=$?

    coverage erase
    black "${application_source_directory}" "${test_source_directory}" --check
    local black_status=$?

    if [[ $pytest_status == 0 ]] ; then
        _print_success "All tests are passing and 100% of application source is covered by test."
    else
        _print_failure "There was a test failure or missing test coverage."
    fi

    if [[ $flake8_status == 0 ]] ; then
        _print_success "All Python application and test source is PEP8 compliant."
      else
        _print_failure "Some application or test source contains linting errors."
    fi

    if [[ $black_status == 0 ]] ; then
        _print_success "All code is properly formatted."
    else
        _print_failure "There were some code formatting errors, please run \`black \"${application_source_directory}\" \"${test_source_directory}\"\` to fix."
    fi

    if [[ $flake8_status != 0 || $black_status != 0 ||  $pytest_status != 0 ]] ; then
        exit 1
    fi
}

eval_in_virtual_environment test_with_flake8_coverage_and_black
