---
name: /dev-setup
description: "[DEPRECATED] Advanced development environment setup with intelligent automation, dependency resolution, and platform optimization - use /project setup instead"
argument-hint: "[environment_type] [automation_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
test_coverage: 0%
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/project setup"
reason: "Consolidated into unified /project command for integrated development environment setup and project management"
removal_date: "2025-08-25"
---

# ⚠️ DEPRECATED: /dev-setup

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Please use `/project setup` instead:**
```
# Old command:
/dev setup full

# New command:
/project setup development --full-stack
```

The new unified `/project` command provides:
- ✅ All legacy development setup functionality in setup mode
- ✅ Enhanced integration with environment provisioning and workflow management
- ✅ Improved full-stack setup capabilities and IDE integration
- ✅ Better platform optimization and dependency management
- ✅ Unified configuration and validation across all setup operations

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
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <!-- Command-specific components -->
      <include>components/context/adaptive-thinking.md</include>
      <include>components/actions/apply-code-changes.md</include>
      <include>components/reporting/generate-structured-report.md</include>
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