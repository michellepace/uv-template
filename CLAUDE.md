# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

Use British spelling consistently in this repo, always.

## Project Capabilities

This is a UV-based Python template supporting:

- **CLI scripts** and **importable packages** (both `src/` and `scripts/`)
- **TDD workflow** with pytest and comprehensive pre-commit quality gates
- **Jupyter notebooks** with project code integration for data analysis and prototyping

## Core Architecture

**Standard Python packaging** with:

- `src/` layout for distributable packages (proper import isolation)
- `scripts/` for standalone utilities
- `notebooks/` for exploratory analysis and documentation
- `tests/` mirroring `src/` structure

## Tech Stack

- **Python**: 3.13+
- **Key Patterns**: Use `pathlib` (not `os`), `dataclasses`, `logging`, `pytest` with `tmp_path`
- **Dependencies**: See [pyproject.toml](pyproject.toml) for complete list

## UV Workflow (Always)

**Strict Rules:**

- Use `uv run` - never activate venv
- Use `uv add` - never pip
- Use `pyproject.toml` - never requirements.txt

**Common Commands:**

```bash
# Setup & Dependencies
uv sync # Match packages to lockfile
uv add --dev <pkg> # Add dev dependency
uv tree # Show installed dependencies
uv lock --upgrade-package <pkg> # Update specific package
uv lock --upgrade && uv sync # Update all packages and apply

# Development
uv run pre-commit run --all-files # (hooks in .pre-commit-config.yaml)
uv run pytest # All tests
uv run pytest -v tests/test_specific.py::test_function
uv run ruff check --fix # Lint and auto-fix (rules in pyproject.toml)
uv run ruff format # Format (see pyproject.toml)
```

## Code Design Principles: Elegant Simplicity over Over-Engineered

**TDD-Driven Design**: Write tests first - this naturally creates better architecture:

- **Pure functions preferred** - no side effects in business logic, easier to test
- **Clear module boundaries** - easier to test and understand
- **Single responsibility** - complex functions are hard to test

**Key Architecture Guidelines**:

- **Layer separation** - CLI → business logic → I/O
- **One module, one purpose** - Each `.py` file has a clear, focused role
- **Handle errors at boundaries** - Catch exceptions in CLI layer, not business logic
- **Type hints required** - All function signatures need type annotations
- **Descriptive naming** - Functions/variables should clearly indicate purpose and be consistent throughout

## TDD Implementation

- Use pytest's `tmp_path` fixture to avoid creating test files
- Avoid mocks as they introduce unnecessary complexity
- Test incrementally: One test should drive one behaviour
- Use focused test names that describe what's being tested

## Code Quality Standards

- **Ruff**: Linting (ALL rules enabled)
- **Pyright**: Type checking (see [pyproject.toml](pyproject.toml))
- **Pre-commit**: Auto-runs on every commit
