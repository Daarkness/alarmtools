#!/usr/bin
gunicorn -w 2 -b 0.0.0.0:5000 -D main:app --access-logfile alert.log



