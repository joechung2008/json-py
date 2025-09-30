# Dockerfile for FastAPI server
FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY src/api_fastapi ./src/api_fastapi
COPY src/lib ./src/lib

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

EXPOSE 8000
ENTRYPOINT ["uvicorn", "src.api_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
