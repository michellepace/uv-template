# CLAUDE.md

General purpose `uv` Python template for projects built with AI coding agents. Tooling configured for deterministic feedback.

## Tech Stack

- Python >=3.14, managed with `uv`
- Dev tooling: `ruff`, `pyright`, `pytest`, `pre-commit`

## Development Commands

```bash
# Dependencies & environment
uv add <deps>          # runtime dependencies
uv add --dev pytest    # dev dependencies
uv sync                # sync env to the lockfile
uv lock --upgrade      # bump locked versions
uv tree                # dependency tree

# Run
uv run <command>       # commands in project env
uv run <entry-point>   # defined in [project.scripts]

# Code quality
uv run ruff format      # format
uv run ruff check --fix # lint + autofix
uv run pyright          # type-check
uv run pytest           # run tests
uv run pre-commit run --all-files   # run all hooks

npx --yes markdownlint-cli2 --fix <file.md>   # lint + autofix
```
