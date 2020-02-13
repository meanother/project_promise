command = '/home/ubpc/promise_project/venv/bin/gunicorn'
pythonpath = '/home/ubpc/promise_project/config'
bind = '0.0.0.0:8283'
workers = 5
user = 'ubpc'
limit_request_field = 3200
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
