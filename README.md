# json-py

JSON parser ported from TypeScript to Python 3.13.7

## License

MIT

## Reference

[json.org](http://json.org)

## Usage

### Run CLI with user input

```sh
poetry run cli
```

You will be prompted to enter JSON input interactively.

### Run CLI with a shell command

```sh
echo '{"key":"value"}' | poetry run cli
```

This allows you to pass JSON data directly to the CLI.

## Running the FastAPI Server

To start the FastAPI server for the API endpoint:

```sh
poetry run fastapi
```

This will start the server at `http://127.0.0.1:8000`.

## Running the Flask Server

To start the Flask server for the API endpoint:

```sh
poetry run flask
```

This will start the Flask server at `http://127.0.0.1:8000`.

## Sending Test Requests with REST Client Extension

You can use the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) in VS Code to send requests to the FastAPI server.

Create a file (e.g., `test-api.http`) with the following content:

```http
POST http://localhost:8000/api/v1/parse HTTP/1.1
Content-Type: text/plain

{"key":"value"}
```

Click "Send Request" above the request in VS Code to test the API.

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
poetry run black
```

This will automatically format your code according to Black's style guide.

## Linting Code with Ruff

To lint all Python files in the project:

```sh
poetry run ruff
```

This will check your code for style and programming errors.

## Running Tests

To run all Python tests using unittest:

```sh
poetry run tests
```

## Measuring Test Coverage

To run tests and measure coverage:

```sh
poetry run coverage
```

To generate a coverage report:

```sh
poetry run coverage report
```

To generate and open an HTML coverage report:

```sh
poetry run coverage html
```
