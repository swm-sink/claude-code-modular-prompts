# Command Design Patterns for Claude Code

## Overview
Slash commands in Claude Code enable reusable, parameterized workflows. Effective command design improves productivity and maintains consistency across projects.

## Command Structure Fundamentals

### Basic Command Template
```markdown
---
name: /command-name
description: Brief description of what the command does
usage: /command-name [required] <optional>
tools: Read, Write, Edit, Bash
---

# Command implementation details
1. Step one
2. Step two
3. Step three
```

### Command Location Hierarchy
```
~/.claude/commands/          # Global commands
/project/.claude/commands/   # Project commands
/project/module/.claude/     # Module-specific
```

## Core Design Patterns

### 1. Mode-Based Commands

**Pattern**: Consolidate related functionality into a single command with modes.

**Example**:
```markdown
---
name: /test
description: Run various types of tests
usage: /test <mode> [options]
modes:
  - unit: Run unit tests
  - integration: Run integration tests  
  - coverage: Generate coverage report
  - watch: Run tests in watch mode
---

Based on mode:
- unit: `npm run test:unit [options]`
- integration: `npm run test:integration`
- coverage: `npm run test:coverage`
- watch: `npm run test:watch`
```

**Benefits**:
- Reduces command proliferation
- Intuitive organization
- Flexible parameter handling

### 2. Workflow Commands

**Pattern**: Encapsulate multi-step processes into single commands.

**Example** (from My Claude Code Setup):
```markdown
---
name: /security-audit
description: Comprehensive security analysis
tools: Read, Grep, Bash, Write
---

1. Static code analysis
   - Run semgrep rules
   - Check for hardcoded secrets
   
2. Dependency audit
   - Check for known vulnerabilities
   - Review licenses
   
3. Configuration review
   - Validate security headers
   - Check CORS settings
   
4. Generate report
   - Summarize findings
   - Prioritize by severity
```

### 3. Generator Commands

**Pattern**: Create boilerplate code or project structures.

```markdown
---
name: /generate
description: Generate code structures
usage: /generate <type> <name> [options]
types:
  - component: React component
  - api: REST API endpoint
  - test: Test file
  - migration: Database migration
---

For component generation:
1. Create component file
2. Create test file
3. Create styles file
4. Update index exports
```

### 4. Analysis Commands

**Pattern**: Provide insights about code or project state.

```markdown
---
name: /analyze-complexity
description: Analyze code complexity
tools: Read, Grep, Bash
---

1. Find all JavaScript/TypeScript files
2. Calculate cyclomatic complexity
3. Identify files exceeding threshold
4. Generate complexity report
5. Suggest refactoring targets
```

### 5. Maintenance Commands

**Pattern**: Automate routine maintenance tasks.

**Example** (from tutorials):
```markdown
---
name: /cleanup-context
description: Optimize documentation token usage
tools: Read, Write, Edit
---

1. Analyze CLAUDE.md size
2. Identify redundant information
3. Compress verbose sections
4. Archive outdated content
5. Update with concise versions
```

### 6. Integration Commands

**Pattern**: Connect with external services or tools.

```markdown
---
name: /deploy
description: Deploy to various environments
usage: /deploy <env> [--dry-run]
environments:
  - staging: Deploy to staging
  - production: Deploy to production
  - preview: Create preview deployment
---

Pre-deployment checks:
1. Run tests
2. Check build status
3. Validate environment variables

Deployment steps:
1. Build application
2. Push to registry
3. Update infrastructure
4. Run smoke tests
```

### 7. Diagnostic Commands

**Pattern**: Help troubleshoot issues.

```markdown
---
name: /diagnose
description: Diagnose common issues
tools: Bash, Read, Grep
---

System checks:
- Node version
- Dependencies installed
- Environment variables set
- Services running
- Port availability

Generate diagnostic report with findings
```

## Advanced Command Patterns

### 1. Parameterized Commands

**Pattern**: Accept and validate parameters.

```markdown
---
name: /create-pr
description: Create pull request with validation
usage: /create-pr <branch> <title> [--draft]
validation:
  - branch: Must follow naming convention
  - title: Must be <72 characters
---

1. Validate branch exists
2. Check for uncommitted changes
3. Run tests
4. Create PR with template
5. Add reviewers based on CODEOWNERS
```

### 2. Conditional Execution

**Pattern**: Adapt behavior based on context.

```markdown
---
name: /setup
description: Project setup based on environment
---

Detect environment:
- If new clone: Full setup
- If existing: Update dependencies
- If CI: Minimal setup

Execute appropriate setup steps
```

### 3. Command Composition

**Pattern**: Build complex commands from simpler ones.

```markdown
---
name: /release
description: Full release workflow
composes:
  - /test all
  - /build production
  - /generate changelog
  - /deploy production
  - /notify team
---
```

### 4. Interactive Commands

**Pattern**: Gather input during execution.

```markdown
---
name: /refactor-code
description: Interactive refactoring assistant
---

1. Ask: Which files to refactor?
2. Analyze current structure
3. Suggest refactoring options
4. Ask: Which approach to use?
5. Implement chosen refactoring
6. Run tests to verify
```

## Command Organization Strategies

### By Function
```
commands/
├── development/
│   ├── test.md
│   ├── build.md
│   └── debug.md
├── deployment/
│   ├── deploy.md
│   └── rollback.md
└── maintenance/
    ├── cleanup.md
    └── update.md
```

### By Frequency
```
commands/
├── daily/         # Frequently used
├── weekly/        # Regular maintenance
├── occasional/    # Special purposes
└── emergency/     # Crisis management
```

### By Complexity
```
commands/
├── simple/        # Single-step commands
├── workflows/     # Multi-step processes
└── advanced/      # Complex operations
```

## Best Practices

### 1. Naming Conventions
- Use descriptive verb-noun format
- Keep names concise but clear
- Avoid abbreviations
- Use consistent terminology

### 2. Documentation
- Clear description
- Usage examples
- Required tools
- Expected outcomes
- Error scenarios

### 3. Error Handling
```markdown
Error scenarios:
- Missing dependencies: Install first
- Invalid parameters: Show usage
- Failed steps: Rollback changes
- Permissions: Request elevation
```

### 4. Progress Feedback
```markdown
Steps with status:
- [✓] Analyzing code
- [✓] Running tests
- [→] Building application
- [ ] Deploying
```

### 5. Idempotency
Commands should be safe to run multiple times without side effects.

## Anti-Patterns to Avoid

### 1. Command Sprawl
❌ Separate command for every variation
✅ Mode-based commands with parameters

### 2. Hidden Dependencies
❌ Assuming tools/files exist
✅ Explicit checks and setup

### 3. Unclear Purpose
❌ Vague command names like `/process`
✅ Specific names like `/process-images`

### 4. No Validation
❌ Accepting any input
✅ Parameter validation and sanitization

## Real-World Examples

### From Claude CMD
- 184+ curated commands
- Dynamic loading system
- Version management
- Security profiles

### From My Claude Code Setup
- Security-focused commands
- Token optimization
- Subagent integration
- MCP server commands

### From Awesome Claude Code
- Community-contributed commands
- Categorized collections
- Best practice examples
- Innovation showcase

## Command Testing

### Test Template
```markdown
---
name: /test-command
test:
  - input: "/command arg1 arg2"
    expect: "Success message"
  - input: "/command --invalid"
    expect: "Error: Invalid argument"
---
```

### Validation Checklist
- [ ] Clear purpose and description
- [ ] Proper parameter handling
- [ ] Error scenarios covered
- [ ] Tools correctly specified
- [ ] Idempotent execution
- [ ] Progress feedback
- [ ] Documentation complete

## Conclusion

Effective command design in Claude Code requires:
- Clear purpose and naming
- Thoughtful parameter design
- Comprehensive error handling
- Mode-based consolidation
- Proper documentation
- Regular maintenance

Well-designed commands become powerful productivity multipliers for development teams.