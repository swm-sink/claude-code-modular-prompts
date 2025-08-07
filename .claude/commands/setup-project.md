---
name: /setup-project
description: Complete setup workflow - discover, generate, and configure Claude for your project
usage: "/setup-project [--quick | --full]"
allowed-tools: [Read, Write, Edit, LS, Glob, Grep]
category: setup
version: "1.0"
---

# Setup Project - Complete Claude Code Configuration for Your Project

## Purpose
This command orchestrates the complete setup process, transforming Claude from a generic assistant into YOUR project expert by:
1. Discovering your project's DNA
2. Generating custom commands
3. Creating project-specific context
4. Configuring Claude for your workflow

## Setup Modes

### Quick Setup (Default)
```
/setup-project
```
- Automatic discovery
- Generate essential commands
- Basic context creation
- ~5 minutes

### Full Setup
```
/setup-project --full
```
- Deep discovery with questions
- Generate comprehensive commands
- Rich context creation
- ~15 minutes

## The Setup Process

### Phase 1: Discovery (2-3 minutes)
```
🔍 Analyzing your project...
  ✓ Detected: React + TypeScript
  ✓ Found: Jest testing framework
  ✓ Discovered: Atomic design pattern
  ✓ Identified: REST API with Axios
```

### Phase 2: Generation (1-2 minutes)
```
🏗️ Generating custom commands...
  ✓ Created: /create-component
  ✓ Created: /add-test
  ✓ Created: /create-hook
  ✓ Created: /debug-issue
```

### Phase 3: Context Creation (1-2 minutes)
```
📝 Building project context...
  ✓ Created: CLAUDE.md
  ✓ Created: .claude/context/technical-architecture.md
  ✓ Created: .claude/context/project-patterns.md
  ✓ Created: .claude/context/team-conventions.md
```

### Phase 4: Configuration (30 seconds)
```
⚙️ Configuring Claude...
  ✓ Set: Project type markers
  ✓ Set: Testing preferences
  ✓ Set: Code style rules
  ✓ Set: Debugging patterns
```

## What You Get

### 1. Custom Commands
Commands that match YOUR project:
```bash
/create-component Button       # Uses YOUR component pattern
/add-test UserService          # Follows YOUR test style
/create-endpoint /users GET    # Matches YOUR API pattern
/debug-issue "login failing"   # Uses YOUR debugging approach
```

### 2. Project Context (CLAUDE.md)
```markdown
# Project Context

## You are working on: E-Commerce Platform
- React 18 + TypeScript frontend
- Node.js + Express backend
- PostgreSQL database
- Jest + React Testing Library

## Key Patterns
- Atomic design for components
- Redux Toolkit for state
- REST API with OpenAPI docs
- Feature-based folder structure

## When coding, always:
- Use TypeScript strict mode
- Write tests first (TDD)
- Follow team's ESLint rules
- Use async/await over promises
```

### 3. Contextual Understanding
Claude now knows:
- Your tech stack details
- Your coding patterns
- Your testing approach
- Your debugging methods
- Your team conventions

## Interactive Features

### Confirmation Points
```
📊 Discovery Results:
  - Framework: React 18.2.0
  - Language: TypeScript 4.9
  - Testing: Jest + RTL
  - State: Redux Toolkit

✅ Does this look correct? (y/n/edit)
```

### Customization Options
```
🎨 Customize generation:
  1. Component patterns
  2. Testing approach
  3. API patterns
  4. Skip customization

Choose (1-4):
```

### Validation
```
🧪 Testing generated commands...
  ✓ /create-component: Valid
  ✓ /add-test: Valid
  ✓ /create-endpoint: Valid
  
Ready to use! Try: /create-component Button
```

## Error Handling

### Missing Dependencies
```
⚠️ Could not detect framework
Please specify:
  1. React
  2. Vue
  3. Angular
  4. Other (specify)
```

### Pattern Conflicts
```
⚠️ Found multiple patterns:
  - Some files use camelCase
  - Some files use kebab-case
  
Which is preferred? (1/2)
```

### Recovery Options
```
❌ Setup failed at: Generation phase

Options:
  1. Retry generation
  2. Skip to context creation
  3. Manual setup
  4. Report issue
```

## Post-Setup

### Immediate Actions
```
✨ Setup complete! You can now:

1. Try a command:
   /create-component Header

2. View your commands:
   /help

3. Check project context:
   cat CLAUDE.md

4. Customize further:
   /customize-commands
```

### Validation Commands
```bash
# Test that commands work
/create-component TestComponent
/add-test TestComponent

# Verify context is loaded
/task "explain our auth flow"
# Claude should know your specific auth implementation
```

## Advanced Options

### Flags
- `--quick`: Skip confirmations, use defaults
- `--full`: Deep analysis with all options
- `--update`: Update existing setup
- `--reset`: Start fresh

### Manual Overrides
```
/setup-project --framework react --testing jest --style atomic
```

### Project Types
Optimized setups for:
- **Frontend**: React, Vue, Angular, Svelte
- **Backend**: Express, Django, Rails, FastAPI
- **Mobile**: React Native, Flutter
- **Desktop**: Electron, Tauri
- **CLI**: Commander, Click, Cobra

## Troubleshooting

### "No project detected"
- Ensure you're in project root
- Check for package.json or requirements.txt
- Use manual override flags

### "Generation failed"
- Check PROJECT-DNA.md was created
- Verify file permissions
- Try --reset flag

### "Commands not working"
- Verify .claude/commands/ exists
- Check command file syntax
- Run /validate-commands

## The Result

After setup, Claude becomes YOUR project expert:

### Before Setup
```
You: "Create a new user component"
Claude: "Here's a generic React component..."
```

### After Setup
```
You: "Create a new user component"
Claude: "I'll create it following your atomic design pattern,
using your CSS modules approach, with your standard test file,
and export it through your barrel file..."
```

Claude now writes code like YOUR team writes code!

## Complete Example

```bash
# 1. Run setup
/setup-project

# 2. Claude discovers your project
🔍 Analyzing...
Found: React + TypeScript + Redux Toolkit + Jest

# 3. Claude generates custom commands
🏗️ Generating...
Created 12 custom commands

# 4. Claude creates context
📝 Building context...
Created comprehensive project understanding

# 5. You're ready!
✨ Setup complete!
Try: /create-component Button

# 6. Use your custom command
/create-component Button atoms

# 7. Claude creates YOUR style component
Created: src/components/atoms/Button/Button.tsx
Created: src/components/atoms/Button/Button.module.css
Created: src/components/atoms/Button/__tests__/Button.test.tsx
Created: src/components/atoms/Button/index.ts
Updated: src/components/atoms/index.ts
```

Your project setup is complete!