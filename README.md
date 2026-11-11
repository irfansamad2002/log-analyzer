# IT Log Analyzer

A command-line Python tool for analysing application log files.

## Features

- Count log entries by severity (INFO, WARNING, ERROR).
- Filter log entries by severity.
- Configure default filtering through a JSON configuration file.
- Override configuration using command-line arguments.
- Log application events and errors.
- Handle missing files and invalid configuration.
- Automated unit tests.

## Project Structure

```text
log-analyzer/
├── config.json
├── data/
│   └── sample.log
├── src/
│   ├── analyzer.py
│   └── main.py
└── tests/
    ├── test_analyzer.py
    └── test_config.py
```

## Requirements

- Python 3.10 or newer
- No external Python packages required

## Usage

Run the analyzer from the project root:

```bash
python -m src.main data/sample.log
```

Filter by a specific severity:

```bash
python -m src.main data/sample.log --level ERROR
```

View available arguments:

```bash
python -m src.main --help
```

## Configuration

Edit `config.json` to change the default filter:

```json
{
    "default_level": "ALL"
}
```

Available levels:

- `ALL`
- `INFO`
- `WARNING`
- `ERROR`

A command-line `--level` argument takes priority over the configuration file.

## Running Tests

Run the automated test suite:

```bash
python -m unittest discover -s tests -v
```

## Learning Objectives

This project was built to practise:

- Python project structure and imports
- Command-line interfaces with `argparse`
- JSON configuration
- Logging and exception handling
- Unit testing with `unittest`
- Git and GitHub workflows