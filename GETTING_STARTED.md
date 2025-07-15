# Getting Started with Claude Code Modular Prompts Framework

> 🚀 **5-minute setup**: Transform Claude Code from good to exceptional with intelligent commands that adapt to YOUR project.

## What You'll Achieve

✅ **Immediate Benefits**: Claude Code suggests tech-specific solutions, follows your project patterns, enforces quality automatically  
✅ **Smart Commands**: `/auto`, `/task`, `/feature`, `/query` that adapt to your codebase  
✅ **Quality Enforcement**: Automatic TDD, test coverage, security checks  
✅ **Framework Learning**: Commands get smarter about your project over time  

---

## Quick Start (30 seconds)

### 1. Copy Framework to Your Project
```bash
# Clone the framework
git clone https://github.com/swm-sink/claude-code-modular-prompts.git

# Copy to your project (replace 'your-project' with your actual project path)
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/

# Navigate to your project
cd your-project/
```

### 2. Test Basic Functionality
```bash
# Test the framework responds
/auto "analyze my project structure"
```

**✅ Success Indicator**: Claude Code responds with project-specific analysis and suggestions

---

## Step-by-Step Setup (5 minutes)

### Step 1: Prerequisites Check
Ensure you have:
- [ ] **Claude Code** (Claude Desktop App) installed
- [ ] **Git** for version control
- [ ] **GitHub CLI** (`gh`) for issue tracking: `gh auth login`
- [ ] **Python 3.8+** for monitoring: `python --version`
- [ ] **Basic terminal access**

### Step 2: Framework Installation
```bash
# 1. Clone the repository
git clone https://github.com/swm-sink/claude-code-modular-prompts.git
cd claude-code-modular-prompts

# 2. Verify framework structure
ls -la .claude/
# Should show: commands/, modules/, system/, domain/, templates/, etc.

# 3. Copy framework to your project
cp -r .claude /path/to/your-project/
cp CLAUDE.md /path/to/your-project/
cp PROJECT_CONFIG.xml /path/to/your-project/
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

## Essential Commands Overview

### 🤖 `/auto` - Intelligent Routing
**When to use**: When you're unsure which command to use or want framework to decide
```bash
/auto "add user authentication"     # → Routes to /feature (complex feature)
/auto "fix login bug"              # → Routes to /task (focused fix)
/auto "understand auth system"     # → Routes to /query (research)
```

### 🔧 `/task` - Focused Development
**When to use**: Single component work, bug fixes, small features
```bash
/task "add password validation"    # → Creates tests first, then implementation
/task "fix email validation bug"   # → Identifies issue, creates test, fixes
```

### 🏗️ `/feature` - Complete Feature Development
**When to use**: New features, major functionality, multi-component work
```bash
/feature "shopping cart system"    # → PRD → planning → implementation → validation
/feature "user profile with avatar upload"  # → Complete feature lifecycle
```

### 🔍 `/query` - Research & Analysis
**When to use**: Understanding code, research, analysis without changes
```bash
/query "how does our auth work?"   # → Analysis without modifications
/query "what are the security patterns?"  # → Research existing patterns
```

---

## Success Validation

### ✅ Tier 1 Complete (30 seconds - 5 minutes)
- [ ] Framework responds to `/auto` command
- [ ] Suggestions mention your actual tech stack (React, Django, Go, etc.)
- [ ] Quality enforcement works (mentions tests, security, performance)
- [ ] Commands understand your project structure

### ✅ Tier 2 Complete (5-30 minutes)
- [ ] `/task` creates tests before implementation (TDD)
- [ ] `/feature` produces PRD and implementation plan
- [ ] `/query` analyzes without changing code
- [ ] Commands suggest patterns specific to your project
- [ ] Quality gates enforce coverage thresholds

### ✅ Tier 3 Complete (30+ minutes)
- [ ] Framework learns your coding style and patterns
- [ ] Commands adapt to your project's specific requirements
- [ ] Meta-commands optimize workflow for your team
- [ ] Custom configuration improves suggestions over time

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
- **[examples/quick-start/](examples/quick-start/)** - Working examples you can try
- **[docs/user-guide/](docs/user-guide/)** - Comprehensive command guides
- **[CLAUDE.md](CLAUDE.md)** - Complete framework reference (developers)

### 🔧 **Configuration**
- **[PROJECT_CONFIG.xml](PROJECT_CONFIG.xml)** - Customize for your project
- **[examples/project-configs/](examples/project-configs/)** - Pre-built configurations

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