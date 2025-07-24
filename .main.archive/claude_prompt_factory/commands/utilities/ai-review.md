---
description: Intelligent AI-powered code review with advanced context awareness, comprehensive quality checks, and actionable feedback
argument-hint: "[review_scope] [feedback_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /ai review - Intelligent AI Code Review

Advanced AI code review system with intelligent context awareness, comprehensive quality checks, and actionable, constructive feedback.

## Usage
```bash
/ai review function "Review this function"   # Review a specific function
/ai review --file "Review this file"       # Review an entire file
/ai review --detailed "Provide detailed feedback" # Provide detailed review feedback
/ai review --concise "Summarize key issues"      # Provide a concise review summary
```

<command_file>
  <metadata>
    <n>/ai review</n>
    <purpose>Intelligent AI-powered code review with advanced context awareness, comprehensive quality checks, and actionable feedback</purpose>
    <usage>
      <![CDATA[
      /ai review [review_scope] "[description]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="review_scope" type="string" required="true" default="function">
      <description>Scope of code to review (e.g., function, file, component)</description>
    </argument>
    <argument name="description" type="string" required="true">
      <description>Specific focus for the review (e.g., security, performance, readability)</description>
    </argument>
    <argument name="feedback_level" type="string" required="false" default="high">
      <description>Level of detail for the review feedback</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Review a specific function</description>
      <usage>/ai review function "Review this function for potential race conditions"</usage>
    </example>
    <example>
      <description>Review an entire file</description>
      <usage>/ai review --file "Review this file for adherence to our coding standards"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced AI code review specialist. The user wants a thorough code review with intelligent context awareness and actionable feedback.

**Review Process:**
1. **Requirement Analysis**: Analyze the review request and context
2. **Contextual Awareness**: Gather relevant codebase context, dependencies, and standards
3. **In-depth Analysis**: Perform a deep analysis of the code for quality, security, and performance
4. **Feedback Generation**: Generate clear, constructive, and actionable feedback
5. **Report Formulation**: Format the review into a structured, easy-to-understand report

**Implementation Strategy:**
- Analyze user requests to understand the specific review focus and goals
- Implement intelligent context gathering with dependency and coding standards analysis
- Perform in-depth code analysis, checking for bugs, vulnerabilities, and anti-patterns
- Generate clear, constructive feedback with examples and suggestions for improvement
- Format the review report with severity levels, code snippets, and clear explanations

<include component="components/analysis/codebase-discovery.md" />
<include component="components/quality/anti-pattern-detection.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>ai_review.feedback.detail_level</value>
      <value>quality.coding_standards.file</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Process

Based on enterprise AI review patterns:
1. Analyze code structure and patterns
2. Check adherence to best practices
3. Identify performance optimizations
4. Review error handling and edge cases
5. Assess maintainability and readability
6. Generate scored recommendations

## Review Areas
- **Code Quality**: Structure, naming, complexity
- **Best Practices**: Language-specific conventions
- **Performance**: Bottlenecks and optimizations
- **Security**: Vulnerability patterns
- **Maintainability**: Documentation, modularity
- **Testing**: Coverage and test quality

## Output Format
```
AI CODE REVIEW: component.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Score: 8.2/10

QUALITY BREAKDOWN:
Structure:      9/10  ✓ Well organized
Performance:    7/10  ⚠ Optimization opportunities
Security:       9/10  ✓ No vulnerabilities found
Maintainability: 8/10  ✓ Good documentation

IMPROVEMENTS IDENTIFIED:
[HIGH] Line 45: Extract complex condition to method
  Impact: Readability +2, Maintainability +1
  
[MEDIUM] Line 78: Add input validation
  Impact: Security +1, Robustness +1
```

## Options
- `--depth`: Review thoroughness (quick/thorough/comprehensive)
- `--fix`: Apply suggested improvements
- `--score`: Include numerical quality scores
- `--focus`: Target specific aspects (performance/security/style)

## Related Commands
- `/analyze quality` - Quality metrics analysis
- `/refactor suggest` - Refactoring suggestions
- `/security scan` - Security-focused review