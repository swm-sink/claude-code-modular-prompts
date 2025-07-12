# Runtime Integration Guide - Claude Code Modular Prompts Framework 3.0

**Version**: 3.0.0  
**Last Updated**: 2025-07-12  
**Purpose**: Comprehensive guide for understanding how the framework integrates with Claude Code

## Overview

The Claude Code Modular Prompts Framework uses a **two-tier architecture** where simple command files integrate with Claude Code, while sophisticated module infrastructure provides the underlying capabilities.

```
User Input → Claude Code → Command File → Module Infrastructure → Execution
     ↓              ↓              ↓                   ↓              ↓
  "/task X"    Interprets    task.md        Delegates to         TDD workflow
                command     instructions    task-management.md    + quality gates
```

## How Commands Execute in Claude Code

### 1. Command Discovery

When you type `/task "Add validation"`, Claude Code:

1. **Locates Command File**: Finds `.claude/commands/task.md`
2. **Reads Instructions**: Parses the markdown content
3. **Interprets Workflow**: Converts instructions to executable steps
4. **Delegates Execution**: Claude applies the command's workflow

### 2. Command File Structure

Commands use a simplified format optimized for Claude Code:

```markdown
# Command Name

Brief description of command purpose.

## Instructions

Step-by-step workflow with specific instructions for Claude to follow.

## Critical Rules

- Mandatory requirements that must be followed
- Quality gates and constraints

## Examples

- Example usage patterns
```

### 3. Command Types and Execution Patterns

#### Development Commands (`/task`, `/feature`, `/swarm`)

**Execution Flow**:
```
Input → Parse requirements → Research phase → TDD cycle → Quality validation → Output
```

**Key Features**:
- Mandatory TDD enforcement (RED→GREEN→REFACTOR)
- 90%+ test coverage requirements
- Quality gate validation
- Production-ready standards

#### Research Commands (`/query`, `/auto`)

**Execution Flow**:
```
Input → Analysis → Information gathering → Synthesis → Presentation
```

**Key Features**:
- No code modification (read-only)
- Comprehensive analysis
- Evidence-based conclusions
- Intelligent routing (for `/auto`)

#### Session Commands (`/session`, `/protocol`)

**Execution Flow**:
```
Input → Context management → Workflow execution → State preservation → Cleanup
```

**Key Features**:
- Long-running task management
- GitHub issue integration
- Context preservation
- Recovery mechanisms

### 4. Module Infrastructure Integration

While commands are simple, they leverage sophisticated module infrastructure:

#### Quality Gates Integration
```
Command Instruction: "Validate against production standards"
        ↓
Module Delegation: system/quality/universal-quality-gates.md
        ↓
Execution: TDD enforcement + security validation + performance checks
```

#### Pattern Library Integration
```
Command Instruction: "Follow TDD workflow"
        ↓
Module Delegation: patterns/tdd-cycle-pattern.md
        ↓
Execution: RED phase → GREEN phase → REFACTOR phase with coverage validation
```

## Configuration Resolution Mechanism

### PROJECT_CONFIG.xml System

The framework uses dynamic configuration resolution:

```xml
<project_config>
  <test_directory>tests</test_directory>
  <test_coverage>
    <threshold>90</threshold>
  </test_coverage>
  <commands>
    <test>pytest --cov=. --cov-report=term-missing</test>
  </commands>
</project_config>
```

### Placeholder Resolution

In module files, placeholders resolve at runtime:

```markdown
Test coverage must be [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%
```

**Resolution Process**:
1. Check for PROJECT_CONFIG.xml in project root
2. Extract value from specified path
3. Fall back to default if not found
4. Replace placeholder with resolved value

### Configuration Hierarchy

```
User PROJECT_CONFIG.xml → Framework defaults → Hard-coded fallbacks
```

## Integration with Claude Code Features

### 1. Memory Management

**Framework Integration**:
- Commands stored in `.claude/commands/` for persistent access
- Module references use relative paths for portability
- Context preserved across sessions

**Best Practices**:
```bash
# Framework files are automatically included in Claude Code context
# No manual @import needed for commands
/task "Add validation"  # Just works

# For specific modules, use relative paths
@import .claude/modules/quality/tdd.md
```

### 2. Tool Integration

**Automatic Tool Selection**:
Commands automatically trigger appropriate tools:

```markdown
## Instructions
1. Research existing patterns (triggers: Read, Grep tools)
2. Write failing tests (triggers: Write, Edit tools)  
3. Run test coverage (triggers: Bash tool with coverage commands)
```

**Parallel Execution**:
Framework leverages Claude 4's parallel execution:
```markdown
## Workflow
Execute these steps concurrently:
- Read existing implementation
- Analyze test coverage
- Review quality standards
```

### 3. Session Management

**Long-running Tasks**:
```bash
/session "Complex feature development"
# Automatically creates GitHub issue
# Tracks progress across multiple interactions
# Preserves context and state
```

**Recovery Mechanisms**:
```bash
/protocol "Resume interrupted work"
# Analyzes current state
# Identifies incomplete tasks
# Provides recovery options
```

## Troubleshooting Common Issues

### Issue 1: Command Not Found

**Symptoms**: `/task` command not recognized

**Causes**:
- Command file missing from `.claude/commands/`
- Incorrect file naming (should be `task.md`)
- File permissions

**Resolution**:
```bash
# Check command exists
ls .claude/commands/task.md

# Verify file content
cat .claude/commands/task.md
```

### Issue 2: Module References Broken

**Symptoms**: Commands execute but modules not found

**Causes**:
- Broken relative paths in module references
- Modules moved to different locations
- Missing modules

**Resolution**:
```bash
# Run dependency analyzer
python module_dependency_analyzer.py

# Fix broken references
python scripts/fix_module_references.py

# Verify fixes
python module_dependency_analyzer.py
```

### Issue 3: Quality Gates Not Enforcing

**Symptoms**: Code generated without tests or coverage

**Causes**:
- TDD enforcement disabled
- Quality modules not accessible
- Configuration overrides

**Resolution**:
```bash
# Verify quality modules exist
ls .claude/system/quality/

# Check TDD enforcement
grep -r "TDD" .claude/commands/

# Validate quality gates
python tests/integration/test_command_workflows.py
```

### Issue 4: Configuration Not Resolving

**Symptoms**: Default values used instead of project config

**Causes**:
- PROJECT_CONFIG.xml missing or malformed
- Incorrect XML structure
- Path resolution issues

**Resolution**:
```bash
# Validate PROJECT_CONFIG.xml
python scripts/framework/config_validator.py

# Check XML structure
cat PROJECT_CONFIG.xml

# Test placeholder resolution
python scripts/framework/template_resolver.py
```

## Performance Optimization

### 1. Context Management

**Best Practices**:
- Use specific commands rather than generic instructions
- Leverage module composition for complex workflows
- Take advantage of parallel execution

**Example**:
```bash
# Optimized: Specific command with clear workflow
/feature "Add user authentication"

# Less optimal: Generic instruction requiring interpretation
"Please add user authentication with tests and validation"
```

### 2. Module Efficiency

**Parallel Loading**:
```bash
# Framework automatically loads required modules in parallel
/swarm "Multi-component feature"
# Loads: multi-agent.md + worktree-isolation.md + coordination-patterns.md
```

**Context Window Optimization**:
- Commands load only necessary modules
- Module references are relative and efficient
- Token usage optimized through hierarchical loading

## Advanced Usage Patterns

### 1. Command Composition

**Chaining Commands**:
```bash
/query "Analyze authentication patterns"
# Followed by:
/feature "Implement OAuth integration"
```

**Session-based Workflows**:
```bash
/session "Authentication refactor"
/task "Extract auth service"
/task "Add OAuth provider"
/task "Update test coverage"
/protocol "Finalize and deploy"
```

### 2. Custom Configuration

**Project-specific Setup**:
```xml
<project_config>
  <source_directory>src</source_directory>
  <test_directory>__tests__</test_directory>
  <commands>
    <test>npm test -- --coverage</test>
    <lint>npm run lint</lint>
    <build>npm run build</build>
  </commands>
  <quality_standards>
    <test_coverage>
      <threshold>95</threshold>
    </test_coverage>
  </quality_standards>
</project_config>
```

### 3. Meta-Framework Integration

**Framework Evolution** (Planned):
```bash
/meta-review "Audit framework compliance"
/meta-optimize "Improve workflow efficiency"
/meta-evolve "Upgrade to latest patterns"
```

## Integration Testing and Validation

### 1. End-to-End Testing

```bash
# Test complete workflow
python tests/integration/test_command_workflows.py

# Validate specific command
python tests/integration/test_command_workflows.py::TestCommandWorkflows::test_task_command_workflow
```

### 2. Module Validation

```bash
# Check all module references
python module_dependency_analyzer.py

# Generate dependency map
python scripts/create_dependency_graph.py

# Visual analysis (if Graphviz installed)
dot -Tpng module_dependencies.dot -o dependencies.png
```

### 3. Performance Monitoring

```bash
# Time command execution
time /task "Simple validation function"

# Monitor context usage
grep -c "token" claude_code_session.log

# Analyze parallel efficiency
python scripts/performance_analyzer.py
```

## Conclusion

The Claude Code Modular Prompts Framework provides a sophisticated yet user-friendly integration with Claude Code through:

- **Simple Commands**: Easy-to-use slash commands for common workflows
- **Powerful Modules**: Comprehensive infrastructure for complex operations
- **Dynamic Configuration**: Project-specific adaptation and customization
- **Quality Enforcement**: Built-in TDD and quality gate validation
- **Performance Optimization**: Parallel execution and efficient context management

The two-tier architecture ensures that users get immediate value from simple commands while having access to enterprise-grade capabilities when needed.

For additional support, see:
- [Integration Test Report](integration_test_report.md) - Detailed validation results
- [Module Dependency Map](../module_dependency_map.md) - Visual framework structure
- [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md) - Common issues and solutions