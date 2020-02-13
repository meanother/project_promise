#!/bin/bash

source /home/ubpc/promise_project/venv/bin/activate
exec gunicorn -c "/home/ubpc/promise_project/config/gunicorn_config.py" config.wsgi