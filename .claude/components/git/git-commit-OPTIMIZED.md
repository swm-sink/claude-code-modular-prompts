# Intelligent Git Commit Management

**Purpose**: Advanced git commit workflow with intelligent message generation, change analysis, and commit organization following conventional commit standards.

**Usage**: 
- Analyzes and classifies changes (feature, fix, docs, refactor, test, chore)
- Groups related changes into atomic commits with logical separation
- Generates conventional commit messages with proper type, scope, and description
- Validates code quality and commit hygiene before committing
- Ensures proper commit structure and references to issues/tickets

**Compatibility**: 
- **Works with**: git-operations, git-merge, all development workflows
- **Requires**: staged_files, change_analysis, conventional_commit_format
- **Conflicts**: None (enhances git workflow)

**Implementation**:
```bash
# Conventional commit format
type(scope): description

# Automated detection
feat(auth): add OAuth2 authentication
fix(api): resolve null pointer exception
docs(readme): update installation steps
```

**Category**: git | **Complexity**: moderate | **Time**: 1 hour