# Claude Code Prompt Templates Library

**📚 102 Curated Prompt Templates for Claude Code** - A comprehensive collection of battle-tested Claude Code command templates (64 active, 38 deprecated) with guided manual customization for your specific project.

## What This Actually Is

**A template library with manual customization guides:**
- 📋 **Step-by-step checklists** for customizing each template
- 📝 **102 command templates** (64 active, 38 deprecated) with [INSERT_XXX] placeholders
- 🔍 **Manual validation tools** to check your progress
- 📁 **Dual folder structure** - working copy + reference copy
- ✍️ **Find & Replace guides** for updating placeholders

## What This Is NOT
- ❌ **Not an automation engine** - requires manual work
- ❌ **Not self-adapting** - you customize it yourself
- ❌ **Not a 5-minute setup** - expect 30-60 minutes
- ❌ **Not magic** - it's good templates + guides

## The Value: Skip the Learning Curve

What these templates help you avoid:
- ❌ **Common Claude Code mistakes** documented in 48+ anti-patterns
- ❌ **Inefficient prompt structures** that waste tokens
- ❌ **Reinventing patterns** that already work well
- ❌ **Security vulnerabilities** in command design
- ❌ **Performance pitfalls** in context management

**You get proven patterns, but YOU must customize them manually.**

## The Manual Process

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Install        │     │  Get Guidance    │     │  Manual Work    │
│  Templates      │ --> │  & Checklists    │ --> │  30-60 mins     │
│  (2 minutes)    │     │ /adapt-to-project│     │  Find & Replace │
└─────────────────┘     └──────────────────┘     └─────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
   102 Templates         ┌──────────────┐          ┌─────────────┐
    Anti-patterns         │ Replacement  │          │ Customized  │
    Components            │    Guide     │          │  Templates  │
    Examples              │  Generated   │          │    Ready    │
                          └──────────────┘          └─────────────┘
```

## Quick Start: Intelligent Adaptation

### Step 1: Install the Engine (2 minutes)
```bash
# Method 1: Git Submodule (Recommended - enables updates)
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh

# Method 2: Direct Integration
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../your-project
```

### Step 2: Get Your Customization Guide (5 minutes)
```bash
# Start Claude Code and run:
/adapt-to-project

# Answer questions about your project
# Get a complete replacement guide listing:
# - All files that need updates
# - Exact placeholders to replace
# - Validation checklist
```

### Step 3: Manual Customization Work
You will need to:
- 📋 **Tell the guide** about your tech stack and project
- 🔍 **Manually find** placeholders in your editor
- ✍️ **Replace** each [INSERT_XXX] placeholder yourself
- ✅ **Run validation** commands to check your work
- 📝 **Document** your customizations for future reference

## What You Get: Dual Structure

```
your-project/
├── .claude/                    # YOUR customized commands
│   ├── commands/              # Adapted with your project details
│   │   ├── core/             # task, help, auto - customized
│   │   ├── database/         # db-migrate for YOUR database
│   │   └── api/              # api-design for YOUR style
│   ├── components/           # 70 components adapted
│   ├── context/              # Anti-patterns configured
│   └── config/
│       └── project-config.yaml # YOUR configuration
│
├── .claude-framework/         # Reference library (read-only)
│   └── [original templates]   # Preserved for updates
│
├── .claude-adaptations/       # Adaptation tracking
│   ├── history/              # What was customized
│   ├── patterns/             # Shareable adaptations
│   └── backups/              # Automatic backups
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

- Claude Code (Desktop or API)
- Git (for submodule approach)
- Bash (for setup script)
- 5 minutes of your time

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

## Community & Updates

- 🔄 **Regular Updates**: Pull new patterns via git submodule
- 🤝 **Share Adaptations**: Export your patterns for others
- 📣 **Discussions**: GitHub Discussions for Q&A
- 🐛 **Issues**: Report bugs or request features
- 🌟 **Star Us**: If this saves you months of work!

## FAQ

**Q: Is this just templates?**  
A: No! It's a comprehensive template library with guided manual customization that helps you adapt 102 proven patterns to your specific project.

**Q: How is this different from copying snippets?**  
A: The template library provides consistency guidance, documented anti-patterns to avoid, component relationships, and a complete integrated system - not just isolated snippets.

**Q: Can I customize further after adaptation?**  
A: Absolutely! The templates give you a solid foundation with manual customization guidance. You own all customized files and can modify anything.

**Q: Will updates break my customizations?**  
A: No! The dual structure keeps your customizations separate from the reference library. Updates are pulled conservatively with your approval.

## Get Started Now

**Save 12-18 months of Claude Code expertise:**

```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh
```

Then in Claude Code: `/adapt-to-project`

---

*Built by the community, for the community. Star ⭐ if this saves you months of work!*

## License

MIT - Use freely in your projects

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Special thanks to all contributors who've shared their patterns and adaptations.