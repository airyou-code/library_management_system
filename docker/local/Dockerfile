FROM python:3.12-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # fix ImportError: failed to find libmagic
  && apt-get install -y libmagic-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # git is required for pip install from git repo
  && apt-get install -y git ssh \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && apt update && apt install -y curl

# Requirements are installed here to ensure they will be cached.
COPY ./src/backend/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./docker/deploy/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/deploy/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
COPY ./src/backend /app

ENTRYPOINT ["/entrypoint"]
