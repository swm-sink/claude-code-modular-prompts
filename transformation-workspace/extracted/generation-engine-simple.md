# Command Generation - Claude Native Implementation
# Extracted from 358-line YAML → 40-line prompt template
# Web Validated: 2025-01-09

## Generate Project-Specific Commands

### Simple Generation Process

```markdown
## Step 1: Analyze What We Discovered

From consultation, we learned:
- Tech Stack: [from package.json/requirements.txt]
- Architecture: [from code structure analysis]
- Patterns: [from grep searches]
- Domain: [from model/entity analysis]

## Step 2: Generate Commands Based on Patterns

For each discovered pattern, create a command:

### Example for React Project:
/component-create → Based on finding "components/" directory
/hook-generate → Based on finding custom hooks pattern
/test-component → Based on Jest/RTL in package.json

### Example for Python API:
/endpoint-create → Based on finding FastAPI/Flask routes
/model-generate → Based on SQLAlchemy/Pydantic models
/test-api → Based on pytest configuration

### Example for Node Backend:
/service-create → Based on service layer pattern
/migration-generate → Based on database migrations
/seed-database → Based on seed scripts found

## Step 3: Command Template Structure

Each generated command follows this pattern:

```yaml
---
name: [domain-specific-name]
description: [what it does for THIS project]
usage: "/[name] [specific-args]"
allowed-tools: [Read, Write, Edit, Bash]
---

# [Command Name] - Generated for [Project Name]

This command was generated based on discovering:
- Pattern: [what we found]
- Location: [where we found it]
- Convention: [project's specific approach]

## How to use:
[Project-specific instructions]

## Implementation:
[Direct Claude tool usage, no scripts]
```

## Step 4: Validation Before Generation

Check each command:
1. Does it match a real pattern we found?
2. Will it work with project's actual structure?
3. Does it follow project's conventions?
4. Is it actually useful (not just generic)?
```

### Key Simplifications from Original YAML

1. **From**: Complex pipeline with 5 components
   **To**: Simple 4-step process using Claude's intelligence

2. **From**: Abstract pattern matching algorithms
   **To**: Direct analysis of actual code

3. **From**: Template inheritance and preprocessing
   **To**: Simple markdown with YAML frontmatter

4. **From**: Multi-stage validation pipeline
   **To**: Quick checklist validation

5. **From**: 358 lines of configuration
   **To**: 40 lines of actionable process

### Storage of Generated Commands

```bash
# Simple file structure:
outputs/
└── generated-commands/
    ├── component-create.md    # React component generator
    ├── endpoint-create.md     # API endpoint generator
    ├── test-generate.md       # Test file generator
    └── [project-specific].md  # Based on discoveries
```

This approach generates REAL, WORKING commands based on ACTUAL project analysis, not theoretical patterns.