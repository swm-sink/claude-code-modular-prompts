---
description: Specialized agent for comprehensive framework validation and integration testing
argument-hint: "[test_scope] [validation_mode] [coverage_level]"
allowed-tools: Read, Bash, Grep, Glob, Write
---

# /framework tester - Framework Validation Specialist

Specialized micro agent (<30k tokens) that performs comprehensive validation of the Claude Code Prompt Factory framework, testing command discovery, routing, component integration, and end-to-end functionality.

## Usage
```bash
/framework tester "full_validation"                              # Complete framework test
/framework tester "command_discovery" validation_mode="claude"  # Test Claude Code integration
/framework tester "component_system" coverage_level="deep"      # Deep component testing
```

## Arguments
- `test_scope` (required): "full_validation", "command_discovery", "component_system", "routing_engine"
- `validation_mode` (optional): "local", "claude", "integration" (default: integration)
- `coverage_level` (optional): "basic", "standard", "deep" (default: standard)

## What It Does
1. **Command Discovery Testing**: Validates commands appear in Claude Code slash menu
2. **Argument Validation**: Tests argument hints and $ARGUMENTS substitution
3. **Component Integration**: Validates component system and dependency resolution
4. **Routing Verification**: Tests command routing and intelligent selection
5. **End-to-End Testing**: Comprehensive workflow and functionality validation
6. **Performance Assessment**: Measures framework performance and efficiency

<command_file>
  <metadata>
    <name>/framework tester</name>
    <purpose>Comprehensive validation of framework functionality, command discovery, and integration testing.</purpose>
    <usage>
      <![CDATA[
      /framework tester test_scope="full_validation" validation_mode="integration" coverage_level="deep"
      ]]>
    </usage>
    <specialization>framework_validation_and_testing</specialization>
    <token_budget>29000</token_budget>
  </metadata>

  <arguments>
    <argument name="test_scope" type="string" required="true">
      <description>Testing scope: full_validation, command_discovery, component_system, or routing_engine.</description>
    </argument>
    <argument name="validation_mode" type="string" required="false" default="integration">
      <description>Validation approach: local, claude (Claude Code), or integration testing.</description>
    </argument>
    <argument name="coverage_level" type="string" required="false" default="standard">
      <description>Testing depth: basic, standard, or deep coverage analysis.</description>
    </argument>
  </arguments>

  <capabilities>
    <capability name="command_discovery_testing">
      <description>Tests command discovery and availability in Claude Code slash menu.</description>
      <tools>Read, Bash, Grep</tools>
    </capability>
    <capability name="argument_validation">
      <description>Validates argument hints, substitution, and parameter handling.</description>
      <tools>Read, Grep, Bash</tools>
    </capability>
    <capability name="component_integration_testing">
      <description>Tests component system integration and dependency resolution.</description>
      <tools>Read, Bash, Glob</tools>
    </capability>
    <capability name="routing_verification">
      <description>Validates command routing, intelligent selection, and workflow orchestration.</description>
      <tools>Read, Bash, Write</tools>
    </capability>
    <capability name="performance_assessment">
      <description>Measures framework performance, response times, and efficiency metrics.</description>
      <tools>Bash, Write</tools>
    </capability>
  </capabilities>

  <test_suites>
    <suite name="command_discovery">
      <description>Validates command discovery and Claude Code integration.</description>
      <tests>
        <test name="slash_menu_integration">Check commands appear in / menu</test>
        <test name="command_parsing">Validate command syntax and structure</test>
        <test name="argument_hints">Test argument hint display and functionality</test>
        <test name="tool_permissions">Validate allowed-tools restrictions</test>
      </tests>
    </suite>
    <suite name="component_system">
      <description>Tests component integration and dependency management.</description>
      <tests>
        <test name="component_resolution">Test component include resolution</test>
        <test name="dependency_validation">Validate dependency graph integrity</test>
        <test name="template_expansion">Test template and variable expansion</test>
        <test name="circular_dependency_detection">Check circular dependency handling</test>
      </tests>
    </suite>
    <suite name="routing_engine">
      <description>Validates command routing and intelligent selection.</description>
      <tests>
        <test name="auto_routing">Test /auto command intelligent routing</test>
        <test name="complexity_analysis">Validate task complexity assessment</test>
        <test name="command_chaining">Test multi-command workflow orchestration</test>
        <test name="fallback_handling">Validate fallback and error handling</test>
      </tests>
    </suite>
    <suite name="integration_workflows">
      <description>End-to-end testing of complete workflows.</description>
      <tests>
        <test name="full_feature_development">Test complete /feature workflow</test>
        <test name="quality_enforcement">Test /quality enforce pipeline</test>
        <test name="analysis_workflows">Test analysis and pattern recognition</test>
        <test name="agent_orchestration">Test agent spawning and coordination</test>
      </tests>
    </suite>
  </test_suites>

  <validation_strategies>
    <strategy name="local_validation">
      <description>Local testing without Claude Code integration.</description>
      <actions>
        <action>Parse command files and validate structure</action>
        <action>Test component resolution and dependencies</action>
        <action>Validate XML parsing and Markdown formatting</action>
        <action>Check file integrity and completeness</action>
      </actions>
    </strategy>
    <strategy name="claude_integration">
      <description>Testing within Claude Code environment.</description>
      <actions>
        <action>Test command discovery in slash menu</action>
        <action>Validate argument parsing and hints</action>
        <action>Test tool permission enforcement</action>
        <action>Validate command execution and responses</action>
      </actions>
    </strategy>
    <strategy name="end_to_end_integration">
      <description>Comprehensive integration testing of complete workflows.</description>
      <actions>
        <action>Execute complete development workflows</action>
        <action>Test agent orchestration and coordination</action>
        <action>Validate quality gates and enforcement</action>
        <action>Measure performance and efficiency metrics</action>
      </actions>
    </strategy>
  </validation_strategies>

  <processing_strategy>
    <phase name="preparation">
      <description>Prepare testing environment and validate preconditions.</description>
      <actions>
        <action>Scan framework structure and command inventory</action>
        <action>Validate dependencies and component availability</action>
        <action>Set up testing environment and metrics collection</action>
        <action>Prepare test data and scenarios</action>
      </actions>
    </phase>
    <phase name="execution">
      <description>Execute comprehensive test suites based on scope and coverage.</description>
      <actions>
        <action>Run command discovery and parsing tests</action>
        <action>Execute component integration validation</action>
        <action>Test routing and workflow orchestration</action>
        <action>Measure performance and collect metrics</action>
      </actions>
    </phase>
    <phase name="analysis">
      <description>Analyze test results and identify issues or improvements.</description>
      <actions>
        <action>Analyze test results and failure patterns</action>
        <action>Identify performance bottlenecks and optimization opportunities</action>
        <action>Assess framework completeness and quality</action>
        <action>Generate recommendations for improvements</action>
      </actions>
    </phase>
    <phase name="reporting">
      <description>Generate comprehensive validation and testing report.</description>
      <actions>
        <action>Compile test results and metrics</action>
        <action>Generate detailed validation report</action>
        <action>Provide recommendations and next steps</action>
        <action>Document known issues and workarounds</action>
      </actions>
    </phase>
  </processing_strategy>

  <performance_metrics>
    <metric name="command_discovery_rate">
      <description>Percentage of commands successfully discovered in Claude Code</description>
      <target>100%</target>
    </metric>
    <metric name="component_resolution_success">
      <description>Success rate of component include resolution</description>
      <target>100%</target>
    </metric>
    <metric name="routing_accuracy">
      <description>Accuracy of intelligent command routing</description>
      <target>95%</target>
    </metric>
    <metric name="workflow_completion_rate">
      <description>Success rate of end-to-end workflow execution</description>
      <target>98%</target>
    </metric>
  </performance_metrics>

  <includes_components>
    <component>components/constitutional/safety-framework.md</component>
  </includes_components>
  
  <claude_prompt>
    <![CDATA[
You are executing the Framework Tester command. This command provides advanced functionality with comprehensive automation and intelligent processing.

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
    <focus_area>Command Discovery Validation</focus_area>
    <focus_area>Claude Code Integration Testing</focus_area>
    <focus_area>Component System Validation</focus_area>
    <focus_area>End-to-End Workflow Testing</focus_area>
    <focus_area>Performance and Efficiency Assessment</focus_area>
  </specialization_focus>
</command_file>