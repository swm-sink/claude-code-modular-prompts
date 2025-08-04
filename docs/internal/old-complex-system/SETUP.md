# 🚀 Claude Context Architect Setup Guide
## Realistic Timeline: 1-2 Hours to Production-Ready Context System

**Time Required**: 1-2 hours (5 min setup + 45-90 min customization)  
**Result**: Claude Context Architect system with anti-pattern prevention

---

## Prerequisites

- **Git installed** (`git --version` should work)
- **Claude Code access** (Desktop app or API)
- **Text editor** with Find & Replace (VS Code, IntelliJ, Sublime, etc.)
- **Project directory** where templates will be installed
- **1-2 hours** of focused time for proper customization
- **Clear project requirements**: tech stack, domain, team size

---

## Quick Start (2 Methods)

### Method 1: Git Submodule (Recommended)

Best for: Projects that want to receive system updates

**Pros**: Easy updates, clean separation, reference preservation  
**Cons**: Requires git submodule knowledge  
**Time**: 5 minutes setup + 45-90 minutes customization

```bash
# 1. Navigate to your project root
cd /path/to/your/project

# 2. Add context engineering system as submodule
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# 3. Initialize the templates
cd .claude-framework
./setup.sh
# Follow interactive prompts for integration method

# 4. Return to project and verify
cd ..
ls -la .claude/         # Your customizable context system
ls -la .claude-framework/ # Reference system (read-only)
```

### Method 2: Direct Integration

Best for: Projects that want full control without submodules

**Pros**: Full ownership, no submodule complexity  
**Cons**: Manual updates required  
**Time**: 5 minutes setup + 45-90 minutes customization

```bash
# 1. Clone the context engineering system
git clone https://github.com/swm-sink/claude-code-modular-prompts

# 2. Run integration script
cd claude-code-modular-prompts
./setup.sh /path/to/your/project
# Choose "Direct Copy" when prompted

# 3. Navigate to your project and verify
cd /path/to/your/project
ls -la .claude/         # Your context system
ls -la .claude-framework/ # Reference copy
```

---

## What Gets Installed

```
your-project/
├── .claude/                    # Your customizable workspace
│   ├── commands/              # 102 command templates (64 active, 38 deprecated)
│   │   ├── core/             # help, task, auto, query
│   │   ├── development/      # dev, api-design, dev-setup
│   │   ├── database/         # db-migrate, db-backup, db-restore, db-seed
│   │   ├── security/         # secure-audit, secure-scan
│   │   ├── testing/          # test-unit, test-integration
│   │   ├── devops/           # deploy, ci-setup, ci-run, cd-rollback
│   │   ├── quality/          # analyze-code, analyze-system, monitor
│   │   ├── monitoring/       # monitor-setup, monitor-alerts
│   │   ├── meta/             # adapt-to-project, validate-adaptation
│   │   └── deprecated/       # 38 deprecated commands (remove if unused)
│   ├── components/           # 70 reusable prompt components
│   ├── context/              # Anti-patterns, best practices, frameworks
│   ├── docs/                 # Documentation and guides
│   └── config/
│       └── project-config.yaml # Configuration template
├── .claude-framework/          # Reference library (read-only)
│   └── [original templates]    # Preserved for updates and reference
└── CLAUDE.md                   # Project memory file
```

---

## Post-Setup Customization Process

**IMPORTANT**: The real work begins after installation. You must manually customize the templates.

### Step 1: Get Customization Guidance (10 minutes)
```bash
# Start Claude Code and run:
/adapt-to-project

# This will:
# - Ask about your tech stack, domain, team size
# - Generate a replacement checklist
# - List all placeholders that need updating
# - Provide validation steps
```

### Step 2: Manual Placeholder Replacement (45-90 minutes)
You'll need to use Find & Replace in your editor to update:

**15 Standard Placeholders** (affects ~150-200 replacements across 64 commands):
- `[INSERT_PROJECT_NAME]` → Your project name
- `[INSERT_DOMAIN]` → Your application domain (e.g., "e-commerce")
- `[INSERT_TECH_STACK]` → Your technology stack
- `[INSERT_TEAM_SIZE]` → Your team size
- `[INSERT_DATABASE_TYPE]` → Your database system
- Plus 10 more specialized placeholders

**Editor Instructions**:
- **VS Code**: Ctrl+Shift+H (project-wide Find & Replace)
- **IntelliJ**: Ctrl+Shift+R (Replace in Path)
- **Sublime**: Ctrl+Shift+F (Find in Files → Replace)

### Step 3: Remove Unused Commands (15 minutes)
```bash
# Archive deprecated commands (38 files)
mkdir .claude/commands/archive
mv .claude/commands/deprecated/* .claude/commands/archive/

# Remove domain-specific commands you don't need
# Example: If not doing data science
rm -rf .claude/commands/data-science/
```

---

### Step 4: Validate Your Work (10 minutes)
```bash
# Run validation script
./.claude/validate.sh

# Or use Claude Code command
/validate-adaptation

# Should show:
# ✅ All placeholders replaced
# ✅ Project configured  
# ✅ Readiness Score: 100%
```

### Step 5: Team Documentation (15 minutes)
```bash
# Document your customizations
/share-adaptation > CLAUDE-ADAPTATION-NOTES.md

# Commit your work
git add .claude/ CLAUDE.md CLAUDE-ADAPTATION-NOTES.md
git commit -m "Add customized Claude Code templates for [PROJECT_NAME]"
```

## Advanced Customization Options

### Add Project-Specific Commands
```bash
# Create team-specific commands
mkdir .claude/commands/team
cat > .claude/commands/team/deploy-staging.md << 'EOF'
---
name: /deploy-staging
description: Deploy to staging environment
---

Deploy [PROJECT_NAME] to staging using [CI_CD_PLATFORM]...
EOF
```

### Configure Domain-Specific Anti-Patterns
```bash
# Add to existing anti-pattern files
echo "## Project-Specific Anti-Patterns" >> .claude/context/llm-antipatterns.md
echo "- Deploying without running tests" >> .claude/context/llm-antipatterns.md
```

---

## Updating Templates (For Future Versions)

### If Using Git Submodule
```bash
# Check for updates monthly
cd .claude-framework
git pull origin main

# Use sync command for guided merge
/sync-from-reference
# Follow the manual merge instructions provided
```

### If Using Direct Integration
```bash
# Manual update process
# 1. Backup your customizations
cp -r .claude/ .claude-backup-$(date +%Y%m%d)

# 2. Check what's new in the repository
git clone https://github.com/swm-sink/claude-code-modular-prompts temp-update
cd temp-update
git log --oneline --since="2025-07-01"  # Check recent changes

# 3. Manually merge beneficial changes
# 4. Re-apply your customizations
# 5. Clean up
cd .. && rm -rf temp-update
```

---

## Success Verification

### 1. Structure Check
```bash
# Verify dual structure exists
ls -la .claude/                # Your customizable workspace
ls -la .claude-framework/      # Reference library

# Check command count
find .claude/commands -name "*.md" | wc -l  # Should show ~64 active commands
find .claude/components -name "*.md" | wc -l  # Should show ~70 components
```

### 2. Claude Code Integration Test
```bash
# In Claude Code, test these commands:
/help                          # Should list your commands
/task "add user authentication" # Should give project-specific guidance
/adapt-to-project              # Should show "already adapted" status
```

### 3. Customization Verification
```bash
# Check that placeholders were replaced
grep -r "INSERT_" .claude/commands/ | wc -l  # Should be 0

# Verify project configuration
cat .claude/config/project-config.yaml       # Should show your values

# Test validation
./.claude/validate.sh                        # Should report 100% readiness
```

### 4. Anti-Pattern Prevention Check
```bash
# Verify context files are present
ls .claude/context/
# Should include:
# - llm-antipatterns.md (48+ documented patterns)
# - git-history-antipatterns.md (15+ patterns)
# - prompt-engineering-best-practices.md
```

---

## Troubleshooting Common Issues

### Setup Issues

**"setup.sh: Permission denied"**
```bash
chmod +x setup.sh
./setup.sh
```

**"Git submodule failed"**
```bash
# Initialize git repository first if needed
git init
git add .
git commit -m "Initial commit"

# Then add submodule
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
```

**"Commands don't appear in Claude Code"**
1. Verify `.claude/` is in project root directory
2. Check command files have YAML frontmatter:
   ```yaml
   ---
   name: /command-name
   description: Brief description
   ---
   ```
3. Restart Claude Code after installation

### Customization Issues

**"Too many placeholders to replace"**
```bash
# Use the guide command for a checklist
/replace-placeholders

# Start with essential placeholders only:
# 1. PROJECT_NAME (most critical)
# 2. DOMAIN (affects command behavior)
# 3. TECH_STACK (affects technical guidance)
```

**"Find & Replace affecting wrong files"**
- Limit search scope to `.claude/commands/` directory only
- Use exact placeholder text (including brackets)
- Review changes before applying
- Work on one placeholder at a time

**"Commands feel overwhelming"**
```bash
# Start minimal - archive most commands
mkdir .claude/commands/archive
mv .claude/commands/specialized/* .claude/commands/archive/
mv .claude/commands/deprecated/* .claude/commands/archive/

# Keep only core commands initially:
# - core/ (help, task, auto, query)
# - development/ (basic dev workflow)
# Add others back gradually
```

### Performance Issues

**"Claude Code loads slowly"**
```bash
# Check for oversized command files
find .claude/commands -name "*.md" -size +50k -exec ls -lh {} \;

# Archive unused commands
mv .claude/commands/deprecated .claude/commands/archive/

# Simplify complex commands if needed
```

---

## Next Steps

1. **Read Anti-Patterns First**
   - `.claude/context/llm-antipatterns.md`
   - `.claude/context/git-history-antipatterns.md`
   - Learn from others' mistakes

2. **Start with Core Commands**
   - `/help` - Discover commands
   - `/task` - TDD workflow
   - `/auto` - Smart routing

3. **Customize Gradually**
   - Don't modify everything at once
   - Test changes in Claude
   - Keep what works

4. **Contribute Back**
   - Share useful patterns
   - Report issues
   - Submit improvements

---

## Support Resources

### Self-Service (Recommended First)
- **FAQ**: `FAQ.md` - Covers 90% of common questions
- **Examples**: `EXAMPLES.md` - Real customization patterns
- **Installation Guide**: `INSTALLATION.md` - Comprehensive step-by-step instructions
- **Validation**: Run `./claude/validate.sh` for automated diagnostics

### Community Support
- **GitHub Issues**: Bug reports and technical problems
- **GitHub Discussions**: Questions, best practices, sharing patterns
- **Documentation**: Comprehensive guides and troubleshooting

### Emergency Recovery
```bash
# If something goes wrong, start fresh:
rm -rf .claude/
cd .claude-framework && ./setup.sh

# Or restore from automatic backup:
cp -r .claude-backup-TIMESTAMP/ .claude/
```

---

## Time Investment Summary

**Total Setup Time**: 1-2 hours broken down as:
- **Initial installation**: 5-10 minutes
- **Customization planning**: 10-15 minutes (/adapt-to-project)
- **Placeholder replacement**: 45-90 minutes (depending on project complexity)
- **Cleanup and validation**: 15-30 minutes
- **Team documentation**: 15 minutes

**Return on Investment**: Saves 3-6 months of prompt engineering trial-and-error

**Next Steps**:
1. Complete the customization process thoroughly
2. Train your team on the available commands
3. Monitor usage and remove unused commands
4. Share useful patterns with the community

*You now have battle-tested Claude Code templates ready for production use!*