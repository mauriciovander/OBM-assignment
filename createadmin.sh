#!/bin/sh

USER_NAME=admin
USER_EMAIL=admin@example.com
USER_PASSWORD=password1234

python manage.py createsuperuser --email $USER_EMAIL --username $USER_NAME --noinput
echo $USER_PASSWORD > python manage.py changepassword $USER_NAME