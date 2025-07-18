# Query Command - Research and analyze code without changing anything

**Description**: Research and analyze code without changing anything

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/research-analysis-pattern.md</delegation_target>
  <orchestration_flow>
    1. Define research scope and questions
    2. Delegate to research analysis pattern module
    3. Perform read-only analysis and investigation
    4. Generate comprehensive findings report
  </orchestration_flow>
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

## Examples

- `/query "Find all database queries"` - Identifies and catalogs database interactions
- `/query "Analyze error handling patterns"` - Documents error handling approaches across codebase
- `/query "Map component dependencies"` - Creates dependency visualization and analysis