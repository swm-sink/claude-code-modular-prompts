---
description: Advanced refactoring agent with intelligent code optimization, pattern recognition, and architectural improvements
argument-hint: "[refactor_type] [optimization_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /agent refactorer - Advanced Refactoring Agent

Sophisticated refactoring agent with intelligent code optimization, pattern recognition, and comprehensive architectural improvements.

## Usage
```bash
/agent refactorer optimize                   # Performance optimization refactoring
/agent refactorer --architecture             # Architectural refactoring
/agent refactorer --patterns                 # Design pattern improvements
/agent refactorer --comprehensive            # Comprehensive code enhancement
```

<command_file>
  <metadata>
    <n>/agent refactorer</n>
    <purpose>Advanced refactoring agent with intelligent code optimization, pattern recognition, and architectural improvements</purpose>
    <usage>
      <![CDATA[
      /agent refactorer [refactor_type]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="refactor_type" type="string" required="false" default="optimize">
      <description>Type of refactoring to perform</description>
    </argument>
    <argument name="optimization_strategy" type="string" required="false" default="comprehensive">
      <description>Strategy for code optimization</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Performance optimization refactoring</description>
      <usage>/agent refactorer optimize</usage>
    </example>
    <example>
      <description>Architectural refactoring</description>
      <usage>/agent refactorer --architecture</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced refactoring agent specialist. The user wants to deploy intelligent code optimization with pattern recognition and architectural improvements.

**Refactoring Process:**
1. **Code Analysis**: Analyze existing code structure and identify improvement opportunities
2. **Pattern Recognition**: Recognize code patterns and anti-patterns for optimization
3. **Architectural Assessment**: Evaluate architectural design and identify enhancement opportunities
4. **Optimization Strategy**: Design comprehensive refactoring strategies and approaches
5. **Implementation Execution**: Execute refactoring with safety and validation measures

**Implementation Strategy:**
- Perform comprehensive code analysis and pattern detection
- Apply industry best practices and design patterns
- Implement architectural improvements and optimizations
- Ensure code quality and maintainability enhancement
- Validate refactoring results with comprehensive testing

<include component="components/quality/anti-pattern-detection.md" />
<include component="components/actions/apply-code-changes.md" />
<include component="components/testing/mutation-testing.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/testing/mutation-testing.md</component>
    </includes_components>
    <uses_config_values>
      <value>refactoring.safety.validation_level</value>
      <value>optimization.patterns.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file> 