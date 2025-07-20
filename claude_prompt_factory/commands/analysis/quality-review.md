# /quality review - Automated Code Review Command

**Purpose**: Perform an automated, comprehensive code review, checking for compliance with coding standards, best practices, and architectural principles.

## Usage
```bash
/quality review [path]
```

## Workflow

The `/quality review` command follows a systematic process to perform a comprehensive code review.

```xml
<review_workflow>
  <step name="Analyze Code">
    <description>Perform a deep analysis of the code, checking for compliance with coding standards, best practices in error handling and documentation, and adherence to established design patterns.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase for a wide range of quality issues.</description>
    </tool_usage>
  </step>
  
  <step name="Assess Quality Gates">
    <description>Evaluate the code against the project's defined quality gates, including test coverage, documentation standards, and security best practices.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read the `<quality_standards>` section of `PROJECT_CONFIG.xml`.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Review Report">
    <description>Generate a detailed code review report, including a quality score, a list of any violations or issues found, and a set of actionable recommendations for improvement.</description>
    <output>A comprehensive code review report.</output>
  </step>
</review_workflow>
```

## Review Areas
- Coding standards compliance
- Design patterns usage
- Error handling completeness
- Test coverage and quality
- Documentation accuracy
- Security best practices
- Performance considerations
- Maintainability factors

*Automates comprehensive quality review in Claude Code*