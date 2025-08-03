# Claude Code Best Practices Synthesis

## Overview
This document synthesizes best practices from 15+ verified Claude Code sources, providing actionable guidance for effective usage.

## 1. Project Setup Best Practices

### Initial Configuration
```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Configure API key
claude config set -g apiKey YOUR_API_KEY

# Set preferred model
claude config set -g model claude-sonnet-4

# Verify installation
claude /doctor
```

### Directory Structure
```
project/
├── CLAUDE.md                    # Project context (git-tracked)
├── CLAUDE.local.md             # Personal overrides (gitignored)
└── .claude/
    ├── settings.json           # Project settings
    ├── settings.local.json     # Personal settings
    ├── commands/               # Custom commands
    └── hooks/                  # Automation scripts
```

## 2. CLAUDE.md Best Practices

### Structure Template
```markdown
# Project Name

## Quick Reference
- Build: `npm run build`
- Test: `npm run test:unit`
- Deploy: `npm run deploy:staging`

## Code Standards
- TypeScript with strict mode
- 2-space indentation
- Functional components preferred
- Tests required for new features

## Project Specifics
- API uses JWT auth (24hr expiry)
- Database migrations in db/migrations/
- Environment vars in .env.example

## Known Issues
- Hot reload broken on Windows
- Test DB needs manual reset after failed migrations
```

### Key Principles
1. **Concise**: 200-500 tokens optimal
2. **Specific**: Project-specific info only
3. **Current**: Regular updates
4. **Actionable**: Clear instructions

### Dynamic Updates
- Press `#` to add new instructions
- Ask Claude to update CLAUDE.md
- Commit changes for team benefit

## 3. Tool Usage Best Practices

### Tool Selection Matrix
| Task | Recommended Tool | Why |
|------|-----------------|-----|
| Find specific file | Read | Direct access |
| Search by pattern | Glob | Efficient matching |
| Search content | Grep | Full-text search |
| Multiple edits | MultiEdit | Atomic changes |
| System commands | Bash | Native execution |
| Complex search | Task | Multi-round capability |

### Performance Optimization
```python
# Good: Parallel execution
results = parallel([
    Read("file1.js"),
    Read("file2.js"),
    Grep("pattern", "src/")
])

# Bad: Sequential execution
r1 = Read("file1.js")
r2 = Read("file2.js")
r3 = Grep("pattern", "src/")
```

### TodoWrite Usage
- Use for tasks with 3+ steps
- One task in_progress at a time
- Update immediately after completion
- Keep descriptions concise

## 4. Command Design Best Practices

### Effective Command Structure
```markdown
---
name: /feature-build
description: Build new feature with tests
usage: /feature-build <name> [--skip-tests]
tools: Read, Write, Edit, MultiEdit, Bash, TodoWrite
---

1. Create feature structure
2. Implement core logic
3. Write unit tests
4. Update documentation
5. Run quality checks
```

### Command Categories
1. **Daily Use**: test, build, lint
2. **Development**: generate, refactor
3. **Maintenance**: cleanup, update
4. **Deployment**: deploy, rollback

### Mode-Based Design
```markdown
/test unit        # Run unit tests
/test integration # Run integration tests
/test coverage    # Generate coverage
/test all        # Run everything
```

## 5. Workflow Best Practices

### Planning Before Execution
1. Assess task complexity
2. Break into milestones
3. Define quality gates
4. Plan error recovery
5. Execute incrementally

### Quality Gates
```bash
# After each milestone
npm run lint
npm run typecheck  
npm run test
npm run build
```

### State Management
- Use ClaudeFlow for multi-phase projects
- Save context with `/memory`
- Restore with `/recall`
- Document decisions in commits

## 6. Context Engineering Best Practices

### Hierarchical Loading
```
Global context → Project context → Local context
~/.claude/     → /project/.claude/ → Current directory
```

### Context Optimization
1. Load only what's needed
2. Summarize large documents
3. Use references for details
4. Prune stale information
5. Monitor token usage

### Effective Hooks
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "command": "npm run lint:fix"
    }]
  }
}
```

## 7. Security Best Practices

### Tool Permissions
```json
{
  "tools": {
    "allowedTools": ["Read", "Write", "Edit"],
    "blockedTools": ["Bash"],
    "requireConfirmation": ["Write", "MultiEdit"]
  }
}
```

### Sensitive Data
- Never commit API keys
- Use environment variables
- Sanitize logs
- Review Claude's outputs

## 8. Team Collaboration Best Practices

### Shared Knowledge
1. Document patterns in CLAUDE.md
2. Share commands via git
3. Create team conventions
4. Regular context updates

### Git Integration
```bash
# Workflow commands
/git-feature "user-auth"      # Create feature branch
/git-commit "feat: add login" # Commit with convention
/git-pr "Add user auth"       # Create pull request
```

## 9. Performance Best Practices

### Response Time
- Batch operations
- Limit search scope
- Cache frequent reads
- Use specific file types

### Token Usage
- Concise CLAUDE.md
- Targeted file reads
- Efficient prompts
- Regular cleanup

## 10. Error Handling Best Practices

### Graceful Failures
```python
try:
    execute_task()
except ToolError as e:
    diagnose_issue(e)
    attempt_recovery()
    log_for_human_review()
```

### Recovery Strategies
1. Validate before execution
2. Create backups
3. Implement rollbacks
4. Log detailed context

## 11. Common Pitfalls to Avoid

### Documentation
❌ Verbose CLAUDE.md files
✅ Concise, specific instructions

### Tool Usage
❌ Reading entire codebases
✅ Targeted, specific reads

### Commands
❌ Monolithic do-everything commands
✅ Focused, composable commands

### Workflows
❌ Black-box automation
✅ Transparent, trackable progress

## 12. Integration Best Practices

### IDE Integration
- VS Code: Claude Code extension
- Cursor: Native support
- Terminal: Direct CLI usage

### CI/CD Integration
- GitHub Actions: claude-code-action
- Hooks: Pre-commit validation
- Automation: Scheduled tasks

## Quick Reference Card

### Essential Commands
```bash
claude                  # Interactive mode
claude -p "query"       # One-shot query
claude -c              # Continue session
claude commit          # Smart commit
/clear                 # Clear history
/help                  # Show commands
```

### Key Shortcuts
- `#` - Add to CLAUDE.md
- `/` - Show commands
- `Tab` - Autocomplete

### Performance Tips
1. Batch related operations
2. Use mode-based commands
3. Keep context focused
4. Update patterns regularly

## Conclusion

Successful Claude Code usage combines:
- Strategic context management
- Efficient tool usage
- Well-designed commands
- Clear workflows
- Team collaboration
- Continuous improvement

The key is treating Claude Code as a powerful development partner that thrives on clear context and well-defined patterns.