# Quick Start - 5 Minutes to Success

> **Goal**: Get the framework running and execute your first command in under 5 minutes.

## 🚀 Ultra-Fast Setup

### 1. Copy Framework Files (30 seconds)
```bash
# Clone the framework
git clone https://github.com/swm-sink/claude-code-modular-prompts.git

# Copy to your project (replace 'your-project' with your actual project directory)
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/

# Navigate to your project
cd your-project/
```

### 2. Verify Installation (10 seconds)
```bash
# Check that framework files are present
ls -la CLAUDE.md PROJECT_CONFIG.xml .claude/
```

You should see:
- `CLAUDE.md` - Framework control document
- `PROJECT_CONFIG.xml` - Your project configuration
- `.claude/` - Framework modules and commands

### 3. Test Framework (30 seconds)
```bash
# Test with a simple query (this should work immediately)
/query "what files are in this project?"
```

**Success**: You should get an analysis of your project structure!

### 4. Customize Basic Settings (2 minutes)
Edit `PROJECT_CONFIG.xml` with your project details:

```xml
<project_info>
  <name>Your Project Name</name>
  <domain>web-development</domain>          <!-- or mobile-development, data-science, etc. -->
  <primary_language>typescript</primary_language>  <!-- your main language -->
  <framework_stack>react+nextjs</framework_stack>  <!-- your tech stack -->
</project_info>
```

### 5. Try Your First Real Command (1 minute)
```bash
# Let the framework analyze and route intelligently
/auto "help me understand the current codebase structure"

# Or try a specific task
/task "add a simple utility function for string formatting"
```

**🎉 You're done!** The framework is now running and adapted to your project.

## ✅ Success Checklist

- [ ] Framework files copied to your project
- [ ] `/query` command works and analyzes your project
- [ ] `PROJECT_CONFIG.xml` updated with your project details
- [ ] `/auto` or `/task` command executed successfully
- [ ] Framework responds with project-appropriate suggestions

## 🚧 Quick Troubleshooting

### "Permission denied" errors
```bash
# Fix permissions (common on macOS/Linux)
chmod +x .claude/commands/*
```

### "Command not found" errors
- Ensure you're in your project directory (where CLAUDE.md exists)
- Check that `.claude/` directory was copied correctly

### "Framework doesn't understand my project"
- Update `PROJECT_CONFIG.xml` with correct tech stack
- Try `/query "detect project type"` to see what framework recognizes

## 🎯 Next Steps

### Immediate (5-10 minutes)
- **Learn essential commands**: [First Commands](first-commands.md)
- **Understand command selection**: [When to use which command](../user-guide/commands/command-selection.md)

### Today (30 minutes)
- **Explore workflows**: [Common Patterns](../user-guide/workflows/common-patterns.md)
- **Customize configuration**: [Project Configuration](../user-guide/customization/project-config.md)

### This Week
- **Master advanced features**: [Advanced Workflows](../user-guide/workflows/advanced-patterns.md)
- **Integrate with your team**: [Team Configuration](../user-guide/customization/team-setup.md)

## 💡 Pro Tips for Immediate Success

1. **Start with `/auto`** - When unsure, let intelligent routing decide
2. **Use `/query` for understanding** - Research before making changes
3. **Try `/task` for focused work** - Single-component modifications
4. **Trust the framework** - It adapts to your project automatically

## 🔄 Common First Commands

```bash
# Understand your codebase
/query "explain the main architecture"
/query "find all TODO comments"
/query "analyze test coverage"

# Make improvements
/task "fix a specific bug"
/auto "add feature X"
/feature "complete user story Y"

# Documentation and planning
/docs "create API documentation"
/session "plan multi-day feature"
```

---

**Ready for more?** Continue to [First Commands](first-commands.md) to learn the essential commands you'll use every day.

**Having issues?** Check the [troubleshooting guide](../reference/troubleshooting.md) or [installation details](installation.md).