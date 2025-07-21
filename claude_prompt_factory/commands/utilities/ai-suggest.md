---
description: Intelligent AI-powered suggestions for code improvements, refactoring, and best practices
argument-hint: "[suggestion_scope] [suggestion_type]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /ai suggest - Intelligent AI Code Suggestions

Advanced AI-powered suggestion system for code improvements, refactoring opportunities, and adherence to best practices.

## Usage
```bash
/ai suggest improvements "Suggest improvements for this code" # Get general improvement suggestions
/ai suggest --refactor "Find refactoring opportunities"      # Get refactoring suggestions
/ai suggest --best-practices "Check for best practices"      # Get best practice suggestions
/ai suggest --performance "Find performance optimizations"   # Get performance-related suggestions
```

<command_file>
  <metadata>
    <n>/ai suggest</n>
    <purpose>Intelligent AI-powered suggestions for code improvements, refactoring, and best practices</purpose>
    <usage>
      <![CDATA[
      /ai suggest [suggestion_scope] "[prompt]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="suggestion_scope" type="string" required="true" default="file">
      <description>The scope of the code to provide suggestions for (e.g., file, function, component)</description>
    </argument>
    <argument name="prompt" type="string" required="true">
      <description>The specific request for suggestions</description>
    </argument>
    <argument name="suggestion_type" type="string" required="false" default="improvements">
      <description>The type of suggestions to provide (e.g., improvements, refactoring, best_practices, performance)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Get general improvement suggestions</description>
      <usage>/ai suggest improvements "What are some ways to improve this code?"</usage>
    </example>
    <example>
      <description>Get refactoring suggestions</description>
      <usage>/ai suggest --refactor "Are there any opportunities to refactor this code for better readability?"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced AI code suggestion specialist. The user is looking for suggestions to improve their code.

**Suggestion Process:**
1. **Analyze Request**: Understand the user's request and the type of suggestions they are looking for
2. **Contextual Analysis**: Analyze the relevant code and its context within the codebase
3. **Generate Suggestions**: Generate high-quality, actionable suggestions based on the analysis
4. **Categorize &amp; Prioritize**: Categorize and prioritize the suggestions based on impact and effort
5. **Present Suggestions**: Present the suggestions in a clear, structured, and easy-to-understand format

**Implementation Strategy:**
- Analyze the user's prompt to determine the focus of the suggestions (e.g., performance, readability, security)
- Perform a deep analysis of the code, identifying areas for improvement, potential issues, and best practice violations
- Generate a list of concrete, actionable suggestions with clear explanations and examples
- Categorize suggestions (e.g., Critical, Recommended, Optional) and prioritize them to guide the user
- Present the suggestions in a structured report with code snippets and links to relevant documentation

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
      <value>ai_suggestions.priority_level</value>
      <value>reporting.output.format</value>
    </uses_config_values>
  </dependencies>
</command_file>