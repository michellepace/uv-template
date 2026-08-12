![UV logo with cute Python snake](uv-banner.jpg)

General purpose [uv](https://docs.astral.sh/uv/) Python template for projects built with AI coding agents. Tooling configured for deterministic feedback.

Dev tooling includes ruff (linting), pyright (type-checking), pytest (testing), pre-commit (running all checks on every commit).

## Usage

Step 1: [Install uv](https://docs.astral.sh/uv/getting-started/installation/) on your machine and then get this template repo without my commit history:

```shell
# Use this template to create your own repo "my-project" (on GitHub)
gh repo create my-project --template michellepace/uv-package-template --private

# Clone it to your machine
gh repo clone my-project
cd my-project

# Install dependencies and pre-commit hooks
uv sync && uv run pre-commit install
```

Step 2: Prompt to "de-template":

```markdown
This repo is a template; help me make it my own.

Rename package from `uv_package_template` to `my_project` everywhere:
- the `src/uv_package_template/` directory
- `pyproject.toml` (project name + `[project.scripts]`)
- imports and references in `tests/`
- this `README.md` (replace template content with my project's)
- `.claude/CLAUDE.md` (minimal for now)

Once complete, ask me about my new project so at the very least we can do
a one line addition under the title of `.claude/CLAUDE.md`.
```

Step 3 (optional): For querying the official uv docs from your agent with `/ask-docs uv [your question]`, see https://github.com/michellepace/docs-for-ai

## --package vs --app

Initialised with:

```shell
uv init --package --python 3.14 --author-from none
```

`--app` (the default) gives a flat layout with a root `main.py` and **no build system** — uv installs the project's dependencies but not its own code. `--package` makes the code an installed, importable package, which is what's needed the moment a project adds tests or reusable commands.

| What | `--app` (default) | `--package` 🙂 |
| :--- | :--- | :--- |
| Layout | flat (`main.py` in root) | `src/<pkg>/__init__.py` |
| `[build-system]` | none | `uv_build` backend |
| Code installed into `.venv`? | no (deps only) | yes (editable) |
| `import <pkg>` resolves | only from cwd | anywhere (proper package) |
| `[project.scripts]` named commands | no (needs a build system) | yes (`uv run <command>`) |
| `src/` + `tests/` layout | no | yes |
| Good for | quick scripts, throwaway apps | tested projects, CLIs, anything reused |
