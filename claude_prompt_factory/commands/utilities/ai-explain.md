---
description: Intelligent AI-powered code explanation with advanced context awareness, comprehensive detail levels, and clear, structured output
argument-hint: "[explanation_scope] [detail_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /ai explain - Intelligent AI Code Explanation

Advanced AI code explanation system with intelligent context awareness, comprehensive detail levels, and clear, structured output.

## Usage
```bash
/ai explain function "Explain this function"   # Explain a specific function
/ai explain --file "Summarize this file"     # Explain an entire file
/ai explain --detailed "Explain the architecture" # Provide a detailed explanation
/ai explain --concise "What does this do?"       # Provide a concise explanation
```

<command_file>
  <metadata>
    <n>/ai explain</n>
    <purpose>Intelligent AI-powered code explanation with advanced context awareness, comprehensive detail levels, and clear, structured output</purpose>
    <usage>
      <![CDATA[
      /ai explain [explanation_scope] "[question]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="explanation_scope" type="string" required="true" default="function">
      <description>Scope of code to explain (e.g., function, file, component)</description>
    </argument>
    <argument name="question" type="string" required="true">
      <description>Specific question about the code</description>
    </argument>
    <argument name="detail_level" type="string" required="false" default="high">
      <description>Level of detail for the explanation</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Explain a specific function</description>
      <usage>/ai explain function "Explain the purpose of this function"</usage>
    </example>
    <example>
      <description>Explain an entire file</description>
      <usage>/ai explain --file "Summarize the key components in this file"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced AI code explanation specialist. The user wants a clear explanation of code with intelligent context awareness and comprehensive detail.

**Explanation Process:**
1. **Requirement Analysis**: Analyze the explanation request and context
2. **Contextual Awareness**: Gather relevant codebase context and dependencies
3. **Code Analysis**: Perform in-depth analysis of the code to be explained
4. **Explanation Generation**: Generate a clear, structured, and accurate explanation
5. **Output Formatting**: Format the explanation for clarity and readability

**Implementation Strategy:**
- Analyze user questions to understand the desired explanation depth
- Implement intelligent context gathering with dependency and usage analysis
- Perform in-depth code analysis to understand functionality and design
- Generate clear, structured explanations with examples and analogies
- Format output with markdown, code blocks, and diagrams for clarity

<include component="components/context/find-relevant-code.md" />
<include component="components/analysis/codebase-discovery.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>ai_explanation.detail.level</value>
      <value>reporting.output.format</value>
    </uses_config_values>
  </dependencies>
</command_file>