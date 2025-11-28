# pyci-lint

Python lint check with GitHub Actions

## GitHub Actions

The following linter results are detected by GitHub Actions.

- ruff
- mypy

## Supported Python Versions

- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13

## Setup

```bash
make init
```

## Commands

| Command | Description |
|---------|-------------|
| `make init` | Install dependencies |
| `make lint` | Run lint checks (ruff check, ruff format --check, mypy) |
| `make fmt` | Auto-format code (ruff format, ruff check --fix) |
| `make run` | Run the application |

## Development Rules

- Use pydantic for type safety
- One class per file
- Follow object-oriented design principles
- Always run `make lint` after code changes

See [CLAUDE.md](CLAUDE.md) for details.
