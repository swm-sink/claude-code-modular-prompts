---
name: /env-setup
description: "[DEPRECATED] Intelligent environment setup with automated toolchain installation, configuration management, and comprehensive dependency resolution - use /project setup instead"
argument-hint: "[environment_type] [automation_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
test_coverage: 0%
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/project setup"
reason: "Consolidated into unified /project command for integrated environment setup and project management"
removal_date: "2025-08-25"
---
# ⚠️ DEPRECATED: /env-setup

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Please use `/project setup` instead:**
```
# Old command:
/env setup development --automated

# New command:
/project setup development --automated
```

The new unified `/project` command provides:
- ✅ All legacy environment setup functionality in setup mode
- ✅ Enhanced integration with infrastructure provisioning and development workflows
- ✅ Improved multi-environment support and configuration management
- ✅ Better dependency resolution and toolchain management capabilities
- ✅ Unified validation and testing across all setup operations

---

# /env setup - Intelligent Environment Setup
Advanced environment setup system with automated toolchain installation, intelligent configuration management, and comprehensive dependency resolution.
## Usage
```bash
/env setup development                     # Development environment setup
/env setup --automated                     # Fully automated setup process
/env setup --production                    # Production environment setup
/env setup --comprehensive                 # Comprehensive environment management
```
<command_file>
  <metadata>
    <n>/env setup</n>
    <purpose>Intelligent environment setup with automated toolchain installation, configuration management, and comprehensive dependency resolution</purpose>
    <usage>
      <![CDATA[
      /env setup [environment_type]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="environment_type" type="string" required="false" default="development">
      <description>Type of environment to set up</description>
    </argument>
    <argument name="automation_level" type="string" required="false" default="automated">
      <description>Level of automation for the setup process</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Development environment setup</description>
      <usage>/env setup development</usage>
    </example>
    <example>
      <description>Fully automated setup process</description>
      <usage>/env setup --automated</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced environment setup specialist. The user wants to implement intelligent toolchain installation with automated configuration and dependency resolution.
**Setup Process:**
1. **Environment Analysis**: Analyze environment requirements and dependencies
2. **Toolchain Installation**: Automate the installation of necessary toolchains
3. **Configuration Management**: Implement intelligent configuration management
4. **Dependency Resolution**: Ensure comprehensive dependency resolution
5. **Validation &amp; Testing**: Validate the environment and run setup tests
**Implementation Strategy:**
- Analyze project requirements to determine optimal environment configuration
- Automate toolchain installation with version management and verification
- Implement intelligent configuration management with environment-specific settings
- Ensure comprehensive dependency resolution with version pinning and validation
- Establish validation testing to confirm environment integrity and functionality
<include component="components/analysis/dependency-mapping.md" />
<include component="components/integration/cicd-integration.md" />
<include component="components/testing/framework-validation.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/integration/cicd-integration.md</component>
      <component>components/testing/framework-validation.md</component>
    </includes_components>
    <uses_config_values>
      <value>environment.setup.auto_install</value>
      <value>dependency_resolution.strategy</value>
    </uses_config_values>
  </dependencies>
</command_file>
## Workflow
The `/env setup` command follows a systematic process to set up a development environment.
```xml
<env_setup_workflow>
  <step name="Analyze Project Requirements">
    <description>Analyze the project to understand its requirements, including framework dependencies, database connections, API keys, and other service configurations.</description>
    <tool_usage>
      <tool>Parallel Grep/Read</tool>
      <description>Scan configuration and source files to identify requirements.</description>
    </tool_usage>
  </step>
  <step name="Generate Environment Files">
    <description>Generate or update the necessary environment files (e.g., `.env`, `.env.example`, environment-specific configs) with the required variables.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create or modify environment files.</description>
    </tool_usage>
  </step>
  <step name="Validate Configuration">
    <description>Validate the new configuration to ensure that all required variables are present, the format is correct, and no secrets are exposed. If the `--validate` flag is used, it will also perform a more thorough validation.</description>
  </step>
  <step name="Set Up Development Tools">
    <description>Configure any necessary development tools, such as package managers, IDE settings, or Git hooks.</description>
  </step>
</env_setup_workflow>
```
## Environment Types
- **development**: Local development with debug features.
- **staging**: Pre-production testing environment.
- **production**: Live environment with security hardening.
- **testing**: Isolated testing configuration.