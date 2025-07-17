# Getting Started Guide

> 🚀 **5-minute setup**: Install and configure the Framework 3.0 for your project.

**What this guide covers**: Framework installation, project configuration, command validation, and production-ready setup

## Quick Start (30 seconds)

```bash
# 1. Clone and copy to your project
git clone https://github.com/swm-sink/claude-code-modular-prompts.git
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/

# 2. Test framework responds
cd your-project/
/auto "analyze my project structure"
```

**✅ Success**: Claude Code responds with intelligent, project-specific analysis

## Step-by-Step Setup (5 minutes)

### Step 1: Prerequisites Check
Ensure you have:
- [ ] **Claude Code** (Claude Desktop App) installed
- [ ] **Git** for version control
- [ ] **GitHub CLI** (`gh`) for issue tracking: `gh auth login`
- [ ] **Python 3.8+** for monitoring: `python --version`
- [ ] **Basic terminal access**

### Step 2: Framework Installation
Use the Quick Start commands above, then verify the structure:
```bash
ls -la .claude/
# Should show: commands/, modules/, system/, domain/, templates/, etc.
```

### Step 3: Project Configuration
```bash
# Navigate to your project
cd /path/to/your-project/

# Edit PROJECT_CONFIG.xml for your project
# See PROJECT_CONFIG.xml comments for all options
```

**Key Configuration Areas:**
- **Tech Stack**: Set your primary language (Python, JavaScript, Go, etc.)
- **Project Structure**: Define your src/, tests/, docs/ directories
- **Quality Standards**: Set test coverage thresholds, lint rules
- **Development Commands**: Customize test, build, lint commands

### Step 4: Framework Validation
```bash
# Test each essential command
/auto "understand my project"         # Should analyze your codebase
/task "create a simple function"      # Should create tests first
/feature "add user authentication"    # Should create PRD and plan
/query "how is my code structured?"   # Should analyze without changing
```

**✅ Validation Checklist:**
- [ ] `/auto` provides project-specific suggestions
- [ ] `/task` mentions creating tests first (TDD)
- [ ] `/feature` asks about requirements or creates PRD
- [ ] `/query` analyzes without modifying code
- [ ] All commands reference your actual tech stack

---

## Command Validation

Test the 4 essential commands work correctly:
```bash
/auto "understand my project"         # Should analyze your codebase
/task "create a simple function"      # Should create tests first
/feature "add user authentication"    # Should create PRD and plan
/query "how is my code structured?"   # Should analyze without changing
```

**✅ Success Indicators**:
- [ ] Commands respond with intelligent, project-specific suggestions
- [ ] `/task` enforces TDD by creating tests first
- [ ] `/auto` provides intelligent routing and picks appropriate approaches
- [ ] Suggestions match your actual tech stack and project patterns

👉 **[Learn commands in detail](examples/01-beginner/basic-commands/)** with hands-on examples

---

## Common Troubleshooting

### Issue: "Command not recognized"
**Solution**: Ensure CLAUDE.md is in your project root and Claude Code can access it
```bash
# Check file exists
ls -la CLAUDE.md

# Check .claude directory
ls -la .claude/
```

### Issue: "Generic suggestions, not project-specific"
**Solution**: Customize PROJECT_CONFIG.xml for your tech stack
```xml
<!-- Edit PROJECT_CONFIG.xml -->
<project_config>
  <tech_stack>
    <primary_language>python</primary_language>
    <framework>django</framework>
    <database>postgresql</database>
  </tech_stack>
</project_config>
```

### Issue: "Commands don't enforce quality"
**Solution**: Verify quality gates are enabled in PROJECT_CONFIG.xml
```xml
<quality_standards>
  <test_coverage>
    <threshold>90</threshold>
    <enforcement>blocking</enforcement>
  </test_coverage>
</quality_standards>
```

### Issue: "Framework seems slow"
**Solution**: 
1. Check .claude directory has reasonable file count (should be ~166 files)
2. Reduce context by focusing commands on specific areas
3. Use `/query` for research, `/task` for implementation

---

## What's Next?

### 🎯 **Master the Basics** (recommended next step)
Try all 4 essential commands in your project:
1. `/auto "analyze my project"`
2. `/task "create a simple utility function"`
3. `/feature "add basic search functionality"`
4. `/query "what are my project's main components?"`

### 🔧 **Customize for Your Project**
- Edit PROJECT_CONFIG.xml for your exact tech stack
- Adjust quality thresholds and enforcement rules
- Add custom development commands for your workflow

### 🚀 **Advanced Usage**
- Explore `/session` for long-running work
- Use `/swarm` for complex multi-component features
- Try `/protocol` for production-ready workflows
- Investigate meta-commands for framework optimization

---

## Support & Resources

### 📚 **Documentation**
- **[examples/01-beginner/](examples/01-beginner/)** - Working examples you can try
- **[docs/user-guide/](docs/user-guide/)** - Comprehensive command guides
- **[CLAUDE.md](CLAUDE.md)** - Complete framework reference (developers)

### 🔧 **Configuration**
- **[PROJECT_CONFIG.xml](PROJECT_CONFIG.xml)** - Customize for your project
- **[examples/project-templates/](examples/project-templates/)** - Pre-built configurations

### 🆘 **Help**
- **Issues**: [GitHub Issues](https://github.com/swm-sink/claude-code-modular-prompts/issues)
- **Quick Help**: Use `/query "your question"` for research
- **Framework Questions**: Use `/docs generate` for documentation

---

## Quick Reference

### Essential Commands
```bash
/auto "your request"      # Intelligent routing
/task "focused work"      # Single component with TDD
/feature "new feature"    # Complete feature lifecycle  
/query "research question" # Analysis without changes
```

### Quality Validation
```bash
# Check framework is working
/auto "analyze project"

# Validate TDD enforcement
/task "create test function"

# Validate feature planning
/feature "add simple feature"
```

### Common Configuration
```xml
<!-- PROJECT_CONFIG.xml essentials -->
<project_config>
  <tech_stack>
    <primary_language>your-language</primary_language>
    <framework>your-framework</framework>
  </tech_stack>
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
    </test_coverage>
  </quality_standards>
</project_config>
```

---

🎉 **You're Ready!** Start with `/auto "understand my project"` and let the framework adapt to your specific needs.

> **Remember**: The framework gets smarter about YOUR project every time you use it. Each command learns your patterns and improves suggestions over time.