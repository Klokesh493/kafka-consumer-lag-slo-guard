# Development and security

## Local setup

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
make check PYTHON=python
```

| Tool | Purpose |
| --- | --- |
| Python | Runs the application and its verification helpers. |
| venv and pip | Isolate and install the pinned developer tools. |
| Make | Runs project verification, lint, and the security gate. |
| Ruff | Detects import errors, undefined names, and selected syntax issues. |
| Bandit | Fails the security target on medium-or-higher severity and confidence findings. |
| Git | Review the diff before committing changes. |
| unittest | Runs the checked-in regression tests through `make verify`. |
| Replay runner | Compares observed sample output with the checked-in baseline. |
| Docker | Packages the documented demo. Follow the README container steps. |

## Review and release

Run `make check` before merging changes. Review behavior changes using the sample and expected output.
The [GitHub Actions template](github-actions/ci.yml) contains the same gate. It is stored under docs and requires workflow-enabled credentials to activate.

Use synthetic input for published demos. Review lower severity Bandit findings with `python -m bandit -r . -x ./.venv,./.git`.
The static scan covers Python code. Container images, running services, and cloud permissions require separate checks.
