# Copilot Instructions for json-py

## Project Overview

- **json-py** is a Python 3.13+ port of a JSON parser originally written in TypeScript.
- Main components are in `src/lib/` (core parsing logic) and `src/cli/main.py` (CLI entry point).
- The project is structured for clarity and separation: parsing logic is modularized by JSON type (see `array.py`, `object.py`, `string.py`, etc.).

## Key Files & Structure

- `src/lib/`: Core parser modules. Each file implements logic for a specific JSON type or concept.
- `src/cli/main.py`: CLI interface for interactive or piped JSON input.
- `src/api_django/`: Django server exposing a REST API for parsing JSON input.
- `src/api_fastapi/main.py`: FastAPI server exposing a REST API for parsing JSON input.
- `src/api_flask/main.py`: Flask server exposing a REST API for parsing JSON input.
- `pyproject.toml`: Project configuration and dependencies (Poetry compatible).
- `tests/`: Unit tests for parser components.

## Project-Specific Patterns

- **Parser Design:** Each JSON type (array, object, string, number, etc.) has its own module in `src/lib/`. Cross-module imports are used for type composition.
- **CLI Pattern:** The CLI reads from stdin or prompts the user, then delegates parsing to the core modules.
- **API Pattern:** The API servers (Django, FastAPI, Flask) expose a POST endpoint `/api/v1/parse` that accepts plaintext JSON, parses it using the core parser, and returns either a parsed result or an error message.
- **Testing:** Tests are in `tests/`, using Python's built-in `unittest` framework. Coverage is measured with `coverage`.
- **Formatting & Linting:** Black and ruff are used; see `.vscode/settings.json` for formatter config.

## Integration Points

- No external APIs or services; all logic is local and self-contained.
- Poetry is used for dependency management; Black and ruff for code quality.

## Conventions

- Python 3.13+ syntax is used throughout.
- Modular file structure: each JSON concept/type in its own file.
- CLI, API, and library code are strictly separated.
- All new code should be covered by unit tests in `tests/`.

For detailed setup and running instructions, see `README.md`. For more details on source files, see `src/lib/`, `src/cli/`, `src/api_django`, `src/api_fastapi/`, and `src/api_flask/`.
