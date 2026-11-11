VALID_LEVELS = ("INFO", "WARNING", "ERROR")

def filter_log_entries(log_text: str, level:str) -> list[str]:
    if level not in VALID_LEVELS:
        raise ValueError(
            f"Invalid log level: {level}. "
            f"Expected one of: {', '.join(VALID_LEVELS)}")

    matching_entries = []

    for line in log_text.splitlines():
        if line.startswith(f"[{level}]"):
            matching_entries.append(line)

    return matching_entries

def count_log_levels(log_text: str) -> dict[str, int]:
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in log_text.splitlines():
        for level in counts:
            if line.startswith(f"[{level}]"):
                counts[level] += 1
                break
    return counts