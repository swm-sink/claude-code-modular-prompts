---
name: /share-adaptation
description: Export your adaptation patterns to share with the community (v1.0)
version: "1.0"
usage: '/share-adaptation [--name pattern-name] [--description text] [--anonymize]'
category: meta
allowed-tools:
- Read
- Write
- TodoWrite
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---

# Document Your Adaptation Pattern

## 🎯 What This Command Actually Does

**I help you document your adaptation, not upload it.** I'll guide you to create:
- 📝 A shareable pattern document
- 📋 Configuration templates others can use
- 💡 Lessons learned documentation
- 📧 Format for manual sharing (GitHub, forums, etc.)

## ⚠️ What I Cannot Do
- ❌ Upload patterns to any repository
- ❌ Submit to a community database
- ❌ Automatically share anything
- ❌ Track downloads or usage

## Why Share?

Your adaptation for **[INSERT_TECH_STACK]** and **[INSERT_DOMAIN]** could help others:
- Save setup time
- Avoid common pitfalls
- Learn best practices
- Build on your innovations

## What Gets Shared

### Configuration Pattern
Your successful setup:
- Domain: [INSERT_DOMAIN]
- Tech Stack: [INSERT_TECH_STACK]
- Team Size: [INSERT_TEAM_SIZE]
- Workflow: [INSERT_WORKFLOW_TYPE]

### Adaptation Choices
What worked for you:
- Command selections
- Placeholder values
- Custom configurations
- Excluded components

### Success Metrics
Proof of value:
- Readiness score achieved
- Time to adapt
- Team feedback
- Productivity gains

## Privacy & Security

### Automatically Excluded
Your sensitive data is protected:
- ❌ API keys and secrets
- ❌ Company-specific names
- ❌ Internal URLs
- ❌ Private configurations

### Anonymization Option
Remove identifying information:
```bash
/share-adaptation --anonymize
```
- Replaces [INSERT_COMPANY_NAME] with "Company"
- Genericizes project names
- Removes personal details
- Keeps patterns intact

## Manual Documentation Process

### 1. You Tell Me About Your Adaptation
Share details about:
- What you customized and why
- Which commands you kept/removed
- What worked well
- Challenges you faced

### 2. I'll Generate a Pattern Document
I'll create a markdown template like:

```markdown
# [Your Project Type] Adaptation Pattern

## Overview
- **Domain**: [Your domain]
- **Stack**: [Your tech stack]
- **Team Size**: [Your team size]
- **Created**: [Date]

## What This Pattern Includes
- Selected commands: [List]
- Key customizations: [Details]
- Excluded items: [List]

## Configuration Template
```xml
<project-config>
  <!-- Your successful config -->
</project-config>
```

## Lessons Learned
[Your insights]

## How to Apply This Pattern
1. [Step-by-step guide]
```

### 3. You Can Then Share It
- Post to GitHub as a gist
- Share in Claude Code discussions
- Add to your team's documentation
- Include in blog posts

## Documentation Options

### Quick Template
Get a basic pattern document:
```
"I want to document my React+Node adaptation"
```

### Detailed Documentation
With full context and lessons:
```
"Help me create detailed docs for my enterprise Java setup"
```

### Specific Focus Areas
Document particular aspects:
- Security configurations
- Performance optimizations
- Team workflow adaptations
- Testing strategies

## Pattern Categories

Share patterns for:
- **Startup** - Fast iteration, lean
- **Enterprise** - Compliance, scale
- **Open Source** - Community, contribution
- **SaaS** - Multi-tenant, billing
- **Mobile** - Cross-platform, offline
- **Data Science** - Notebooks, ML
- **DevOps** - Infrastructure, automation

## Attribution

Choose how you're credited:
- **Named**: Include your GitHub username
- **Anonymous**: "Community contributor"
- **Team**: "TeamName contributors"

## Quality Guidelines

Great patterns include:
- ✅ Clear use case
- ✅ Proven in production
- ✅ Time savings data
- ✅ Pitfalls avoided
- ✅ Team size context

## Review Process

Before sharing:
1. **Validation** - Pattern tested
2. **Privacy** - Sensitive data removed
3. **Quality** - Meets guidelines
4. **Format** - Properly structured

## Community Benefits

Your pattern helps others:
- **Similar Projects** - Direct reuse
- **Learning** - See what works
- **Inspiration** - Adaptation ideas
- **Time Savings** - Faster setup

## Manual Sharing Process

Once I generate your pattern document:

1. **Review & Edit**: Make sure it accurately reflects your experience
2. **Remove Sensitive Info**: Double-check for any private data
3. **Choose Where to Share**:
   - GitHub Gist or Repository
   - Team wiki or documentation
   - Claude Code forum/discussions
   - Technical blog post

## Ready to Document?

Tell me:
1. **Your domain**: (web-dev, data-science, etc.)
2. **Your tech stack**: (specific technologies)
3. **What worked well**: (key successes)
4. **What to highlight**: (unique aspects)

I'll help you create a well-structured pattern document that others can learn from and manually apply to their projects.