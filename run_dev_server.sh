#!/usr/bin/env bash

source ./setup.sh
eval_in_virtual_environment "gunicorn demo.wsgi:app"
