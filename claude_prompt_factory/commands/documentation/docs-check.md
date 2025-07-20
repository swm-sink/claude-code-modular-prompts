# /docs check - Documentation Validation Command

**Purpose**: Validate the completeness, accuracy, and consistency of the project's documentation.

## Usage
```bash
/docs check [target]
```

## Workflow

The `/docs check` command follows a systematic process to validate the project's documentation.

```xml
<doc_check_workflow>
  <step name="Scan Documentation">
    <description>Recursively scan the target directory to identify all documentation files and build a model of the documentation structure.</description>
    <tool_usage>
      <tool>Parallel Glob</tool>
      <description>Find all documentation files in the target directory.</description>
    </tool_usage>
  </step>
  
  <step name="Perform Validation Checks">
    <description>Perform a comprehensive set of validation checks on the documentation, including checking for completeness, accuracy, consistency, and quality.</description>
    <checks>
      <check name="Completeness">Check for missing READMEs, undocumented functions, and incomplete tutorials.</check>
      <check name="Accuracy">Validate that code examples execute correctly and that API documentation matches the implementation.</check>
      <check name="Consistency">Check for consistent formatting, naming conventions, and documentation structure.</check>
      <check name="Quality">Assess the readability, grammar, and freshness of the content.</check>
    </checks>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed report of the documentation's health, including a quality score, a list of any issues found, and a set of actionable recommendations for improvement.</description>
    <output>A comprehensive documentation health report.</output>
  </step>
</doc_check_workflow>
```

## Output Format
```
Documentation Health: 85/100
├── Completeness: 90% (3 missing files)
├── Accuracy: 80% (2 broken examples)
├── Consistency: 85% (formatting issues)
└── Quality: 85% (minor improvements)

Issues Found:
🔴 api/auth.md: Example fails to execute
🟡 README.md: Outdated installation steps
🟡 docs/: Missing contributor guide

Recommendations:
• Update code examples in authentication docs
• Refresh installation instructions
• Add contributor documentation
```

## Implementation Notes
- Uses parallel execution for fast validation
- Caches results for large documentation sets
- Integrates with code analysis for accuracy
- Provides actionable improvement suggestions