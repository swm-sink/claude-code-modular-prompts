# Claude Code Prompt Templates Library

**📚 102 Curated Prompt Templates for Claude Code** - A comprehensive collection of battle-tested Claude Code command templates (64 active, 38 deprecated) with guided manual customization for your specific project.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-green.svg)](https://github.com/swm-sink/claude-code-modular-prompts/releases)
[![Templates: 102](https://img.shields.io/badge/Templates-102-blue.svg)](https://github.com/swm-sink/claude-code-modular-prompts/tree/main/.claude/commands)
[![Last Updated: 2025-07-29](https://img.shields.io/badge/Updated-2025--07--29-brightgreen.svg)](https://github.com/swm-sink/claude-code-modular-prompts/commits/main)

## What This Actually Is

**A template library with manual customization guides:**
- 📋 **Step-by-step checklists** for customizing each template
- 📝 **102 command templates** (64 active, 38 deprecated) with [INSERT_XXX] placeholders
- 🔍 **Manual validation tools** to check your progress
- 📁 **Dual folder structure** - working copy + reference copy
- ✍️ **Find & Replace guides** for updating placeholders

## What This Is NOT
- ❌ **Not an automation engine** - requires manual work (30-60 minutes)
- ❌ **Not self-adapting** - you customize it yourself using Find & Replace
- ❌ **Not a 5-minute setup** - realistic timeline is 1-2 hours including customization
- ❌ **Not magic** - it's proven templates + step-by-step guides

## The Value: Skip the Learning Curve

What these templates help you avoid:
- ❌ **Common Claude Code mistakes** documented in 48+ anti-patterns
- ❌ **Inefficient prompt structures** that waste tokens
- ❌ **Reinventing patterns** that already work well
- ❌ **Security vulnerabilities** in command design
- ❌ **Performance pitfalls** in context management

**You get proven patterns, but YOU must customize them manually.**

## The Manual Process (Realistic Timeline)

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Install        │     │  Get Guidance    │     │  Manual Work    │
│  Templates      │ --> │  & Checklists    │ --> │  45-90 mins     │
│  (5 minutes)    │     │ /adapt-to-project│     │  Find & Replace │
└─────────────────┘     └──────────────────┘     └─────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
   102 Templates         ┌──────────────┐          ┌─────────────┐
    70 Components         │ Replacement  │          │ Customized  │
    48 Anti-patterns      │ Checklist    │          │  Templates  │
    Testing Framework     │  Generated   │          │    Ready    │
                          └──────────────┘          └─────────────┘
```

## Quick Start: Intelligent Adaptation

### Step 1: Install Templates (5 minutes)
```bash
# Method 1: Git Submodule (Recommended - enables updates)
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh

# Method 2: Direct Integration
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../your-project
```

### Step 2: Get Your Customization Guide (10 minutes)
```bash
# Start Claude Code and run:
/adapt-to-project

# Answer questions about your project
# Get a complete replacement guide listing:
# - All files that need updates
# - Exact placeholders to replace
# - Validation checklist
```

### Step 3: Manual Customization Work (45-90 minutes)
You will need to:
- 📋 **Answer questions** about your tech stack, domain, and team size
- 🔍 **Use Find & Replace** in your editor to update 15 standard placeholders
- ✍️ **Review and customize** 64 active commands for your project
- 🗑️ **Remove unused commands** from the 38 deprecated ones
- ✅ **Run validation** commands to verify completeness
- 📝 **Document** your choices for team reference and future updates

## What You Get: Dual Structure

```
your-project/
├── .claude/                    # YOUR customized commands (64 active)
│   ├── commands/              # Adapted with your project details
│   │   ├── core/             # help, task, auto, query - customized
│   │   ├── development/      # dev, api-design - your tech stack
│   │   ├── database/         # db-migrate, db-backup - your database
│   │   ├── security/         # secure-audit, secure-scan - your compliance
│   │   ├── testing/          # test-unit, test-integration - your framework
│   │   ├── devops/           # deploy, ci-setup - your pipeline
│   │   ├── quality/          # quality checks - your standards
│   │   ├── monitoring/       # alerts and setup - your tools
│   │   └── deprecated/       # 38 deprecated commands (remove if unused)
│   ├── components/           # 70 prompt components adapted
│   ├── context/              # Anti-patterns and best practices
│   ├── docs/                 # Project documentation
│   └── config/
│       └── project-config.yaml # YOUR configuration
│
├── .claude-framework/         # Reference library (read-only)
│   └── [original templates]   # Preserved for updates
│
└── CLAUDE.md                  # Your project memory
```

## Adaptation Examples

### Before Adaptation (Generic Placeholder)
```markdown
# Deploy [INSERT_PROJECT_NAME] to [INSERT_DEPLOYMENT_TARGET]
Using [INSERT_CI_CD_PLATFORM] for [INSERT_TECH_STACK]...
```

### After Adaptation (Your Project)
```markdown
# Deploy AwesomeApp to AWS ECS
Using GitHub Actions for React+Node.js...
```

## Guide Commands: Manual Customization Helpers

- **`/adapt-to-project`** - Get customization checklist and replacement guide
- **`/validate-adaptation`** - Get validation checklist to verify your work
- **`/replace-placeholders`** - Get list of all replacements needed
- **`/sync-from-reference`** - Get instructions for manual sync
- **`/share-adaptation`** - Create documentation of your customizations
- **`/undo-adaptation`** - Get recovery instructions if something goes wrong

## Supported Domains & Stacks

The engine adapts for:
- **Web Development**: React, Vue, Angular, Next.js, Node.js, Django, Rails
- **Data Science**: Jupyter, pandas, scikit-learn, TensorFlow, PyTorch
- **DevOps**: Docker, Kubernetes, Terraform, AWS, Azure, GCP
- **Mobile**: React Native, Flutter, Swift, Kotlin
- **Enterprise**: Java Spring, .NET, microservices, SOA

## Why Use This?

**Without this library**: Start from scratch, learn all the anti-patterns the hard way, spend months building your command library.

**With this library**: Start with 102 proven templates, avoid documented pitfalls, customize in an afternoon with clear guidance.

The value isn't automation - it's having curated, tested patterns you can adapt.

## Requirements

- **Claude Code** (Desktop application or API access)
- **Git** (for submodule approach and updates)
- **Bash shell** (for setup and validation scripts)
- **Text editor** with Find & Replace (VS Code, IntelliJ, Sublime, etc.)
- **1-2 hours** of focused customization time
- **Basic understanding** of your project's tech stack and requirements

## Advanced Features

### Partial Adaptation
Choose only what you need:
```bash
/adapt-to-project --components "api,database,testing"
```

### Domain-Specific Patterns
```bash
/adapt-to-project --domain "e-commerce" 
# Adds: checkout flows, payment integration, inventory patterns
```

### Team Configurations
```bash
/adapt-to-project --team-size "large" --workflow "agile"
# Adapts: PR workflows, code review patterns, standup tools
```

## 📚 Documentation & Support

### Complete Guides
- **[Quick Start](QUICKSTART.md)**: Get running in 10 minutes
- **[Installation Guide](INSTALLATION.md)**: Comprehensive setup with troubleshooting
- **[Setup Guide](SETUP.md)**: Technical details and customization
- **[FAQ](FAQ.md)**: 90% of questions answered
- **[Examples](EXAMPLES.md)**: Real-world customization patterns
- **[Project Status](PROJECT-STATUS.md)**: Current state and roadmap

### Community & Updates
- 🔄 **Regular Updates**: Monthly releases via git submodule
- 🤝 **Share Adaptations**: Export your patterns with `/share-adaptation`
- 📣 **Discussions**: GitHub Discussions for Q&A and best practices
- 🐛 **Issues**: Report bugs or request features
- 🌟 **Star Us**: If this saves you months of prompt engineering work!

## ❓ Quick FAQ

**Q: How long does this actually take?**  
A: 10 minutes for basic functionality, 1-2 hours for complete professional setup.

**Q: Is this just templates?**  
A: It's 102 battle-tested templates + 70 components + 48 anti-patterns + comprehensive guides + validation framework.

**Q: Do I need all 102 commands?**  
A: No! Start with 6 core commands, add others gradually. Archive the rest.

**Q: What if it doesn't fit my project?**  
A: Templates are designed to be customized. Use Find & Replace, remove unused commands, add project-specific ones.

**Q: Will updates break my work?**  
A: No! Dual structure keeps your customizations separate. Updates never overwrite your changes.

**→ [Complete FAQ with Advanced Troubleshooting](FAQ.md)**

## 🚀 Get Started Now

**Three ways to get started:**

### ⚡ Quick Start (10 minutes)
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh && cd ..
# Then: /adapt-to-project in Claude Code
```
**→ [Complete Quick Start Guide](QUICKSTART.md)**

### 📖 Full Setup (1-2 hours)
**→ [Comprehensive Installation Guide](INSTALLATION.md)**

### 🛠️ Detailed Technical Setup
**→ [Technical Setup Guide](SETUP.md)**

---

*Built by the community, for the community. Star ⭐ if this saves you months of work!*

## License

MIT - Use freely in your projects

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Special thanks to all contributors who've shared their patterns and adaptations.