#!/usr/bin/env bash

source ./setup.sh
eval_in_virtual_environment "gunicorn falcon_web_demo.wsgi:app"
