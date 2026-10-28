# Full Gitflow Simulation — command walkthrough

Run commands from the extracted project folder. The GitHub website steps are described in the README.

## 1. Initialize and publish main

```bash
git init -b main
git add .
git commit -m "chore: initialize calculator and CI"
git remote add origin https://github.com/YOUR_USERNAME/Week7_Full_Gitflow_Simulation.git
git push -u origin main
```

Create an **empty** repository with this name on GitHub first (no generated README/license). If the URL is already configured, skip `git remote add origin`.

## 2. Create develop

```bash
git switch -c develop
git push -u origin develop
```

## 3. Feature branch and PR

```bash
git switch -c feature/percentage
```

Add the following function to `src/calculator.py`:

```python
def percentage(value: float, total: float) -> float:
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (value / total) * 100
```

Add a test to `tests/test_calculator.py`, and include `percentage` in its import:

```python
def test_percentage():
    assert percentage(25, 200) == 12.5
```

Then:

```bash
git add src/calculator.py tests/test_calculator.py
git commit -m "feat: add percentage operation"
git push -u origin feature/percentage
```

On GitHub: open a PR **feature/percentage → develop**, check CI passed, then merge. Back on your Mac:

```bash
git switch develop
git pull origin develop
```

## 4. Release branch and PR

```bash
git switch -c release/v1.0.0
git push -u origin release/v1.0.0
```

On GitHub: open a PR **release/v1.0.0 → main**, review checks, then merge. Also merge release back to **develop** by PR (or merge it locally). Then:

```bash
git switch main
git pull origin main
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0
```

## 5. Hotfix branch and PR

```bash
git switch main
git pull origin main
git switch -c hotfix/rounding
```

Make a small, tested change (for example, add a `round_result(value, digits=2)` helper and test it), then:

```bash
git add .
git commit -m "fix: add result rounding helper"
git push -u origin hotfix/rounding
```

Open PR **hotfix/rounding → main**, merge once CI passes; merge the fix back to **develop** too.

```bash
git switch main
git pull origin main
git tag -a v1.0.1 -m "Hotfix release"
git push origin v1.0.1
```

## 6. Evidence for submission

Capture screenshots of: branch list; merged feature PR; release PR; hotfix PR; passing Actions run; installed hook successfully running on commit; release tags `v1.0.0` and `v1.0.1`.

Check branches and tags with:

```bash
git branch -a
git tag
git log --oneline --graph --decorate --all
```

> GitHub PRs and CI cannot be generated merely by extracting the ZIP. Run the steps on your own GitHub repository to complete the simulation.
