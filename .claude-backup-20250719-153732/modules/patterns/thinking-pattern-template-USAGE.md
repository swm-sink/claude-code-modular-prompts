| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-14   | stable |

# Thinking Pattern Template - Usage Guide

## Overview

The thinking-pattern-template.md module provides standardized checkpoint-based thinking patterns optimized for Claude 4's advanced capabilities. This guide shows how to use and integrate this critical module.

## Quick Start

### Basic Usage in Commands

```xml
<command name="/task">
  <thinking_pattern>
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Understand task requirements</action>
      <validation>Requirements clear and acceptance criteria defined</validation>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Write failing tests first (RED phase)</action>
      <validation>Tests fail as expected, coverage targets set</validation>
    </checkpoint>
  </thinking_pattern>
</command>
```

### Integration in Modules

```xml
<module_dependency>
  <pattern>patterns/thinking-pattern-template.md</pattern>
  <usage>
    <inherit_checkpoints>true</inherit_checkpoints>
    <extend_with_custom>true</extend_with_custom>
  </usage>
</module_dependency>
```

## Checkpoint Structure

### Standard Checkpoint Format

```xml
<checkpoint id="[number]" verify="[true/false]" enforcement="[BLOCKING/CONDITIONAL/OPTIONAL]">
  <action>What specific action to take</action>
  <interleaved_thinking>
    <pre_analysis>Context and constraints analysis</pre_analysis>
    <critical_thinking>30-second minimum deep analysis</critical_thinking>
    <decision_reasoning>Evidence-based decision making</decision_reasoning>
  </interleaved_thinking>
  <validation>Measurable success criteria</validation>
  <enforcement>What happens if checkpoint fails</enforcement>
  <context_transfer>Information passed to next checkpoint</context_transfer>
</checkpoint>
```

## Common Patterns

### 1. Research-First Pattern

```xml
<checkpoint id="1" verify="true" enforcement="BLOCKING">
  <action>Research existing codebase and patterns</action>
  <validation>Found relevant code, understood constraints</validation>
  <context_transfer>research_findings, existing_patterns</context_transfer>
</checkpoint>
```

### 2. TDD Pattern

```xml
<checkpoint id="2" verify="true" enforcement="BLOCKING">
  <action>Write failing test first</action>
  <validation>Test fails correctly, covers requirements</validation>
  <context_transfer>test_file_path, coverage_target</context_transfer>
</checkpoint>
```

### 3. Quality Gate Pattern

```xml
<checkpoint id="5" verify="true" enforcement="BLOCKING">
  <action>Run quality validation</action>
  <validation>Coverage >= 90%, linting passed, types correct</validation>
  <enforcement>BLOCK if quality gates fail</enforcement>
</checkpoint>
```

## Enforcement Levels

1. **BLOCKING**: Must pass or execution stops
2. **CONDITIONAL**: Depends on context, may proceed with warnings
3. **OPTIONAL**: Best practice but not required

## Integration Examples

### With Task Management

```python
# Task module uses thinking pattern
thinking_pattern = load_module('patterns/thinking-pattern-template.md')
checkpoints = thinking_pattern.get_checkpoints('task_execution')

for checkpoint in checkpoints:
    result = execute_checkpoint(checkpoint)
    if not result.success and checkpoint.enforcement == 'BLOCKING':
        raise CheckpointFailure(checkpoint.id, result.reason)
```

### With Quality Gates

```xml
<quality_integration>
  <checkpoint id="3" verify="true" enforcement="BLOCKING">
    <action>Validate code quality</action>
    <delegates_to>quality/universal-quality-gates.md</delegates_to>
    <validation>All quality gates passed</validation>
  </checkpoint>
</quality_integration>
```

## Best Practices

1. **Always Include Critical Thinking**: Minimum 30 seconds analysis
2. **Make Validation Measurable**: Use specific metrics, not vague criteria
3. **Transfer Context**: Pass relevant data between checkpoints
4. **Handle Failures Gracefully**: Define clear recovery paths

## Common Mistakes to Avoid

1. **Skipping Checkpoints**: All checkpoints must execute in order
2. **Vague Validation**: "Code looks good" vs "Coverage >= 90%"
3. **Missing Context Transfer**: Loses important information
4. **Ignoring Enforcement**: BLOCKING means BLOCKING

## Performance Optimization

- Use parallel execution where checkpoints are independent
- Batch tool calls within checkpoints
- Cache checkpoint results when appropriate
- Minimize context transfer size

## Troubleshooting

### Checkpoint Failures

```xml
<error_handling>
  <checkpoint_failure>
    <log>Checkpoint {id} failed: {reason}</log>
    <attempt_recovery>true</attempt_recovery>
    <max_retries>3</max_retries>
  </checkpoint_failure>
</error_handling>
```

### Performance Issues

- Review checkpoint dependencies
- Check for unnecessary validation
- Optimize tool call batching

## Related Modules

- `module-composition-framework.md` - How modules compose
- `critical-thinking-pattern.md` - Deep analysis patterns
- `quality-validation-pattern.md` - Quality enforcement