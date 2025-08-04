# ⚡ Quick Start Guide - Get Running in 2 Minutes

**Goal**: Get Claude Context Architect installed and context engineering system configured with minimal effort.  
**Time**: 2 minutes to fully functional, context-aware commands.

---

## 🎯 2-Minute Automated Setup

### Step 1: Install Context Engineering System (1 minute)
```bash
# Navigate to your project
cd /path/to/your/project

# Add context engineering system as git submodule
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Run automated setup
cd .claude-framework && ./setup.sh && cd ..
```

### Step 2: Configure Context Engineering for Your Project (1 minute)
```bash
# Start Claude Code and run the auto-configuration command:
/adapt-to-project

# Answer a few quick questions about your project:
# - Project name?
# - Domain (web-app, data-science, etc.)?
# - Tech stack?
# - Team size?

# The system configures context engineering patterns for your project
```

**Result**: Fully configured Claude Context Architect working with your specific project context in 2 minutes.

## ✅ Verify Your Setup

After the 2-minute setup, test your context-aware commands:

```bash
# Verify installation
ls -la .claude/commands/core/  # Should show context-aware commands

# Test core functionality in Claude Code:
/help        # Shows your context-aware command list
/task        # Provides task breakdown using your tech stack
/auto        # Smart routing based on your project domain
/query       # Project-aware Q&A
```

**Success**: Commands now use context engineering patterns with your project name, tech stack, and domain-specific knowledge.

---

## 🎯 Essential Commands to Try First

### Core Workflow Commands
```bash
/help               # List all your context-aware commands
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

### "/adapt-to-project didn't work"
```bash
# 1. Ensure you're in Claude Code, not terminal
# 2. Run the setup script again:
cd .claude-framework && ./setup.sh && cd ..

# 3. Try the adaptation command again
```

### "Setup script failed"
```bash
chmod +x setup.sh
./setup.sh

# If still fails:
git submodule update --init --recursive
```

---

## 📈 What's Next?

### Immediate Usage (Day 1)
- Start with core commands: `/help`, `/task`, `/auto`, `/query`
- All commands are already customized for your project
- Share the setup process with your team

### Weekly Optimization (Week 1)
- Add team-specific commands in `.claude/commands/team/`
- Document your most-used workflows
- Archive any specialized commands you don't need

### Ongoing Enhancement
- Monthly: Check for template updates with `/sync-from-reference`
- As needed: Create project-specific command variations
- Quarterly: Share improvements with the community

---

## 🎯 Success Criteria

### After 2 Minutes
- [ ] `/help` shows your context-aware command list
- [ ] `/task` provides guidance using your tech stack
- [ ] Commands use context engineering patterns with your project name and domain
- [ ] No manual placeholder replacement needed

### After 1 Week
- [ ] Team members using the same automated setup
- [ ] Common workflows documented
- [ ] Project-specific commands added as needed

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

## 🎉 Immediate Benefits

### What You Get in 2 Minutes
- **Context-Aware Commands**: All patterns automatically configured for your tech stack
- **Smart Task Breakdown**: `/task` understands your project domain and tools
- **Context Engineering Guidance**: Commands use deep context understanding of your actual project
- **Context Engineering Setup**: Automated context configuration with minimal manual work

### Why This Matters
- **Skip the Learning Curve**: Months of prompt engineering trial-and-error eliminated
- **Team Ready**: Everyone gets the same automated setup experience
- **Production Quality**: Anti-patterns and best practices built in from day one

---

**Next Steps**: 
1. Complete the 2-minute setup above
2. Try `/help`, `/task`, `/auto`, and `/query`
3. Share the automated setup with your team
4. Start building with confidence!

---

*The goal is instant value with zero complexity. Setup once, benefit immediately.*