# Query Command - Research and analyze code without changing anything

**Description**: Research and analyze code without changing anything

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.1.0   | 2025-07-19   | stable | 98%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/research-analysis-pattern-parallel.md</delegation_target>
  <orchestration_flow>
    1. Define research scope and questions
    2. Delegate to parallel-optimized research analysis module
    3. Perform read-only analysis with 3-10x performance boost
    4. Generate comprehensive findings report efficiently
  </orchestration_flow>
  <performance_features>
    <parallel_execution>Validated 6x average speedup in testing</parallel_execution>
    <batch_operations>Process multiple files simultaneously</batch_operations>
    <concurrent_searches>Run pattern searches in parallel</concurrent_searches>
  </performance_features>
  <read_only_enforcement>
    <no_modifications>Strictly forbids any code changes</no_modifications>
    <analysis_focus>Deep understanding and documentation</analysis_focus>
    <investigation_scope>Codebase patterns, architecture, issues</investigation_scope>
  </read_only_enforcement>
</command_orchestration>
```

## Usage

**Understand existing codebase:**
```
/query "How does the authentication system work?"
```

**Investigate issues:**
```
/query "What's causing the memory leaks in the image processing?"
```

**Architecture analysis:**
```
/query "Document the API structure and dependencies"
```

## What This Command Does

- **Read-only**: Never modifies code, only analyzes and reports
- **Deep analysis**: Investigates patterns, architecture, and relationships
- **Comprehensive**: Generates detailed findings and documentation
- **Research focus**: Perfect for understanding before making changes
- **Foundation**: Often used before /task or /feature commands

## Actual Capabilities

This command excels at:
- Code pattern analysis and documentation
- Dependency mapping and visualization
- Architecture understanding and diagramming
- Issue investigation without modification
- Preparing groundwork for development tasks
- **NEW: Parallel execution for 3-10x faster analysis** (Validated: 6x average speedup)

## Future Enhancements

*Note: The following features are planned but not yet implemented:*
- Framework-specific audit capabilities
- Performance bottleneck analysis
- Token usage optimization recommendations
- Module effectiveness metrics

## Examples

- `/query "Find all database queries"` - Identifies and catalogs database interactions
- `/query "Analyze error handling patterns"` - Documents error handling approaches across codebase
- `/query "Map component dependencies"` - Creates dependency visualization and analysis