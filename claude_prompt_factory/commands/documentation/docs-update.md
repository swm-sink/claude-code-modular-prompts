---
description: Intelligent documentation updates with automated synchronization, version control, and comprehensive maintenance
argument-hint: "[update_scope] [sync_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /docs update - Intelligent Documentation Updates

Automated documentation update system with intelligent synchronization, comprehensive version control, and maintenance automation.

## Usage
```bash
/docs update sync                            # Synchronize documentation with code
/docs update --comprehensive                 # Comprehensive documentation updates
/docs update --automated                     # Fully automated update process
/docs update --version                       # Version-controlled updates
```

<command_file>
  <metadata>
    <n>/docs update</n>
    <purpose>Intelligent documentation updates with automated synchronization, version control, and comprehensive maintenance</purpose>
    <usage>
      <![CDATA[
      /docs update [update_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="update_scope" type="string" required="false" default="sync">
      <description>Scope of documentation updates to perform</description>
    </argument>
    <argument name="sync_strategy" type="string" required="false" default="automated">
      <description>Strategy for documentation synchronization</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Synchronize documentation with code</description>
      <usage>/docs update sync</usage>
    </example>
    <example>
      <description>Comprehensive documentation updates</description>
      <usage>/docs update --comprehensive</usage>
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
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/quality/framework-validation.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/documentation/sync-automation.md</include>
      <include>components/quality/change-tracking.md</include>
      
You are an advanced documentation update specialist. The user wants to implement intelligent synchronization with automated maintenance and version control.

**Update Process:**
1. **Documentation Analysis**: Analyze current documentation state and requirements
2. **Synchronization Planning**: Plan comprehensive sync with codebase changes
3. **Automated Updates**: Execute automated updates with intelligent detection
4. **Version Control**: Implement version-controlled documentation management
5. **Quality Assurance**: Validate updates for accuracy and completeness

**Implementation Strategy:**
- Analyze documentation gaps and outdated content systematically
- Implement automated synchronization with codebase changes
- Apply intelligent content generation and update strategies
- Create comprehensive version control and change tracking
- Establish quality gates for documentation accuracy
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/quality/framework-validation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>documentation.sync.auto_enabled</value>
      <value>version_control.documentation.strategy</value>
    </uses_config_values>
  </dependencies>
</command_file>