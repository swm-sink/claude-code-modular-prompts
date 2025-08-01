---
description: Specialized agent for fixing XML parsing errors and validating command file structure
argument-hint: "[target_files] [error_mode] [validation_depth]"
allowed-tools: Read, Write, Edit, Grep, Bash
---

# /xml parser - XML Validation & Error Fixing Specialist

Specialized micro agent (<30k tokens) that identifies, diagnoses, and fixes XML parsing errors in command files while preserving all functionality and improving structure.

## Usage
```bash
/xml parser "commands/**/*.md"                           # Scan and fix all XML errors
/xml parser "error_files.txt" error_mode="aggressive"   # Fix specific error files
/xml parser "validation_only" validation_depth="deep"   # Deep validation without fixing
```

## Arguments
- `target_files` (required): File pattern, error list, or validation mode specification
- `error_mode` (optional): "conservative", "standard", "aggressive" (default: standard)
- `validation_depth` (optional): "basic", "standard", "deep" (default: standard)

## What It Does
1. **Error Detection**: Scans command files for XML parsing errors and malformed structure
2. **Syntax Analysis**: Analyzes XML syntax issues, unclosed tags, invalid characters
3. **CDATA Fixing**: Fixes CDATA sections with unescaped angle brackets and special characters
4. **Tag Validation**: Ensures proper XML tag structure and self-closing elements
5. **Structure Repair**: Repairs broken XML hierarchy and missing elements
6. **Validation Report**: Generates comprehensive validation and error fixing report

<command_file>
  <metadata>
    <name>/xml parser</name>
    <purpose>Identifies, diagnoses, and fixes XML parsing errors in command files while preserving functionality.</purpose>
    <usage>
      <![CDATA[
      /xml parser target_files="commands/**/*.md" error_mode="standard" validation_depth="deep"
      ]]>
    </usage>
    <specialization>xml_validation_and_repair</specialization>
    <token_budget>28000</token_budget>
  </metadata>

  <arguments>
    <argument name="target_files" type="string" required="true">
      <description>File pattern, error list, or validation mode (e.g., "commands/**/*.md", "error_files.txt", "validation_only").</description>
    </argument>
    <argument name="error_mode" type="string" required="false" default="standard">
      <description>Error fixing aggressiveness: conservative, standard, or aggressive approach.</description>
    </argument>
    <argument name="validation_depth" type="string" required="false" default="standard">
      <description>Validation thoroughness: basic, standard, or deep XML structure analysis.</description>
    </argument>
  </arguments>

  <capabilities>
    <capability name="xml_error_detection">
      <description>Comprehensive XML parsing error detection and classification.</description>
      <tools>Read, Grep, Bash</tools>
    </capability>
    <capability name="syntax_repair">
      <description>Automated repair of XML syntax errors, malformed tags, and structure issues.</description>
      <tools>Read, Write, Edit</tools>
    </capability>
    <capability name="cdata_sanitization">
      <description>Fixes CDATA sections with unescaped characters and improper content.</description>
      <tools>Read, Edit, Write</tools>
    </capability>
    <capability name="structure_validation">
      <description>Deep validation of XML hierarchy, dependencies, and component references.</description>
      <tools>Read, Grep, Bash</tools>
    </capability>
  </capabilities>

  <error_patterns>
    <pattern name="unclosed_tags">
      <description>Detects and fixes unclosed XML tags and improper nesting.</description>
      <regex>&lt;([^/&gt;]+)&gt;(?!.*&lt;/\1&gt;)</regex>
      <fix_strategy>Add proper closing tags or convert to self-closing</fix_strategy>
    </pattern>
    <pattern name="cdata_angle_brackets">
      <description>Fixes unescaped angle brackets in CDATA sections.</description>
      <regex>&lt;!\[CDATA\[.*&lt;[^!].*\]\]&gt;</regex>
      <fix_strategy>Escape angle brackets or restructure content</fix_strategy>
    </pattern>
    <pattern name="malformed_attributes">
      <description>Repairs malformed XML attributes and quotation issues.</description>
      <regex>\w+=[^"'][^&gt;\s]*</regex>
      <fix_strategy>Add proper quotation and escape special characters</fix_strategy>
    </pattern>
    <pattern name="invalid_characters">
      <description>Removes or escapes invalid XML characters.</description>
      <regex>[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]</regex>
      <fix_strategy>Remove or replace with valid XML entities</fix_strategy>
    </pattern>
  </error_patterns>

  <processing_strategy>
    <phase name="scanning">
      <description>Comprehensive scan for XML parsing errors and structural issues.</description>
      <actions>
        <action>Run dependency graph analysis to identify error files</action>
        <action>Extract XML sections from hybrid Markdown+XML files</action>
        <action>Parse XML with detailed error reporting</action>
        <action>Classify errors by type and severity</action>
      </actions>
    </phase>
    <phase name="analysis">
      <description>Deep analysis of error patterns and repair strategies.</description>
      <actions>
        <action>Analyze error context and surrounding structure</action>
        <action>Determine optimal repair strategy for each error</action>
        <action>Check for cascading effects and dependencies</action>
        <action>Plan repair sequence to avoid conflicts</action>
      </actions>
    </phase>
    <phase name="repair">
      <description>Systematic repair of XML errors with validation.</description>
      <actions>
        <action>Apply targeted fixes based on error patterns</action>
        <action>Preserve original functionality and intent</action>
        <action>Validate each fix with XML parser</action>
        <action>Test component inclusion and dependencies</action>
      </actions>
    </phase>
    <phase name="validation">
      <description>Comprehensive validation and quality assurance.</description>
      <actions>
        <action>Re-run dependency graph analysis</action>
        <action>Validate all XML structures parse correctly</action>
        <action>Check component resolution and includes</action>
        <action>Generate detailed repair and validation report</action>
      </actions>
    </phase>
  </processing_strategy>

  <dependencies>
    <component path="components/quality/anti-pattern-detection.md" />
    <component path="components/reporting/generate-structured-report.md" />
  </dependencies>

  <specialization_focus>
    <focus_area>XML Parsing Error Detection</focus_area>
    <focus_area>CDATA Section Sanitization</focus_area>
    <focus_area>Tag Structure Validation</focus_area>
    <focus_area>Character Encoding Issues</focus_area>
    <focus_area>Component Reference Validation</focus_area>
  </specialization_focus>
</command_file>