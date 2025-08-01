---
description: Specialized agent for converting command files to hybrid Markdown+XML format
argument-hint: "[file_batch] [conversion_mode] [validation_level]"
allowed-tools: Read, Write, Edit, MultiEdit, Grep, Glob
---

# /command converter - Command File Conversion Specialist

Specialized micro agent (<30k tokens) that converts Claude Code command files from pure XML to hybrid Markdown+XML format with YAML frontmatter for maximum compatibility.

## Usage
```bash
/command converter "commands/analysis/*.md"                    # Convert analysis commands
/command converter "batch=10" conversion_mode="parallel"      # Parallel batch conversion
/command converter "all_commands" validation_level="strict"   # Convert all with validation
```

## Arguments
- `file_batch` (required): File pattern or batch specification for conversion
- `conversion_mode` (optional): "sequential", "parallel", "adaptive" (default: adaptive)
- `validation_level` (optional): "basic", "standard", "strict" (default: standard)

## What It Does
1. **File Analysis**: Analyzes current command file structure and content
2. **Template Application**: Applies hybrid Markdown+XML template format
3. **Content Preservation**: Preserves all XML functionality and components
4. **YAML Generation**: Creates frontmatter with description, arguments, tools
5. **Validation**: Ensures proper XML structure and Markdown formatting
6. **Batch Processing**: Handles multiple files efficiently with progress tracking

<command_file>
  <metadata>
    <name>/command converter</name>
    <purpose>Converts command files to hybrid Markdown+XML format for Claude Code compatibility.</purpose>
    <usage>
      <![CDATA[
      /command converter file_batch="commands/**/*.md" conversion_mode="parallel" validation_level="strict"
      ]]>
    </usage>
    <specialization>command_file_transformation</specialization>
    <token_budget>25000</token_budget>
  </metadata>

  <arguments>
    <argument name="file_batch" type="string" required="true">
      <description>File pattern or batch specification for conversion (e.g., "commands/analysis/*.md", "batch=10", "all_commands").</description>
    </argument>
    <argument name="conversion_mode" type="string" required="false" default="adaptive">
      <description>Conversion execution mode: sequential, parallel, or adaptive based on file complexity.</description>
    </argument>
    <argument name="validation_level" type="string" required="false" default="standard">
      <description>Validation strictness: basic, standard, or strict XML and Markdown validation.</description>
    </argument>
  </arguments>

  <capabilities>
    <capability name="hybrid_format_conversion">
      <description>Converts pure XML command files to hybrid Markdown+XML format with YAML frontmatter.</description>
      <tools>Read, Write, Edit, MultiEdit</tools>
    </capability>
    <capability name="batch_processing">
      <description>Efficiently processes multiple command files in parallel or sequential batches.</description>
      <tools>Glob, Grep, MultiEdit</tools>
    </capability>
    <capability name="xml_preservation">
      <description>Preserves all existing XML functionality while adding Markdown compatibility.</description>
      <tools>Read, Edit, Write</tools>
    </capability>
    <capability name="yaml_frontmatter_generation">
      <description>Generates proper YAML frontmatter for Claude Code compatibility.</description>
      <tools>Read, Write</tools>
    </capability>
  </capabilities>

  <processing_strategy>
    <phase name="analysis">
      <description>Analyze target files and determine conversion requirements.</description>
      <actions>
        <action>Scan file patterns and identify conversion candidates</action>
        <action>Analyze existing XML structure and components</action>
        <action>Determine batch size and processing strategy</action>
      </actions>
    </phase>
    <phase name="conversion">
      <description>Apply hybrid template format to each command file.</description>
      <actions>
        <action>Generate YAML frontmatter from XML metadata</action>
        <action>Add Markdown headers and usage examples</action>
        <action>Preserve XML structure for advanced features</action>
        <action>Apply consistent formatting and structure</action>
      </actions>
    </phase>
    <phase name="validation">
      <description>Validate converted files for correctness and compatibility.</description>
      <actions>
        <action>Verify XML structure integrity</action>
        <action>Validate YAML frontmatter syntax</action>
        <action>Check Markdown formatting compliance</action>
        <action>Test component inclusion and dependencies</action>
      </actions>
    </phase>
  </processing_strategy>

  <dependencies>
    <component path="components/context/hierarchical-loading.md" />
    <component path="components/quality/quality-metrics.md" />
    <component path="components/reporting/generate-structured-report.md" />
  </dependencies>

  <specialization_focus>
    <focus_area>Command File Structure Conversion</focus_area>
    <focus_area>Hybrid Format Template Application</focus_area>
    <focus_area>XML Functionality Preservation</focus_area>
    <focus_area>YAML Frontmatter Generation</focus_area>
    <focus_area>Batch Processing Optimization</focus_area>
  </specialization_focus>
</command_file>