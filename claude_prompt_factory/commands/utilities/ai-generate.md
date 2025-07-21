---
description: Intelligent AI-powered code generation with advanced context awareness, multi-file support, and comprehensive quality assurance
argument-hint: "[generation_scope] [quality_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /ai generate - Intelligent AI Code Generation

Advanced AI code generation system with intelligent context awareness, comprehensive multi-file support, and robust quality assurance.

## Usage
```bash
/ai generate component "Login form"          # Generate a new component
/ai generate --multi-file "User auth flow" # Generate a multi-file feature
/ai generate --with-tests "API endpoint"   # Generate code with tests
/ai generate --quality-high "Data model"     # Generate with high quality standards
```

<command_file>
  <metadata>
    <n>/ai generate</n>
    <purpose>Intelligent AI-powered code generation with advanced context awareness, multi-file support, and comprehensive quality assurance</purpose>
    <usage>
      <![CDATA[
      /ai generate [generation_scope] "[description]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="generation_scope" type="string" required="true" default="component">
      <description>Scope of code generation (e.g., component, feature, service)</description>
    </argument>
    <argument name="description" type="string" required="true">
      <description>Detailed description of the code to generate</description>
    </argument>
    <argument name="quality_level" type="string" required="false" default="high">
      <description>Level of quality assurance and testing to apply</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate a new component</description>
      <usage>/ai generate component "Login form with email and password fields"</usage>
    </example>
    <example>
      <description>Generate a multi-file feature</description>
      <usage>/ai generate --multi-file "User authentication flow with JWT"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced AI code generation specialist. The user wants to generate code with intelligent context awareness and comprehensive quality assurance.

**Generation Process:**
1. **Requirement Analysis**: Analyze generation requirements and context
2. **Contextual Awareness**: Gather relevant codebase context and patterns
3. **Code Generation**: Generate high-quality code with best practices
4. **Quality Assurance**: Apply comprehensive quality checks and testing
5. **Integration & Review**: Integrate generated code and prepare for review

**Implementation Strategy:**
- Analyze user requirements to create a detailed generation plan
- Implement intelligent context gathering with codebase analysis
- Generate high-quality, idiomatic code with clear documentation
- Apply comprehensive quality assurance with linting, formatting, and testing
- Establish seamless integration and review processes for generated code

<include component="components/context/find-relevant-code.md" />
<include component="components/quality/framework-validation.md" />
<include component="components/testing/test-e2e.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/quality/framework-validation.md</component>
      <component>components/testing/test-e2e.md</component>
    </includes_components>
    <uses_config_values>
      <value>ai_generation.quality.level</value>
      <value>testing.e2e.auto_run</value>
    </uses_config_values>
  </dependencies>
</command_file>