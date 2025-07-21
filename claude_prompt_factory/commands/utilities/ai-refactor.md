---
description: Intelligent AI-powered code refactoring with advanced context awareness, comprehensive quality improvements, and robust safety checks
argument-hint: "[refactor_scope] [quality_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /ai refactor - Intelligent AI Code Refactoring

Advanced AI code refactoring system with intelligent context awareness, comprehensive quality improvements, and robust safety checks.

## Usage
```bash
/ai refactor function "Optimize this function" # Refactor a specific function
/ai refactor --file "Improve readability"      # Refactor an entire file
/ai refactor --with-tests "Add error handling" # Refactor with test validation
/ai refactor --quality-high "Update legacy code" # Refactor with high quality standards
```

<command_file>
  <metadata>
    <n>/ai refactor</n>
    <purpose>Intelligent AI-powered code refactoring with advanced context awareness, comprehensive quality improvements, and robust safety checks</purpose>
    <usage>
      <![CDATA[
      /ai refactor [refactor_scope] "[description]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="refactor_scope" type="string" required="true" default="function">
      <description>Scope of code refactoring (e.g., function, file, component)</description>
    </argument>
    <argument name="description" type="string" required="true">
      <description>Detailed description of the desired refactoring</description>
    </argument>
    <argument name="quality_level" type="string" required="false" default="high">
      <description>Level of quality assurance and testing to apply</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Refactor a specific function</description>
      <usage>/ai refactor function "Optimize this function for performance"</usage>
    </example>
    <example>
      <description>Refactor an entire file</description>
      <usage>/ai refactor --file "Improve readability and add comments"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced AI code refactoring specialist. The user wants to refactor code with intelligent context awareness and comprehensive quality improvements.

**Refactoring Process:**
1. **Requirement Analysis**: Analyze refactoring requirements and context
2. **Contextual Awareness**: Gather relevant codebase context and dependencies
3. **Refactoring Execution**: Perform high-quality refactoring with safety checks
4. **Quality Assurance**: Apply comprehensive quality checks and testing
5. **Validation & Review**: Validate refactoring and prepare for review

**Implementation Strategy:**
- Analyze user requirements to create a detailed refactoring plan
- Implement intelligent context gathering with dependency analysis
- Perform high-quality, safe refactoring with clear justifications
- Apply comprehensive quality assurance with linting, formatting, and testing
- Establish seamless validation and review processes for refactored code

<include component="components/analysis/dependency-mapping.md" />
<include component="components/quality/framework-validation.md" />
<include component="components/testing/mutation-testing.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/quality/framework-validation.md</component>
      <component>components/testing/mutation-testing.md</component>
    </includes_components>
    <uses_config_values>
      <value>ai_refactoring.quality.level</value>
      <value>testing.mutation.auto_run</value>
    </uses_config_values>
  </dependencies>
</command_file>