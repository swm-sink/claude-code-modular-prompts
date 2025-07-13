# Module Composition Framework - Usage Guide

## Overview

The module-composition-framework.md defines how modules are discovered, loaded, composed, and executed within the Claude Code framework. This is a critical infrastructure module.

## Core Concepts

### Module Lifecycle

```
Discovery → Loading → Validation → Composition → Execution → Cleanup
```

### Module Categories

1. **Core Modules**: Essential functionality (e.g., thinking patterns, TDD)
2. **Contextual Modules**: Task-specific modules  
3. **Support Modules**: Utilities and helpers

## Basic Usage

### Loading a Module

```python
from framework import ModuleRuntime

runtime = ModuleRuntime()
module = runtime.load_module('patterns/tdd-cycle-pattern.md')
```

### Composing Modules

```xml
<module_composition>
  <core_modules>
    <module priority="1">patterns/thinking-pattern-template.md</module>
    <module priority="2">patterns/tdd-cycle-pattern.md</module>
  </core_modules>
  <contextual_modules>
    <module condition="has_tests">patterns/test-runner.md</module>
  </contextual_modules>
</module_composition>
```

## Command Integration

### How Commands Use Module Composition

```xml
<command name="/task">
  <module_requirements>
    <core>
      <module>patterns/thinking-pattern-template.md</module>
      <module>development/task-management.md</module>
    </core>
    <quality>
      <module>patterns/quality-validation-pattern.md</module>
    </quality>
  </module_requirements>
</command>
```

### Runtime Execution

```python
# Command delegates to module runtime
modules = runtime.compose_for_command('/task', context)
results = runtime.execute_workflow(modules, inputs)
```

## Dependency Management

### Declaring Dependencies

```xml
<module_dependencies>
  <required>
    <module version="3.0.0">patterns/thinking-pattern-template.md</module>
  </required>
  <optional>
    <module>development/session-management.md</module>
  </optional>
</module_dependencies>
```

### Dependency Resolution

The framework automatically:
1. Resolves dependency trees
2. Loads in topological order
3. Handles circular dependencies
4. Validates version compatibility

## State Management

### Module State Isolation

```python
# Each module maintains isolated state
module_state = {
    'module_id': 'unique_id',
    'inputs': {},
    'outputs': {},
    'context': {},
    'errors': []
}
```

### State Transfer

```xml
<state_transfer>
  <from_module>patterns/research-analysis.md</from_module>
  <to_module>development/implementation.md</to_module>
  <data>
    <research_findings/>
    <constraints/>
    <recommendations/>
  </data>
</state_transfer>
```

## Error Handling

### Module-Level Errors

```python
try:
    result = module.execute(inputs)
except ModuleExecutionError as e:
    # Module-specific error handling
    recovery_strategy = get_recovery_strategy(e.module_id)
    result = recovery_strategy.execute()
```

### Composition Errors

```xml
<error_recovery>
  <missing_module>
    <strategy>Use fallback module</strategy>
    <fallback>patterns/generic-handler.md</fallback>
  </missing_module>
  <version_conflict>
    <strategy>Use compatible version</strategy>
    <resolution>Downgrade to common version</resolution>
  </version_conflict>
</error_recovery>
```

## Performance Optimization

### Parallel Module Execution

```python
# Modules without dependencies execute in parallel
parallel_modules = runtime.identify_parallel_modules(module_graph)
results = await runtime.execute_parallel(parallel_modules)
```

### Module Caching

```xml
<caching_policy>
  <cache_results>true</cache_results>
  <ttl_seconds>3600</ttl_seconds>
  <invalidate_on>
    <file_change/>
    <dependency_update/>
  </invalidate_on>
</caching_policy>
```

## Advanced Patterns

### Dynamic Module Selection

```python
# Select modules based on runtime conditions
if task.complexity > threshold:
    modules.append('patterns/advanced-analysis.md')
else:
    modules.append('patterns/simple-execution.md')
```

### Module Composition Templates

```xml
<composition_template name="feature_development">
  <phases>
    <research>
      <module>patterns/research-analysis-pattern.md</module>
    </research>
    <planning>
      <module>development/feature-planning.md</module>
    </planning>
    <implementation>
      <module>development/tdd-implementation.md</module>
    </implementation>
  </phases>
</composition_template>
```

## Monitoring and Debugging

### Execution Traces

```python
# Enable detailed execution tracing
runtime.enable_tracing()
execution_trace = runtime.get_execution_trace()
```

### Performance Metrics

```xml
<performance_metrics>
  <module_load_time>45ms</module_load_time>
  <composition_time>12ms</composition_time>
  <execution_time>230ms</execution_time>
  <total_modules>5</total_modules>
</performance_metrics>
```

## Best Practices

1. **Minimize Dependencies**: Keep module dependencies focused
2. **Use Standard Interfaces**: Follow interface contracts
3. **Handle Errors Gracefully**: Always provide recovery paths
4. **Optimize for Parallel**: Design for concurrent execution
5. **Document State Transfer**: Be explicit about data flow

## Integration Points

- **Command System**: Commands use composition for execution
- **Quality Gates**: Integrated at composition boundaries
- **Session Management**: State preserved across compositions
- **Error Recovery**: Unified error handling across modules