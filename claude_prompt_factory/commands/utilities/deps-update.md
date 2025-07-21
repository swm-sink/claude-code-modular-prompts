---
description: Intelligent dependency updates with automated vulnerability scanning, compatibility validation, and rollback safety
argument-hint: "[update_scope] [validation_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /deps update - Intelligent Dependency Updates

Advanced dependency management with automated vulnerability scanning, intelligent compatibility validation, and comprehensive rollback safety.

## Usage
```bash
/deps update security                        # Security-focused dependency updates
/deps update --automated                     # Fully automated dependency management
/deps update --compatibility                 # Compatibility-validated updates
/deps update --comprehensive                 # Comprehensive dependency optimization
```

<command_file>
  <metadata>
    <n>/deps update</n>
    <purpose>Intelligent dependency updates with automated vulnerability scanning, compatibility validation, and rollback safety</purpose>
    <usage>
      <![CDATA[
      /deps update [update_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="update_scope" type="string" required="false" default="security">
      <description>Scope of dependency updates to perform</description>
    </argument>
    <argument name="validation_level" type="string" required="false" default="comprehensive">
      <description>Level of validation and safety checks</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Security-focused dependency updates</description>
      <usage>/deps update security</usage>
    </example>
    <example>
      <description>Fully automated dependency management</description>
      <usage>/deps update --automated</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced dependency management specialist. The user wants to implement intelligent updates with vulnerability scanning and comprehensive safety validation.

**Update Process:**
1. **Dependency Analysis**: Analyze current dependencies and identify update candidates
2. **Security Scanning**: Perform comprehensive vulnerability and security scanning
3. **Compatibility Testing**: Validate compatibility and breaking change detection
4. **Automated Updates**: Execute intelligent updates with rollback mechanisms
5. **Validation & Monitoring**: Monitor updates and validate system stability

**Implementation Strategy:**
- Analyze dependency trees for security vulnerabilities and outdated packages
- Implement automated security scanning with vulnerability databases
- Apply intelligent compatibility testing and breaking change detection
- Create comprehensive rollback mechanisms and safety nets
- Establish continuous monitoring for dependency health and security

<include component="components/analysis/dependency-mapping.md" />
<include component="components/security/owasp-compliance.md" />
<include component="components/testing/framework-validation.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/security/owasp-compliance.md</component>
      <component>components/testing/framework-validation.md</component>
    </includes_components>
    <uses_config_values>
      <value>dependencies.auto_update.enabled</value>
      <value>security.vulnerability.scan_level</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Workflow

The `/deps update` command follows a systematic process to safely update dependencies.

```xml
<deps_update_workflow>
  <step name="Analyze Dependencies & Plan Updates">
    <description>Analyze the project's dependencies to identify outdated packages and plan the update strategy (e.g., minor updates only, patch updates only). Check for any known breaking changes.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate package manager command to check for outdated dependencies.</description>
    </tool_usage>
  </step>
  
  <step name="Update Dependencies Incrementally">
    <description>Update the dependencies incrementally, one at a time or in small, safe groups. Create a pre-update snapshot or backup to enable easy rollback.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate package manager command to update dependencies.</description>
    </tool_usage>
  </step>
  
  <step name="Validate Updates">
    <description>After each update, run the full test suite to ensure that the change has not introduced any regressions. If tests fail, automatically roll back the update.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the test suite and, if necessary, the package manager command to roll back the update.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed report of the updates, including version changes, any breaking change warnings, and a summary of the test results.</description>
    <output>A comprehensive dependency update report.</output>
  </step>
</deps_update_workflow>

## Key Features
- **Smart Updates**: Analyzes dependency compatibility before updating.
- **Incremental Updates**: Updates dependencies individually or in safe groups.
- **Test Validation**: Runs the full test suite after each update.
- **Breaking Change Detection**: Identifies potential API changes in new versions.
- **Automated Rollback**: Reverts updates on test failures or compatibility issues.