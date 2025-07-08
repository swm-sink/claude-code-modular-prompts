| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-08   | stable |

# Getting Started with Claude Code Framework 3.0

────────────────────────────────────────────────────────────────────────────────

> **30 Second Quickstart**: Copy and paste these commands to start immediately!

```bash
# Not sure what to use? Let the framework decide:
/auto "Add user authentication to my app"

# Quick development task:
/task "Fix the login bug"

# Just researching:
/query "How does the caching work?"

# Creating documentation:
/docs generate "API Guide"
```

> **🚨 Confused about `/docs` vs `/query`?** → [**Command Selection Guide**](COMMAND_SELECTION_GUIDE.md) - 2 minute read!

---

## What is This? (30 seconds)

A **revolutionary Framework 3.0 meta-prompting system** that makes Claude Code smarter through:
- 🎯 **Smart Commands** - TDD-aware intelligent routing
- 🧩 **Modular Prompts** - 100+ reusable components with runtime engine
- 📊 **GitHub Tracking** - Session management with issue integration
- ✅ **Quality Gates** - Universal validation with TDD enforcement
- 🧠 **Meta-Prompting** - Self-improving framework capabilities
- ⚡ **Claude 4 Optimized** - Advanced thinking patterns and parallel execution

**Framework 3.0 Philosophy**: *"Commands delegate, modules implement, meta-prompting evolves."*

---

## Visual Command Flow

```
     Your Request
          │
          ▼
    ┌─────────────┐
    │   /auto     │ ← Start here when unsure!
    └─────┬───────┘
          │ Analyzes & Routes
          ▼
    ┌─────────────────────────────────────────┐
    │            Smart Routing                 │
    ├─────────────┬───────────────┬───────────┤
    ▼             ▼               ▼           ▼
 ┌──────┐    ┌────────┐    ┌─────────┐   ┌───────┐
 │/task │    │/feature│    │ /swarm  │   │/query │
 └──────┘    └────────┘    └─────────┘   └───────┘
  Single      Complete      Multi-Agent    Research
  Component   Feature       Complex Work   Only
    │            │              │             │
    ▼            ▼              ▼             ▼
  Quick Fix   Full PRD      GitHub Issue   Analysis
  With TDD    + MVP         + Tracking     Report
```

---

## The 5 Essential Commands

### 1. `/auto` - The Smart Router
```bash
/auto "I need to add user authentication"
# → Analyzes your need
# → Routes to best command
# → You don't need to think about which tool
```

### 2. `/task` - Focused Development
```bash
/task "Add password validation to the login form"
# → Single component work
# → Enforces TDD (tests first!)
# → Quick and focused
```

### 3. `/feature` - Complete Feature Development
```bash
/feature "Build a shopping cart with checkout"
# → Creates Product Requirements Doc (PRD)
# → Plans MVP strategy
# → Implements systematically
# → Full test coverage
```

### 4. `/swarm` - Complex Multi-Component Work
```bash
/swarm "Migrate from REST to GraphQL"
# → Creates GitHub tracking issue
# → Coordinates specialized agents
# → Handles dependencies
# → Tracks all progress
```

### 5. `/query` - Research Without Changes
```bash
/query "What design patterns are used in the auth system?"
# → Read-only analysis
# → No code modifications
# → Comprehensive report
```

---

## Common Workflows

### "I need to fix a bug" → Use `/task`
```bash
/task "Fix: Users can't reset passwords"
```
**What happens**:
1. Writes failing test for the bug
2. Fixes the code
3. Verifies test passes
4. Ensures no regressions

### "I need a new feature" → Use `/feature`
```bash
/feature "Add two-factor authentication"
```
**What happens**:
1. Creates comprehensive PRD
2. Defines MVP approach
3. Implements with tests
4. Validates everything works

### "I need to understand the code" → Use `/query`
```bash
/query "How does the payment processing work?"
```
**What happens**:
1. Analyzes codebase
2. Maps relationships
3. Explains architecture
4. No changes made

### "I have a complex project" → Use `/swarm`
```bash
/swarm "Build admin dashboard with analytics"
```
**What happens**:
1. Creates GitHub epic issue
2. Breaks into sub-tasks
3. Assigns specialized agents
4. Coordinates everything

---

## Quick Tips

### Let the Framework Guide You
```bash
# When in doubt:
/auto "your request here"

# It figures out what you need!
```

### Working with Permissions
If you see permission errors, one command fixes it:
```bash
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### Finding Help
```bash
/docs "what does swarm do?"
/docs "show TDD examples"
/docs "list all commands"
```

---

## Interactive Examples

### Example 1: Adding Authentication
```bash
# Step 1: Start with auto
/auto "I need users to be able to log in"

# Framework responds: "This looks like a feature. Let me route to /feature..."

# Step 2: It automatically runs
/feature "User authentication with email/password"

# You get:
# - Complete PRD with requirements
# - Security considerations
# - Test suite
# - Working implementation
```

### Example 2: Fixing Performance
```bash
# Step 1: Research first
/query "Which API endpoints are slowest?"

# Step 2: Fix identified issues
/task "Optimize the /api/search endpoint"

# Framework ensures:
# - Performance tests written first
# - Optimization implemented
# - No functionality broken
```

### Example 3: Major Refactor
```bash
# Complex work triggers GitHub tracking
/swarm "Convert monolith to microservices"

# Creates:
# - GitHub epic issue
# - Phase breakdown
# - Progress tracking
# - Coordinated execution
```

---

## Troubleshooting

### "Command not found"
Check your syntax:
```bash
✓ /task "Add login feature"     # Correct
✗ task "Add login feature"      # Missing /
✗ /task Add login feature       # Missing quotes
```

### "Permission denied"
Run the one-line fix:
```bash
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### "Not sure which command"
Always start with:
```bash
/auto "what you want to do"
```

---

## What Makes This Framework Special?

### For You:
- **Less Typing**: Smart commands understand context
- **Better Quality**: TDD and best practices automatic
- **Never Lose Work**: GitHub tracking for complex tasks
- **Fast Learning**: Framework guides you

### Under the Hood:
- **Modular Design**: Each piece does one thing well
- **Claude-Native**: Built for Claude Code's strengths
- **Token-Efficient**: Optimized prompt engineering
- **Real Patterns**: Based on actual development needs

---

## Next Steps

1. **Try it now**: `/auto "your first task"`
2. **Explore commands**: `/docs "list all commands"`
3. **Check examples**: See the Examples section above
4. **Customize**: Create `.claude/settings.local.json`

---

**Remember**: *"The best framework is the one you don't have to think about."*

Start with `/auto` and let the framework handle the complexity! 🚀