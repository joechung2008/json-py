# json-py

A small JSON parser library, ported from TypeScript to Python, with a CLI and simple HTTP APIs implemented in FastAPI, Flask, and Django.

## License

MIT

## Reference

[json.org](http://json.org)

## Overview

- Library: JSON tokenizer/parser in plain Python (src/lib/\*).
- CLI: Reads JSON from stdin and pretty-prints the parsed structure.
- HTTP APIs: POST /api/v1/parse that accepts raw body (text/plain or application/json) and returns a pretty-printed parse result.
- Tests: unittest-based tests under tests/ and sample REST requests in testdata/.

## Tech stack and package manager

- Language: Python (requires >= 3.10 per pyproject.toml)
- Package manager/build: Poetry (pyproject.toml)
- Web frameworks (optional, for APIs):
  - FastAPI (served via uvicorn)
  - Flask
  - Django + Django REST framework
- Dev tools: black, ruff, coverage

## Requirements

- Python 3.10 or newer
- Poetry installed (recommended via pipx: pipx install poetry)
- Optional: uvicorn for FastAPI (installed via Poetry dependencies)

## Installation

Using Poetry (recommended):

- Windows PowerShell

  - pipx install poetry
  - poetry install

- macOS/Linux (or WSL)
  - pipx install poetry
  - poetry install

You can run commands with the environment isolated via poetry run <cmd> or activate the venv:

- PowerShell: .venv\Scripts\Activate.ps1 (if you configured in-project venv)
- Bash/zsh: source $(poetry env info --path)/bin/activate

## Running

### CLI

- Interactive from stdin
  - Windows PowerShell: Get-Content -Raw .\path\to\input.json | poetry run python -m src.cli.main
  - macOS/Linux: cat path/to/input.json | poetry run python -m src.cli.main
- One-liner with echo (POSIX shells): echo '{"key": "value"}' | poetry run python -m src.cli.main
- Via Poetry script (defined in pyproject.toml): poetry run cli

### FastAPI (recommended HTTP API)

- Run: poetry run uvicorn src.api_fastapi.main:app --reload
- Endpoint: POST http://127.0.0.1:8000/api/v1/parse
- Request headers: Content-Type: text/plain; charset=utf-8 (or application/json)

### Flask

Run (development):
  poetry run python -m src.api_flask.main
Run (production, recommended):
  poetry run gunicorn -b 0.0.0.0:8000 src.api_flask.main:app
Endpoint: POST http://127.0.0.1:8000/api/v1/parse

### Django

Run from project root:
  - cd src/api_django
  - poetry run python manage.py runserver  # Development only
  - poetry run gunicorn -b 0.0.0.0:8000 json_parser.wsgi:application  # Production
Endpoint: POST http://127.0.0.1:8000/api/v1/parse
Note: A sys.path tweak in src/api_django/api/views.py includes an absolute Linux path. This is likely stale for other environments. See TODOs below.

## Scripts

Defined in pyproject.toml:

- Poetry script: cli -> src.cli.main:main
  - Run with: poetry run cli

Common ad-hoc commands:

- Lint: poetry run ruff check .
- Format: poetry run black .
- Tests: poetry run python -m unittest discover -v
- Coverage: poetry run coverage run -m unittest discover && poetry run coverage report
- FastAPI dev server: poetry run uvicorn src.api_fastapi.main:app --reload

## Environment variables and configuration

- No required environment variables for library or CLI.
- Encoding: APIs detect request body charset from the Content-Type header; defaults to utf-8 if unspecified.
- Flask: You may override port/host by modifying src/api_flask/main.py (defaults to 0.0.0.0:8000).
- Django: Default development settings in src/api_django/json_parser/settings.py are used. For production, configure SECRET_KEY, DEBUG, ALLOWED_HOSTS, etc.
- FastAPI: No special env; use uvicorn flags for host/port, e.g., --host 0.0.0.0 --port 8000.

## Tests

- Run all tests: poetry run python -m unittest discover -v
- Coverage:
  - poetry run coverage run -m unittest discover
  - poetry run coverage report
  - poetry run coverage html (open htmlcov/index.html)

Sample requests are provided in testdata/\*.rest, compatible with VS Code REST Client or JetBrains HTTP Client. Example (HTTP file):

```http
POST http://localhost:8000/api/v1/parse
Content-Type: text/plain

{"key": "value"}
```

## Project structure

- LICENSE
- README.md
- pyproject.toml
- poetry.lock
- src/
  - lib/ (parser library)
    - **init**.py, json.py, value.py, string.py, number.py, array.py, object.py, pair.py, types.py
  - cli/
    - main.py (entry point for CLI; exposed as Poetry script cli)
  - api_fastapi/
    - main.py (FastAPI app with POST /api/v1/parse)
  - api_flask/
    - main.py (Flask app with POST /api/v1/parse)
  - api_django/
    - manage.py, json_parser/ (Django project), api/ (Django app with POST /api/v1/parse)
- tests/ (unittest test suite)
- testdata/ (\*.rest example requests)
