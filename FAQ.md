# Frequently Asked Questions

## Getting Started

### Q: How long does setup actually take?
**A: 2-5 minutes** for basic setup, 10-15 minutes for full customization.

```bash
# Basic setup (2 minutes)
git submodule add [url] .claude-framework
cd .claude-framework && ./setup.sh

# Add customization (5-10 more minutes)
# Remove unwanted commands, add project-specific ones
```

### Q: What if I already have a .claude directory?
**A: The setup script handles this gracefully.**

Options when existing .claude detected:
1. **Merge** (recommended) - Keeps your existing commands, adds framework patterns
2. **Backup & Replace** - Saves your .claude to .claude.backup, fresh install
3. **Cancel** - No changes made

### Q: Do I need to use all 102 commands?
**A: No! Start with 5-10 core commands from the 64 active ones.**

Profiles available:
- `general` - Just core commands (help, task, auto, query, dev)
- `web-dev` - Frontend/backend patterns
- `data-science` - Analysis and ML workflows
- `devops` - Infrastructure and CI/CD

### Q: What if the framework doesn't work for my use case?
**A: Customize or simplify patterns as needed.**

```bash
# Remove complex XML structures
find .claude/commands -name "*.md" -exec sed -i 's/<[^>]*>//g' {} \;

# Add your own commands
mkdir .claude/commands/my-project
# Create custom commands for your domain
```

## Technical Questions

### Q: How do I update the framework without losing my customizations?
**A: Use git submodule update with the update script.**

```bash
# For git submodule installations
cd .claude-framework
git pull origin main
./update.sh  # Preserves customizations

# For direct installations
./adapt.sh --update --preserve-custom
```

### Q: What's the difference between git submodule and direct clone?
**A: Submodule gets updates easily, direct clone gives full control.**

| Method | Updates | Control | Best For |
|--------|---------|---------|----------|
| **Git Submodule** | Easy (`git pull`) | Framework managed | Active projects |
| **Direct Clone** | Manual | Full ownership | One-time setup |

### Q: Can I remove the .claude-framework directory after setup?
**A: Yes for direct integration, no for submodule approach.**

- **Direct integration**: Framework is copied to your .claude/, can remove source
- **Git submodule**: Keep .claude-framework for updates and reference

### Q: Will this conflict with my existing Claude Code setup?
**A: Only if you already have conflicting command names.**

The framework:
- ✅ Adds to your .claude/ directory
- ✅ Can merge with existing commands  
- ❌ Won't overwrite without asking
- ❌ Doesn't modify Claude Code itself

## Usage Questions

### Q: How do I know if it's working?
**A: Test with Claude Code after setup.**

```bash
# After setup, in Claude Code conversation:
/help          # Should list available commands
/task          # Should start TDD workflow
/auto "debug this error"  # Should route intelligently
```

### Q: Can I use this with teams?
**A: Yes! It's designed for team consistency.**

```bash
# Each team member runs:
git submodule update --init
cd .claude-framework && ./setup.sh

# Everyone gets the same foundation
# Add team-specific commands to shared repo
```

### Q: What if I want to simplify the complex patterns?
**A: Multiple simplification options available.**

```bash
# Remove XML complexity
./adapt.sh --simplify

# Manual simplification
find .claude -name "*.md" -exec sed -i 's/<include.*>//g' {} \;

# Start with minimal profile
./setup.sh --profile general
```

### Q: How do I add my own commands?
**A: Create them in your .claude/commands/ directory.**

```bash
# Add domain-specific command
mkdir -p .claude/commands/my-app
cat > .claude/commands/my-app/deploy.md << 'EOF'
---
name: /deploy
description: Deploy my application
---

Guide me through deploying this application...
EOF
```

## Project Questions

### Q: Is this officially supported by Claude/Anthropic?
**A: No, this is a community project.**

- Created by users for users
- Not officially endorsed by Anthropic
- Open source and community maintained
- Based on real experience with Claude Code

### Q: Why not just start from scratch?
**A: You'll likely reinvent the same patterns and make the same mistakes.**

Common reinventions:
- Command structure and organization
- Component composition patterns  
- Context loading strategies
- Error handling approaches
- Token optimization techniques

### Q: What if I find bugs or issues?
**A: Report them and we'll fix them quickly.**

1. **Check FAQ first** (this document)
2. **Search existing issues** on GitHub
3. **Create new issue** with reproduction steps
4. **Join discussions** for questions and sharing

### Q: Can I contribute back improvements?
**A: Yes! Contributions welcome.**

```bash
# Add your patterns
1. Fork the repository
2. Add your command/component patterns
3. Test with your use case
4. Submit pull request
5. Share how it helped your project
```

## Troubleshooting

### Q: setup.sh says "permission denied"
**A: Make the script executable.**

```bash
chmod +x setup.sh
./setup.sh
```

### Q: Commands don't show up in Claude Code
**A: Check .claude directory location and command format.**

Requirements:
- ✅ `.claude/` in project root
- ✅ Commands have proper YAML frontmatter
- ✅ Command files end in `.md`
- ✅ YAML includes `name: /command-name`

### Q: Too many commands, feels overwhelming
**A: Start minimal and add gradually.**

```bash
# Archive most commands
mkdir .claude/commands/archive
mv .claude/commands/specialized/* .claude/commands/archive/
mv .claude/commands/deprecated/* .claude/commands/archive/

# Keep only core
# Add back one at a time as needed
```

### Q: Setup fails with "directory not found"
**A: Ensure you're in the framework directory.**

```bash
# Common mistake - wrong directory
cd .claude-framework  # Must be in framework directory
./setup.sh

# Or use absolute path
/path/to/.claude-framework/setup.sh --target /path/to/my-project
```

### Q: Git submodule update fails
**A: Initialize submodules first.**

```bash
git submodule update --init --recursive
cd .claude-framework
git checkout main
git pull origin main
```

## Advanced Usage

### Q: Can I create multiple profiles for different projects?
**A: Yes, use different profiles or create custom ones.**

```bash
# Different profiles for different projects
./setup.sh --profile web-dev     # For frontend projects
./setup.sh --profile data-science # For ML projects
./setup.sh --profile devops      # For infrastructure

# Custom profile (coming soon)
./setup.sh --profile custom --commands "help,task,deploy,monitor"
```

### Q: How do I share customizations with my team?
**A: Add team commands to your shared repository.**

```bash
# In your project repo
mkdir .claude/commands/team
# Add team-specific commands
git add .claude/commands/team/
git commit -m "Add team-specific Claude Code commands"

# Team members get them automatically
git pull
```

### Q: Can I use this in CI/CD?
**A: Yes, for automated Claude Code tasks.**

```yaml
# Example GitHub Action
- name: Setup Claude Code Framework
  run: |
    git submodule update --init
    cd .claude-framework
    ./setup.sh --profile devops
```

## Support

### Q: Where can I get help?
**A: Multiple support channels available.**

- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - Questions and community help
- **Documentation** - SETUP.md, ADAPTATION-GUIDE.md
- **Examples** - EXAMPLES.md with real usage patterns

### Q: How often is the framework updated?
**A: Regularly, based on community feedback.**

Updates include:
- New command patterns
- Improved existing patterns
- Bug fixes
- New domain profiles
- Community contributions

### Q: What's the roadmap?
**A: Focus on user success and community growth.**

Next priorities:
1. More domain-specific profiles
2. Video tutorials
3. Case studies from users
4. Integration with Claude ecosystem
5. Community contribution tools

---

## Still have questions?

- **[GitHub Discussions](https://github.com/swm-sink/claude-code-modular-prompts/discussions)** - Ask the community
- **[GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)** - Report bugs
- **[Examples](EXAMPLES.md)** - See real usage patterns *(coming soon)*

**Remember**: The goal is to save you time. If something isn't working, let us know and we'll fix it!