# Troubleshooting Guide - Claude Code Modular Prompts Framework 3.0

**Version**: 3.0.0  
**Last Updated**: 2025-07-12  
**Purpose**: Quick resolution guide for common framework issues

## Quick Diagnostic Commands

Run these commands to quickly assess framework health:

```bash
# 1. Check framework structure
ls -la .claude/commands/
ls -la .claude/modules/

# 2. Validate module references
python module_dependency_analyzer.py

# 3. Test command functionality
python tests/integration/test_command_workflows.py

# 4. Verify configuration
python scripts/framework/config_validator.py
```

## Common Issues and Solutions

### 1. Commands Not Working

#### Issue: `/task` command not recognized
```bash
Error: Command /task not found
```

**Quick Fix**:
```bash
# Check if command file exists
ls .claude/commands/task.md

# If missing, framework may not be properly installed
git checkout main -- .claude/commands/
```

**Root Cause Analysis**:
- Command file deleted or moved
- Framework not properly cloned
- File permissions issue

**Prevention**:
- Don't modify `.claude/commands/` manually
- Use git to restore if needed
- Verify framework integrity after updates

---

#### Issue: Commands execute but produce unexpected results
```bash
/task "Add validation" → Creates code without tests
```

**Quick Fix**:
```bash
# Check command content for TDD enforcement
grep -n "TDD\|test" .claude/commands/task.md

# Verify quality modules exist
ls .claude/system/quality/tdd.md
```

**Root Cause Analysis**:
- Command file corrupted or modified
- Quality modules missing
- Module references broken

**Full Resolution**:
```bash
# Restore original command files
git checkout main -- .claude/commands/

# Fix broken module references
python internal/development/tools/fix_module_references.py

# Verify functionality
python tests/integration/test_command_workflows.py
```

### 2. Module Reference Errors

#### Issue: Broken module references
```bash
Error: Module patterns/critical-thinking-pattern.md not found
```

**Quick Fix**:
```bash
# Run automated reference fixer
python internal/development/tools/fix_module_references.py
```

**Check Progress**:
```bash
# See improvement in broken references
python module_dependency_analyzer.py
# Should show reduced broken percentage
```

**Manual Resolution** (if automation fails):
1. Find the correct module location:
   ```bash
   find .claude -name "*critical-thinking*" -type f
   ```

2. Update references manually:
   ```bash
   # Old: patterns/critical-thinking-pattern.md
   # New: prompt_eng/patterns/thinking/critical-thinking-pattern.md
   ```

---

#### Issue: Circular dependencies detected
```bash
Warning: Circular dependency between module A and module B
```

**Understanding**: This won't break functionality but indicates design issues.

**Quick Assessment**:
```bash
# View all circular dependencies
python module_dependency_analyzer.py | grep -A 20 "CIRCULAR DEPENDENCIES"
```

**Resolution Strategy**:
- Minor circles (2-3 modules): Usually safe to ignore
- Major circles (5+ modules): May need refactoring
- Critical workflows affected: Priority fix needed

### 3. Quality Gate Failures

#### Issue: Tests not enforced despite TDD commands
```bash
/task "Add feature" → No tests created
```

**Quick Fix**:
```bash
# Verify TDD module exists
cat .claude/system/quality/tdd.md

# Check command integration
grep -n "test\|TDD" .claude/commands/task.md
```

**Common Causes**:
1. **Missing TDD module**: Quality modules not accessible
2. **Broken delegation**: Commands don't reference quality gates
3. **Configuration override**: PROJECT_CONFIG.xml disables enforcement

**Resolution**:
```bash
# 1. Verify quality infrastructure
ls .claude/system/quality/

# 2. Check command-module integration
python tests/integration/test_command_workflows.py::TestCommandWorkflows::test_quality_gate_integration

# 3. Validate configuration
cat PROJECT_CONFIG.xml | grep -i "tdd\|test"
```

---

#### Issue: Coverage requirements not met
```bash
Error: Test coverage 65% below required 90%
```

**Quick Fix**:
```bash
# Check current coverage
pytest --cov=. --cov-report=term-missing

# Identify uncovered lines
pytest --cov=. --cov-report=html
open htmlcov/index.html
```

**Systematic Resolution**:
1. **Identify gaps**: Use coverage report to find untested code
2. **Write tests**: Focus on business logic and edge cases
3. **Verify**: Re-run coverage to confirm improvement
4. **Maintain**: Add coverage checks to CI/CD pipeline

### 4. Configuration Issues

#### Issue: PROJECT_CONFIG.xml not being used
```bash
# Expected: Custom test command from config
# Actual: Framework defaults used
```

**Quick Fix**:
```bash
# Verify config file exists and is valid
ls PROJECT_CONFIG.xml
python scripts/framework/config_validator.py
```

**Common Problems**:
1. **File location**: Must be in project root
2. **XML syntax**: Malformed XML won't parse
3. **Structure**: Incorrect element nesting
4. **Permissions**: File not readable

**Validation Commands**:
```bash
# 1. Check XML syntax
xmllint --noout PROJECT_CONFIG.xml 2>&1

# 2. Validate structure
python scripts/framework/config_validator.py PROJECT_CONFIG.xml

# 3. Test placeholder resolution
python scripts/framework/template_resolver.py
```

---

#### Issue: Placeholder resolution failing
```bash
# In modules: [PROJECT_CONFIG: test_directory | DEFAULT: tests]
# Expected: __tests__
# Actual: tests (default used)
```

**Debugging Steps**:
```bash
# 1. Check config content
grep -n "test_directory" PROJECT_CONFIG.xml

# 2. Validate XML path
python -c "
import xml.etree.ElementTree as ET
tree = ET.parse('PROJECT_CONFIG.xml')
print(tree.find('.//test_directory').text if tree.find('.//test_directory') is not None else 'NOT FOUND')
"

# 3. Test resolution manually
python scripts/framework/template_resolver.py --test "test_directory"
```

### 5. Performance Issues

#### Issue: Commands executing slowly
```bash
/feature "Complex feature" → Takes >5 minutes
```

**Quick Diagnostics**:
```bash
# Check module dependency depth
python module_dependency_analyzer.py | grep -A 10 "deep_dependency_chain"

# Monitor context usage
grep -c "Loading module" debug.log
```

**Optimization Strategies**:
1. **Reduce dependencies**: Simplify module relationships
2. **Parallel loading**: Ensure modules load concurrently
3. **Context management**: Use specific commands vs. generic instructions
4. **Caching**: Leverage Claude Code's context caching

**Performance Commands**:
```bash
# Time command execution
time echo "/task 'Simple function'" | claude-code

# Analyze dependency complexity
python internal/development/optimization/performance_optimizer.py

# Optimize context window
python scripts/context_optimizer.py
```

### 6. Integration Issues

#### Issue: Commands work but modules don't integrate
```bash
/swarm "Multi-file feature" → Single-threaded execution
```

**Diagnostic Process**:
```bash
# 1. Check command structure
cat .claude/commands/swarm.md

# 2. Verify module delegation
grep -n "multi-agent\|coordination" .claude/commands/swarm.md

# 3. Test module accessibility
ls .claude/modules/patterns/multi-agent.md
```

**Common Integration Problems**:
1. **Command-module mismatch**: Commands don't reference correct modules
2. **Module missing**: Referenced modules don't exist
3. **Execution model**: Claude doesn't understand delegation patterns

**Resolution**:
```bash
# Update command-module mapping
python scripts/update_command_mapping.py

# Validate integration
python tests/integration/test_command_workflows.py

# Fix any broken references
python internal/development/tools/fix_module_references.py
```

## Framework Health Assessment

### Quick Health Check

```bash
#!/bin/bash
echo "=== Framework Health Check ==="

# 1. Command availability
echo "Commands found: $(ls .claude/commands/*.md | wc -l)"

# 2. Module integrity
echo "Modules found: $(find .claude/modules -name "*.md" | wc -l)"

# 3. Reference health
python module_dependency_analyzer.py | grep "broken_percentage"

# 4. Quality infrastructure
if [ -f ".claude/system/quality/tdd.md" ]; then
  echo "Quality gates: ✅ Available"
else
  echo "Quality gates: ❌ Missing"
fi

# 5. Configuration status
if [ -f "PROJECT_CONFIG.xml" ]; then
  echo "Configuration: ✅ Found"
else
  echo "Configuration: ⚠️ Using defaults"
fi
```

### Comprehensive Validation

```bash
# Full framework validation
python tests/framework_validation.py

# Integration testing
python tests/integration/test_command_workflows.py

# Dependency analysis
python module_dependency_analyzer.py

# Performance baseline
python tests/performance_benchmark.py
```

## Recovery Procedures

### Framework Corruption Recovery

If the framework appears completely broken:

```bash
# 1. Backup current state
cp -r .claude .claude.backup.$(date +%Y%m%d_%H%M%S)

# 2. Reset to known good state
git checkout main -- .claude/

# 3. Apply custom fixes
python internal/development/tools/fix_module_references.py

# 4. Validate recovery
python tests/integration/test_command_workflows.py

# 5. If issues persist, check git history
git log --oneline .claude/ | head -10
```

### Module Reference Recovery

If references are severely broken:

```bash
# 1. Generate reference map
python module_dependency_analyzer.py > reference_analysis.txt

# 2. Create fix script
python scripts/generate_reference_fixes.py reference_analysis.txt

# 3. Apply fixes in batches
python internal/development/tools/fix_module_references.py --batch-size 10

# 4. Verify each batch
python module_dependency_analyzer.py

# 5. Iterate until health acceptable
```

### Configuration Recovery

If configuration is corrupted:

```bash
# 1. Backup current config
cp PROJECT_CONFIG.xml PROJECT_CONFIG.xml.backup

# 2. Generate new config from template
python scripts/framework/generate_config.py --template basic

# 3. Merge user customizations
python scripts/framework/merge_config.py PROJECT_CONFIG.xml.backup

# 4. Validate new configuration
python scripts/framework/config_validator.py
```

## Prevention Strategies

### 1. Regular Maintenance

```bash
# Weekly health check
python module_dependency_analyzer.py
python tests/integration/test_command_workflows.py

# Monthly reference cleanup
python internal/development/tools/fix_module_references.py

# Quarterly full validation
python tests/framework_validation.py
```

### 2. Change Management

- **Never edit `.claude/commands/` directly**
- **Use git for framework updates**
- **Test changes in isolated branches**
- **Backup before major modifications**

### 3. Monitoring Setup

```bash
# Add to .git/hooks/pre-commit
#!/bin/bash
python module_dependency_analyzer.py | grep "broken_percentage" | awk '{
  if ($3 > 50) {
    echo "ERROR: Broken references exceed 50%"
    exit 1
  }
}'
```

## Getting Help

### 1. Self-Diagnosis

```bash
# Generate comprehensive diagnostic report
python scripts/generate_diagnostic_report.py > framework_diagnosis.txt

# Include in support requests
cat framework_diagnosis.txt
```

### 2. Community Support

- **GitHub Issues**: [claude-code-modular-prompts/issues](https://github.com/user/claude-code-modular-prompts/issues)
- **Documentation**: Check [Runtime Integration Guide](RUNTIME_INTEGRATION_GUIDE.md)
- **Examples**: Review [Integration Test Report](integration_test_report.md)

### 3. Debug Information

When reporting issues, include:

```bash
# Framework version
head -1 CLAUDE.md | grep "version"

# System information
uname -a
python --version

# Recent git changes
git log --oneline -10 .claude/

# Health metrics
python module_dependency_analyzer.py | head -20

# Configuration status
ls -la PROJECT_CONFIG.xml
python scripts/framework/config_validator.py
```

This troubleshooting guide should resolve 90%+ of common framework issues. For complex problems, use the diagnostic tools to gather information before seeking additional support.