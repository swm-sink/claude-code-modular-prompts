# 🚀 Installation Guide - Claude Context Architect

**Complete Installation and Customization Guide** - Everything you need to know to successfully install and customize the Claude Context Architect for your project.

## 📋 Pre-Installation Checklist

**Before you begin, ensure you have:**

- [ ] **Claude Code** installed and working
- [ ] **Git** installed (`git --version` should work)
- [ ] **Text editor** with Find & Replace capability
- [ ] **Project directory** where you want to install templates
- [ ] **1-2 hours** of focused time for customization
- [ ] **Clear understanding** of your project's:
  - Tech stack (e.g., "React/Node.js/PostgreSQL")
  - Domain (e.g., "e-commerce", "data-science", "fintech")
  - Team size (e.g., "5-person", "solo", "20+ engineers")
  - Deployment approach (e.g., "AWS", "Kubernetes", "Vercel")

---

## 🛠️ Installation Methods

### Method 1: Git Submodule (Recommended)

**Best for**: Projects that want to receive template updates

**Pros**: Easy updates, clean git history, reference preservation  
**Cons**: Requires git submodule knowledge  
**Time**: 5 minutes setup + 45-90 minutes customization

```bash
# Step 1: Navigate to your project root
cd /path/to/your/project

# Step 2: Add context engineering system as submodule
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Step 3: Initialize the templates
cd .claude-framework
./setup.sh

# Step 4: Return to project root
cd ..

# Step 5: Verify installation
ls -la .claude/
ls -la .claude-framework/
```

**Result**: Dual structure with customizable `.claude/` and reference `.claude-framework/`

### Method 2: Direct Clone & Copy

**Best for**: Projects that want full control without submodules

**Pros**: Full ownership, no submodule complexity  
**Cons**: Manual updates, larger repository  
**Time**: 5 minutes setup + 45-90 minutes customization

```bash
# Step 1: Clone the context engineering system
git clone https://github.com/swm-sink/claude-code-modular-prompts

# Step 2: Run integration script
cd claude-code-modular-prompts
./setup.sh /path/to/your/project

# Step 3: Navigate to your project
cd /path/to/your/project

# Step 4: Verify installation
ls -la .claude/
ls -la .claude-framework/

# Step 5: Clean up (optional)
rm -rf /path/to/claude-code-modular-prompts
```

### Method 3: Selective Integration

**Best for**: Projects that want only specific commands

**Pros**: Minimal footprint, maximum control  
**Cons**: Manual selection process, limited updates  
**Time**: 10 minutes setup + 30-60 minutes customization

```bash
# Step 1: Clone temporarily
git clone https://github.com/swm-sink/claude-code-modular-prompts temp-templates

# Step 2: Create your .claude structure
cd /path/to/your/project
mkdir -p .claude/{commands,components,context,config}

# Step 3: Copy only what you need
cp temp-templates/.claude/commands/core/*.md .claude/commands/
cp temp-templates/.claude/commands/development/*.md .claude/commands/
# ... copy other directories as needed

# Step 4: Copy essential context
cp temp-templates/.claude/context/*.md .claude/context/

# Step 5: Clean up
rm -rf temp-templates
```

---

## 🎯 Post-Installation Customization

### Step 1: Start Claude Code and Get Guidance

```bash
# In your project directory, start Claude Code
# Then run the adaptation command:
/adapt-to-project
```

**This command will:**
- Ask about your project's tech stack, domain, and team size
- Generate a customization checklist with specific instructions
- List all placeholders that need replacement
- Provide validation steps

### Step 2: Manual Placeholder Replacement

You'll need to replace 15 standard placeholders using Find & Replace in your editor:

| Placeholder | Your Value Example | Files Affected |
|-------------|-------------------|----------------|
| `[INSERT_PROJECT_NAME]` | "EcommerceAPI" | ~40 command files |
| `[INSERT_DOMAIN]` | "e-commerce" | ~35 command files |
| `[INSERT_TECH_STACK]` | "React/Node.js/PostgreSQL" | ~30 command files |
| `[INSERT_TEAM_SIZE]` | "5-person" | ~15 command files |
| `[INSERT_COMPANY_NAME]` | "TechStartup Inc" | ~10 files |
| `[INSERT_DATABASE_TYPE]` | "PostgreSQL" | ~8 database commands |
| `[INSERT_CI_CD_PLATFORM]` | "GitHub Actions" | ~6 DevOps commands |
| `[INSERT_CLOUD_PROVIDER]` | "AWS" | ~8 deployment commands |
| `[INSERT_TEST_FRAMEWORK]` | "Jest" | ~5 testing commands |
| `[INSERT_MONITORING_PLATFORM]` | "DataDog" | ~4 monitoring commands |
| `[INSERT_COMPLIANCE_REQUIREMENTS]` | "PCI-DSS" | ~3 security commands |
| `[INSERT_VERSION_CONTROL]` | "GitHub" | ~5 commands |
| `[INSERT_DEPLOYMENT_SCHEDULE]` | "weekly" | ~3 DevOps commands |
| `[INSERT_DOCUMENTATION_TOOL]` | "Docusaurus" | ~2 commands |
| `[INSERT_CONTAINER_PLATFORM]` | "Docker/Kubernetes" | ~4 commands |

**Total replacement tasks**: ~150-200 individual replacements across 64 active commands

### Step 3: Editor-Specific Instructions

#### VS Code
1. Open your project folder
2. Press `Ctrl+Shift+H` (Windows/Linux) or `Cmd+Shift+H` (Mac)
3. In "Find" field: `[INSERT_PROJECT_NAME]`
4. In "Replace" field: `YourProjectName`
5. Click "Replace All"
6. Repeat for all 15 placeholders

#### IntelliJ/WebStorm
1. Open project
2. Press `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
3. Scope: "Whole project"
4. Find/Replace each placeholder
5. Review changes before applying

#### Sublime Text
1. Open project folder
2. Press `Ctrl+Shift+F` (Windows/Linux) or `Cmd+Shift+F` (Mac)
3. Use "Replace" tab
4. Set "Where" to your `.claude` folder
5. Replace each placeholder

### Step 4: Remove Unused Commands

**Commands to consider removing:**

```bash
# Archive deprecated commands (38 files)
mkdir .claude/commands/archive
mv .claude/commands/deprecated/* .claude/commands/archive/

# Remove domain-specific commands you don't need
# For example, if not doing data science:
rm -rf .claude/commands/data-science/

# Remove specialized commands if not applicable
ls .claude/commands/specialized/
# Keep only what's relevant
```

### Step 5: Validate Your Customization

```bash
# Run validation script
./.claude/validate.sh

# Or use Claude Code command
/validate-adaptation
```

**Validation checks:**
- [ ] All placeholders replaced (0 remaining)
- [ ] Project configuration updated
- [ ] Unused commands removed
- [ ] Essential commands present and working
- [ ] Context files properly configured

---

## 🐛 Troubleshooting Guide

### Common Installation Issues

#### Issue: "setup.sh: Permission denied"
```bash
# Solution: Make script executable
chmod +x setup.sh
./setup.sh
```

#### Issue: "No such file or directory"
```bash
# Check if you're in the right directory
pwd
ls -la setup.sh

# If not found, you might be in wrong directory
cd .claude-framework  # For submodule method
./setup.sh
```

#### Issue: "Git submodule failed"
```bash
# Initialize git repository first
git init
git add .
git commit -m "Initial commit"

# Then try submodule again
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
```

#### Issue: "Claude Code doesn't see commands"
**Troubleshooting steps:**
1. Verify `.claude/` is in your project root directory
2. Check that command files have proper YAML frontmatter:
   ```yaml
   ---
   name: /command-name
   description: Command description
   ---
   ```
3. Ensure files end with `.md` extension
4. Restart Claude Code after installation

### Common Customization Issues

#### Issue: "Too many placeholders to replace"
```bash
# Use /replace-placeholders command for checklist
/replace-placeholders

# Or focus on essential placeholders first:
# 1. PROJECT_NAME (most critical)
# 2. DOMAIN (affects categorization)  
# 3. TECH_STACK (affects command behavior)
# 4. Others can be done gradually
```

#### Issue: "Find & Replace affecting wrong files"
**Solutions:**
- Limit search scope to `.claude/commands/` directory only
- Use exact placeholder matching (e.g., `[INSERT_PROJECT_NAME]` not `PROJECT_NAME`)
- Review changes before applying
- Work on one placeholder at a time

#### Issue: "Commands feel overwhelming"
```bash
# Start minimal - keep only core commands
mkdir .claude/commands/archive
mv .claude/commands/specialized/* .claude/commands/archive/
mv .claude/commands/deprecated/* .claude/commands/archive/

# Keep only these essential directories:
# - core/ (help, task, auto, query)
# - development/ (your main workflow)
# - Add others back gradually as needed
```

#### Issue: "Validation shows errors"
**Common fixes:**
```bash
# Check for missed placeholders
grep -r "INSERT_" .claude/commands/

# Update project configuration
vim .claude/config/project-config.yaml

# Verify essential commands exist
ls .claude/commands/core/
# Should show: help.md, task.md, auto.md, query.md
```

### Performance Issues

#### Issue: "Claude Code loads slowly"
**Causes & Solutions:**
- **Too many commands**: Archive unused ones
- **Large command files**: Simplify complex commands
- **Missing optimization**: Check `.claude/context/` files are present

```bash
# Quick optimization
find .claude/commands -name "*.md" -size +50k -exec ls -lh {} \;
# Review and simplify large files

# Archive unused commands
mv .claude/commands/specialized .claude/commands/archive/
```

---

## 🎯 Success Verification

### Checklist: Installation Complete
- [ ] `.claude/` directory exists in project root
- [ ] `.claude-framework/` directory exists (for submodule method)
- [ ] `/help` command works in Claude Code
- [ ] `/task` command provides project-specific guidance
- [ ] No placeholders remain (`grep -r "INSERT_" .claude/commands/` returns nothing)
- [ ] Project configuration reflects your actual setup
- [ ] Validation script passes all checks

### Checklist: Customization Complete
- [ ] All 15 standard placeholders replaced with your values
- [ ] Unused commands archived or removed
- [ ] Domain-specific commands customized for your tech stack
- [ ] Team members can use commands successfully
- [ ] Commands provide relevant, project-specific guidance
- [ ] Documentation updated with your customizations

### Test Your Installation
```bash
# In Claude Code, test these commands:
/help                    # Should list your customized commands
/task "add user login"   # Should provide project-specific guidance
/adapt-to-project        # Should show "already adapted" status
/validate-adaptation     # Should report 100% completion
```

---

## 🚀 Next Steps After Installation

### 1. Team Onboarding
```bash
# Share with team members
git add .claude/
git commit -m "Add Claude Code templates for [PROJECT_NAME]"
git push

# Team members run:
git pull
git submodule update --init  # If using submodules
```

### 2. Create Team Documentation
```bash
# Document your customization choices
/share-adaptation > CLAUDE-ADAPTATION-NOTES.md
git add CLAUDE-ADAPTATION-NOTES.md
git commit -m "Document Claude Code template customizations"
```

### 3. Regular Updates
```bash
# For submodule installations, check for updates monthly:
cd .claude-framework
git pull origin main
/sync-from-reference  # Follow merge guidance
```

### 4. Continuous Improvement
- Monitor which commands your team uses most
- Remove unused commands to reduce cognitive load
- Add project-specific commands to `.claude/commands/team/`
- Share useful patterns with the community

---

## 📞 Getting Help

### Self-Service Options
1. **Check FAQ**: `FAQ.md` covers 90% of common issues
2. **Run diagnostics**: `./claude/validate.sh` identifies most problems
3. **Use guide commands**: `/validate-adaptation`, `/replace-placeholders`

### Community Support
- **GitHub Issues**: Bug reports and technical problems
- **GitHub Discussions**: Questions and best practices
- **Examples**: `EXAMPLES.md` shows real customization patterns

### Emergency Recovery
```bash
# If something goes wrong, you can always start over:
rm -rf .claude/
cd .claude-framework
./setup.sh  # Fresh installation

# Or restore from backup (created automatically):
cp -r .claude-backup-TIMESTAMP/ .claude/
```

---

**Estimated Total Time Investment:**
- **Setup**: 5-10 minutes
- **Customization**: 45-90 minutes (depending on project complexity)
- **Team Training**: 15-30 minutes per team member
- **Total**: 1-2.5 hours for complete project setup

**Return on Investment**: Saves 3-6 months of prompt engineering trial-and-error

---

*Last updated: 2025-07-29*  
*Questions? See [FAQ.md](FAQ.md) or [create an issue](https://github.com/swm-sink/claude-code-modular-prompts/issues)*