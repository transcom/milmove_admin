#!/bin/bash

# # Clear all static files
# python manage.py collectstatic --clear --noinput
# Generate new static files
python manage.py collectstatic --noinput

# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log

# Start Gunicorn processes
echo Starting Gunicorn and Nginx.
exec gunicorn milmove_admin.wsgi:application \
    --name milmove_admin \
    --bind unix:django_app.sock \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log & nginx -g "daemon off;"
