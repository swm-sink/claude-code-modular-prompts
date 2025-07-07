| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Tool Usage Patterns

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="tool_usage" category="patterns">
  
  <purpose>
    Standardized patterns for Claude Code tool usage including batching, parallel execution, error handling, and optimization strategies.
  </purpose>
  
  <tool_patterns>
    
    <pattern_delegation>
      <description>All core execution patterns defined in patterns/pattern-library.md</description>
      <reference>patterns/pattern-library.md#execution_patterns for parallel_execution and batch_operations</reference>
      <tool_specific_patterns>Tool usage optimizations specific to Claude Code tools</tool_specific_patterns>
    </pattern_delegation>
    
    <read_before_write>
      <description>Always read file content before making any modifications</description>
      <pattern>
        ```python
        # ALWAYS read first
        Read("file.md")
        # Then modify
        Edit("file.md", old="...", new="...")
        ```
      </pattern>
      <enforcement>Mandatory - prevents destructive operations</enforcement>
    </read_before_write>
    
    <tool_specific_optimizations>
      <description>Tool-specific patterns not covered in pattern-library.md</description>
      <validation_first>Check paths exist → Verify permissions → Execute tool</validation_first>
      <error_recovery>Attempt operation → Log error → Continue with alternatives</error_recovery>
      <lazy_loading>Load content only when needed for large file analysis</lazy_loading>
    </tool_specific_optimizations>
    
  </tool_patterns>
  
  <error_handling>
    
    <graceful_degradation>
      <description>Handle tool failures without stopping execution</description>
      <pattern>Attempt operation → Log error → Continue with alternatives</pattern>
    </graceful_degradation>
    
    <validation_first>
      <description>Validate inputs before tool execution</description>
      <pattern>Check paths exist → Verify permissions → Execute tool</pattern>
    </validation_first>
    
  </error_handling>
  
  <optimization_strategies>
    
    <lazy_loading>
      <description>Load content only when needed</description>
      <application>Large file analysis, module composition</application>
    </lazy_loading>
    
    <smart_caching>
      <description>Cache frequently accessed content</description>
      <application>Pattern matching, validation results</application>
    </smart_caching>
    
  </optimization_strategies>
  
  <integration_points>
    <git_operations>Git commands with proper error handling and validation</git_operations>
    <security_audit>Safe file operations with permission checks</security_audit>
    <tdd_workflow>Tool usage in test-driven development cycles</tdd_workflow>
    <research_analysis>Efficient search and analysis patterns</research_analysis>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Core Tool Usage Principles

```xml
<tool_usage_principles>
  <principle>Batch independent operations for maximum performance</principle>
  <principle>Read before write - always verify current state</principle>
  <principle>Handle errors gracefully without stopping execution</principle>
  <principle>Validate inputs before execution</principle>
  <principle>Use appropriate tools for each task type</principle>
</tool_usage_principles>
```

────────────────────────────────────────────────────────────────────────────────

## Pattern Usage Examples

```xml
<usage_examples>
  <example type="file_analysis">
    # Parallel file reading for analysis
    Read("src/main.py"), Read("src/utils.py"), Read("tests/test_main.py")
  </example>
  
  <example type="search_operations">
    # Efficient search across codebase
    Glob("**/*.py"), Grep("class.*Exception", "src/")
  </example>
  
  <example type="bulk_modifications">
    # Multiple edits in single operation
    MultiEdit("config.md", [
      {"old": "version: 1.0", "new": "version: 2.0"},
      {"old": "status: draft", "new": "status: stable"}
    ])
  </example>
</usage_examples>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Used by git-operations.md, tdd.md, audit.md, research-analysis.md for standardized tool usage patterns.