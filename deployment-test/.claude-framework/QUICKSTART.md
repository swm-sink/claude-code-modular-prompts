# ⚡ Quick Start Guide - Get Running in 10 Minutes

**Goal**: Get Claude Code templates installed and working with minimal time investment.  
**Time**: 10 minutes to basic functionality, 1-2 hours for full customization.

---

## 🎯 10-Minute Quick Setup

### Step 1: Install (2 minutes)
```bash
# Navigate to your project
cd /path/to/your/project

# Add templates as git submodule
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Run setup
cd .claude-framework && ./setup.sh && cd ..
```

### Step 2: Test Basic Functionality (3 minutes)
```bash
# Verify installation
ls -la .claude/commands/core/  # Should show: help.md, task.md, auto.md, query.md

# Start Claude Code and test:
# /help     - Should list available commands
# /task     - Should start task breakdown (will have placeholders)
```

### Step 3: Quick Essential Customization (5 minutes)
```bash
# In Claude Code, get your customization guide:
/adapt-to-project

# Minimal customization - replace just these 3 critical placeholders:
# 1. [INSERT_PROJECT_NAME] → YourProjectName
# 2. [INSERT_DOMAIN] → your-domain (e.g., "web-app", "data-science")  
# 3. [INSERT_TECH_STACK] → your-stack (e.g., "React/Node.js")

# Use your editor's Find & Replace:
# VS Code: Ctrl+Shift+H, IntelliJ: Ctrl+Shift+R, Sublime: Ctrl+Shift+F
```

**Result**: Basic Claude Code templates working with your project context in 10 minutes.

---

## 🚀 1-Hour Professional Setup

### Phase 1: Complete Installation (15 minutes)
```bash
# If you used quick setup above, you're already done
# Otherwise, follow the installation process above

# Verify structure
ls -la .claude/                 # Your workspace
ls -la .claude-framework/       # Reference library
```

### Phase 2: Comprehensive Customization (30 minutes)
```bash
# 1. Get complete customization guide
/adapt-to-project
# Answer all questions about your project thoroughly

# 2. Replace all 15 standard placeholders using Find & Replace:
```

| Priority | Placeholder | Your Value | Time |
|----------|-------------|------------|------|
| **Critical** | `[INSERT_PROJECT_NAME]` | Your project name | 2 min |
| **Critical** | `[INSERT_DOMAIN]` | Your app domain | 2 min |
| **Critical** | `[INSERT_TECH_STACK]` | Your technology stack | 3 min |
| **Important** | `[INSERT_TEAM_SIZE]` | Your team size | 2 min |
| **Important** | `[INSERT_DATABASE_TYPE]` | Your database | 2 min |
| Standard | `[INSERT_COMPANY_NAME]` | Your organization | 2 min |
| Standard | `[INSERT_CI_CD_PLATFORM]` | Your CI/CD tool | 2 min |
| Standard | `[INSERT_CLOUD_PROVIDER]` | Your cloud platform | 2 min |
| Optional | 7 remaining placeholders | Various | 10 min |

```bash
# 3. Use validation to check progress
/validate-adaptation
```

### Phase 3: Cleanup and Optimization (15 minutes)
```bash
# 1. Archive deprecated commands (38 files)
mkdir .claude/commands/archive
mv .claude/commands/deprecated/* .claude/commands/archive/

# 2. Remove unused domain-specific commands
# Example: If not doing data science
rm -rf .claude/commands/data-science/

# 3. Archive complex commands you won't use initially
mv .claude/commands/specialized/* .claude/commands/archive/

# 4. Final validation
./.claude/validate.sh  # Should show 100% readiness

# 5. Document your choices
/share-adaptation > CLAUDE-ADAPTATION-NOTES.md
```

**Result**: Production-ready Claude Code templates customized for your project in 1 hour.

---

## 🎯 Essential Commands to Try First

### Core Workflow Commands
```bash
/help               # List all your customized commands
/task "user login"  # Break down complex tasks with your tech stack
/auto "debug error" # Smart routing to appropriate helpers
/query "how to..."  # Project-specific Q&A
```

### Development Commands
```bash
/dev                # Development workflow guidance
/api-design         # API design patterns for your stack
/db-migrate         # Database migration guidance
```

### Quality Commands
```bash
/test-unit          # Unit testing guidance
/analyze-code       # Code analysis and improvements
/secure-audit       # Security assessment
```

---

## 🛠️ Troubleshooting Quick Fixes

### "Commands don't appear in Claude Code"
```bash
# 1. Check location
pwd                 # Should be project root
ls -la .claude/     # Should exist

# 2. Restart Claude Code completely
# 3. Try: /help
```

### "Too many placeholders to replace"
```bash
# Focus on critical ones first:
grep -r "INSERT_PROJECT_NAME" .claude/commands/ | wc -l
grep -r "INSERT_DOMAIN" .claude/commands/ | wc -l
grep -r "INSERT_TECH_STACK" .claude/commands/ | wc -l

# Replace these 3 first, others can wait
```

### "Setup script failed"
```bash
chmod +x setup.sh
./setup.sh

# If still fails:
git submodule update --init --recursive
```

---

## 📈 Progressive Enhancement Path

### Week 1: Basic Usage
- Use core commands: `/help`, `/task`, `/auto`, `/query`
- Replace critical placeholders
- Remove unused commands

### Week 2: Team Adoption
- Share with team members
- Create team-specific commands in `.claude/commands/team/`
- Document common workflows

### Month 1: Advanced Features
- Add back specialized commands as needed
- Customize complex workflows
- Contribute improvements to community

### Ongoing: Maintenance
- Monthly: Check for template updates
- Quarterly: Review and optimize command set
- As needed: Add project-specific commands

---

## 🎯 Success Criteria

### After 10 Minutes
- [ ] `/help` shows your available commands
- [ ] `/task` provides project-specific guidance
- [ ] Basic placeholders replaced in core commands

### After 1 Hour
- [ ] All 15 standard placeholders replaced
- [ ] Unused commands archived
- [ ] Validation shows 100% completion
- [ ] Team documentation created

### After 1 Week
- [ ] Team members successfully using templates
- [ ] Common workflows documented
- [ ] Project-specific commands added

---

## 🚨 When to Get Help

### Self-Service First
1. Run `./.claude/validate.sh` for diagnostics
2. Check `FAQ.md` for common issues
3. Use `/validate-adaptation` for guidance

### Get Community Help When
- Validation fails after following all guides
- Team members can't replicate your setup
- Templates don't fit your specific domain
- You want to contribute improvements

### Support Channels
- **GitHub Issues**: Technical problems and bugs
- **GitHub Discussions**: Questions and best practices
- **Documentation**: `INSTALLATION.md`, `FAQ.md`, `EXAMPLES.md`

---

## 🎉 Quick Wins

### Immediate Value (First 10 Minutes)
- **Task Breakdown**: `/task` gives structured approach to complex work
- **Smart Routing**: `/auto` directs you to right tools and approaches
- **Context Awareness**: Commands understand your project type and tech stack

### Short-term Value (First Hour)
- **Team Consistency**: Everyone uses same proven patterns
- **Anti-Pattern Prevention**: Built-in warnings about common mistakes
- **Quality Assurance**: Structured approaches to testing and security

### Long-term Value (First Month)
- **Reduced Learning Curve**: Skip months of prompt engineering trial-and-error
- **Improved Productivity**: Faster development with proven workflows
- **Knowledge Sharing**: Team builds collective prompt engineering expertise

---

**Next Steps**: 
1. Complete the 10-minute setup above
2. Try the essential commands
3. When ready, invest the full hour for complete customization
4. Share your success with the community!

---

*Remember: The goal is getting value quickly, then improving gradually. Start simple, add complexity as needed.*