# Dockerfile for Flask server
FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY src/api_flask ./src/api_flask
COPY src/lib ./src/lib

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi \
	&& poetry add gunicorn

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "src.api_flask.main:app"]
