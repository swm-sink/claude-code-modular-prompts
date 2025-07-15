# API Reference

## Overview
This document provides comprehensive API reference for the Claude Code Modular Prompts Framework, including configuration schemas, command interfaces, and integration patterns.

## Configuration API

### PROJECT_CONFIG.xml Schema

#### Root Element
```xml
<project_config version="1.0">
  <!-- All configuration elements -->
</project_config>
```

#### Tech Stack Configuration
```xml
<tech_stack>
  <primary_language>python | javascript | typescript | go | rust | java | php | kotlin | swift</primary_language>
  <framework>django | flask | fastapi | react | nextjs | vue | angular | gin | echo | spring | rails</framework>
  <database>postgresql | mysql | mongodb | redis | sqlite | cassandra | elasticsearch</database>
  <testing_framework>pytest | jest | mocha | go-test | junit | rspec | phpunit</testing_framework>
  <build_system>maven | gradle | npm | yarn | cargo | go-mod | composer</build_system>
</tech_stack>
```

#### Directory Structure
```xml
<directory_structure>
  <source_directory>src | lib | app | main</source_directory>
  <test_directory>tests | test | spec | __tests__</test_directory>
  <docs_directory>docs | documentation | wiki</docs_directory>
  <scripts_directory>scripts | bin | tools</scripts_directory>
  <config_directory>config | conf | settings</config_directory>
</directory_structure>
```

#### Commands Configuration
```xml
<commands>
  <test>pytest --cov=src --cov-report=term-missing</test>
  <lint>flake8 src tests</lint>
  <format>black src tests</format>
  <build>python setup.py build</build>
  <deploy>kubectl apply -f deployment.yaml</deploy>
  <start>python manage.py runserver</start>
  <install>pip install -r requirements.txt</install>
</commands>
```

#### Quality Standards
```xml
<quality_standards>
  <test_coverage>
    <threshold>90</threshold>
    <enforcement>blocking | warning | disabled</enforcement>
  </test_coverage>
  <performance>
    <response_time_p95>200</response_time_p95>
    <memory_usage_mb>512</memory_usage_mb>
  </performance>
  <security>
    <vulnerability_scan>enabled | disabled</vulnerability_scan>
    <dependency_check>enabled | disabled</dependency_check>
  </security>
</quality_standards>
```

#### AI Temperature Settings
```xml
<ai_temperature>
  <factual>0.2</factual>
  <analysis>0.0</analysis>
  <creative>0.7</creative>
  <code_generation>0.3</code_generation>
</ai_temperature>
```

#### Context Management
```xml
<context_management>
  <max_file_tokens>4000</max_file_tokens>
  <max_context_tokens>120000</max_context_tokens>
  <reserved_work_tokens>50000</reserved_work_tokens>
  <hierarchical_loading>true | false</hierarchical_loading>
</context_management>
```

#### Team Workflow
```xml
<team_workflow>
  <code_review>
    <required>true | false</required>
    <reviewers>2</reviewers>
    <approval_required>true | false</approval_required>
  </code_review>
  <deployment>
    <strategy>blue-green | rolling | canary</strategy>
    <environment>kubernetes | docker | serverless</environment>
    <approval_gates>staging | production</approval_gates>
  </deployment>
</team_workflow>
```

#### Domain Expertise
```xml
<domain_expertise>
  <type>e-commerce | fintech | healthcare | education | gaming</type>
  <industry>retail | finance | medical | edtech | entertainment</industry>
  <specialization>backend | frontend | fullstack | devops | mobile</specialization>
</domain_expertise>
```

## Command API

### Core Commands

#### /auto Command
```bash
/auto "request description"
```
**Parameters:**
- `request` (string, required): Description of what you want to accomplish

**Returns:**
- Analysis of request scope and complexity
- Selected command with reasoning
- Execution of chosen approach

**Examples:**
```bash
/auto "fix the login bug"
/auto "add user dashboard functionality"
/auto "optimize database performance"
```

#### /task Command
```bash
/task "specific implementation task"
```
**Parameters:**
- `task` (string, required): Specific, focused task description

**Returns:**
- TDD cycle (RED → GREEN → REFACTOR)
- Test files with comprehensive coverage
- Minimal implementation code
- Integration examples

**Examples:**
```bash
/task "add email validation to user registration"
/task "fix memory leak in image processing"
/task "add caching to product search"
```

#### /feature Command
```bash
/feature "complete feature description"
```
**Parameters:**
- `feature` (string, required): Complete feature to be developed

**Returns:**
- Product Requirements Document (PRD)
- Architecture planning
- Implementation phases
- Full feature implementation
- Integration testing

**Examples:**
```bash
/feature "shopping cart system"
/feature "user authentication with 2FA"
/feature "real-time notifications"
```

#### /query Command
```bash
/query "research question or analysis request"
```
**Parameters:**
- `query` (string, required): Question about codebase or system

**Returns:**
- Comprehensive analysis
- Architecture insights
- Usage examples
- Improvement recommendations
- No code modifications

**Examples:**
```bash
/query "how does the authentication system work?"
/query "what are the performance bottlenecks?"
/query "how is the database schema designed?"
```

### Support Commands

#### /docs Command
```bash
/docs "documentation request"
```
**Parameters:**
- `documentation` (string, required): Type of documentation needed

**Returns:**
- Comprehensive documentation
- Code examples
- Usage instructions
- Best practices

**Examples:**
```bash
/docs "API documentation for user endpoints"
/docs "deployment guide for production"
/docs "contributing guidelines"
```

#### /session Command
```bash
/session "long-running work description"
```
**Parameters:**
- `work` (string, required): Description of extended work session

**Returns:**
- Session initialization
- Progress tracking
- Context preservation
- Multi-step coordination

**Examples:**
```bash
/session "refactor user authentication system"
/session "implement microservices architecture"
/session "optimize application performance"
```

#### /protocol Command
```bash
/protocol "production operation"
```
**Parameters:**
- `operation` (string, required): Production-ready operation

**Returns:**
- Safety validation
- Production deployment
- Monitoring setup
- Rollback procedures

**Examples:**
```bash
/protocol "deploy user authentication fixes"
/protocol "migrate database schema"
/protocol "scale application infrastructure"
```

### Meta Commands

#### /meta-review Command
```bash
/meta-review "analysis request"
```
**Parameters:**
- `analysis` (string, required): What to analyze about framework usage

**Returns:**
- Framework performance metrics
- Usage pattern analysis
- Optimization recommendations
- Compliance reporting

**Examples:**
```bash
/meta-review "analyze framework performance"
/meta-review "check quality gate compliance"
/meta-review "review usage patterns"
```

#### /meta-optimize Command
```bash
/meta-optimize "optimization target"
```
**Parameters:**
- `target` (string, required): What to optimize

**Returns:**
- Performance improvements
- Configuration optimization
- Workflow enhancements
- Resource efficiency

**Examples:**
```bash
/meta-optimize "improve response time"
/meta-optimize "reduce token usage"
/meta-optimize "enhance code quality"
```

#### /meta-evolve Command
```bash
/meta-evolve "adaptation request"
```
**Parameters:**
- `adaptation` (string, required): How framework should adapt

**Returns:**
- Framework adaptation
- Pattern learning
- Workflow evolution
- Team integration

**Examples:**
```bash
/meta-evolve "adapt to team coding patterns"
/meta-evolve "learn from project architecture"
/meta-evolve "optimize for domain-specific work"
```

## Integration Patterns

### Git Integration
```bash
# Automatic commit creation
git add -A
git commit -m "Feature: Add user authentication

- Implemented JWT token authentication
- Added password validation
- Created comprehensive test suite
- Updated API documentation

🤖 Generated with [Claude Code](https://claude.ai/code)
Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Testing Integration
```python
# Pytest integration
def test_password_validation():
    """Test password validation requirements"""
    assert validate_password("short") == False
    assert validate_password("ValidPass123!") == True

# Jest integration
describe('Password Validation', () => {
  test('should reject short passwords', () => {
    expect(validatePassword('short')).toBe(false);
  });
  
  test('should accept valid passwords', () => {
    expect(validatePassword('ValidPass123!')).toBe(true);
  });
});
```

### CI/CD Integration
```yaml
# GitHub Actions integration
name: Framework Quality Gates
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Tests
        run: pytest --cov=src --cov-fail-under=90
      - name: Quality Gates
        run: |
          flake8 src tests
          black --check src tests
```

### IDE Integration
```json
{
  "claude-code": {
    "framework": "enabled",
    "auto-commit": true,
    "quality-gates": "blocking",
    "tdd-enforcement": true
  }
}
```

## Response Formats

### Command Response Structure
```json
{
  "command": "/task",
  "analysis": {
    "scope": "single-component",
    "complexity": "medium",
    "estimated_time": "15-30 minutes"
  },
  "execution": {
    "phases": ["RED", "GREEN", "REFACTOR"],
    "files_created": ["tests/test_validation.py", "src/validation.py"],
    "tests_added": 5,
    "coverage": "95%"
  },
  "results": {
    "success": true,
    "quality_gates_passed": true,
    "next_steps": ["integrate with user model", "add error handling"]
  }
}
```

### Error Response Structure
```json
{
  "error": {
    "code": "QUALITY_GATE_FAILED",
    "message": "Test coverage below threshold",
    "details": {
      "current_coverage": "85%",
      "required_coverage": "90%",
      "missing_coverage": ["src/validation.py lines 45-52"]
    },
    "remediation": "Add tests for validation edge cases"
  }
}
```

## Configuration Validation

### XML Schema Validation
```bash
# Validate PROJECT_CONFIG.xml
xmllint --schema project_config.xsd PROJECT_CONFIG.xml --noout
```

### Required Fields
```xml
<!-- Minimum required configuration -->
<project_config>
  <tech_stack>
    <primary_language>python</primary_language>
  </tech_stack>
</project_config>
```

### Optional Fields
All other configuration elements are optional and will use framework defaults if not specified.

## Environment Variables

### Framework Configuration
```bash
# Debug mode
export CLAUDE_DEBUG=1

# Custom config path
export CLAUDE_CONFIG_PATH="/path/to/PROJECT_CONFIG.xml"

# Disable TDD enforcement (not recommended)
export CLAUDE_DISABLE_TDD=1

# Custom context limits
export CLAUDE_MAX_CONTEXT_TOKENS=150000
```

### CI/CD Variables
```bash
# Production deployment
export CLAUDE_ENVIRONMENT=production
export CLAUDE_QUALITY_GATES=strict

# Testing environment
export CLAUDE_ENVIRONMENT=test
export CLAUDE_COVERAGE_THRESHOLD=95
```

## Error Codes

### Common Error Codes
- `CONFIG_NOT_FOUND`: PROJECT_CONFIG.xml not found
- `INVALID_CONFIG`: XML schema validation failed
- `QUALITY_GATE_FAILED`: Quality standards not met
- `TDD_VIOLATION`: Implementation without tests
- `CONTEXT_LIMIT_EXCEEDED`: Token limit exceeded
- `COMMAND_NOT_FOUND`: Invalid command specified

### Error Handling
```python
try:
    result = execute_command("/task", "add validation")
except FrameworkError as e:
    if e.code == "QUALITY_GATE_FAILED":
        # Handle quality gate failure
        print(f"Quality gate failed: {e.message}")
    elif e.code == "TDD_VIOLATION":
        # Handle TDD violation
        print(f"TDD violation: {e.message}")
```

## Performance Metrics

### Response Time Targets
- Simple `/task` commands: < 30 seconds
- Complex `/feature` commands: < 5 minutes
- `/query` analysis: < 1 minute
- `/meta-*` commands: < 1 minute

### Token Usage Guidelines
- Small tasks: 1,000-5,000 tokens
- Medium features: 5,000-20,000 tokens
- Large features: 20,000-50,000 tokens
- Analysis queries: 2,000-10,000 tokens

### Quality Metrics
- Test coverage: ≥ 90% (configurable)
- Code quality: No linting errors
- Security: No high-severity vulnerabilities
- Performance: Response time < 200ms P95

## Migration Guide

### From Manual Development
1. **Add CLAUDE.md** to project root
2. **Create PROJECT_CONFIG.xml** with tech stack
3. **Start with `/query`** to understand existing code
4. **Use `/task`** for incremental improvements
5. **Add tests gradually** with framework enforcement

### From Other Frameworks
1. **Map existing commands** to framework equivalents
2. **Configure quality standards** to match current practices
3. **Migrate workflows** using `/protocol` command
4. **Update CI/CD** to use framework quality gates

## Best Practices

### Configuration
- **Always customize PROJECT_CONFIG.xml** for your project
- **Use specific tech stack settings** for better responses
- **Configure quality standards** appropriately for your team
- **Set up proper directory structure** mapping

### Command Usage
- **Use `/auto`** when uncertain about approach
- **Use `/query`** before making changes
- **Follow TDD** enforced by framework
- **Use specific commands** when you know what you want

### Performance Optimization
- **Configure context limits** appropriately
- **Use `/compact`** for long sessions
- **Break down large requests** into smaller commands
- **Regular `/meta-optimize`** for continuous improvement

---

## Quick Reference

### Essential Configuration
```xml
<project_config>
  <tech_stack>
    <primary_language>python</primary_language>
    <framework>django</framework>
    <database>postgresql</database>
  </tech_stack>
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>blocking</enforcement>
    </test_coverage>
  </quality_standards>
</project_config>
```

### Command Decision Tree
```
Need to understand? → /query
Know what to build? → /task (single) or /feature (multi)
Unsure about approach? → /auto
Need documentation? → /docs
Production deployment? → /protocol
```

### Error Resolution
```bash
# Most common fixes
# 1. Check CLAUDE.md location
# 2. Validate PROJECT_CONFIG.xml
# 3. Run /meta-review for diagnostics
# 4. Use /validate for configuration check
```