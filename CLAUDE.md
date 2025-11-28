# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A template repository for running Python lint checks (ruff, mypy) with GitHub Actions. Supports Python 3.10-3.13.

## Virtual Environment

Use venv unless otherwise specified:

```bash
python -m venv venv
source venv/bin/activate
```

## Commands

```bash
make init    # Install dependencies
make lint    # ruff check + ruff format --check + mypy
make fmt     # ruff format + ruff check --fix (auto-fix)
make run     # Run main.py
```

## Lint Settings

- **ruff**: Configured in `pyproject.toml`. Line length 79, E/F/I rules enabled
- **mypy**: Strict type checking (`disallow_untyped_defs`, `disallow_untyped_calls`, etc.)

## Development Rules

### Type Safety

- Use pydantic to ensure data type safety
- All functions/methods must have type annotations (enforced by mypy's `disallow_untyped_defs`)

### Import

- Follow PEP 8

### File Structure

- One class per file
- Match class name to file name (e.g., `MyClass` → `my_class.py`)

### Object-Oriented Design

- Follow the single responsibility principle
- Prefer composition over inheritance

### Constants

- No magic numbers/strings
- Define constants in `constants/` and reference them

### Enum Definition

- Do not use `auto()`
- Define as tuple `(code, display_name)` format with property accessors

```python
from enum import Enum

class Status(Enum):
    ACTIVE = (1, "Active")
    INACTIVE = (0, "Inactive")

    def __init__(self, code: int, display_name: str) -> None:
        self._code = code
        self._display_name = display_name

    @property
    def code(self) -> int:
        return self._code

    @property
    def display_name(self) -> str:
        return self._display_name
```

### Directory Structure

Rename the `app/` directory to match your project name, and organize with the following structure:

```text
<project_name>/
├── constants/    # Enums and constants
├── models/       # pydantic models
├── services/     # Business logic
└── exceptions/   # Custom exceptions
tests/            # Test code
```

### Docstring

- Write docstrings for all public APIs (public functions/classes)
- Use Google style

### Testing

- Use pytest
- Place test files in `tests/` with `test_*.py` naming convention

### Logging

- Do not use `print()`
- Use the `logging` module

### Required After Code Changes

- Always run `make lint` after code changes to ensure no lint errors
- Fix any lint errors before committing
