---
description: Advanced context priming with intelligent codebase understanding, adaptive learning, and comprehensive knowledge integration
argument-hint: "[prime_scope] [learning_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /prime - Advanced Context Priming

Sophisticated context priming system with intelligent codebase understanding, adaptive learning, and comprehensive knowledge integration.

## Usage
```bash
/prime codebase                              # Prime with codebase understanding
/prime --architecture                        # Architecture-focused priming
/prime --patterns                            # Code pattern recognition priming
/prime --comprehensive                       # Comprehensive context priming
```

<command_file>
  <metadata>
    <n>/prime</n>
    <purpose>Advanced context priming with intelligent codebase understanding, adaptive learning, and comprehensive knowledge integration</purpose>
    <usage>
      <![CDATA[
      /prime [prime_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="prime_scope" type="string" required="false" default="codebase">
      <description>Scope of context priming to perform</description>
    </argument>
    <argument name="learning_depth" type="string" required="false" default="comprehensive">
      <description>Depth of learning and understanding</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Prime with codebase understanding</description>
      <usage>/prime codebase</usage>
    </example>
    <example>
      <description>Architecture-focused priming</description>
      <usage>/prime --architecture</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced context priming specialist. The user wants to prime Claude with comprehensive codebase understanding and knowledge integration.

**Priming Process:**
1. **Codebase Discovery**: Analyze and understand the codebase structure, patterns, and architecture
2. **Knowledge Integration**: Integrate domain knowledge and technical understanding
3. **Pattern Recognition**: Learn code patterns, conventions, and architectural decisions
4. **Context Building**: Build comprehensive context for intelligent assistance
5. **Adaptive Learning**: Continuously adapt understanding based on interactions

**Implementation Strategy:**
- Perform deep codebase analysis and pattern recognition
- Build comprehensive mental models of system architecture
- Learn domain-specific terminology and conventions
- Create contextual understanding for better assistance
- Establish foundation for intelligent code generation and analysis

<include component="components/context/find-relevant-code.md" />
<include component="components/learning/meta-learning.md" />
<include component="components/context/adaptive-thinking.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/learning/meta-learning.md</component>
      <component>components/context/adaptive-thinking.md</component>
    </includes_components>
    <uses_config_values>
      <value>context.priming.depth</value>
      <value>learning.adaptive.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file> 