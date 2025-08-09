---
name: /onboard
description: Intelligent project setup with auto-detection - analyzes your project and configures Claude Code automatically
usage: "/onboard [--express|--detailed|--team|--enterprise]"
allowed-tools: [Read, Glob, Grep, LS, Write, MultiEdit]
---

# 🚀 Smart Claude Code Onboarding

I'll analyze your project and automatically configure Claude Code to work like a team member who knows your codebase. This process takes 30-60 seconds and detects everything possible to minimize questions.

## Auto-Detection Process

I'll automatically detect:
- **Framework & Language**: React, Vue, Next.js, Django, Rails, etc.
- **Testing Setup**: Jest, Pytest, RSpec, testing patterns
- **Build Tools**: Vite, Webpack, npm, yarn, pnpm
- **Code Patterns**: Component structure, naming conventions
- **Team Standards**: From git history and existing code
- **Project Type**: Web app, API, library, CLI tool, etc.

## Onboarding Modes

- **Default**: Balanced detection with minimal smart questions
- **--express**: Skip all questions, use smart defaults (30 seconds)
- **--detailed**: Comprehensive analysis with more customization
- **--team**: Focus on team consistency and shared standards
- **--enterprise**: Full audit trails and compliance features

## The Process

### Phase 1: Silent Detection (10-15 seconds)
I'll scan your project to understand:
```javascript
// What I detect automatically:
detectFramework()     // From package.json, requirements.txt, etc.
detectLanguage()      // From file extensions and syntax
detectPatterns()      // From existing code structure
detectConventions()   // From naming and organization
detectWorkflow()      // From CI/CD and git history
detectTesting()       // From test files and coverage
```

### Phase 2: Smart Questions (0-15 seconds)
Only if needed, I'll ask questions I couldn't detect:
```
✓ Detected: React 18, TypeScript, Jest, ESLint
? Enforce TDD (tests before code)? [Y/n]
? Team size? [1-5/5-20/20+]
```

With `--express` mode, I skip all questions and use smart defaults.

### Phase 3: Generation (15-20 seconds)
I'll generate custom commands based on YOUR patterns:
- Component creation matching your structure
- API endpoints following your conventions
- Tests using your testing approach
- Commands for your specific workflow

### Phase 4: Configuration (5-10 seconds)
I'll create:
- **CLAUDE.md**: Project context and standards
- **Custom commands**: Based on your patterns
- **Team conventions**: Extracted from your code
- **Progressive system**: Reveals features as you need them

## What Makes This Smart

### 1. Zero Silly Questions
I'll never ask what I can detect:
- ❌ "What's your project name?" (it's in package.json!)
- ❌ "What language?" (obvious from files!)
- ❌ "Use ESLint?" (.eslintrc already exists!)

### 2. Pattern Learning
I analyze your existing code to match YOUR style:
```javascript
// Found: You use PascalCase components in src/components/
// Generated: /create-component will follow this pattern

// Found: Your tests are in __tests__ folders
// Generated: /test will create tests there

// Found: You use conventional commits
// Generated: /commit will enforce this format
```

### 3. Progressive Enhancement
Start simple, unlock advanced features over time:
- **Day 1**: Basic commands (create, test, debug)
- **Week 1**: Optimization commands appear
- **Week 2**: Architecture commands unlock
- **Continuous**: Learns from your corrections

## Quick Start Examples

### Express Mode (30 seconds, zero questions):
```
/onboard --express
# Detects everything, assumes smart defaults
# Perfect for experienced developers
```

### Team Mode (ensures consistency):
```
/onboard --team
# Creates shared configuration
# Extracts team conventions from git history
# Generates team-specific commands
```

### Enterprise Mode (full compliance):
```
/onboard --enterprise
# Audit trail of all detections
# Security scanning included
# Compliance documentation generated
```

## The Magic

The best part? After onboarding, Claude Code will:
- **Know your patterns**: Creates code matching your style
- **Follow your conventions**: Names things like you do
- **Use your tools**: Works with your exact setup
- **Understand your domain**: Knows your business terms
- **Respect your workflow**: Follows your processes

## Ready?

Just run me and I'll handle everything else. In 30-60 seconds, Claude will code like your team.

Example output:
```
🔍 Analyzing your project... (10s)
  ✓ Found: Next.js 14 + TypeScript + Tailwind
  ✓ Detected: Atomic component pattern
  ✓ Identified: REST API structure
  ✓ Recognized: Jest + React Testing Library

🤖 One question:
  Enforce TDD? [Y/n]: y

🚀 Generating your setup... (20s)
  ✓ Created: 12 custom commands
  ✓ Generated: CLAUDE.md with conventions
  ✓ Configured: Team standards
  ✓ Enabled: Progressive enhancement

✨ Done! Try: /create-component Button
```

Let's begin the smart onboarding process!