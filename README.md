# json-py

JSON parser ported from TypeScript to Python 3.13.7

## License

MIT

## Reference

[json.org](http://json.org)

## Usage

### Run CLI with user input

```sh
python src/cli/main.py
```

You will be prompted to enter JSON input interactively.

### Run CLI with a shell command

```sh
echo '{"key": "value"}' | python src/cli/main.py
```

This allows you to pass JSON data directly to the CLI.

## Project Configuration with pyproject.toml

This project uses a `pyproject.toml` file for configuration and dependency management.  
`pyproject.toml` is a standardized file for Python projects that defines build system requirements and project metadata.

You do not run or view `pyproject.toml` with a command; it is a configuration file that you can open and edit in any text editor.  
Tools like Poetry read this file automatically when you run commands such as `poetry install`.

### Poetry

[Poetry](https://python-poetry.org/) is used for dependency management and packaging.  
Install dependencies with:

```sh
poetry install
```

See the [Poetry documentation](https://python-poetry.org/docs/) for details.

## Formatting Code with Black

To format all Python files in the project:

```sh
black .
```

This will automatically format your code according to Black's style guide.

## Linting Code

To lint all Python files in the project:

```sh
ruff check .
```

This will check your code for style and programming errors.

## Running Tests

To run all Python tests using unittest:

```sh
python -m unittest discover -v
```

## Measuring Test Coverage

To run tests and measure coverage:

```sh
coverage run -m unittest discover
```

To generate a coverage report:

```sh
coverage report
```

To generate an HTML coverage report:

```sh
coverage html
```

Open `htmlcov/index.html` in your browser to view the detailed coverage report.
