# Context Engineering Patterns for Claude Code

## Overview
Context engineering in Claude Code involves strategic management of information available to the AI assistant through files, configurations, and memory systems.

## Core Context Management Patterns

### 1. Hierarchical Context Architecture

**Pattern**: Structure context in layers from global to specific.

**Implementation**:
```
~/.claude/                    # Global context
├── CLAUDE.md                # User-wide preferences
├── settings.json            # Global configuration
└── commands/                # Shared commands

/project/
├── CLAUDE.md                # Project context
├── CLAUDE.local.md          # Local overrides
└── .claude/
    ├── settings.json        # Project settings
    ├── settings.local.json  # Personal settings
    └── commands/            # Project commands
```

**Resolution Order**: Local > Project > Global

### 2. Context Window Optimization

**Pattern**: Minimize context size while maximizing relevance.

**Strategies**:
1. **Selective Loading**: Only load files mentioned in conversation
2. **Summary Documents**: Create condensed versions of large docs
3. **Reference Pointers**: Link to detailed docs rather than include
4. **Context Pruning**: Remove outdated information regularly

**Example**:
```markdown
## API Reference
- Full docs: docs/api/README.md
- Quick reference:
  - GET /users - List users
  - POST /users - Create user  
  - GET /users/:id - Get user
  - PUT /users/:id - Update user
```

### 3. Memory Persistence Patterns

**Pattern**: Maintain context across sessions using various storage mechanisms.

**ClaudeFlow Approach**:
```bash
.session/
├── memory-bank.md           # Accumulated knowledge
├── project-state.json       # Current state
└── phase-history/          # Phase completions
```

**Command Pattern**:
```markdown
/memory - Save current context
/recall - Load previous context
```

### 4. Dynamic Context Loading

**Pattern**: Load context based on current task requirements.

**Implementation** (from Claude CMD):
```javascript
// Conditional context loading
if (task.includes('database')) {
  loadContext('database-schemas.md');
  loadContext('migration-guide.md');
}

if (task.includes('frontend')) {
  loadContext('component-library.md');
  loadContext('styling-guide.md');
}
```

### 5. Contextual Hooks

**Pattern**: Use hooks to inject context at specific events.

**Example** (from My Claude Code Setup):
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "type": "command",
        "command": "cat $CLAUDE_PROJECT_DIR/.claude/context/current-sprint.md"
      }
    ]
  }
}
```

### 6. Component-Based Context

**Pattern**: Organize reusable context modules.

**Structure**:
```
.claude/components/
├── error-handling.md        # Error patterns
├── testing-strategy.md      # Test approaches
├── security-checks.md       # Security guidelines
└── performance-tips.md      # Optimization rules
```

**Usage in CLAUDE.md**:
```markdown
## Active Components
@import components/error-handling.md
@import components/security-checks.md
```

### 7. Context Versioning

**Pattern**: Track context changes over time.

**Git Integration**:
```bash
# Track CLAUDE.md changes
git add CLAUDE.md
git commit -m "context: add database migration notes"

# Review context history
git log --oneline -- CLAUDE.md
```

### 8. Scope-Based Context

**Pattern**: Different contexts for different scopes of work.

**MCP Configuration Example**:
```json
{
  "mcpServers": {
    "development": {
      "context": ["dev-setup.md", "local-services.md"]
    },
    "production": {
      "context": ["prod-deploy.md", "monitoring.md"]
    }
  }
}
```

## Advanced Context Patterns

### 1. Context Chaining

**Pattern**: Link contexts to create comprehensive understanding.

```markdown
## Context Chain
1. project-overview.md
   → 2. architecture-decisions.md
      → 3. implementation-details.md
         → 4. current-tasks.md
```

### 2. Contextual Templates

**Pattern**: Reusable context templates for common scenarios.

```markdown
## Bug Fix Context Template
- Problem: [description]
- Error message: [exact error]
- Expected behavior: [what should happen]
- Current behavior: [what happens]
- Relevant files: [list files]
- Previous attempts: [what was tried]
```

### 3. Just-In-Time Context

**Pattern**: Load context only when needed.

```markdown
## Lazy Loading Rules
- Database schemas: Load when querying
- API docs: Load when implementing endpoints
- Test patterns: Load when writing tests
- Security rules: Always loaded
```

### 4. Context Inheritance

**Pattern**: Child contexts inherit and override parent contexts.

```
/app/
├── CLAUDE.md (base rules)
└── modules/
    ├── auth/
    │   └── CLAUDE.md (auth + base rules)
    └── payments/
        └── CLAUDE.md (payments + base rules)
```

## Context Anti-Patterns

### 1. Context Explosion
❌ Loading entire codebase into context
✅ Load only relevant files

### 2. Stale Context
❌ Outdated documentation in CLAUDE.md
✅ Regular context maintenance

### 3. Context Conflicts
❌ Contradicting instructions in different files
✅ Clear precedence rules

### 4. Hidden Context
❌ Important context buried in deep folders
✅ Clear context organization

## Measurement and Optimization

### Context Metrics
- **Size**: Track total context tokens
- **Relevance**: Monitor context hit rate
- **Freshness**: Date of last update
- **Usage**: Which contexts are accessed most

### Optimization Techniques

1. **Context Compression**:
```markdown
<!-- Before: 50 tokens -->
The user authentication system uses JWT tokens with a 24-hour expiration time. Refresh tokens are valid for 30 days.

<!-- After: 20 tokens -->
Auth: JWT (24h) + refresh (30d)
```

2. **Context Caching**:
```javascript
// Cache frequently used contexts
const contextCache = new Map();
contextCache.set('common-patterns', loadContext('patterns.md'));
```

## Real-World Examples

### From Awesome Claude Code
- Curated command collections as context modules
- Hook-based context injection
- Community-shared context patterns

### From Claude Hub
- Webhook-triggered context updates
- Event-specific context loading
- Cross-repository context sharing

### From Claude Code Router
- Model-specific context routing
- Performance-based context selection
- Dynamic context transformation

## Best Practices Summary

1. **Structure**: Use hierarchical organization
2. **Size**: Keep contexts concise and relevant
3. **Maintenance**: Regular updates and pruning
4. **Sharing**: Version control for team contexts
5. **Loading**: Just-in-time and conditional
6. **Persistence**: Multiple storage strategies
7. **Modularity**: Reusable context components
8. **Monitoring**: Track context effectiveness

## Conclusion

Effective context engineering in Claude Code requires:
- Strategic organization and hierarchy
- Dynamic loading based on needs
- Regular maintenance and updates
- Balance between completeness and efficiency
- Clear inheritance and precedence rules

The goal is to provide Claude with exactly the information needed for the current task, no more, no less.