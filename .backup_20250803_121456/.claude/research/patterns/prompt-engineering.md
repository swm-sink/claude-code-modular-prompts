# Prompt Engineering Patterns for Claude Code

## Overview
Patterns extracted from 15+ verified Claude Code implementations focusing on effective prompt design and system configuration.

## Core Patterns

### 1. CLAUDE.md as System Prompt Extension

**Pattern**: Use CLAUDE.md files as persistent, project-specific system prompts that are automatically loaded into context.

**Implementation**:
```markdown
# Project: Authentication Service

## Commands
- npm run test:auth - Run authentication tests only
- npm run build:prod - Production build with optimizations

## Code Style
- Use async/await over promises
- Prefer functional components
- Error messages must be user-friendly

## Gotchas
- The auth service requires Redis to be running
- Test data is reset every hour in staging
```

**Benefits**:
- Persistent context across sessions
- Team knowledge sharing via git
- Reduced token usage vs repeating instructions

### 2. Hierarchical Context Loading

**Pattern**: Layer context from general to specific using multiple CLAUDE.md files.

**Structure**:
```
/workspace/
├── CLAUDE.md              # General project rules
├── CLAUDE.local.md        # Personal preferences (gitignored)
└── backend/
    └── CLAUDE.md          # Backend-specific rules
```

**Loading Order**: Most specific wins (backend > workspace > global)

### 3. Dynamic Memory Building

**Pattern**: Update CLAUDE.md during sessions to capture learnings.

**Methods**:
1. Press `#` to add instruction
2. Ask Claude: "Update CLAUDE.md to remember this"
3. Manual edits between sessions

**Example**:
```bash
# User discovers a quirk
"The test database needs manual reset after failed migrations"

# Claude updates CLAUDE.md
## Known Issues
- Test DB requires manual reset after failed migrations: `npm run db:reset:test`
```

### 4. Token-Conscious Documentation

**Pattern**: Keep CLAUDE.md concise to preserve token budget.

**DO**:
- Use bullet points
- Short, declarative statements
- Focus on non-obvious information
- Group related items

**DON'T**:
- Long explanations
- Redundant information
- Generic best practices
- Verbose descriptions

### 5. Command Chaining Patterns

**Pattern**: Define multi-step workflows as slash commands.

**Example** (from My Claude Code Setup):
```markdown
---
name: /security-audit
steps:
  1. Run static analysis
  2. Check dependencies
  3. Scan for secrets
  4. Generate report
---
```

### 6. Instruction Specificity

**Pattern**: Be explicit about expectations and constraints.

**Examples**:
```markdown
## Testing Requirements
- ALWAYS run tests before committing
- Use `npm run test:single [file]` not full suite
- Tests must complete in <30 seconds
- Mock external services

## Git Workflow  
- Branch names: feature/[issue-id]-[brief-description]
- Commits: conventional format (feat:, fix:, chore:)
- PR titles: "[ISSUE-ID] Brief description"
```

### 7. Error Prevention Through Documentation

**Pattern**: Document common pitfalls and their solutions.

```markdown
## Common Errors and Solutions

### "Module not found" errors
- Run: `npm run clean && npm install`
- Check: Node version is 18+

### Database connection timeouts
- Ensure: VPN is connected for remote DB
- Local: `docker-compose up -d postgres`
```

### 8. Tool Usage Hints

**Pattern**: Guide tool selection through CLAUDE.md.

```markdown
## Tool Preferences
- File search: Use Grep with -n flag for line numbers
- Bulk edits: Prefer MultiEdit over multiple Edit calls
- Tests: Read test files before modifying source
- Performance: Batch Read operations when possible
```

## Anti-Patterns to Avoid

### 1. Information Overload
❌ Including entire API documentation
✅ Link to docs with key examples

### 2. Vague Instructions
❌ "Follow best practices"
✅ "Use 2-space indentation, no semicolons"

### 3. Stale Information
❌ Outdated commands that no longer work
✅ Regular CLAUDE.md maintenance

### 4. Personal Preferences in Shared Files
❌ Editor settings in CLAUDE.md
✅ Team conventions only (personal → CLAUDE.local.md)

## Advanced Techniques

### 1. Conditional Instructions
```markdown
## Environment-Specific
- Production: NEVER use console.log
- Development: console.log OK for debugging
- CI: All logs must use Winston logger
```

### 2. Progressive Disclosure
```markdown
## For Simple Tasks
- See: quick-start.md

## For Complex Features
- Architecture: docs/architecture.md
- Patterns: docs/patterns.md
- Examples: examples/
```

### 3. Meta-Instructions
```markdown
## How to Update This File
1. Test the instruction works
2. Add under appropriate section
3. Include example if non-obvious
4. Commit with message: "docs: update CLAUDE.md with [topic]"
```

## Measurement and Optimization

### Token Usage Tracking
- Typical CLAUDE.md: 200-500 tokens
- Optimal range: 300-400 tokens
- Monitor with `claude config token-usage`

### Effectiveness Metrics
- Reduced repeated questions
- Fewer correction cycles
- Faster task completion
- Team consistency

## Real-World Examples

### From ClaudeFlow:
- Separates planning (`/plan`) from execution (`/act`)
- Uses memory commands for state persistence
- Clear phase documentation

### From Claude Task Workflow:
- Complexity scoring in prompts
- Milestone-based instructions
- Quality gate specifications

### From My Claude Code Setup:
- Security-first prompting
- Token optimization commands
- Subagent instruction patterns

## Conclusion

Effective prompt engineering in Claude Code centers on:
1. Persistent context via CLAUDE.md
2. Concise, specific instructions
3. Dynamic learning and updates
4. Token budget awareness
5. Team knowledge sharing

The most successful implementations treat CLAUDE.md as a living document that evolves with the project.