# 🚀 Claude Code Framework Setup Guide
## 5 Minutes to Your Custom Foundation

**Time Required**: 5-10 minutes  
**Result**: Professional Claude Code foundation with 6+ months of knowledge

---

## Prerequisites

- Git installed
- Claude Code access
- A project that needs Claude Code integration

---

## Quick Start (2 Methods)

### Method 1: Git Submodule (Recommended)

Best for: Projects that want to receive framework updates

```bash
# 1. Navigate to your project root
cd my-awesome-project

# 2. Add framework as submodule
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# 3. Initialize the framework
cd .claude-framework
./setup.sh --project-name "my-awesome-project"

# 4. Your .claude directory is now configured!
cd ..
ls -la .claude/
```

### Method 2: Direct Integration

Best for: Projects that want full control

```bash
# 1. Clone the framework
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts

# 2. Run adaptation script
./adapt.sh --target ../my-awesome-project --profile web-dev

# 3. Framework is now integrated into your project
cd ../my-awesome-project
ls -la .claude/
```

---

## What Gets Installed

```
your-project/
├── .claude/                    # Your Claude Code configuration
│   ├── commands/              # Selected command patterns
│   │   ├── core/             # Essential commands (help, task, auto)
│   │   └── [your-domain]/    # Domain-specific commands
│   ├── components/           # Reusable prompt components
│   ├── context/             # Anti-patterns & best practices
│   └── CLAUDE.md           # Project-specific context
├── .claude-framework/       # Framework source (if using submodule)
└── [your existing files]
```

---

## Configuration Profiles

Choose a profile during setup to get domain-specific patterns:

### `--profile general` (Default)
- Core commands only
- Basic components
- Minimal complexity

### `--profile web-dev`
- React/Vue/Angular patterns
- API development commands
- Frontend testing helpers

### `--profile data-science`
- Data analysis commands
- Jupyter notebook integration
- ML workflow patterns

### `--profile devops`
- Infrastructure patterns
- CI/CD commands
- Deployment workflows

### `--profile custom`
- Interactive selection
- Choose specific commands
- Maximum control

---

## Post-Setup Customization

### 1. Review Installed Commands
```bash
ls .claude/commands/
# Remove any you don't need
rm .claude/commands/specialized/advanced-*.md
```

### 2. Simplify Complex Patterns
```bash
# Edit commands to match your style
vim .claude/commands/core/task.md
# Remove XML complexity if not needed
```

### 3. Add Your Domain Commands
```bash
# Create project-specific commands
cat > .claude/commands/my-project/deploy.md << 'EOF'
---
name: /deploy
description: Deploy to production
---

Guide me through deploying this project...
EOF
```

### 4. Configure Anti-Patterns
```bash
# Add project-specific anti-patterns
echo "Pattern: Deploying to wrong environment" >> .claude/context/project-antipatterns.md
```

---

## Updating the Framework

### If Using Submodule
```bash
# Pull latest improvements
cd .claude-framework
git pull origin main
./update.sh  # Merges improvements while preserving customizations
```

### If Direct Integration
```bash
# Manual update process
cd claude-code-modular-prompts
git pull origin main
./adapt.sh --update ../my-project --preserve-custom
```

---

## Verification

Test your setup:

1. **Check Structure**
   ```bash
   tree .claude/ -L 2
   ```

2. **Test in Claude**
   - Start a Claude Code session
   - Type `/help` - Should list available commands
   - Type `/task` - Should guide TDD workflow

3. **Verify Anti-Patterns**
   - Check `.claude/context/` has anti-pattern files
   - These prevent common mistakes automatically

---

## Troubleshooting

### "setup.sh not found"
```bash
# Make it executable
chmod +x setup.sh
```

### "Permission denied"
```bash
# Use sudo if needed (not recommended)
# Better: fix directory permissions
sudo chown -R $(whoami) .claude-framework
```

### "Commands not working in Claude"
1. Ensure `.claude/` is in your project root
2. Check Claude Code can see the directory
3. Verify command files have proper YAML frontmatter

### "Too many commands overwhelming"
```bash
# Start minimal
mkdir .claude/commands/archive
mv .claude/commands/specialized/* .claude/commands/archive/
# Add back as needed
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

## Support

- **Issues**: [GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)
- **Discussions**: [GitHub Discussions](https://github.com/swm-sink/claude-code-modular-prompts/discussions)
- **Updates**: Watch the repo for improvements

---

*You now have 6+ months of Claude Code knowledge ready to use. Happy building!*