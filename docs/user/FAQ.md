# Frequently Asked Questions

## Getting Started

### Q: How long does setup actually take?
**A: 1-2 hours total** - 5 minutes for installation, 45-90 minutes for proper customization.

**Realistic Timeline Breakdown:**
- Installation: 5-10 minutes
- Getting guidance (/adapt-to-project): 10 minutes
- Manual placeholder replacement: 45-90 minutes
- Removing unused commands: 15 minutes
- Validation and documentation: 15 minutes

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
**A: No! Start with core commands, then add gradually based on need.**

**Recommended Starting Set (8-12 commands):**
- Core: `/help`, `/task`, `/auto`, `/query`
- Development: `/dev`, `/api-design`
- Database: `/db-migrate` (if using databases)
- Testing: `/test-unit` (if writing tests)
- Archive the rest initially, add back as needed

Profiles available:
- `general` - Just core commands (help, task, auto, query, dev)
- `web-dev` - Frontend/backend patterns
- `data-science` - Analysis and ML workflows
- `devops` - Infrastructure and CI/CD

### Q: What if the templates don't fit my project?
**A: The templates are designed to be customized - that's the whole point.**

**Customization Options:**
```bash
# 1. Simplify complex patterns
find .claude/commands -name "*.md" -exec sed -i 's/<[^>]*>//g' {} \;

# 2. Add project-specific commands
mkdir .claude/commands/team
cat > .claude/commands/team/custom-deploy.md << 'EOF'
---
name: /deploy-prod
description: Deploy to production with safety checks
---
Guide me through our production deployment process...
EOF

# 3. Remove entire categories you don't need
rm -rf .claude/commands/data-science/  # If not doing ML/analytics
rm -rf .claude/commands/specialized/   # If not using advanced features
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
**A: Run comprehensive tests after customization.**

**Verification Checklist:**
```bash
# 1. Structure verification
ls -la .claude/commands/core/  # Should show help.md, task.md, auto.md, query.md

# 2. Placeholder verification  
grep -r "INSERT_" .claude/commands/ | wc -l  # Should be 0 after customization

# 3. Claude Code integration test
# In Claude Code conversation:
/help                           # Should list your commands
/task "implement user login"    # Should provide project-specific guidance
/validate-adaptation            # Should report 100% completion

# 4. Configuration verification
cat .claude/config/project-config.yaml  # Should show your project values
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
**A: Multiple simplification strategies available.**

**Option 1: Start Minimal**
```bash
# Archive most commands, keep only essentials
mkdir .claude/commands/archive
mv .claude/commands/specialized/* .claude/commands/archive/
mv .claude/commands/deprecated/* .claude/commands/archive/

# Keep only:
# - core/ (help, task, auto, query)
# - development/ (basic workflow)
# Add others back gradually
```

**Option 2: Simplify Command Content**
```bash
# Remove complex XML/structured patterns
find .claude/commands -name "*.md" -exec sed -i 's/<[^>]*>//g' {} \;

# Simplify verbose commands manually
vim .claude/commands/core/task.md  # Edit to your preferred style
```

**Option 3: Use Selective Installation**
```bash
# During setup, choose "Selective Import"
# Pick only the command categories you need
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
**A: Systematic troubleshooting for command visibility.**

**Step-by-Step Debugging:**
```bash
# 1. Check directory location
pwd  # Should be your project root
ls -la .claude/  # Should exist and contain commands/

# 2. Verify command structure
ls .claude/commands/core/  # Should show .md files
head -10 .claude/commands/core/help.md  # Should show YAML frontmatter

# 3. Check YAML format
grep -A 5 "^---" .claude/commands/core/help.md
# Should show:
# ---
# name: /help
# description: ...
# ---

# 4. Restart Claude Code
# Close and reopen Claude Code completely

# 5. Test with basic command
# In Claude Code, try: /help
```

**Common Fixes:**
- Ensure `.claude/` is in project root (not subdirectory)
- Check YAML frontmatter is properly formatted
- Verify files end with `.md` extension
- Make sure command names start with `/`
- Restart Claude Code after installation

### Q: Too many commands, feels overwhelming
**A: Use the "Start Small, Grow Gradually" approach.**

**Phase 1: Minimal Essential Set (Week 1)**
```bash
# Archive everything except essentials
mkdir .claude/commands/{archive,team-approved}
mv .claude/commands/deprecated/* .claude/commands/archive/
mv .claude/commands/specialized/* .claude/commands/archive/

# Keep only these 6 commands initially:
# .claude/commands/core/help.md
# .claude/commands/core/task.md  
# .claude/commands/core/auto.md
# .claude/commands/core/query.md
# .claude/commands/development/dev.md
# .claude/commands/meta/adapt-to-project.md
```

**Phase 2: Add by Need (Weeks 2-4)**
```bash
# When team asks "How do I...?", add relevant commands:
mv .claude/commands/archive/database/db-migrate.md .claude/commands/database/
mv .claude/commands/archive/testing/test-unit.md .claude/commands/testing/
# etc.
```

**Phase 3: Team Customization (Month 2+)**
```bash
# Create team-specific commands based on common questions
mkdir .claude/commands/team
# Add custom commands for your specific workflows
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
**A: Yes, but focus on team consistency rather than automation.**

**Team Onboarding in CI/CD:**
```yaml
# .github/workflows/onboard-developer.yml
name: Developer Onboarding
on:
  schedule:
    - cron: '0 9 * * MON'  # Weekly reminder

jobs:
  check-claude-setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true
      
      - name: Verify Claude Code Templates
        run: |
          # Check that templates are properly customized
          if grep -r "INSERT_" .claude/commands/; then
            echo "❌ Uncustomized placeholders found"
            echo "Run /adapt-to-project to complete setup"
            exit 1
          fi
          
          # Validate structure
          ./.claude/validate.sh
          
          echo "✅ Claude Code templates properly configured"
```

**Documentation Generation:**
```yaml
# Generate team documentation from templates
- name: Update Claude Code Documentation
  run: |
    # Create team guide from current templates
    echo "# Team Claude Code Commands" > CLAUDE-TEAM-GUIDE.md
    find .claude/commands -name "*.md" -not -path "*/archive/*" -exec basename {} .md \; | sort >> CLAUDE-TEAM-GUIDE.md
```

## Support

### Q: Where can I get help?
**A: Multiple support channels available.**

- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - Questions and community help
- **Documentation** - SETUP.md, ADAPTATION-GUIDE.md
- **Examples** - EXAMPLES.md with real usage patterns

### Q: How often are templates updated?
**A: Monthly releases with continuous improvements.**

**Update Frequency:**
- **Bug fixes**: As needed (usually within days)
- **New commands**: Monthly releases
- **Major improvements**: Quarterly
- **Community contributions**: Integrated weekly

**What Gets Updated:**
- **Command improvements**: Better prompts, clearer instructions
- **New templates**: Community-contributed commands
- **Anti-pattern additions**: New failure modes discovered
- **Documentation**: Better examples and troubleshooting
- **Component library**: New reusable prompt components

**Staying Updated:**
```bash
# For git submodule users (recommended monthly):
cd .claude-framework
git pull origin main
/sync-from-reference  # Get guided merge instructions

# For direct installation users:
# Check releases page quarterly:
# https://github.com/swm-sink/claude-code-modular-prompts/releases
```

**Breaking Changes Policy:**
- No breaking changes to existing command interfaces
- Deprecated commands are clearly marked
- Migration guides provided for major updates
- Your customizations are always preserved

### Q: What's the roadmap?
**A: Community-driven improvements based on real usage.**

**Current Focus (2025 Q3-Q4):**
1. **Better onboarding experience**
   - Improved validation and error messages
   - Video walkthrough of customization process
   - More detailed troubleshooting guides

2. **Template quality improvements**
   - Simplify overly complex commands
   - Add more domain-specific examples
   - Better anti-pattern documentation

3. **Community features**
   - Template sharing mechanism (/share-adaptation improvements)
   - Community-contributed command library
   - Success stories and case studies

4. **Developer experience**
   - Better validation tooling
   - Automated placeholder detection
   - IDE integration guides

**Long-term Vision:**
- Industry-specific template collections (fintech, healthcare, etc.)
- Integration with popular development tools
- Advanced prompt engineering patterns
- Educational content and workshops

**Contribution Opportunities:**
- Share your customized templates with the community
- Report bugs and suggest improvements  
- Contribute domain-specific commands
- Help with documentation and examples

---

## Emergency Troubleshooting

### Q: Everything is broken, how do I start over?
**A: Complete reset procedure:**

```bash
# 1. Backup any custom commands you created
cp -r .claude/commands/team/ ~/claude-backup-$(date +%Y%m%d) 2>/dev/null || true
cp -r .claude/commands/my-project/ ~/claude-backup-$(date +%Y%m%d) 2>/dev/null || true

# 2. Complete reset
rm -rf .claude/

# 3. Fresh installation
cd .claude-framework  # If using submodules
./setup.sh
# OR
git clone https://github.com/swm-sink/claude-code-modular-prompts temp-fresh
cd temp-fresh
./setup.sh /path/to/your/project

# 4. Start customization from scratch
/adapt-to-project
```

### Q: My team member can't get it working
**A: Team troubleshooting checklist:**

```bash
# 1. Verify they're in the right directory
cd /path/to/your/project
pwd  # Should show project root with .claude/ directory

# 2. For submodule users
git submodule update --init --recursive
cd .claude-framework
git pull origin main

# 3. Check their Claude Code installation
# They should be able to see .claude/ directory in Claude Code interface

# 4. Test with minimal command
# In Claude Code: /help
# Should show command list

# 5. If still failing, compare with working setup
diff -r .claude/ /path/to/working-teammate/.claude/
```

---

## Still have questions?

### Self-Service (Try First)
1. **Check validation**: Run `./.claude/validate.sh` for automated diagnostics
2. **Review examples**: See `EXAMPLES.md` for real customization patterns
3. **Check installation**: Review `INSTALLATION.md` for comprehensive setup guide

### Community Support
- **[GitHub Discussions](https://github.com/swm-sink/claude-code-modular-prompts/discussions)** - Ask the community
- **[GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)** - Report bugs and feature requests
- **Search existing issues** - Your question might already be answered

### Creating Good Support Requests

**For bug reports, include:**
```bash
# System information
uname -a
git --version
ls -la .claude/

# Error details
# Paste the exact error message
# Include steps to reproduce
# Show what you expected vs. what happened
```

**For setup questions, include:**
- Which installation method you used (submodule/direct/selective)
- How far you got in the process
- Output of validation script: `./.claude/validate.sh`
- Your project type (web app, data science, etc.)

**Remember**: The goal is to save you months of prompt engineering work. If something isn't working, we want to fix it quickly so you can focus on building your project!