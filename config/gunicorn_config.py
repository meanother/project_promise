command = '/home/ubpc/project_promise/venv/bin/gunicorn'
pythonpath = '/home/ubpc/project_promise/config'
bind = '0.0.0.0:8283'
workers = 5
user = 'ubpc'
limit_request_field = 3200
limit_request_field_size = 0
errorlog = '/home/ubpc/project_promise/bin/error.log'
loglevel = 'info'
accesslog = '/home/ubpc/project_promise/bin/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
redirect_stderr=True
autorestart=True



def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    ## get traceback info
    import threading, sys, traceback
    id2name = {th.ident: th.name for th in threading.enumerate()}
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""),
            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename,
                lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
