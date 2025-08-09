---
name: /onboard-express
description: Fastest possible setup - zero questions, smart defaults, ready in 30 seconds
usage: "/onboard-express"
allowed-tools: [Read, Glob, Grep, LS, Write, MultiEdit]
---

# ⚡ Express Onboarding - Zero Questions, Maximum Speed

Get Claude Code configured for your project in 30 seconds with zero questions. I'll detect everything and use smart defaults based on industry best practices and your existing code patterns.

## What Happens

### 1. Complete Auto-Detection (10 seconds)
```javascript
// I detect EVERYTHING automatically:
await Promise.all([
  detectFramework(),      // React, Vue, Angular, Next.js, etc.
  detectLanguage(),       // TypeScript, JavaScript, Python, etc.
  detectTesting(),        // Jest, Pytest, Mocha, etc.
  detectBuildTools(),     // Vite, Webpack, npm, yarn, pnpm
  detectCodeStyle(),      // ESLint, Prettier, conventions
  detectPatterns(),       // Component structure, file organization
  detectWorkflow(),       // Git flow, CI/CD, deployment
  detectTeamSize(),       // From contributors and commit frequency
])
```

### 2. Smart Default Application (5 seconds)
Based on detection, I apply intelligent defaults:
- **If TypeScript found** → Strict mode enabled
- **If tests exist** → TDD encouraged (not enforced)
- **If ESLint found** → Linting integrated
- **If CI/CD found** → Pipeline commands generated
- **If team > 5** → Team collaboration features
- **If conventional commits** → Commit formatting

### 3. Instant Generation (10 seconds)
Generate everything based on YOUR patterns:
- Custom commands matching your workflow
- CLAUDE.md with your conventions
- Context files for your domain
- Progressive enhancement system

### 4. Ready to Use (5 seconds)
Setup complete with:
- All commands ready
- Context loaded
- Patterns learned
- Zero configuration needed

## Smart Defaults Philosophy

### For Web Projects
- Component generation with your structure
- API endpoints with your patterns
- State management if detected
- Testing commands for your framework

### For Backend Projects
- Endpoint creation with your style
- Database commands if ORM detected
- Migration tools if needed
- API documentation generation

### For Libraries
- Module creation commands
- Documentation generation
- Version management
- Publishing workflows

### For Data Science
- Notebook integration
- Data pipeline commands
- Model training helpers
- Visualization tools

## No Questions Asked

I'll NEVER ask about things I can detect:
- ✅ Framework (detected from dependencies)
- ✅ Language (detected from files)
- ✅ Testing (detected from test files)
- ✅ Linting (detected from config files)
- ✅ Git workflow (detected from history)
- ✅ Team size (detected from contributors)
- ✅ Code style (detected from existing code)
- ✅ Project type (detected from structure)

## Example Express Run

```bash
$ /onboard-express

⚡ Express Setup Initiated...

🔍 Detecting... (10s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Framework    : Next.js 14.0.3
Language     : TypeScript (strict)
Styling      : Tailwind CSS 3.3
Database     : Prisma with PostgreSQL
Testing      : Jest + React Testing Library
API Style    : REST (found 23 endpoints)
Components   : 47 found (Atomic pattern)
Team Size    : 5-10 developers
Conventions  : Conventional commits, PR reviews

🤖 Applying Smart Defaults... (5s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ TDD: Encouraged (not enforced)
✓ TypeScript: Strict mode
✓ Components: Atomic pattern
✓ API: RESTful conventions
✓ Testing: Required for PR
✓ Commits: Conventional format
✓ Code Review: Required

🚀 Generating Setup... (10s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Created: 15 custom commands
✓ Generated: CLAUDE.md (2.3KB)
✓ Configured: Team workflows
✓ Enabled: Progressive features
✓ Indexed: 1,247 patterns

✨ Complete! (28 seconds total)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready commands:
  /component Button  → Creates src/components/atoms/Button/
  /api users        → Creates pages/api/users.ts
  /test Button      → Creates Button.test.tsx
  /refactor         → Applies your patterns
  /commit           → Conventional format

Type /help to see all 15 commands
```

## Why Express Mode?

### For Experienced Developers
- You know what you want
- Your code already has patterns
- You don't need hand-holding
- You value speed over customization

### For Established Projects
- Patterns are already defined
- Conventions are documented
- Team practices are mature
- Just need Claude to follow them

### For Rapid Prototyping
- Get started immediately
- Iterate quickly
- Adjust later if needed
- No setup ceremony

## Progressive Enhancement

Even with express setup, the system learns:
- **Hour 1**: Basic commands work perfectly
- **Day 1**: Starts learning your preferences
- **Week 1**: Unlocks advanced features
- **Month 1**: Fully adapted to your style

## The Express Promise

**30 seconds. Zero questions. Perfect setup.**

Your code patterns ARE the configuration. Your conventions ARE the rules. Your workflow IS the process.

Claude learns from what you've built, not what you say you'll build.

Ready? Just run this command and start coding!