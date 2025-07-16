| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-16 | stable |

# /command-name - Brief description

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Clear, specific purpose of this command">
  
  <delegation target="modules/[category]/[module-name].md">
    Brief description of what gets delegated and why
  </delegation>
  
  <depends_on>
    patterns/pattern-library.md for proven execution patterns
    <!-- Add specific module dependencies here when implementing -->
  </depends_on>
  
  <pattern_usage>
    • Uses pattern_name for specific benefit
    • Applies another_pattern for performance/quality
    • Implements critical_pattern for reliability
    • See modules/patterns/pattern-library.md for pattern details
  </pattern_usage>
  
  <examples>
    /command-name "Basic usage example"      → Expected outcome
    /command-name "Complex scenario"         → Different outcome
    /command-name "Edge case handling"       → Special behavior
  </examples>
  
  <rules>
    <rule priority="critical">ALWAYS follow this critical rule</rule>
    <rule priority="high">Important behavioral constraint</rule>
    <rule priority="standard">Standard operating procedure</rule>
  </rules>
  
  <integration>
    <github_session when="condition">
      Describe when and why GitHub sessions are created
    </github_session>
    <tool_patterns>
      Specific tool usage patterns this command enforces
    </tool_patterns>
  </integration>
  
</command>
```

────────────────────────────────────────────────────────────────────────────────

## Template Usage Guidelines

### Version Table
- **version**: Start at 1.0.0, follow semantic versioning
- **last_updated**: Update whenever changes are made
- **status**: Use draft → review → stable → deprecated

### Command Naming
- Use lowercase with hyphens: `/command-name`
- Be descriptive but concise
- Follow existing patterns (task, feature, query, etc.)

### Purpose Statement
- One clear sentence explaining what the command does
- Focus on user value, not implementation details

### Delegation
- Commands MUST delegate to modules (never implement directly)
- Specify the exact module path
- Explain what aspects are delegated

### Dependencies
- List all modules this command depends on
- Include brief explanation of why each is needed
- Always include pattern-library.md if using patterns

### Pattern Usage
- List specific patterns from pattern-library.md
- Explain the benefit of each pattern
- Use bullet points for readability

### Examples
- Provide 3-5 realistic examples
- Show both simple and complex usage
- Include expected outcomes with → notation

### Rules
- Prioritize rules: critical, high, standard
- Use ALWAYS/NEVER for absolute requirements
- Keep rules actionable and specific

### Integration
- Document GitHub session creation triggers
- Specify tool usage patterns
- Note any special integrations

## Framework Compliance

This template follows Framework 3.0 standards:
- ✅ Version table at top
- ✅ Title after separator line
- ✅ XML-formatted content blocks
- ✅ Separator lines (80 characters: ────...)
- ✅ Semantic XML tags
- ✅ Clear section organization

## Related Documentation
- Framework format: `CLAUDE.md`
- Pattern library: `.claude/modules/patterns/pattern-library.md`
- Module template: `.claude/templates/module-template.md`
- Framework standards: `docs/framework/TEMPLATE_FORMAT.md`