# Dockerfile for CLI
FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY src/cli ./src/cli
COPY src/lib ./src/lib

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

ENTRYPOINT ["python", "-m", "src.cli.main"]
