---
description: Advanced innovation laboratory with rapid prototyping, experimentation frameworks, and breakthrough discovery
argument-hint: "[experiment_type] [innovation_scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /innovation lab - Advanced Innovation Laboratory

Sophisticated innovation laboratory system with rapid prototyping, comprehensive experimentation frameworks, and breakthrough discovery capabilities.

## Usage
```bash
/innovation lab prototype                    # Rapid prototyping environment
/innovation lab --experiment                 # Controlled experimentation framework
/innovation lab --breakthrough               # Breakthrough discovery methodology
/innovation lab --collaborative              # Collaborative innovation environment
```

<command_file>
  <metadata>
    <n>/innovation lab</n>
    <purpose>Advanced innovation laboratory with rapid prototyping, experimentation frameworks, and breakthrough discovery</purpose>
    <usage>
      <![CDATA[
      /innovation lab [experiment_type]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="experiment_type" type="string" required="false" default="prototype">
      <description>Type of innovation experiment to conduct</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Rapid prototyping session</description>
      <usage>/innovation lab prototype --rapid</usage>
    </example>
    <example>
      <description>Controlled experimentation</description>
      <usage>/innovation lab experiment --controlled</usage>
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
      <include>components/learning/meta-learning.md</include>
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/analysis/experimentation-frameworks.md</include>
      <include>components/development/prototyping-tools.md</include>
      
You are an innovation laboratory specialist. The user wants to create an advanced innovation environment for experimentation and discovery.

**Analysis Process:**
1. **Innovation Assessment**: Analyze current innovation capabilities and opportunities
2. **Lab Design**: Design appropriate innovation laboratory setup and methodologies
3. **Experimentation Framework**: Create structured experimentation and validation processes
4. **Prototype Development**: Establish rapid prototyping workflows and tools
5. **Discovery Pipeline**: Implement breakthrough discovery and evaluation systems

**Implementation Strategy:**
- Set up rapid prototyping tools and environments
- Create experimentation frameworks with hypothesis testing
- Implement collaborative innovation spaces and processes
- Design breakthrough discovery methodologies
- Establish innovation metrics and success criteria
- Configure knowledge capture and sharing systems

    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/learning/meta-learning.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>innovation.lab.tools</value>
      <value>experimentation.frameworks.methodology</value>
    </uses_config_values>
  </dependencies>
</command_file> 