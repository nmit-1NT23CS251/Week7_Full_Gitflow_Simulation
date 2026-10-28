# Week 7 — Full Gitflow Simulation

A working Python calculator used to demonstrate the complete **feature → PR → develop → release → main → hotfix** workflow, with pre-commit checks and GitHub Actions CI.

## What's included

- Calculator application with add, subtract, multiply, divide and zero-division validation.
- Pytest unit tests and Ruff linting.
- A Git pre-commit hook that runs lint and tests before each commit.
- GitHub Actions CI to run lint and tests on pushes and PRs.
- A step-by-step Gitflow exercise in [`docs/GITFLOW_COMMANDS.md`](docs/GITFLOW_COMMANDS.md).

## 1. Run on macOS (Terminal)

Open Terminal, then run:

```bash
cd ~/Downloads/Week7_Full_Gitflow_Simulation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
python -m pytest -v
ruff check .
```

**Expected calculator output:**

```text
=== Week 7: Gitflow Calculator ===
12 + 4 = 16
12 - 4 = 8
12 * 4 = 48
12 / 4 = 3.0
```

## 2. Set up Git and the pre-commit hook

Once you are inside the project folder:

```bash
git init -b main
bash scripts/install_hook.sh
git add .
git commit -m "chore: initialize calculator and CI"
```

Before each future commit, the hook automatically runs `ruff check .` and `pytest` and blocks the commit if either fails. Install dependencies first, and keep your virtual environment activated.

**If Git requests your identity:**

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## 3. Perform Gitflow with GitHub

Create a new empty GitHub repo named `Week7_Full_Gitflow_Simulation`. Continue at step **1 (publish main)** in [`docs/GITFLOW_COMMANDS.md`](docs/GITFLOW_COMMANDS.md), but **skip its `git init`, `git add`, and first `git commit` commands** if you already did section 2 above.

The walkthrough guides you through feature, pull request, release and hotfix cycles.

## Project structure

```text
Week7_Full_Gitflow_Simulation/
├── .github/workflows/ci.yml
├── docs/GITFLOW_COMMANDS.md
├── scripts/install_hook.sh
├── scripts/pre-commit
├── src/__init__.py
├── src/calculator.py
├── tests/test_calculator.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Submission checklist

- [ ] GitHub repository URL shared with instructor
- [ ] `main` and `develop` branches created
- [ ] Feature branch PR merged into `develop`
- [ ] Release branch PR merged into `main` and changes synced to `develop`
- [ ] Hotfix branch PR merged into `main` and synced to `develop`
- [ ] GitHub Actions run passes
- [ ] Local pre-commit hook demonstrated
- [ ] `v1.0.0` and `v1.0.1` tags visible

**Note:** This ZIP contains the runnable source and instructions, not a fabricated record of completed GitHub PRs or CI runs. Those must be performed in your own account.
