---
name: /import-pattern
description: Import community adaptation patterns for similar projects (v2.0)
version: 2.0
usage: '/import-pattern [pattern-name] [--preview] [--merge|--replace]'
category: meta
allowed-tools:
- Read
- Write
- MultiEdit
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

# Import Community Adaptation Patterns

Jumpstart your adaptation by importing patterns from projects similar to yours. Learn from the community's experience!

## 🔍 Browse Available Patterns

### By Domain
Find patterns for your industry:
```bash
/import-pattern --browse --domain web-dev
/import-pattern --browse --domain data-science
/import-pattern --browse --domain devops
```

### By Tech Stack
Match your technology:
```bash
/import-pattern --browse --stack "React+Node"
/import-pattern --browse --stack "Python+FastAPI"
/import-pattern --browse --stack "Java+Spring"
```

### By Team Size
Patterns for teams like yours:
```bash
/import-pattern --browse --team small
/import-pattern --browse --team enterprise
```

## 📦 Popular Patterns

### 🚀 Startup Patterns
**"React SaaS Starter"**
- Stack: React, Node.js, PostgreSQL
- Team: Small (2-10)
- Focus: Rapid iteration, MVP
```bash
/import-pattern "React SaaS Starter"
```

**"Python API Quickstart"**
- Stack: FastAPI, PostgreSQL, Redis
- Team: Small
- Focus: REST APIs, async
```bash
/import-pattern "Python API Quickstart"
```

### 🏢 Enterprise Patterns
**"Enterprise Java Platform"**
- Stack: Spring Boot, Oracle, Kubernetes
- Team: Large (50+)
- Focus: Compliance, scale
```bash
/import-pattern "Enterprise Java Platform"
```

**".NET Microservices"**
- Stack: .NET Core, SQL Server, Azure
- Team: Medium-Large
- Focus: Microservices, cloud
```bash
/import-pattern ".NET Microservices"
```

### 📊 Data Science Patterns
**"ML Pipeline Setup"**
- Stack: Python, Jupyter, TensorFlow
- Team: Small-Medium
- Focus: Experimentation, models
```bash
/import-pattern "ML Pipeline Setup"
```

## 🎯 Import Process

### 1. Preview Pattern
See what you'll get:
```bash
/import-pattern "React SaaS Starter" --preview
```

Shows:
- Configuration values
- Selected commands
- Customizations made
- Success metrics

### 2. Compatibility Check
Ensures pattern fits:
- Stack compatibility
- No conflicts
- Version match
- Team alignment

### 3. Import Strategy

**Merge (Default)**
Combine with your setup:
```bash
/import-pattern "pattern-name" --merge
```
- Keeps your changes
- Adds new insights
- Resolves conflicts

**Replace**
Start fresh with pattern:
```bash
/import-pattern "pattern-name" --replace
```
- Full pattern adoption
- Overwrites current
- Clean slate

### 4. Adaptation
After import:
- Placeholders updated
- Configurations merged
- Commands selected
- Ready to customize

## 📊 Pattern Details

Each pattern includes:

### Metadata
```yaml
name: "React SaaS Starter"
author: "@community-member"
created: "2025-06-15"
downloads: 1,247
rating: 4.8/5
verified: true
```

### Configuration
```yaml
domain: "web-dev"
stack: "React+Node+PostgreSQL"
team_size: "small"
workflow: "agile"
security: "standard"
performance: "balanced"
```

### Customizations
- Selected commands (45/79)
- Excluded components
- Special configurations
- Optimization notes

### Success Story
"Reduced setup from 2 weeks to 30 minutes. Perfect for SaaS MVPs!" - Original author

## 🔄 Pattern Compatibility

### Full Match ✅
Your project exactly matches:
- Same tech stack
- Same domain
- Similar team size
= **100% compatible**

### Partial Match ⚠️
Some differences:
- Similar stack
- Different domain
- Adaptable patterns
= **Requires adjustment**

### Learning Mode 📚
Very different but educational:
- Different stack
- Useful patterns
- Good inspiration
= **Manual adaptation**

## 🛡️ Manual Safety Steps

### Before Applying Any Pattern
1. **Backup your current setup**:
   ```bash
   cp -r .claude .claude.backup-$(date +%Y%m%d)
   ```

2. **Commit current state**:
   ```bash
   git add . && git commit -m "Before pattern application"
   ```

### Handling Differences
When the pattern differs from your setup:
- **Compare carefully**: Don't blindly copy everything
- **Cherry-pick**: Take only what makes sense
- **Document changes**: Note what you adopted and why

### After Applying
1. Test key commands work
2. Check no placeholders remain
3. Verify your specific needs are met

## 🌟 After Import

### Customize Further
Pattern is starting point:
1. Run `/validate-adaptation`
2. Adjust for your needs
3. Add missing pieces
4. Test thoroughly

### Share Back
Improve the pattern:
- Your enhancements
- Lessons learned
- Share with `/share-adaptation`

## 💡 Tips for Success

### Do:
- Preview before importing
- Check compatibility scores
- Read success stories
- Understand rationale

### Don't:
- Blindly import everything
- Ignore team differences
- Skip validation
- Forget to customize

## 🔍 Find Your Pattern

Ready to explore? Try:

1. **Browse All** → `/import-pattern --browse`
2. **Your Domain** → `/import-pattern --browse --domain [your-domain]`
3. **Popular** → `/import-pattern --popular`
4. **Search** → `/import-pattern --search "keywords"`

Which pattern would you like to explore?