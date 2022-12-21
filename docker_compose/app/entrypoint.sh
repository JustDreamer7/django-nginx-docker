#!/bin/bash -x


python manage.py collectstatic --noinput
python manage.py migrate --noinput
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi
python manage.py loaddata movies_dump.json

exec "$@"