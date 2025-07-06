# /commit - Intelligent Git Operations

**Purpose**: Streamline git operations with automatic staging, conventional commits, and release management.

## When to Use

Use `/commit` for:
- Creating well-formatted commits
- Automated staging of changes
- Release version management
- Batch commit operations
- PR creation and management

## Core Features

### Smart Staging
```bash
/commit "Add user authentication"

# Automatically:
- Runs git status
- Stages relevant files
- Excludes test/temp files
- Validates changes
- Creates commit
```

### Conventional Commits
```bash
# Automatic type detection
/commit "Add login endpoint"
→ feat: add login endpoint

/commit "Fix memory leak" 
→ fix: resolve memory leak in worker process

/commit "Update API docs"
→ docs: update API documentation

/commit "Refactor auth service"
→ refactor: improve auth service structure
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting)
- `refactor`: Code restructure
- `perf`: Performance improvement
- `test`: Test additions/changes
- `build`: Build system changes
- `ci`: CI configuration
- `chore`: Maintenance tasks
- `revert`: Revert previous commit

## Advanced Options

### Scoped Commits
```bash
/commit "Update user model" --scope api
→ feat(api): update user model

/commit "Fix auth bug" --scope security
→ fix(security): resolve auth bypass vulnerability
```

### Breaking Changes
```bash
/commit "Change API response format" --breaking
→ feat!: change API response format

BREAKING CHANGE: API responses now use camelCase
```

### Multi-line Commits
```bash
/commit "Implement caching layer" --body "
- Add Redis integration
- Implement cache invalidation
- Add performance metrics
"
```

## Release Management

### Version Bumping
```bash
# Semantic versioning
/commit --release patch  # 1.2.3 → 1.2.4
/commit --release minor  # 1.2.3 → 1.3.0
/commit --release major  # 1.2.3 → 2.0.0

# With changelog
/commit --release minor --changelog
```

### Release Process
```python
# Automated release workflow
1. Update version in package.json/pyproject.toml
2. Generate CHANGELOG.md
3. Create git tag
4. Push tag and commits
5. Create GitHub release
6. Trigger CI/CD deployment
```

## PR Integration

### Create PR
```bash
/commit --pr "Feature: Add OAuth support"

# Creates:
- Commits all changes
- Pushes to feature branch
- Opens PR with template
- Links to issues
- Requests reviewers
```

### PR Template
```markdown
## Summary
Brief description of changes

## Type of Change
- [ ] Bug fix
- [x] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [x] Code follows style guidelines
- [x] Self-review completed
- [x] Documentation updated
- [x] No new warnings
```

## Workflow Integration

### Feature Development
```bash
# Complete feature workflow
/commit "Initial auth implementation"
/commit "Add tests for auth service"
/commit "Update documentation"
/commit --pr "Feature: Authentication system"
```

### Hotfix Flow
```bash
# Emergency fix workflow
git checkout -b hotfix/security-patch
/commit "Fix security vulnerability" --scope security
/commit --release patch --changelog
/commit --pr "Hotfix: Security patch" --urgent
```

### Batch Operations
```bash
# Stage and commit multiple logical changes
/commit --batch
→ Analyzing changes...
→ Suggested commits:
  1. feat: add user profile endpoint
  2. test: add profile endpoint tests
  3. docs: update API documentation
→ Proceed? [Y/n]
```

## Quality Checks

### Pre-commit Validation
```bash
# Runs before committing
- Linting (ruff, eslint)
- Type checking (mypy, tsc)
- Test execution
- Security scanning
- Commit message format
```

### Automatic Fixes
```python
# Auto-fix common issues
- Code formatting
- Import sorting
- Trailing whitespace
- Line endings
- File permissions
```

## Git Best Practices

### Atomic Commits
```bash
# One logical change per commit
Bad:  "Update code"
Good: "Fix null pointer in user service"

Bad:  "Various changes"
Good: "Refactor auth to use dependency injection"
```

### Commit Message Rules
1. **Present tense** ("add" not "added")
2. **Imperative mood** ("fix" not "fixes")
3. **No period** at end of subject
4. **50 char limit** for subject
5. **Blank line** before body
6. **72 char wrap** for body

### Interactive Rebase
```bash
# Clean up commit history
/commit --interactive 5
→ Shows last 5 commits
→ Options: squash, reword, drop
→ Maintains clean history
```

## CI/CD Integration

### Automated Triggers
```yaml
# Commit patterns trigger actions
on:
  push:
    branches: [main]
    paths:
      - 'src/**'
      - 'tests/**'
      
# Release tags trigger deployment
on:
  push:
    tags:
      - 'v*'
```

### Status Checks
```bash
# Enforce before merge
- All tests passing
- Code coverage >90%
- No security vulnerabilities
- Documentation updated
- PR approved
```

## Examples

### Simple Commit
```bash
/commit "Add email validation"
→ feat: add email validation
```

### Complex Feature
```bash
/commit "Implement payment processing" --scope payments --body "
- Integrate Stripe API
- Add webhook handling  
- Implement retry logic
- Add comprehensive tests

Closes #123, #124
"
```

### Release
```bash
/commit --release minor --message "Version 2.1.0 - Payment features"
→ Updates version
→ Generates changelog
→ Creates tag v2.1.0
→ Pushes everything
```

## Token Optimization
- Focus on git best practices
- Minimal command examples
- Clear workflow patterns
- Max 8k tokens per operation