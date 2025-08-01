---
description: Specialized agent for managing component dependencies and include resolution
argument-hint: "[operation_mode] [target_scope] [resolution_strategy]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# /component linker - Component Dependency Manager

Specialized micro agent (<30k tokens) that manages component dependencies, resolves includes, validates component references, and optimizes the component graph for the prompt factory framework.

## Usage
```bash
/component linker "validate_all"                                    # Validate all component links
/component linker "resolve_includes" target_scope="commands"        # Resolve command includes
/component linker "optimize_graph" resolution_strategy="aggressive" # Optimize dependency graph
```

## Arguments
- `operation_mode` (required): "validate_all", "resolve_includes", "optimize_graph", "repair_links"
- `target_scope` (optional): "commands", "components", "all" (default: all)
- `resolution_strategy` (optional): "conservative", "standard", "aggressive" (default: standard)

## What It Does
1. **Dependency Analysis**: Maps all component dependencies and include relationships
2. **Link Validation**: Validates all component references and include paths
3. **Include Resolution**: Resolves component includes and template insertions
4. **Graph Optimization**: Optimizes component dependency graph for performance
5. **Circular Detection**: Detects and resolves circular dependency issues
6. **Reference Repair**: Fixes broken component references and missing files

<command_file>
  <metadata>
    <name>/component linker</name>
    <purpose>Manages component dependencies, resolves includes, and validates component references in the framework.</purpose>
    <usage>
      <![CDATA[
      /component linker operation_mode="validate_all" target_scope="all" resolution_strategy="standard"
      ]]>
    </usage>
    <specialization>component_dependency_management</specialization>
    <token_budget>26000</token_budget>
  </metadata>

  <arguments>
    <argument name="operation_mode" type="string" required="true">
      <description>Operation type: validate_all, resolve_includes, optimize_graph, or repair_links.</description>
    </argument>
    <argument name="target_scope" type="string" required="false" default="all">
      <description>Scope of operation: commands, components, or all framework files.</description>
    </argument>
    <argument name="resolution_strategy" type="string" required="false" default="standard">
      <description>Resolution approach: conservative, standard, or aggressive optimization.</description>
    </argument>
  </arguments>

  <capabilities>
    <capability name="dependency_mapping">
      <description>Creates comprehensive maps of all component dependencies and relationships.</description>
      <tools>Read, Grep, Glob</tools>
    </capability>
    <capability name="include_resolution">
      <description>Resolves component includes and validates template insertions.</description>
      <tools>Read, Write, Edit</tools>
    </capability>
    <capability name="circular_detection">
      <description>Detects circular dependencies and proposes resolution strategies.</description>
      <tools>Read, Grep, Bash</tools>
    </capability>
    <capability name="reference_validation">
      <description>Validates all component references and include paths for correctness.</description>
      <tools>Read, Glob, Bash</tools>
    </capability>
    <capability name="graph_optimization">
      <description>Optimizes component dependency graph for performance and maintainability.</description>
      <tools>Read, Write, Edit</tools>
    </capability>
  </capabilities>

  <operation_modes>
    <mode name="validate_all">
      <description>Comprehensive validation of all component dependencies and references.</description>
      <actions>
        <action>Scan all command and component files for dependencies</action>
        <action>Validate each component reference and include path</action>
        <action>Check for missing components and broken links</action>
        <action>Generate validation report with recommendations</action>
      </actions>
    </mode>
    <mode name="resolve_includes">
      <description>Resolve component includes and template insertions throughout the framework.</description>
      <actions>
        <action>Process all component include directives</action>
        <action>Resolve template variables and substitutions</action>
        <action>Validate resolved content for correctness</action>
        <action>Update include references as needed</action>
      </actions>
    </mode>
    <mode name="optimize_graph">
      <description>Optimize component dependency graph for performance and clarity.</description>
      <actions>
        <action>Analyze current dependency graph structure</action>
        <action>Identify optimization opportunities</action>
        <action>Reorganize dependencies for better performance</action>
        <action>Eliminate redundant or unused dependencies</action>
      </actions>
    </mode>
    <mode name="repair_links">
      <description>Repair broken component references and missing dependencies.</description>
      <actions>
        <action>Identify broken component references</action>
        <action>Locate missing component files</action>
        <action>Fix incorrect paths and references</action>
        <action>Create missing components if necessary</action>
      </actions>
    </mode>
  </operation_modes>

  <dependency_patterns>
    <pattern name="component_include">
      <regex>&lt;component\s+path="([^"]+)"\s*/&gt;</regex>
      <description>Standard component include pattern</description>
    </pattern>
    <pattern name="template_include">
      <regex>&lt;include\s+component="([^"]+)"\s*/&gt;</regex>
      <description>Template-based component inclusion</description>
    </pattern>
    <pattern name="dependency_reference">
      <regex>&lt;dependency\s+path="([^"]+)"\s*/&gt;</regex>
      <description>Explicit dependency declaration</description>
    </pattern>
  </dependency_patterns>

  <processing_strategy>
    <phase name="discovery">
      <description>Discover all component dependencies and relationships.</description>
      <actions>
        <action>Scan framework for component files and references</action>
        <action>Parse dependency declarations and includes</action>
        <action>Build comprehensive dependency graph</action>
        <action>Identify potential issues and optimization opportunities</action>
      </actions>
    </phase>
    <phase name="analysis">
      <description>Analyze dependency graph for issues and optimization potential.</description>
      <actions>
        <action>Validate all component references and paths</action>
        <action>Detect circular dependencies and conflicts</action>
        <action>Identify unused or redundant components</action>
        <action>Calculate optimization impact and strategies</action>
      </actions>
    </phase>
    <phase name="resolution">
      <description>Resolve dependencies and apply optimizations.</description>
      <actions>
        <action>Fix broken references and missing components</action>
        <action>Resolve circular dependencies with restructuring</action>
        <action>Apply optimization strategies based on analysis</action>
        <action>Update dependency declarations and includes</action>
      </actions>
    </phase>
    <phase name="validation">
      <description>Validate resolved dependencies and optimizations.</description>
      <actions>
        <action>Re-run dependency analysis to verify fixes</action>
        <action>Test component resolution and inclusion</action>
        <action>Validate framework functionality with changes</action>
        <action>Generate comprehensive resolution report</action>
      </actions>
    </phase>
  </processing_strategy>

  <dependencies>
    <component path="components/context/hierarchical-loading.md" />
    <component path="components/quality/anti-pattern-detection.md" />
    <component path="components/reporting/generate-structured-report.md" />
  </dependencies>

  <specialization_focus>
    <focus_area>Component Dependency Mapping</focus_area>
    <focus_area>Include Resolution and Validation</focus_area>
    <focus_area>Circular Dependency Detection</focus_area>
    <focus_area>Graph Optimization Strategies</focus_area>
    <focus_area>Reference Integrity Management</focus_area>
  </specialization_focus>
</command_file>