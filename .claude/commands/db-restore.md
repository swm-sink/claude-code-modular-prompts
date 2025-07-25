---
description: Advanced database restoration with intelligent recovery, point-in-time restoration, and comprehensive data integrity validation
argument-hint: "[restore_strategy] [recovery_point]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
deprecation_deadline: "2025-08-25"
deprecation_replacement: "/db-admin restore"
deprecation_reason: "Consolidated into unified /db-admin command for better maintenance and consistency"
---
# /db restore - Advanced Database Restoration

⚠️ **DEPRECATION NOTICE** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Migration:** Use `/db-admin restore` instead.

**Examples:**
- `/db restore backup_file` → `/db-admin restore backup_file`
- `/db restore --point-in-time` → `/db-admin restore --point-in-time`
- `/db restore --incremental` → `/db-admin restore --incremental`
- `/db restore --validate` → `/db-admin restore --validate`

The new `/db-admin` command provides all the same functionality with improved consistency and maintainability.

---

Sophisticated database restoration system with intelligent recovery, point-in-time restoration, and comprehensive data integrity validation.
## Usage
```bash
/db restore backup_file                      # Standard database restoration
/db restore --point-in-time                  # Point-in-time recovery
/db restore --incremental                    # Incremental restoration
/db restore --validate                       # Restoration with validation
```
<command_file>
  <metadata>
    <n>/db restore</n>
    <purpose>Advanced database restoration with intelligent recovery, point-in-time restoration, and comprehensive data integrity validation</purpose>
    <usage>
      <![CDATA[
      /db restore [backup_source] [restore_strategy]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="backup_source" type="string" required="true">
      <description>Path or identifier of the backup source to restore from</description>
    </argument>
    <argument name="restore_strategy" type="string" required="false" default="full">
      <description>Restoration strategy (full, incremental, point-in-time)</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Full database restoration</description>
      <usage>/db restore backup_20240101.sql full</usage>
    </example>
    <example>
      <description>Point-in-time recovery</description>
      <usage>/db restore --point-in-time "2024-01-01 12:00:00"</usage>
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
      <include>components/reliability/circuit-breaker.md</include>
      <include>components/quality/framework-validation.md</include>
      <include>components/reporting/generate-structured-report.md</include>
You are a database restoration specialist. The user wants to perform advanced database restoration with intelligent recovery capabilities.
**Restoration Process:**
1. **Backup Validation**: Validate backup integrity and compatibility
2. **Recovery Planning**: Plan optimal restoration strategy and timeline
3. **Data Restoration**: Execute restoration with integrity monitoring
4. **Validation Testing**: Comprehensive testing of restored data
5. **Performance Optimization**: Optimize restored database performance
**Implementation Strategy:**
- Validate backup files and check integrity
- Plan restoration timeline and rollback strategies
- Execute point-in-time or full restoration procedures
- Perform comprehensive data validation and integrity checks
- Optimize database performance post-restoration
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/error/circuit-breaker.md</component>
      <component>components/quality/framework-validation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>database.backup.retention_days</value>
      <value>database.restore.validation_level</value>
    </uses_config_values>
  </dependencies>
</command_file>