---
description: Advanced documentation validation with intelligent analysis, consistency checking, and quality assurance
argument-hint: "[check_scope] [validation_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /docs check - Advanced Documentation Validation

Sophisticated documentation validation system with intelligent analysis, consistency checking, and comprehensive quality assurance.

## Usage
```bash
/docs check all                              # Check all documentation
/docs check --consistency                    # Consistency validation
/docs check --links                          # Link validation and integrity
/docs check --quality                        # Quality assessment and scoring
```

<command_file>
  <metadata>
    <n>/docs check</n>
    <purpose>Advanced documentation validation with intelligent analysis, consistency checking, and quality assurance</purpose>
    <usage>
      <![CDATA[
      /docs check [check_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="check_scope" type="string" required="false" default="all">
      <description>Scope of documentation to validate</description>
    </argument>
    <argument name="validation_level" type="string" required="false" default="comprehensive">
      <description>Level of validation thoroughness</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Check all documentation</description>
      <usage>/docs check all</usage>
    </example>
    <example>
      <description>Consistency validation</description>
      <usage>/docs check --consistency</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced documentation validation specialist. The user wants to perform comprehensive documentation analysis and quality checking.

**Validation Process:**
1. **Content Analysis**: Analyze documentation content for accuracy and completeness
2. **Consistency Checking**: Verify consistency across documentation sections
3. **Quality Assessment**: Evaluate documentation quality and readability
4. **Link Validation**: Check internal and external links for validity
5. **Standards Compliance**: Ensure compliance with documentation standards

**Implementation Strategy:**
- Scan all documentation files for completeness and accuracy
- Validate cross-references and internal links
- Check code examples and technical accuracy
- Assess documentation structure and organization
- Generate comprehensive validation reports

<include component="components/quality/framework-validation.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/quality/framework-validation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>documentation.validation.standards</value>
      <value>quality.checks.thoroughness</value>
    </uses_config_values>
  </dependencies>
</command_file>