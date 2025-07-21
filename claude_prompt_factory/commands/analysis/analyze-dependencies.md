---
description: Advanced dependency analysis with intelligent mapping, vulnerability scanning, and optimization recommendations
argument-hint: "[analysis_type] [scan_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /analyze dependencies - Advanced Dependency Analysis

Sophisticated dependency analysis system with intelligent mapping, vulnerability scanning, and comprehensive optimization recommendations.

## Usage
```bash
/analyze dependencies security               # Security vulnerability analysis
/analyze dependencies --outdated             # Outdated package detection
/analyze dependencies --conflicts            # Dependency conflict resolution
/analyze dependencies --optimization         # Optimization recommendations
```

<command_file>
  <metadata>
    <n>/analyze dependencies</n>
    <purpose>Advanced dependency analysis with intelligent mapping, vulnerability scanning, and optimization recommendations</purpose>
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
      <description>Security vulnerability analysis</description>
      <usage>/analyze dependencies security</usage>
    </example>
    <example>
      <description>Outdated package detection</description>
      <usage>/analyze dependencies --outdated</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced dependency analysis specialist. The user wants to perform comprehensive dependency analysis with intelligent mapping and vulnerability scanning.

**Analysis Process:**
1. **Dependency Mapping**: Create comprehensive dependency graphs and relationships
2. **Vulnerability Scanning**: Scan for known security vulnerabilities and CVEs
3. **Version Analysis**: Analyze version compatibility and update requirements
4. **Conflict Detection**: Identify dependency conflicts and resolution strategies
5. **Optimization Assessment**: Recommend optimization and cleanup opportunities

**Implementation Strategy:**
- Generate detailed dependency trees and impact analysis
- Perform security vulnerability scanning with CVE databases
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