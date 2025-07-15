# Troubleshooting Guide

## Overview
This guide helps you resolve common issues when using the Claude Code Modular Prompts Framework. For quick fixes, see the [CLAUDE.md Quick Reference](../../CLAUDE.md#troubleshooting-quick-fixes).

## Common Issues and Solutions

### 🚫 Framework Not Working

#### Issue: Commands Not Recognized
**Symptoms:**
- Generic AI responses instead of framework behavior
- Commands like `/auto`, `/task`, `/feature` not working
- No structured approach to tasks

**Solutions:**
1. **Check CLAUDE.md Location**
   ```bash
   # Verify CLAUDE.md is in project root
   ls -la CLAUDE.md
   ```
   - CLAUDE.md MUST be in the project root directory
   - Cannot be in subdirectories or renamed

2. **Verify File Content**
   ```bash
   # Check file starts with framework header
   head -10 CLAUDE.md
   ```
   - Should contain framework version and configuration
   - File should not be empty or corrupted

3. **Check Directory Structure**
   ```bash
   # Verify .claude directory exists (if using modules)
   ls -la .claude/
   ```
   - Create .claude directory if missing
   - Ensure proper module structure

**Quick Fix:**
```bash
# Reset framework files
cp CLAUDE.md CLAUDE.md.backup
# Re-download or recreate CLAUDE.md
```

#### Issue: PROJECT_CONFIG.xml Not Found
**Symptoms:**
- Framework uses default settings
- No project-specific behavior
- Generic responses for tech stack

**Solutions:**
1. **Create PROJECT_CONFIG.xml**
   ```bash
   # Copy template and customize
   cp PROJECT_CONFIG.xml.template PROJECT_CONFIG.xml
   ```

2. **Verify Configuration**
   ```xml
   <!-- Minimum required configuration -->
   <project_config>
     <tech_stack>
       <primary_language>python</primary_language>
       <framework>django</framework>
     </tech_stack>
   </project_config>
   ```

3. **Validate XML Syntax**
   ```bash
   # Check XML is well-formed
   xmllint --noout PROJECT_CONFIG.xml
   ```

### 🔧 Quality Gates Not Enforcing

#### Issue: TDD Not Being Enforced
**Symptoms:**
- Code generated without tests
- No test-driven development cycle
- Quality gates skipped

**Solutions:**
1. **Check Quality Standards Configuration**
   ```xml
   <quality_standards>
     <test_coverage>
       <threshold>90</threshold>
       <enforcement>blocking</enforcement>
     </test_coverage>
   </quality_standards>
   ```

2. **Verify Test Commands**
   ```xml
   <commands>
     <test>pytest --cov=src</test>
     <lint>flake8 src</lint>
     <build>python setup.py build</build>
   </commands>
   ```

3. **Test Command Execution**
   ```bash
   # Verify test command works
   pytest --cov=src
   ```

**Quick Fix:**
```xml
<!-- Add to PROJECT_CONFIG.xml -->
<quality_standards>
  <test_coverage>
    <threshold>90</threshold>
    <enforcement>blocking</enforcement>
  </test_coverage>
</quality_standards>
```

#### Issue: Coverage Not Measured
**Symptoms:**
- Tests run but coverage ignored
- No coverage reports generated
- Coverage gates not enforced

**Solutions:**
1. **Install Coverage Tools**
   ```bash
   # Python
   pip install pytest-cov
   
   # JavaScript
   npm install --save-dev jest
   
   # Go
   go install github.com/boumenot/gocover-cobertura@latest
   ```

2. **Configure Coverage Commands**
   ```xml
   <commands>
     <test>pytest --cov=src --cov-report=term-missing --cov-fail-under=90</test>
   </commands>
   ```

3. **Verify Coverage Reports**
   ```bash
   # Check coverage output
   pytest --cov=src --cov-report=html
   open htmlcov/index.html
   ```

### 🐌 Performance Issues

#### Issue: Slow Response Times
**Symptoms:**
- Long delays before responses
- High token usage
- Context timeouts

**Solutions:**
1. **Run Performance Analysis**
   ```bash
   # Use meta command for analysis
   /meta-review "analyze framework performance"
   ```

2. **Check Context Management**
   ```xml
   <context_management>
     <max_file_tokens>4000</max_file_tokens>
     <max_context_tokens>120000</max_context_tokens>
   </context_management>
   ```

3. **Optimize File Reading**
   ```bash
   # Reduce file sizes being processed
   # Use .gitignore to exclude large files
   echo "*.log" >> .gitignore
   echo "node_modules/" >> .gitignore
   ```

**Quick Fix:**
```bash
# Use meta-optimize command
/meta-optimize "improve response time and token usage"
```

#### Issue: High Token Usage
**Symptoms:**
- Expensive API calls
- Frequent context limits
- Slow processing

**Solutions:**
1. **Enable Context Optimization**
   ```xml
   <context_optimization>
     <hierarchical_loading>true</hierarchical_loading>
     <token_budget_tracking>true</token_budget_tracking>
   </context_optimization>
   ```

2. **Use Targeted Commands**
   ```bash
   # Instead of broad requests
   /auto "fix everything"
   
   # Use specific commands
   /task "fix login validation bug"
   ```

3. **Implement Strategic Compaction**
   ```bash
   # Use /compact when context gets large
   /compact "summarize current session"
   ```

### 🤖 Generic AI Responses

#### Issue: Not Following Framework Patterns
**Symptoms:**
- Generic programming responses
- No domain-specific expertise
- Missing framework structure

**Solutions:**
1. **Customize PROJECT_CONFIG.xml**
   ```xml
   <project_config>
     <tech_stack>
       <primary_language>python</primary_language>
       <framework>django</framework>
       <database>postgresql</database>
     </tech_stack>
     <domain_expertise>
       <type>e-commerce</type>
       <industry>retail</industry>
     </domain_expertise>
   </project_config>
   ```

2. **Use Framework Evolution**
   ```bash
   # Adapt framework to your patterns
   /meta-evolve "adapt to our Django e-commerce patterns"
   ```

3. **Verify Configuration Loading**
   ```bash
   # Check if config is being used
   grep -r "primary_language" .
   ```

**Quick Fix:**
```bash
# Force framework adaptation
/meta-evolve "adapt framework to our specific tech stack and usage patterns"
```

### 🔗 Integration Issues

#### Issue: Git Integration Problems
**Symptoms:**
- Commits not being created
- Git operations failing
- Branch management issues

**Solutions:**
1. **Check Git Configuration**
   ```bash
   # Verify git is configured
   git config user.name
   git config user.email
   ```

2. **Verify Repository State**
   ```bash
   # Check git status
   git status
   git log --oneline -5
   ```

3. **Fix Git Issues**
   ```bash
   # Initialize if needed
   git init
   git add .
   git commit -m "Initial commit"
   ```

#### Issue: IDE Integration Problems
**Symptoms:**
- Framework not working in IDE
- Code completion issues
- Debugging problems

**Solutions:**
1. **Check IDE Configuration**
   - Verify Claude Code CLI is installed
   - Check IDE Claude Code extension
   - Verify authentication tokens

2. **Reset IDE Connection**
   ```bash
   # Reset Claude Code authentication
   claude-code auth logout
   claude-code auth login
   ```

3. **Verify File Associations**
   - Check .claude files are recognized
   - Verify markdown syntax highlighting
   - Check XML validation

### 📊 Validation and Testing

#### Issue: Examples Not Working
**Symptoms:**
- Example code fails to run
- Configuration examples invalid
- Workflow examples incomplete

**Solutions:**
1. **Test Example Validation**
   ```bash
   # Run example validation script
   python scripts/validate_examples.py
   ```

2. **Check Example Dependencies**
   ```bash
   # Verify example requirements
   pip install -r examples/requirements.txt
   ```

3. **Update Examples**
   ```bash
   # Regenerate examples
   python scripts/generate_examples.py
   ```

#### Issue: Configuration Validation Failures
**Symptoms:**
- PROJECT_CONFIG.xml validation errors
- Schema validation failures
- Configuration not loading

**Solutions:**
1. **Validate XML Schema**
   ```bash
   # Check XML syntax
   xmllint --noout PROJECT_CONFIG.xml
   
   # Validate against schema
   xmllint --schema project_config.xsd PROJECT_CONFIG.xml
   ```

2. **Check Required Fields**
   ```xml
   <!-- Minimum required configuration -->
   <project_config>
     <tech_stack>
       <primary_language>python</primary_language>
     </tech_stack>
   </project_config>
   ```

3. **Reset Configuration**
   ```bash
   # Start with template
   cp PROJECT_CONFIG.xml.template PROJECT_CONFIG.xml
   ```

## Advanced Troubleshooting

### Debug Mode
Enable debug mode for detailed logging:
```bash
# Set debug environment variable
export CLAUDE_DEBUG=1

# Run with verbose output
/auto "debug issue" --verbose
```

### Log Analysis
Check framework logs for issues:
```bash
# View recent logs
tail -f ~/.claude/logs/framework.log

# Search for errors
grep -i error ~/.claude/logs/framework.log
```

### Performance Profiling
Profile framework performance:
```bash
# Use meta-review for performance analysis
/meta-review "analyze performance bottlenecks"

# Check context usage
/meta-review "analyze token usage patterns"
```

## Getting Help

### Self-Diagnosis
1. **Run Framework Validation**
   ```bash
   /validate "check framework setup"
   ```

2. **Check System Status**
   ```bash
   /meta-review "system health check"
   ```

3. **Analyze Usage Patterns**
   ```bash
   /meta-review "analyze usage patterns and issues"
   ```

### Community Support
1. **Search Documentation**
   - [User Guide](README.md)
   - [Command Reference](commands/README.md)
   - [FAQ](faq.md)

2. **Framework Help**
   ```bash
   # Get framework-specific help
   /query "how to resolve [specific issue]"
   ```

3. **Report Issues**
   - [GitHub Issues](https://github.com/user/claude-code-modular-prompts/issues)
   - Include configuration and error details
   - Provide reproduction steps

### Emergency Recovery
If the framework is completely broken:
```bash
# Backup current state
cp -r . ../project_backup

# Reset to clean state
rm -rf .claude/
rm CLAUDE.md
rm PROJECT_CONFIG.xml

# Restore from templates
cp CLAUDE.md.template CLAUDE.md
cp PROJECT_CONFIG.xml.template PROJECT_CONFIG.xml

# Reinitialize
/init "restore framework setup"
```

## Prevention

### Best Practices
1. **Regular Validation**
   ```bash
   # Weekly framework health check
   /meta-review "weekly system validation"
   ```

2. **Configuration Backup**
   ```bash
   # Backup configuration
   cp PROJECT_CONFIG.xml PROJECT_CONFIG.xml.backup
   ```

3. **Keep Updated**
   ```bash
   # Update framework regularly
   /meta-evolve "update framework to latest patterns"
   ```

### Monitoring
1. **Performance Monitoring**
   ```bash
   # Regular performance checks
   /meta-review "performance monitoring"
   ```

2. **Usage Analysis**
   ```bash
   # Analyze usage patterns
   /meta-review "usage pattern analysis"
   ```

3. **Quality Metrics**
   ```bash
   # Track quality metrics
   /meta-review "quality metrics analysis"
   ```

## Quick Reference

### Essential Diagnostic Commands
```bash
# Framework health check
/meta-review "system health check"

# Performance analysis
/meta-review "performance analysis"

# Configuration validation
/validate "check configuration"

# Reset framework
/init "reset framework setup"
```

### Common Quick Fixes
```bash
# Fix command recognition
cp CLAUDE.md.template CLAUDE.md

# Fix quality gates
# Add enforcement to PROJECT_CONFIG.xml

# Fix performance
/meta-optimize "improve performance"

# Fix generic responses
/meta-evolve "adapt to project patterns"
```

### Emergency Commands
```bash
# Complete reset
/init "emergency framework reset"

# Restore from backup
cp CLAUDE.md.backup CLAUDE.md

# Quick validation
/validate "emergency validation"
```

---

**Remember**: Most issues can be resolved by ensuring CLAUDE.md is in the project root and PROJECT_CONFIG.xml is properly configured for your tech stack. When in doubt, start with `/meta-review "analyze current issue"` to get framework-specific guidance.