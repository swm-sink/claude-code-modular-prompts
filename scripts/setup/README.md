# Setup Scripts

User setup utilities for initial framework configuration and environment preparation.

## Scripts

### `setup_precommit.sh`
**Purpose**: Configure pre-commit hooks for framework validation

**Features**:
- Installs pre-commit if not already installed
- Configures git hooks for automatic validation
- Tests hook setup on all files
- Provides emergency bypass instructions

**Usage**:
```bash
bash scripts/setup/setup_precommit.sh
```

**What it sets up**:
- Framework validation (runs on every commit)
- Framework tests (runs when .py or .md files change)
- Python formatting with Black
- Python linting with Ruff
- YAML validation
- File size limits

**Emergency bypass**: Use `git commit --no-verify` to skip hooks if needed.

## Requirements

- Git repository
- Python 3.8+
- pip package manager

## Notes

- Run from project root directory
- Hooks will automatically validate all commits
- Setup is idempotent - safe to run multiple times