import json
import os

try:
    # Try relative import (if running as a package)
    from .task import Task
except ImportError:
    # Fallback if running script directly
    from task import Task


def read_tasks(filepath):
    """Read tasks from JSON file and return a list of Task objects."""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return [Task(**task) for task in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def write_tasks(filepath, tasks):
    """Write list of Task objects to JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)