# Troubleshooting Guide

> **Quick Fix**: Most issues are resolved by checking you're in the project directory with `CLAUDE.md` and ensuring proper file permissions.

## 🚨 Emergency Quick Fixes

### Commands Not Working At All
```bash
# 1. Verify you're in the right directory
ls -la CLAUDE.md PROJECT_CONFIG.xml .claude/
# All three should exist

# 2. Fix permissions (macOS/Linux)
chmod +x .claude/commands/*
chmod -R u+r .claude/

# 3. Test basic functionality  
/query "framework status"
```

### "Permission Denied" Errors
```bash
# One-line fix for most permission issues
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json

# Alternative: Fix all permissions
chmod -R u+rw .claude/
find .claude/ -type f -name "*.md" -exec chmod +r {} \;
```

### Framework Not Recognizing Project
```bash
# Check PROJECT_CONFIG.xml exists and is valid
cat PROJECT_CONFIG.xml | head -10

# Re-run initialization if needed
/init-custom  # For existing projects
/init-new     # For new projects
```

## 🔍 Common Issues and Solutions

### Command Execution Issues

#### Problem: Commands don't respond or give generic responses
**Symptoms**: Commands run but don't seem framework-aware

**Solutions**:
```bash
# 1. Verify framework files are in place
ls -la CLAUDE.md .claude/

# 2. Check PROJECT_CONFIG.xml is configured
grep -A 5 "<project_info>" PROJECT_CONFIG.xml

# 3. Test framework detection
/query "what framework version is running?"

# 4. Re-initialize if needed
/init-validate
```

#### Problem: "Command not found" errors
**Symptoms**: Framework doesn't recognize commands like `/task` or `/query`

**Solutions**:
```bash
# 1. Ensure you're in project root (where CLAUDE.md exists)
pwd
ls CLAUDE.md

# 2. Check command files exist
ls .claude/commands/

# 3. Verify CLAUDE.md wasn't corrupted
head -20 CLAUDE.md | grep "Claude Code"
```

#### Problem: Commands work but produce wrong results
**Symptoms**: Commands execute but don't match your project type

**Solutions**:
```bash
# 1. Check PROJECT_CONFIG.xml configuration
/query "what project configuration is active?"

# 2. Update configuration for your project
# Edit PROJECT_CONFIG.xml with correct:
# - domain (web-development, mobile-development, etc.)
# - primary_language 
# - framework_stack

# 3. Let framework re-learn your project
/meta-evolve "adapt to current project patterns"
```

### Configuration Issues

#### Problem: Framework doesn't understand your tech stack
**Symptoms**: Suggestions don't match your technology choices

**Solutions**:
```bash
# 1. Update PROJECT_CONFIG.xml with your stack
<project_info>
  <primary_language>your-language</primary_language>
  <framework_stack>your-framework+your-libraries</framework_stack>
</project_info>

# 2. Use specific domain configuration
<domain>web-development</domain>        <!-- React, Vue, Angular -->
<domain>mobile-development</domain>     <!-- React Native, Flutter -->
<domain>data-science</domain>           <!-- Python, R, Jupyter -->
<domain>devops-platform</domain>        <!-- Infrastructure, DevOps -->

# 3. Test updated configuration
/query "what tech stack does framework detect?"
```

#### Problem: Quality standards too strict or too lenient
**Symptoms**: Tests fail quality gates or quality gates don't catch issues

**Solutions**:
```bash
# Update quality standards in PROJECT_CONFIG.xml
<quality_standards>
  <test_coverage>
    <threshold>85</threshold>           <!-- Adjust threshold -->
    <enforcement>BLOCKING</enforcement>  <!-- or WARNING -->
  </test_coverage>
  <performance>
    <response_time_p95>200ms</response_time_p95>
  </performance>
</quality_standards>

# Test new standards
/task "create simple test function" # Should respect new thresholds
```
<!-- BROKEN EXAMPLE: Line 6: Path does not exist: .claude/commands/* - Agent V24 validation -->

### File and Directory Issues

#### Problem: Framework creates files in wrong locations
**Symptoms**: Files appear in unexpected directories

**Solutions**:
```bash
# 1. Check project structure configuration
<project_structure>
  <source_directory>src</source_directory>      <!-- Your source dir -->
  <test_directory>tests</test_directory>        <!-- Your test dir -->
  <docs_directory>docs</docs_directory>         <!-- Your docs dir -->
</project_structure>

# 2. Verify current structure
/query "analyze project directory structure"

# 3. Update configuration to match your project
# Edit PROJECT_CONFIG.xml with actual directory names
```

#### Problem: Cannot read or write certain files
**Symptoms**: Permission errors on specific files or directories

**Solutions**:
```bash
# 1. Check specific file permissions
ls -la path/to/problematic/file

# 2. Fix permissions for specific directory
chmod -R u+rw src/ tests/ docs/

# 3. Check for file locks or processes
lsof path/to/file

# 4. Alternative: Create files manually first
mkdir -p src/components
touch src/components/NewComponent.tsx
```

### Performance Issues

#### Problem: Commands are slow to respond
**Symptoms**: Long delays before command execution

**Solutions**:
```bash
# 1. Check for large files in project
find . -size +10M -not -path "./.git/*" -not -path "./node_modules/*"

# 2. Exclude large directories
# Add to .gitignore:
node_modules/
build/
dist/
*.log

# 3. Optimize framework performance
/meta-optimize "improve response time for this project"

# 4. Check available memory and CPU
# Framework works better with adequate resources
```

#### Problem: Framework uses too much memory
**Symptoms**: System becomes slow during framework operations

**Solutions**:
```bash
# 1. Reduce context window usage
# Avoid processing very large files simultaneously

# 2. Use focused commands instead of broad ones
/task "fix specific component"     # Better than
/auto "fix everything"             # Too broad

# 3. Break large operations into smaller tasks
/session "large refactoring project"  # Use session management
```

### Integration Issues

#### Problem: GitHub integration not working
**Symptoms**: No issues created for `/swarm` or `/session` commands

**Solutions**:
```bash
# 1. Check if you're in a git repository
git status

# 2. Verify GitHub CLI is installed and authenticated
gh auth status

# 3. Configure git if needed
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 4. Test GitHub integration
/session "test GitHub integration"
```

#### Problem: Version control conflicts
**Symptoms**: Git conflicts when framework makes changes

**Solutions**:
```bash
# 1. Always work on clean git state
git status  # Should be clean before major operations

# 2. Use framework's atomic commit strategy
# Framework automatically handles commits if configured

# 3. Use protocol for production changes
/protocol "production-critical change"  # Maximum safety

# 4. Resolve conflicts manually if needed
git status
git diff
# Resolve conflicts and commit
```

## 🔧 Advanced Troubleshooting

### Framework Behavior Issues

#### Problem: Framework giving inconsistent results
**Symptoms**: Same command produces different outputs

**Diagnosis**:
```bash
# 1. Check framework state consistency
/meta-review "analyze framework consistency"

# 2. Verify configuration hasn't changed
git log --oneline PROJECT_CONFIG.xml

# 3. Check for conflicting settings
/query "identify any configuration conflicts"
```

**Solutions**:
```bash
# 1. Reset framework learning if needed
/meta-fix "reset inconsistent behavior patterns"

# 2. Re-validate configuration
/init-validate

# 3. Start fresh session if needed
# Clear any problematic context and start over
```

#### Problem: Framework not learning project patterns
**Symptoms**: Suggestions don't improve over time

**Solutions**:
```bash
# 1. Explicitly teach framework your patterns
/meta-evolve "learn from existing code patterns in src/"

# 2. Provide feedback on suggestions
# Use /query to analyze results and provide feedback

# 3. Configure domain-specific settings
# Ensure PROJECT_CONFIG.xml domain matches your project type
```

### Quality Gate Issues

#### Problem: Tests always fail quality gates
**Symptoms**: Valid code fails quality checks

**Solutions**:
```bash
# 1. Check quality configuration
<quality_standards>
  <test_coverage>
    <threshold>90</threshold>  <!-- May be too high -->
    <enforcement>WARNING</enforcement>  <!-- Try WARNING instead of BLOCKING -->
  </test_coverage>
</quality_standards>

# 2. Verify test tooling
npm test  # Or your test command
# Ensure tests can run outside framework

# 3. Debug specific quality gate
/query "analyze why quality gate failed for last change"
```

#### Problem: Quality gates not catching real issues
**Symptoms**: Poor code passes quality checks

**Solutions**:
```bash
# 1. Increase quality standards
<quality_standards>
  <test_coverage>
    <threshold>95</threshold>
    <enforcement>BLOCKING</enforcement>
  </test_coverage>
</quality_standards>

# 2. Add additional quality tools
<code_quality>
  <linter>eslint</linter>
  <formatter>prettier</formatter>
  <type_checker>typescript</type_checker>
</code_quality>

# 3. Review quality gate implementation
/query "analyze current quality gate effectiveness"
```

## 🏥 Diagnostic Commands

### Framework Health Check
```bash
# Comprehensive framework status
/meta-review "complete framework health check"

# Configuration validation
/init-validate

# Performance analysis
/meta-optimize "analyze performance issues"
```

### Project Analysis
```bash
# Project configuration status
/query "analyze current project configuration"

# Tech stack detection
/query "what technology stack is detected?"

# Quality standards review
/query "review current quality standards and compliance"
```

### Error Investigation
```bash
# Recent error analysis
/query "analyze any recent errors or failures"

# Command effectiveness review
/query "review last 10 commands and their effectiveness"

# Framework learning status
/meta-review "show framework learning and adaptation status"
```
<!-- BROKEN EXAMPLE: Line 2: Path does not exist: .claude/settings.json - Agent V24 validation -->

## 📞 Getting Additional Help

### Self-Help Resources
```bash
# Framework documentation
/docs search "topic" "search all documentation"

# Command usage examples
/query "show examples of using [command] command"

# Best practices
/query "what are best practices for [specific situation]?"
```

### Community and Support
1. **Check Documentation**: Use `/docs search` to find relevant guides
2. **Review Examples**: Look at existing project configurations in `examples/`
3. **Validate Setup**: Run `/init-validate` for comprehensive checks
4. **Framework Self-Help**: Use meta-commands for framework optimization

### Escalation Path
1. **Basic Issues**: Use this troubleshooting guide
2. **Configuration Issues**: Review [Configuration Guide](../user-guide/customization/project-config.md)
3. **Complex Issues**: Use framework's self-diagnostic capabilities
4. **Framework Bugs**: Document with `/query` analysis and report

## ✅ Troubleshooting Checklist

Before asking for help, verify:

- [ ] You're in the project directory with `CLAUDE.md`
- [ ] Framework files (`.claude/`, `PROJECT_CONFIG.xml`) exist
- [ ] File permissions are correct (`chmod +x .claude/commands/*`)
- [ ] PROJECT_CONFIG.xml is configured for your project
- [ ] Basic commands like `/query "framework status"` work
- [ ] You've tried `/init-validate` for comprehensive check
- [ ] You've reviewed this troubleshooting guide

## 🎯 Prevention Tips

### Avoid Common Issues
1. **Always work in project root** where `CLAUDE.md` exists
2. **Keep PROJECT_CONFIG.xml updated** with your actual tech stack
3. **Use `/query` first** to understand before making changes
4. **Test changes incrementally** rather than making large changes
5. **Use appropriate commands** for the task scope

### Maintain Framework Health
1. **Regular validation**: Run `/init-validate` periodically
2. **Performance optimization**: Use `/meta-optimize` monthly
3. **Configuration updates**: Update PROJECT_CONFIG.xml as project evolves
4. **Clean git state**: Keep git repository clean for best results

---

**Issue resolved?** Great! Return to [Getting Started](../getting-started/) or [User Guide](../user-guide/) to continue.

**Still stuck?** Try the framework's self-diagnostic capabilities with `/meta-review "help with [your specific issue]"`.