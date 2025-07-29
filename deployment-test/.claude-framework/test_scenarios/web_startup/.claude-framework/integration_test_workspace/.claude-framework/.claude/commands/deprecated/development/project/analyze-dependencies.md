---
name: /analyze-dependencies
description: "[DEPRECATED] Advanced dependency analysis with intelligent mapping, compatibility assessment, and optimization recommendations - use /analyze-system dependencies instead"
argument-hint: "[analysis_type] [scan_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
test_coverage: 0%
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/analyze-system dependencies"
reason: "Superseded by unified /analyze-system command with comprehensive dependency analysis"
migration_deadline: "2025-08-25"
---
<command_file>

# ⚠️ DEPRECATED: /analyze-dependencies

**This command is deprecated and will be removed on 2025-08-25.**

**Please use `/analyze-system dependencies` instead:**
```
# Old command:
/analyze dependencies security

# New command:
/analyze-system dependencies --type=security
```

The new unified `/analyze-system` command provides:
- ✅ All legacy dependency analysis functionality in dependencies mode
- ✅ Enhanced compatibility assessment with latest dependency data
- ✅ Intelligent dependency mapping with visualization
- ✅ Advanced conflict resolution strategies
- ✅ Better integration with security and performance analysis

---

# /analyze dependencies - Advanced Dependency Analysis
Sophisticated dependency analysis system with intelligent mapping, compatibility assessment, and comprehensive optimization recommendations.
## Usage
```bash
/analyze dependencies compatibility         # Dependency compatibility analysis
/analyze dependencies --outdated             # Outdated package detection
/analyze dependencies --conflicts            # Dependency conflict resolution
/analyze dependencies --optimization         # Optimization recommendations
```
<command_file>
  <metadata>
    <n>/analyze dependencies</n>
    <purpose>Advanced dependency analysis with intelligent mapping, compatibility assessment, and optimization recommendations</purpose>
    <usage>
      <![CDATA[
      /analyze dependencies [analysis_type]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="analysis_type" type="string" required="false" default="comprehensive">
      <description>Type of dependency analysis to perform</description>
    </argument>
    <argument name="scan_depth" type="string" required="false" default="deep">
      <description>Depth of dependency scanning</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Dependency compatibility analysis</description>
      <usage>/analyze dependencies compatibility</usage>
    </example>
    <example>
      <description>Outdated package detection</description>
      <usage>/analyze dependencies --outdated</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
You are an advanced dependency analysis specialist. The user wants to perform comprehensive dependency analysis with intelligent mapping and compatibility assessment.
**Analysis Process:**
1. **Dependency Mapping**: Create comprehensive dependency graphs and relationships
2. **Compatibility Assessment**: Analyze compatibility and potential issues
3. **Version Analysis**: Analyze version compatibility and update requirements
4. **Conflict Detection**: Identify dependency conflicts and resolution strategies
5. **Optimization Assessment**: Recommend optimization and cleanup opportunities
**Implementation Strategy:**
- Generate detailed dependency trees and impact analysis
- Perform thorough compatibility analysis with dependency databases
- Analyze license compatibility and compliance issues
- Identify circular dependencies and resolution strategies
- Create prioritized update and optimization roadmaps
<include component="components/analysis/dependency-mapping.md" />
<include component="components/security/owasp-compliance.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/security/owasp-compliance.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>dependencies.scan.security_level</value>
      <value>analysis.vulnerability.sources</value>
    </uses_config_values>
  </dependencies>
</command_file>

</command_file>