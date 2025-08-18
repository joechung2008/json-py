# Copilot Instructions for json-py

## Project Overview

- **json-py** is a Python 3.13+ port of a JSON parser originally written in TypeScript.
- Main components are in `src/lib/` (core parsing logic) and `src/cli/main.py` (CLI entry point).
- The project is structured for clarity and separation: parsing logic is modularized by JSON type (see `array.py`, `object.py`, `string.py`, etc.).

## Key Files & Structure

- `src/lib/`: Core parser modules. Each file implements logic for a specific JSON type or concept.
- `src/cli/main.py`: CLI interface for interactive or piped JSON input.
- `pyproject.toml`: Project configuration and dependencies (Poetry compatible).
- `tests/`: Unit tests for parser components.

## Developer Workflows

- **Install dependencies:** `poetry install` (uses `pyproject.toml`).
- **Run CLI:** `python src/cli/main.py` (interactive or piped input).
- **Run tests:** `python -m unittest discover -v` (all tests in `tests/`).
- **Measure coverage:** `coverage run -m unittest discover` then `coverage report` or `coverage html`.
- **Format code:** `black .` (Black is the standard formatter).
- **Lint code:** `flake8 src/cli src/lib` (flake8 is recommended for linting).

## Project-Specific Patterns

- **Parser Design:** Each JSON type (array, object, string, number, etc.) has its own module in `src/lib/`. Cross-module imports are used for type composition.
- **CLI Pattern:** The CLI reads from stdin or prompts the user, then delegates parsing to the core modules.
- **Testing:** Tests are in `tests/`, using Python's built-in `unittest` framework. Coverage is measured with `coverage`.
- **Formatting & Linting:** Black and flake8 are used; see `.vscode/settings.json` for formatter config.

## Integration Points

- No external APIs or services; all logic is local and self-contained.
- Poetry is used for dependency management; Black and flake8 for code quality.

## Conventions

- Python 3.13+ syntax is used throughout.
- Modular file structure: each JSON concept/type in its own file.
- CLI and library code are strictly separated.
- All new code should be covered by unit tests in `tests/`.

## Example: Adding a New JSON Type

1. Create a new module in `src/lib/` (e.g., `boolean.py`).
2. Implement parsing logic, following patterns in existing modules.
3. Add unit tests in `tests/`.
4. Update CLI logic if user input should support the new type.

---

For more details, see `README.md` and source files in `src/lib/` and `src/cli/`.
