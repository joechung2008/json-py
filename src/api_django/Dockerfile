# Dockerfile for Django server
FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY src/api_django ./src/api_django
COPY src/lib ./src/lib

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

WORKDIR /app/src/api_django

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "json_parser.wsgi:application"]
