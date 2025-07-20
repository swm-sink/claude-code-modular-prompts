# /analyze patterns - Design Pattern Analysis Command

**Purpose**: Detect design patterns, identify violations and anti-patterns, and suggest architectural improvements in the codebase.

## Usage
```bash
/analyze patterns [path]
```

## Workflow

The `/analyze patterns` command follows a systematic process to analyze the codebase for design patterns.

```xml
<pattern_analysis_workflow>
  <step name="Scan Codebase Structure">
    <description>Scan the codebase to understand its structure, component relationships, and overall architecture.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase to build a model of its structure.</description>
    </tool_usage>
  </step>
  
  <step name="Detect Design Patterns">
    <description>Identify the design patterns (e.g., Gang of Four, architectural, domain-specific) that are currently in use in the codebase.</description>
  </step>
  
  <step name="Identify Violations & Anti-Patterns">
    <description>Detect any violations of established design patterns, as well as any common anti-patterns that may be present.</description>
  </step>
  
  <step name="Generate Improvement Suggestions">
    <description>Generate a list of suggestions for improving the codebase's architecture, including opportunities for new patterns, refactoring existing patterns, and fixing anti-patterns.</description>
    <output>A report detailing the detected patterns, violations, and suggestions for improvement.</output>
  </step>
</pattern_analysis_workflow>
```

## Analysis Focus Areas
- Design pattern identification (GoF, architectural, domain-specific)
- Anti-pattern detection and impact assessment
- Pattern consistency across codebase
- Architectural pattern alignment
- Refactoring opportunities for pattern adoption
- Performance implications of current patterns

*Enhances code quality through intelligent pattern analysis*