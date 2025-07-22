---
description: Intelligent codebase query and analysis with contextual understanding and comprehensive insights
argument-hint: "[query_type] [analysis_scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

<command_file>
  <metadata>
    <name>/query</name>
    <purpose>Intelligent codebase query and analysis with contextual understanding and comprehensive insights</purpose>
    <usage>
      <![CDATA[
      /query "[question about codebase]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="question" type="string" required="true">
      <description>Question about the codebase to analyze and answer</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Query authentication implementation</description>
      <usage>/query "How does user authentication work in this app?"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/context/find-relevant-code.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/context/intelligent-summarization.md</include>

You are an intelligent codebase analyst. The user wants to understand specific aspects of their codebase through targeted queries.

**Analysis Process:**
1. **Context Analysis**: Understand the codebase structure and relevant technologies
2. **Query Processing**: Parse and interpret the user's question
3. **Code Investigation**: Search and analyze relevant code sections
4. **Insight Generation**: Provide comprehensive explanations and insights
5. **Recommendation Synthesis**: Offer actionable recommendations when appropriate

**Implementation Strategy:**
- Perform semantic code search to find relevant implementations
- Analyze code patterns, dependencies, and relationships
- Provide clear explanations with code examples
- Identify potential improvements or issues
- Generate actionable insights and recommendations
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file> 