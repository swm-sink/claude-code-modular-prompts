---
name: /config-hierarchy
description: Manage hierarchical configuration system - global, project, and session-level settings
usage: "/config-hierarchy [--show|--set|--get|--sync] [level] [key] [value]"
allowed-tools: [Read, Write, MultiEdit, LS]
---

# 🏗️ Hierarchical Configuration System

Manage Claude Code configuration across three levels: global (user), project (team), and session (temporary). Settings cascade from global to project to session, with more specific levels overriding general ones.

## Configuration Hierarchy

```
~/.claude/CLAUDE.md           # 🌍 Global (User-wide)
    ↓ inherited by
./CLAUDE.md                    # 📁 Project (Team-shared)  
    ↓ inherited by
./.claude/memory.md            # 🧠 Session (Learning)
    ↓ applied to
Claude's Current Context       # 🤖 Active Configuration
```

## Configuration Levels

### 🌍 Global Level (~/.claude/CLAUDE.md)
**Your personal preferences across all projects:**
```yaml
# User preferences that apply everywhere
user_preferences:
  name: "Your Name"
  style:
    indent: "spaces"
    indent_size: 2
    quotes: "single"
    semicolons: false
  
  editor: "vscode"
  
  testing:
    prefer_tdd: true
    coverage_threshold: 80
  
  ai_behavior:
    verbosity: "concise"
    explain_code: true
    suggest_improvements: true
    
  shortcuts:
    cc: "/create-component"
    tc: "/test-component"
```

### 📁 Project Level (./CLAUDE.md)
**Team-shared configuration (git-tracked):**
```yaml
# Project configuration (overrides global)
project_config:
  name: "E-Commerce Platform"
  team: "Frontend Team"
  
  conventions:
    components: "atomic"
    naming: "PascalCase"
    imports: "@/ alias"
    
  requirements:
    testing: "mandatory"
    reviews: 2
    documentation: "required"
    
  tech_stack:
    framework: "Next.js 14"
    language: "TypeScript"
    styling: "Tailwind CSS"
    state: "Zustand"
```

### 🧠 Session Level (./.claude/memory.md)
**Learning and temporary overrides:**
```yaml
# Session-specific learning (git-ignored)
session_memory:
  learned_patterns:
    - "User prefers async/await over promises"
    - "Team uses feature-flag pattern"
    - "Custom error boundary implementation"
    
  recent_context:
    current_feature: "checkout-flow"
    last_component: "PaymentForm"
    active_branch: "feature/payment"
    
  temporary_overrides:
    verbose_mode: true  # Temporary for debugging
    skip_tests: false   # Usually true, false for this session
```

## Configuration Commands

### Show Current Configuration
```bash
/config-hierarchy --show [level]

📋 Configuration Hierarchy:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌍 Global (~/.claude/CLAUDE.md):
  indent: spaces (2)
  testing: prefer_tdd=true
  verbosity: concise
  
📁 Project (./CLAUDE.md): [Overrides]
  components: atomic ✓
  testing: mandatory ✓ (stricter)
  framework: Next.js 14
  
🧠 Session (./.claude/memory.md): [Active]
  current_feature: checkout-flow
  verbose_mode: true (temporary)
  learned: 7 patterns

🤖 Effective Configuration:
  indent: spaces (2)         [from: global]
  components: atomic          [from: project]
  testing: mandatory          [from: project]
  verbose_mode: true          [from: session]
  framework: Next.js 14       [from: project]
```

### Set Configuration Value
```bash
/config-hierarchy --set project conventions.naming "PascalCase"

✏️ Setting Configuration:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Level: project
Key: conventions.naming
Value: "PascalCase"

⚠️ This will affect all team members
Update project configuration? [Y/n]: Y

✓ Updated ./CLAUDE.md
✓ Configuration applied
✓ Git-tracked (remember to commit)
```

### Get Configuration Value
```bash
/config-hierarchy --get testing

🔍 Configuration Lookup: "testing"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Found in multiple levels:

🌍 Global: 
  prefer_tdd: true
  coverage_threshold: 80
  
📁 Project: (takes precedence)
  testing: "mandatory"
  coverage: 85
  
🤖 Effective Value: "mandatory" with 85% coverage
Source: Project level (./CLAUDE.md)
```

### Sync Configuration
```bash
/config-hierarchy --sync

🔄 Synchronizing Configuration:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Checking for updates...
✓ Global config: Up to date
⚠️ Project config: Changed by teammate

Changes in project config:
  + api.version: "v2"
  ~ testing.coverage: 80 → 85
  - deprecated.oldAuth: removed

Apply changes? [Y/n]: Y

✓ Configuration synchronized
✓ Memory updated with changes
✓ Active context refreshed
```

## Smart Inheritance

### Override Rules
```javascript
// More specific levels override general ones
resolveConfiguration() {
  const config = {}
  
  // Start with global
  Object.assign(config, loadGlobal())
  
  // Override with project
  Object.assign(config, loadProject())
  
  // Override with session
  Object.assign(config, loadSession())
  
  // Apply smart merging for arrays and objects
  return smartMerge(config)
}
```

### Smart Merging
```javascript
// Arrays combine, objects merge deeply
smartMerge(configs) {
  // Simple values: last wins
  verbosity: "concise" → "verbose" = "verbose"
  
  // Arrays: combine and dedupe
  patterns: ["atomic"] + ["domain"] = ["atomic", "domain"]
  
  // Objects: deep merge
  testing: {tdd: true} + {coverage: 80} = {tdd: true, coverage: 80}
}
```

### Precedence Examples
```yaml
# Global says:
indent: "tabs"

# Project says:
indent: "spaces"

# Result: "spaces" (project wins)

---

# Global says:
testing.prefer_tdd: true

# Project says nothing

# Result: true (inherited from global)

---

# Project says:
api.version: "v1"

# Session says:
api.version: "v2"  # Testing new version

# Result: "v2" (session wins temporarily)
```

## Configuration Patterns

### Developer Workflow
```bash
# Morning: Start work
/config-hierarchy --sync
# Pulls latest team configuration

# During work: Learn pattern
Claude: "I notice you prefer early returns"
/config-hierarchy --set session patterns.early_returns true
# Remembers for this session

# End of day: Share learning
/config-hierarchy --promote session.patterns project
# Shares pattern with team
```

### Team Onboarding
```bash
# New developer joins
git clone project
/config-hierarchy --init

# Automatically:
- Detects existing CLAUDE.md
- Merges with their global preferences
- Creates session memory
- Shows effective configuration
```

### Configuration Templates
```bash
# Use templates for common setups
/config-hierarchy --template enterprise

Applying enterprise template:
✓ Strict TypeScript
✓ 90% test coverage
✓ Mandatory documentation
✓ Security scanning
✓ Audit logging
```

## Advanced Features

### Configuration Validation
```javascript
validateConfiguration(config) {
  // Check for conflicts
  if (config.typescript.strict && !config.typescript.enabled) {
    warn("Strict mode requires TypeScript enabled")
  }
  
  // Check for missing required
  if (config.team.size > 5 && !config.reviews.required) {
    suggest("Large teams should require reviews")
  }
  
  // Check for outdated
  if (config.framework.version < currentVersion) {
    notify("Framework version outdated")
  }
}
```

### Configuration Migration
```bash
# When configuration structure changes
/config-hierarchy --migrate

🔄 Configuration Migration:
Version 1.0 → 2.0

Changes needed:
  - Move: testing.tdd → testing.prefer_tdd
  - Rename: style → code_style
  - Add: New required field 'team.name'

Migrate automatically? [Y/n]: Y
✓ Configuration migrated successfully
```

### Configuration Export/Import
```bash
# Export configuration for sharing
/config-hierarchy --export

📤 Exported configuration to: claude-config.json
Includes: Global + Project settings
Excludes: Session memory (private)

# Import configuration
/config-hierarchy --import claude-config.json

📥 Importing configuration...
✓ Validated structure
✓ Merged with existing
✓ Configuration updated
```

## Use Cases

### Personal Preferences Stay Personal
```yaml
# Your global config (private):
user_preferences:
  theme: "dark"
  font_size: 14
  vim_mode: true

# Never affects teammates, always applies to you
```

### Team Standards Stay Consistent
```yaml
# Project config (shared):
team_standards:
  pr_template: required
  commit_format: conventional
  branch_naming: feature/*

# Everyone follows same standards
```

### Experiments Stay Isolated
```yaml
# Session memory (temporary):
experiments:
  trying_new_pattern: true
  verbose_debugging: true
  skip_slow_tests: true

# Only affects current session
```

## The Magic

Three levels of configuration working in harmony:
- **Personal** preferences preserved
- **Team** standards enforced
- **Learning** captured and evolved

**Your way. Team's way. Right way. All at once.**