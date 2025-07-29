---
name: /welcome
description: "Interactive onboarding guide for new Claude Code Adaptation Engine users"
usage: /welcome [--quick|--detailed] [--role developer|lead|architect]
category: meta-commands
tools: Read, Write
---

# 👋 Welcome to Claude Code Prompt Templates!

## 🎯 What This Actually Is

**I'm a guide to help you manually customize prompt templates.** This is a collection of 102 Claude Code command templates (64 active, 38 deprecated) that you'll adapt for your project through:
- 📋 Manual placeholder replacement
- 🔧 Copy-paste configurations
- 📝 Step-by-step customization guides
- ✅ Validation checklists

## ⚠️ What This Is NOT
- ❌ Not an automated "engine" that adapts itself
- ❌ Not a tool that detects your tech stack
- ❌ Not a system that configures itself in 5 minutes
- ❌ Not magic - it's manual work with good guidance

## 🚀 What You'll Actually Do

### The Manual Process
1. **Answer questions** about your project setup
2. **Receive a guide** with all needed replacements
3. **Manually edit** files to replace placeholders
4. **Copy configurations** I provide into your project
5. **Use checklists** to verify your work

### Time Investment
- **Realistic time**: 30-60 minutes of manual work
- **Not 5 minutes** - that's just to answer initial questions
- **Value**: Skip months of learning what works/doesn't

## 📋 Manual Setup Check

Please verify these manually:

```bash
# Check if framework is present
ls -la .claude-framework/
ls -la .claude/

# Count available commands
find .claude/commands -name "*.md" | wc -l
```

**You should see:**
- [ ] `.claude-framework/` directory (reference copy)
- [ ] `.claude/` directory (your working copy)
- [ ] 102 command files ready for manual customization (64 active, 38 deprecated)

## 🎯 Choose Your Approach

### 🏃 Quick Reference (Get replacement list fast)
```
/adapt-to-project
```
- Answer basic questions (5 min)
- Get complete replacement guide
- Start manual editing immediately

### 🚶 Guided Learning (Understand what you're doing)
```
/adapt-to-project --guided
```
- Learn why each placeholder exists (15 min)
- Understand customization impact
- Make informed choices

### 🎓 Deep Dive (Master the framework)
Best for team leads who'll train others:
- Read `.claude/context/` documentation
- Study anti-patterns to avoid
- Review all command categories
- Understand architectural decisions

## 🏗️ The Manual Process Explained

1. **You Tell Me About Your Project**
   - What tech stack you use
   - Your domain (web, data science, etc.)
   - Team size and workflow

2. **I Generate Replacement Guides**
   ```
   File: .claude/commands/core/task.md
   - Line 23: Replace "[INSERT_PROJECT_NAME]" with "YourApp"
   - Line 45: Replace "[INSERT_TESTING_FRAMEWORK]" with "Jest"
   ```

3. **You Manually Update Files**
   - Open each file in your editor
   - Find & Replace as instructed
   - Save your changes

4. **Validate Your Work**
   ```bash
   # Check for missed placeholders
   grep -r "\[INSERT_" .claude/
   ```

## 📊 What You Get

After adaptation, you'll have:
- ✅ **Customized Commands**: Tailored to your project
- ✅ **Anti-Pattern Protection**: Avoid common mistakes
- ✅ **Team Workflows**: Configured for your process
- ✅ **Domain Expertise**: Industry-specific patterns

## 🎮 See Example Output

Want to see what you'll get? Here's a sample:

**Before customization:**
```markdown
# Task for [INSERT_PROJECT_NAME]
Run tests with [INSERT_TESTING_FRAMEWORK]
```

**After your manual replacement:**
```markdown
# Task for MyAwesomeApp
Run tests with Jest
```

**What you'll do:**
1. Open `.claude/commands/core/task.md`
2. Find "[INSERT_PROJECT_NAME]"
3. Replace with "MyAwesomeApp"
4. Save the file
5. Repeat for all placeholders

## 💡 First-Timer Tips

### Before You Start:
1. **Make a backup**: `cp -r .claude .claude.backup`
2. **Use version control**: `git add . && git commit -m "Before adaptation"`
3. **Have project details ready**: Name, tech stack, team size
4. **Set aside time**: 30-60 minutes for full customization

### Don't Worry About:
- Getting everything perfect first try
- Understanding all 102 commands immediately
- Complex nested placeholders (I'll explain)
- Making mistakes (you have backups!)

## 🛟 Safety Net

### Manual Recovery Options:
- **Git revert**: `git checkout -- .claude/`
- **Backup restore**: `cp -r .claude.backup/* .claude/`
- **Start fresh**: Copy from `.claude-framework/`
- **Get help**: `/undo-adaptation` for recovery guide

## 🚀 Ready to Begin?

Start your manual customization journey:

1. **Get replacement guide** → `/adapt-to-project`
2. **Learn while doing** → `/adapt-to-project --guided`
3. **Check your work** → `/validate-adaptation`
4. **Need help?** → `/help [command-name]`

## 📈 Realistic Expectations

What you'll achieve:
- **Manual work required**: 30-60 minutes
- **Commands to customize**: 102 templates (64 active, 38 deprecated)
- **Placeholders to replace**: ~200 across all files
- **Value**: Curated patterns that prevent common mistakes

What this saves you:
- Learning which patterns work/fail
- Discovering Claude Code quirks
- Building command library from scratch
- Finding and fixing anti-patterns

## 🤝 Getting Support

- **Replacement help**: `/replace-placeholders`
- **Recovery guide**: `/undo-adaptation`
- **Validation**: `/validate-adaptation`
- **Command help**: `/help [command-name]`

---

**Let's start your customization!**

Tell me:
1. Your project name
2. Your domain (web-dev, data-science, devops, etc.)
3. Your main tech stack

Or run `/adapt-to-project` to begin the guided process.