---
name: /validate-automation
description: "Comprehensive validation and testing framework for template automation system"
usage: /validate-automation [--scope=templates|scripts|integration|full] [--fix-issues]
category: meta-commands
tools: Read, Write, Edit, Bash, Glob, Grep, LS
---

# Automation System Validation Framework

**Comprehensive testing and validation of template library automation components.**

## What This Validates (COMPLETE SYSTEM VERIFICATION)

Automated validation of:
1. **Template Quality**: YAML frontmatter, markdown structure, placeholder consistency
2. **Script Functionality**: Framework detection, placeholder replacement, file operations
3. **Integration Points**: MCP memory, sub-agent coordination, meta-prompting cycles
4. **User Experience**: Command discoverability, documentation clarity, workflow efficiency
5. **System Reliability**: Error handling, recovery mechanisms, data integrity

## Validation Scopes

### Template Validation (--scope=templates)
```
/validate-automation --scope=templates
```

**Validates All Command Templates:**
- ✅ YAML frontmatter completeness and syntax
- ✅ Required fields: name, description, usage, tools
- ✅ Markdown structure and formatting consistency
- ✅ Placeholder syntax and replacement patterns
- ✅ Example code blocks and command demonstrations
- ✅ Tool specification accuracy and availability

**Quality Metrics:**
```yaml
template_validation_results:
  total_templates: 64
  passing_templates: 62
  failing_templates: 2
  warnings: 5
  
  detailed_results:
    yaml_syntax_errors: 0
    missing_required_fields: 1
    placeholder_inconsistencies: 1
    markdown_formatting_issues: 3
    broken_tool_references: 0
```

### Script Functionality (--scope=scripts)
```
/validate-automation --scope=scripts
```

**Validates All Automation Scripts:**
- ✅ Framework detection accuracy across project types
- ✅ Placeholder replacement completeness and correctness
- ✅ File operation safety and error handling
- ✅ JSON output format consistency
- ✅ Edge case handling and graceful failures

**Test Cases:**
```javascript
const scriptTests = {
  "detect-framework.sh": [
    {
      testCase: "React + TypeScript project",
      expectedFrameworks: ["react", "typescript"],
      projectStructure: ["package.json", "tsconfig.json"],
      confidenceThreshold: 0.9
    },
    {
      testCase: "Django + PostgreSQL API",
      expectedFrameworks: ["django", "postgresql"],
      projectStructure: ["manage.py", "requirements.txt"],
      confidenceThreshold: 0.85
    }
  ],
  
  "replace-placeholders.sh": [
    {
      testCase: "Complete placeholder replacement",
      inputTemplates: ["api-create.md", "component-create.md"],
      expectedReplacements: 23,
      dryRunFirst: true
    }
  ]
}
```

### Integration Testing (--scope=integration)
```
/validate-automation --scope=integration
```

**Validates System Integration:**
- ✅ MCP memory system persistence and retrieval
- ✅ Sub-agent coordination and communication
- ✅ Meta-prompting cycle effectiveness
- ✅ Cross-command data sharing and context
- ✅ User feedback loop functionality

**Integration Test Scenarios:**
```yaml
integration_tests:
  memory_persistence:
    - Initialize MCP memory system
    - Store user preferences and project context
    - Restart Claude Code session
    - Verify context restoration and continuity
    
  sub_agent_coordination:
    - Launch multiple specialists simultaneously
    - Verify shared context and communication
    - Test conflict resolution mechanisms
    - Validate result aggregation quality
    
  template_adaptation:
    - Run framework detection on test project
    - Execute automated placeholder replacement
    - Verify template customization accuracy
    - Test rollback and recovery procedures
```

### Full System Validation (--scope=full)
```
/validate-automation --scope=full
```

**Comprehensive End-to-End Testing:**
- 🔍 Complete template library scan and validation
- ⚙️ All automation scripts functionality verification
- 🔗 Integration points and data flow testing
- 👤 User workflow simulation and experience validation
- 📊 Performance benchmarking and optimization analysis

## Validation Test Suite

### 1. Template Syntax Validation
```bash
# Automated YAML frontmatter validation
validate_yaml_frontmatter() {
  local template_file=$1
  local yaml_section=$(sed -n '/^---$/,/^---$/p' "$template_file")
  
  # Check required fields
  local required_fields=("name" "description" "usage" "tools")
  for field in "${required_fields[@]}"; do
    if ! echo "$yaml_section" | grep -q "^$field:"; then
      echo "❌ Missing required field: $field in $template_file"
      return 1
    fi
  done
  
  # Validate YAML syntax
  if ! echo "$yaml_section" | python3 -c "import yaml, sys; yaml.safe_load(sys.stdin)"; then
    echo "❌ Invalid YAML syntax in $template_file"
    return 1
  fi
  
  echo "✅ $template_file - Valid YAML frontmatter"
  return 0
}
```

### 2. Placeholder Consistency Check
```javascript
// Validate placeholder patterns across templates
const placeholderValidation = {
  standardPlaceholders: [
    "[INSERT_PROJECT_NAME]",
    "[INSERT_TECH_STACK]",
    "[INSERT_FRAMEWORK]",
    "[INSERT_AUTHOR]"
  ],
  
  validateConsistency: (templateContent) => {
    const found = templateContent.match(/\[INSERT_[^\]]+\]/g) || [];
    const nonStandard = found.filter(p => !this.standardPlaceholders.includes(p));
    
    return {
      standardFound: found.filter(p => this.standardPlaceholders.includes(p)),
      nonStandardFound: nonStandard,
      isConsistent: nonStandard.length === 0
    };
  }
}
```

### 3. Script Functionality Testing
```bash
# Test framework detection accuracy
test_framework_detection() {
  local test_projects_dir="./test-projects"
  
  # Test React project detection
  local react_result=$(./detect-framework.sh "$test_projects_dir/react-app" json)
  if echo "$react_result" | grep -q '"react": "detected"'; then
    echo "✅ React detection working"
  else
    echo "❌ React detection failed"
    return 1
  fi
  
  # Test Python Django detection
  local django_result=$(./detect-framework.sh "$test_projects_dir/django-api" json)
  if echo "$django_result" | grep -q '"django": "detected"'; then
    echo "✅ Django detection working"
  else
    echo "❌ Django detection failed"
    return 1
  fi
}
```

### 4. Integration Workflow Testing
```yaml
# Complete workflow validation
workflow_tests:
  new_project_onboarding:
    steps:
      1. "Create test project with specific tech stack"
      2. "Run /adapt-to-project-auto"
      3. "Verify framework detection accuracy"
      4. "Confirm placeholder replacement completion"
      5. "Test generated commands functionality"
      6. "Validate MCP memory persistence"
    
    success_criteria:
      - framework_detection_accuracy: "> 90%"
      - placeholder_replacement_rate: "100%"
      - command_functionality: "All generated commands work"
      - memory_persistence: "Context survives session restart"
```

## Automated Issue Detection and Fixing

### Issue Detection Patterns
```javascript
const issueDetectors = {
  missingTools: {
    pattern: /tools:.*(?!Read|Write|Edit|Bash|Glob|Grep)/,
    severity: "warning",
    description: "Command references tools not in standard set"
  },
  
  brokenPlaceholders: {
    pattern: /\[INSERT_[^\]]*[^A-Z_\]]/,
    severity: "error", 
    description: "Malformed placeholder syntax"
  },
  
  inconsistentYAML: {
    pattern: /^(usage|argument-hint):/,
    severity: "warning",
    description: "Non-standard YAML field names"
  }
}
```

### Automatic Issue Resolution (--fix-issues)
```bash
# Automated issue fixing capabilities
fix_common_issues() {
  local template_file=$1
  
  # Fix YAML field inconsistencies
  sed -i 's/argument-hint:/usage:/g' "$template_file"
  sed -i 's/allowed-tools:/tools:/g' "$template_file"
  
  # Standardize placeholder format
  sed -i 's/\[INSERT_\([^]]*\)\]/[INSERT_\U\1]/g' "$template_file"
  
  # Add missing required fields with defaults
  if ! grep -q "^category:" "$template_file"; then
    sed -i '/^tools:/a category: general' "$template_file"
  fi
  
  echo "🔧 Applied automatic fixes to $template_file"
}
```

## Performance and Quality Benchmarks

### Template Performance Metrics
```yaml
performance_benchmarks:
  template_load_time: "< 100ms per template"
  placeholder_replacement_speed: "< 2s for 64 templates"
  framework_detection_time: "< 5s for complex projects"
  memory_operation_latency: "< 50ms for read/write"
  
quality_thresholds:
  yaml_syntax_compliance: "100%"
  placeholder_consistency: "> 95%"
  tool_reference_accuracy: "100%"
  documentation_completeness: "> 90%"
```

### User Experience Validation
```javascript
// UX validation through automated workflow testing
const uxValidation = {
  commandDiscoverability: {
    test: "Can users find relevant commands?",
    metric: "Search success rate",
    threshold: 0.85
  },
  
  workflowEfficiency: {
    test: "How many steps to complete common tasks?",
    metric: "Average steps per workflow",
    threshold: "< 5 steps"
  },
  
  errorRecovery: {
    test: "Can users recover from common mistakes?",
    metric: "Recovery success rate",
    threshold: 0.90
  }
}
```

## Validation Reports and Analytics

### Comprehensive Validation Report
```
📊 TEMPLATE LIBRARY VALIDATION REPORT
=====================================

🎯 Overall Health Score: 94/100

📋 Template Quality:
   ✅ 62/64 templates passing all checks
   ⚠️  2 templates with minor issues
   📈 Quality trend: +5% improvement over last validation

⚙️ Script Functionality:
   ✅ Framework detection: 97% accuracy
   ✅ Placeholder replacement: 100% success rate
   ✅ Error handling: All edge cases covered

🔗 Integration Status:
   ✅ MCP memory system: Fully operational
   ✅ Sub-agent coordination: Tested and verified
   ✅ Meta-prompting cycles: High effectiveness

👤 User Experience:
   ✅ Command discoverability: 89% success rate
   ✅ Workflow efficiency: 4.2 avg steps per task
   ✅ Error recovery: 92% recovery success

🚀 Performance Metrics:
   ✅ Template loading: 87ms average
   ✅ Framework detection: 3.2s average
   ✅ Memory operations: 42ms average

🔧 Recommendations:
   1. Update 2 templates with minor YAML issues
   2. Optimize framework detection for monorepo projects
   3. Add more examples to complex workflow templates
```

### Continuous Validation
```bash
# Set up automated validation in CI/CD
validate_on_commit() {
  # Run validation on every template change
  git diff --name-only HEAD~1 | grep '\.claude/commands' | while read file; do
    /validate-automation --scope=templates --file="$file"
  done
  
  # Run full validation weekly
  if [[ $(date +%u) == 1 ]]; then
    /validate-automation --scope=full --generate-report
  fi
}
```

---

## Ready for System Validation?

Ensure your template automation system maintains high quality, reliability, and user experience through comprehensive automated validation.

**Example**: `/validate-automation --scope=full --fix-issues` to run complete system validation with automatic issue resolution.