# Contributing to OracleTrace

Thanks for your interest in contributing to OracleTrace.

OracleTrace is focused on practical Python performance regression detection: lightweight tracing, clear comparison output, and useful CLI workflows.

Contributions are welcome for:

* Performance regression detection improvements
* Trace comparison quality
* CLI usability
* Output clarity and visualization
* Documentation and examples

---

## Before You Start

* Read [README.md](README.md)
* Check docs under [docs/docs](docs/docs)
* Browse open issues, especially good first issues:
  https://github.com/KaykCaputo/oracletrace/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22

---

## Development Setup

### 1. Clone your fork

```bash
git clone https://github.com/<your-user>/oracletrace.git
cd oracletrace
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install in editable mode

```bash
pip install -e .
```

### 4. Verify CLI

```bash
oracletrace --help
```

---

## Project Structure

* [oracletrace/cli.py](oracletrace/cli.py): CLI arguments and command flow
* [oracletrace/tracer.py](oracletrace/tracer.py): tracing engine and output rendering
* [oracletrace/compare.py](oracletrace/compare.py): baseline vs current comparison logic
* [docs/docs](docs/docs): documentation pages
* [docs/mkdocs.yml](docs/mkdocs.yml): docs configuration

---

## Contribution Workflow

### 1. Create a branch

```bash
git checkout -b feature/short-description
```

### 2. Make focused changes

Keep PRs small and scoped to one clear objective.

### 3. Validate locally

Run the checks in the Validation section.

### 4. Commit and push

Use clear commit messages and push your branch.

### 5. Open a Pull Request

Explain the motivation, what changed, and expected impact.

---

## Coding Guidelines

* Prefer simple, readable solutions over complex abstractions
* Keep behavior changes explicit and documented
* Preserve existing CLI behavior unless the PR is intentionally changing it
* Follow existing style and naming patterns
* Avoid new dependencies unless clearly justified

---

## Validation

This repository currently has no automated test suite, so manual validation is important.

### CLI smoke check

```bash
oracletrace --help
```

### Functional trace run

```bash
oracletrace your_script.py
```

### JSON export and compare flow

```bash
oracletrace your_script.py --json baseline.json
oracletrace your_script.py --json current.json --compare baseline.json
```

### Docs build (if docs changed)

```bash
mkdocs build -f docs/mkdocs.yml
```

---

## Documentation Contributions

If your PR changes flags, behavior, output format, or workflows:

* Update the relevant page in [docs/docs](docs/docs)
* Keep examples executable and aligned with real CLI behavior
* Ensure docs build succeeds

---

## Bug Reports and Feature Requests

When opening an issue, include:

* Expected behavior
* Actual behavior
* Steps to reproduce
* Python version
* OS/environment details
* Sample commands and output (if applicable)

---

## Pull Request Tips

* Keep PRs small and focused
* Link related issues (for example: Closes #123)
* Add before/after output snippets when changing CLI behavior
* Highlight any backward-incompatible changes

---

## Questions

If anything is unclear, open an issue.

Discussion is welcome and encouraged.
