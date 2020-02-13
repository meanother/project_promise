#!/bin/bash

source /home/ubpc/project_promise/venv/bin/activate
exec gunicorn -c "/home/ubpc/project_promise/config/gunicorn_config.py" config.wsgi
