---
description: Specialized agent for collecting, prioritizing, and managing all XML parsing and transformation errors
argument-hint: "[collection_mode] [priority_strategy] [resolution_approach]"
allowed-tools: Read, Write, Bash, Grep, Glob
---

# /error aggregator - Error Collection & Management Specialist

Specialized utility agent (<22k tokens) that collects, analyzes, prioritizes, and coordinates resolution of all XML parsing errors, transformation issues, and framework validation problems.

## Usage
```bash
/error aggregator "collect_all"                                      # Collect all errors across framework
/error aggregator "prioritize" priority_strategy="impact_based"      # Prioritize errors by impact
/error aggregator "resolution_plan" resolution_approach="parallel"   # Create resolution strategy
```

## Arguments
- `collection_mode` (required): "collect_all", "prioritize", "resolution_plan", "status_report"
- `priority_strategy` (optional): "severity_based", "impact_based", "frequency_based" (default: impact_based)
- `resolution_approach` (optional): "sequential", "parallel", "hybrid" (default: parallel)

## What It Does
1. **Error Collection**: Systematically collects all XML parsing and transformation errors
2. **Error Classification**: Categorizes errors by type, severity, and impact
3. **Priority Assignment**: Prioritizes errors based on blocking impact and resolution complexity
4. **Resolution Coordination**: Coordinates error resolution across multiple specialized agents
5. **Progress Tracking**: Tracks error resolution progress and success rates
6. **Pattern Analysis**: Identifies error patterns and prevention strategies

<command_file>
  <metadata>
    <name>/error aggregator</name>
    <purpose>Collects, analyzes, prioritizes, and coordinates resolution of all framework errors and issues.</purpose>
    <usage>
      <![CDATA[
      /error aggregator collection_mode="collect_all" priority_strategy="impact_based" resolution_approach="parallel"
      ]]>
    </usage>
    <specialization>error_management_and_resolution</specialization>
    <token_budget>22000</token_budget>
  </metadata>
  
  <arguments>
    <argument name="target" type="string" required="false">
      <description>Target specification for command execution</description>
    </argument>
    <argument name="options" type="object" required="false">
      <description>Additional options for command configuration</description>
    </argument>
  </arguments>

  <error_collection_system>
    <collection_source name="xml_parsing_errors">
      <description>Collects XML parsing errors from dependency graph analysis</description>
      <command><![CDATA[python archive/generate_dependency_graph.py 2>&1 | grep "XML PARSE ERROR"]]></command>
      <pattern>XML PARSE ERROR in (.+): (.+): line (\d+), column (\d+)</pattern>
    </collection_source>
    <collection_source name="component_resolution_errors">
      <description>Collects component include and dependency resolution errors</description>
      <search_pattern>component.*not found|include.*missing|dependency.*unresolved</search_pattern>
    </collection_source>
    <collection_source name="format_validation_errors">
      <description>Collects hybrid format validation and compliance errors</description>
      <validation_checks>
        <check>YAML frontmatter syntax</check>
        <check>Markdown header structure</check>
        <check>XML section validity</check>
        <check>Component reference integrity</check>
      </validation_checks>
    </collection_source>
    <collection_source name="framework_integration_errors">
      <description>Collects framework integration and functionality errors</description>
      <integration_tests>
        <test>Command discovery failures</test>
        <test>Argument parsing errors</test>
        <test>Tool permission violations</test>
        <test>Workflow execution failures</test>
      </integration_tests>
    </collection_source>
  </error_collection_system>

  <error_classification>
    <category name="critical_blockers">
      <description>Errors that completely block framework functionality</description>
      <examples>
        <error>XML parsing failures preventing command loading</error>
        <error>Missing core components breaking framework</error>
        <error>Circular dependencies causing infinite loops</error>
      </examples>
      <priority>1</priority>
    </category>
    <category name="functionality_impairers">
      <description>Errors that reduce framework functionality or performance</description>
      <examples>
        <error>Component resolution failures</error>
        <error>Incomplete command conversions</error>
        <error>Performance degradation issues</error>
      </examples>
      <priority>2</priority>
    </category>
    <category name="quality_issues">
      <description>Errors affecting code quality, consistency, or maintainability</description>
      <examples>
        <error>Format compliance violations</error>
        <error>Documentation inconsistencies</error>
        <error>Style and structure issues</error>
      </examples>
      <priority>3</priority>
    </category>
    <category name="optimization_opportunities">
      <description>Areas for improvement and optimization</description>
      <examples>
        <error>Performance optimization opportunities</error>
        <error>Code duplication and redundancy</error>
        <error>Efficiency improvements</error>
      </examples>
      <priority>4</priority>
    </category>
  </error_classification>

  <resolution_coordination>
    <strategy name="parallel_resolution">
      <description>Coordinate parallel error resolution across multiple specialized agents</description>
      <coordination_approach>
        <step>Group errors by type and assign to specialized agents</step>
        <step>Coordinate agent activities to prevent conflicts</step>
        <step>Monitor resolution progress and adjust strategies</step>
        <step>Validate fixes and ensure no regression</step>
      </coordination_approach>
    </strategy>
    <strategy name="dependency_aware_sequencing">
      <description>Sequence error resolution based on dependencies and blocking relationships</description>
      <sequencing_rules>
        <rule>Resolve blocking errors before dependent errors</rule>
        <rule>Address root causes before symptoms</rule>
        <rule>Handle critical infrastructure before feature errors</rule>
        <rule>Batch similar errors for efficiency</rule>
      </sequencing_rules>
    </strategy>
  </resolution_coordination>

  <progress_tracking>
    <tracking_metrics>
      <metric name="total_errors_identified">Count of all identified errors</metric>
      <metric name="errors_resolved">Successfully resolved errors</metric>
      <metric name="errors_in_progress">Currently being addressed</metric>
      <metric name="errors_pending">Waiting for resolution</metric>
      <metric name="resolution_rate">Errors resolved per hour</metric>
      <metric name="success_rate">Percentage of successful resolutions</metric>
    </tracking_metrics>
    <reporting_frequency>
      <real_time>Continuous monitoring and updates</real_time>
      <summary_reports>Hourly progress summaries</summary_reports>
      <completion_analysis>Final resolution analysis and patterns</completion_analysis>
    </reporting_frequency>
  </progress_tracking>

  <pattern_analysis>
    <pattern_detection>
      <pattern name="recurring_xml_errors">
        <description>Common XML syntax patterns causing repeated errors</description>
        <prevention>Template improvements and validation enhancements</prevention>
      </pattern>
      <pattern name="component_reference_issues">
        <description>Patterns in component path and reference problems</description>
        <prevention>Improved path validation and reference checking</prevention>
      </pattern>
      <pattern name="conversion_challenges">
        <description>Common issues in XML to hybrid format conversion</description>
        <prevention>Enhanced conversion templates and validation</prevention>
      </pattern>
    </pattern_detection>
  </pattern_analysis>

  <includes_components>
    <component>components/constitutional/safety-framework.md</component>
  </includes_components>
  
  <claude_prompt>
    <![CDATA[
You are executing the Error Aggregator command. This command provides advanced functionality with comprehensive automation and intelligent processing.

## Execution Framework

1. **Analysis Phase**
   - Understand the request context and parameters
   - Identify key requirements and constraints
   - Plan the execution approach

2. **Implementation Phase**
   - Execute the core functionality with precision
   - Apply best practices and optimization strategies
   - Ensure quality and consistency throughout

3. **Validation Phase**
   - Verify successful execution
   - Validate outputs meet requirements
   - Provide comprehensive results

## Key Principles

- **Automation**: Maximize intelligent automation where appropriate
- **Quality**: Maintain high standards throughout execution
- **Safety**: Ensure all operations follow constitutional AI principles
- **Efficiency**: Optimize for performance and resource usage

Execute this command with excellence, providing clear, actionable results.
    ]]>
  </claude_prompt>

  <specialization_focus>
    <focus_area>Comprehensive Error Collection</focus_area>
    <focus_area>Impact-Based Error Prioritization</focus_area>
    <focus_area>Multi-Agent Resolution Coordination</focus_area>
    <focus_area>Error Pattern Analysis and Prevention</focus_area>
    <focus_area>Resolution Progress Tracking</focus_area>
  </specialization_focus>
</command_file>