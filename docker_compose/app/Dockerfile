FROM python:3.10-slim-bullseye

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh
COPY config/.env_example .env_example

RUN  mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

EXPOSE 8000/tcp


RUN chmod a+x /opt/app/entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]