![UV logo with cute Python snake](uv-banner.jpg)

General purpose [uv](https://docs.astral.sh/uv/) Python template for projects built with AI coding agents, specifically Claude Code.

Tooled up for deterministic feedback and a wonderful workflow.

## Tooling Configured

🌸 DETERMINISTIC

- `ruff` — linting
- `pyright` — type-checking
- `pytest` — testing
- `pre-commit` — check all pre-commit

---

🌸 PLUGINS (all disabled)

- [`pyright-lsp@claude-plugins-official`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pyright-lsp) — Claude sees pyright errors, see [`pyproject.toml`](pyproject.toml)
- [`mattpocock-skills@claude-plugins-official`](https://github.com/mattpocock/skills) — Full workflows `grilling`, `tdd`, `to-spec`
- [`alwayson-misc@my-claude-marketplace`](https://github.com/michellepace/my-claude-marketplace/tree/main/plugins/alwayson-misc) — My own, skills like: `manage-plugins`, `uv-pep723`
- [`git-utils@my-claude-marketplace`](https://github.com/michellepace/my-claude-marketplace/tree/main/plugins/git-utils) — My own, skills like `gg-commit`, `gg-land-branch`

Plugins that you want to keep must be installed not just configured, run:

```shell
claude plugin marketplace add <owner/repo> --scope project
claude plugin enable <plugin>@<marketplace> --scope project
```

## Usage

1. Step 1: Install [uv](https://docs.astral.sh/uv/getting-started/installation/) on your machine

2. Step 2: Get this template repo without my commit history:

   ```shell
   # Use this template to create your own repo "my-project" (on GitHub)
   gh repo create my-project --template michellepace/uv-template --private

   # Clone it to your machine
   gh repo clone my-project
   cd my-project

   # Install dependencies and pre-commit hooks
   uv sync && uv run pre-commit install
   ```

3. Step 3: Prompt to "de-template" and make it yours:

   ```markdown
   # TASK: Help me make this template my own

   Take my project's name from this repo's name and make the template mine.

   First read @README.md — but don't rename anything inside it yet.

   1. Rename/replace everywhere except `README.md`, then verify with
      `uv sync --reinstall && uv run pre-commit install && uv run pre-commit run --all-files`

   2. Rewrite `README.md` and `.claude/CLAUDE.md` for my project

   3. Ask if I want to install the Plugins or cleanup `.claude/settings.json`.

   Await my confirmation, then edit the file.

   I like simple clear messages that are easy to read, with emojis 🙂.
   ```

4. Step 4: Install the recommended VS Code [`extensions.json`](.vscode/extensions.json)

5. Step 5 (optional): Ask uv docs `/ask-docs uv [your question]`, needs [this](https://github.com/michellepace/docs-for-ai) repo.

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
