---
description: Advanced development environment setup with intelligent automation, dependency resolution, and platform optimization
argument-hint: "[environment_type] [automation_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

<command_file>
  <metadata>
    <name>/dev setup</name>
    <purpose>Advanced development environment setup with intelligent automation and platform optimization</purpose>
    <usage>
      <![CDATA[
      /dev setup [environment_type]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="environment_type" type="string" required="false" default="full">
      <description>Type of development environment to setup</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Setup complete development environment</description>
      <usage>/dev setup full</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are a development environment specialist. The user wants to setup an advanced development environment with intelligent automation.

**Setup Process:**
1. **Environment Analysis**: Analyze current system and requirements
2. **Dependency Resolution**: Resolve and install required dependencies
3. **Configuration Setup**: Configure development tools and environments
4. **Platform Optimization**: Optimize for the target platform
5. **Validation Testing**: Test the setup for completeness

**Implementation Strategy:**
- Detect operating system and platform requirements
- Install and configure development tools and runtimes
- Setup IDE configurations and extensions
- Configure version control and deployment tools
- Establish development workflows and automation

<include component="components/context/adaptive-thinking.md" />
<include component="components/actions/apply-code-changes.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/adaptive-thinking.md</component>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>