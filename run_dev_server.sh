#!/usr/bin/env bash

source ./setup.sh

function run_dev_server {
    gunicorn falcon_web_demo.wsgi:app
}

eval_in_virtual_environment run_dev_server
