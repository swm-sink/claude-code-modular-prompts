---
description: Advanced code analysis with intelligent pattern detection, quality assessment, and comprehensive insights
argument-hint: "[analysis_scope] [analysis_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /analyze code - Advanced Code Analysis

Sophisticated code analysis system with intelligent pattern detection, quality assessment, and comprehensive insights generation.

## Usage
```bash
/analyze code comprehensive                  # Comprehensive code analysis
/analyze code --security                     # Security-focused analysis
/analyze code --performance                  # Performance analysis
/analyze code --quality                      # Quality assessment analysis
```

<command_file>
  <metadata>
    <n>/analyze code</n>
    <purpose>Advanced code analysis with intelligent pattern detection, quality assessment, and comprehensive insights</purpose>
    <usage>
      <![CDATA[
      /analyze code [analysis_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="analysis_scope" type="string" required="false" default="comprehensive">
      <description>Scope of code analysis to perform</description>
    </argument>
    <argument name="analysis_depth" type="string" required="false" default="detailed">
      <description>Depth of analysis to conduct</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Comprehensive code analysis</description>
      <usage>/analyze code comprehensive</usage>
    </example>
    <example>
      <description>Security-focused analysis</description>
      <usage>/analyze code --security</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

You are an advanced code analysis specialist. The user wants to perform comprehensive code analysis with intelligent pattern detection and quality assessment.

**Analysis Process:**
1. **Code Discovery**: Scan and catalog codebase structure and components
2. **Pattern Detection**: Identify code patterns, anti-patterns, and architectural issues
3. **Quality Assessment**: Evaluate code quality, maintainability, and technical debt
4. **Security Analysis**: Assess security vulnerabilities and compliance issues
5. **Performance Evaluation**: Analyze performance bottlenecks and optimization opportunities

**Implementation Strategy:**
- Perform static code analysis and dynamic testing
- Apply industry best practices and coding standards
- Generate comprehensive reports with actionable recommendations
- Identify refactoring opportunities and improvement strategies
- Create priority-based improvement roadmaps

<include component="components/analysis/codebase-discovery.md" />
<include component="components/quality/anti-pattern-detection.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>analysis.quality.standards</value>
      <value>security.scan.depth</value>
    </uses_config_values>
  </dependencies>
</command_file>