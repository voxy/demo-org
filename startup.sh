#!/bin/sh

/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py runserver 0.0.0.0:8005
