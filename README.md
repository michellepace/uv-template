![UV logo with cute Python snake](uv-banner.jpg)

General purpose [uv](https://docs.astral.sh/uv/) Python template for projects built with AI coding agents, specifically Claude Code.

Tooled up for deterministic feedback and a wonderful workflow.

## Tooling Configured

🌸 DETERMINISTIC

ruff (linting), pyright (type-checking), pytest (testing), pre-commit (running all checks on every commit).

🌸 PLUGINS

The [pyright-lsp](https://claude.com/plugins/pyright-lsp) plugin so Claude sees pyright errors as it writes, config in [`pyproject.toml`](pyproject.toml). The wonderful [mattpocock-skills](https://www.aihero.dev/skills) workflow, disabled by default. See [`.claude/settings.json`](.claude/settings.json), both from the Claude Code Official marketplace.

> *`mattpocock-skills` AI Skills for Real Engineers. A practical skill system for engineers who want to use AI without giving up their standards.*

## Usage

Pre-requisite: install [uv](https://docs.astral.sh/uv/getting-started/installation/) on your machine

Step 1: Get this template repo without my commit history:

```shell
# Use this template to create your own repo "my-project" (on GitHub)
gh repo create my-project --template michellepace/uv-template --private

# Clone it to your machine
gh repo clone my-project
cd my-project

# Install dependencies and pre-commit hooks
uv sync && uv run pre-commit install
```

Step 2: Prompt to "de-template" and make it yours:

```markdown
# TASK: Help me make this template my own

Take my project's name from this repo's name and make the template mine.

First read @README.md — but don't rename anything inside it yet.

1. Rename/replace everywhere except `README.md`, then verify with
   `uv sync && uv run pre-commit install && uv run pre-commit run --all-files`

2. Rewrite `README.md` and `.claude/CLAUDE.md` for my project

3. In a friendly way, ask me if I want to:
    - Remove plugin `git-utils` and its marketplace `my-claude-marketplace` (it's Michelle's)
    - Enable plugin `mattpocock-skills` and try the `/grilling` Skill

Await my confirmation, then do it with `claude plugin` commands (`--scope project`).
I like simple clear messages with emojis 🙂.
```

Step 3: Choose what to do with Matt Pocock:

```shell
# Want to use it? Currently disabled, so enable it:
claude plugin enable mattpocock-skills@claude-plugins-official --scope project

# Not sure? Watch a video
# https://www.youtube.com/@mattpocockuk

# Don't want it? (it's really good)
claude plugin uninstall mattpocock-skills@claude-plugins-official --scope project
# (don't remove the marketplace — pyright-lsp comes from it too)
```

Step 4: Install the recommended VS Code [`extensions.json`](.vscode/extensions.json)

Step 5 (optional):

Query official uv docs from your agent with `/ask-docs uv [your question]` — see [michellepace/docs-for-ai](https://github.com/michellepace/docs-for-ai)

## This project is a "packaged application"

> *A Python project must be built to be installed. This process is generally referred to as "packaging". See [uv project config docs](https://docs.astral.sh/uv/concepts/projects/config/#project-packaging)*.

The docs say you probably need a package if you want to: add commands to the project, use a `src`/`tests` layout, write a library, or distribute to others (PyPI). This template needs the first two. Happily, a packaged application is now the `uv init` default (since uv 0.12)!

A **packaged application** gives you three things: a `src/<pkg>/` layout, a `[build-system]` (the `uv_build` backend), and a `[project.scripts]` for commands.

"Packaged" just means uv builds and installs *your own code* into `.venv` alongside your dependencies — a local install, nothing to do with PyPI. This lets `import <pkg>` work from anywhere (such as `tests/`), and named commands run via `uv run <command>`.

This project was initialised with `uv init` (the default):

| Command | You get | Good for |
| :--- | :--- | :--- |
| `uv init` | `src/` layout, your code installed, a CLI command | most projects — anything with tests or commands |
| `uv init --no-package` | flat `main.py`, no build system, deps only | quick scripts, throwaway experiments |
| `uv init --lib` | `src/` layout + `py.typed` marker, no CLI command | libraries you'll publish for others to import |
