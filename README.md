# test-codecov

A minimal Python library project for testing pytest coverage output and Codecov uploads.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

## Run tests with coverage

```bash
pytest --cov=test_codecov --cov-report=term-missing --cov-report=xml
```

The terminal command prints a coverage table and writes `coverage.xml`, which the GitHub Actions workflow uploads to Codecov.

