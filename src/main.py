import argparse
import json
import logging
from pathlib import Path

from src.analyzer import (
    VALID_LEVELS,
    count_log_levels,
    filter_log_entries
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.json"

DEFAULT_CONFIG = {"default_level": "ALL"}
ALLOWED_LEVELS = ("ALL", *VALID_LEVELS)

def configure_logging():
    log_directory = PROJECT_ROOT / "logs"
    log_directory.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=str(log_directory / "app.log"),
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8"
    )

def load_config(config_path=CONFIG_PATH):
    try:
        config = json.loads(
            config_path.read_text(encoding="utf-8")
        )
    except FileNotFoundError:
        return DEFAULT_CONFIG.copy()

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON configuration: {error}"
        ) from error

    except OSError as error:
        raise ValueError(
            f"Could not read configuration: {error}"
        ) from error

    if not isinstance(config, dict):
        raise ValueError("Configuration must be a JSON object.")

    default_level = config.get("default_level", "ALL")

    if default_level not in ALLOWED_LEVELS:
        raise ValueError(
            f"default_level must be one of: {','.join(ALLOWED_LEVELS)}"
        )

    return {"default_level": default_level}

def main():
    parser = argparse.ArgumentParser(
        description="Analyse IT application logs."
    )

    parser.add_argument(
        "log_file",
        type=Path,
        help="Path to the log file."
    )

    parser.add_argument(
        "--level",
        choices=["ALL", *VALID_LEVELS],
        default=None,
        help="Filter entries by log level."
    )

    args = parser.parse_args()

    configure_logging()

    logging.info("Application started.")

    try:
        config = load_config()

    except ValueError as error:
        logging.exception("Configuration loading failed.")
        print(f"Configuration error: {error}")
        return 1

    # Command-line argument takes priority over config.
    selected_level = args.level or config["default_level"]

    logging.info("Selected filter: %s", selected_level)

    try:
        log_text = args.log_file.read_text(encoding="utf-8")

    except OSError as error:
        logging.exception("Could not read input file.")
        print(f"Could not read file: {error}")
        return 1

    logging.info("Successfully read input file: %s", args.log_file)

    counts = count_log_levels(log_text)

    print("\nLog Analysis Results")
    print("----------------------------")

    for level, count in counts.items():
        print(f"{level}: {count}")

    if selected_level != "ALL":
        entries = filter_log_entries(log_text, selected_level)

        print(f"\nMatching {selected_level} entries:")

        if not entries:
            print("No matching entries found.")
        else:
            for entry in entries:
                print(entry)

    logging.info("Analysis completed successfuly.")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())