---
description: Meta-coordinator for tracking transformation progress across all 121 command files
argument-hint: "[tracking_mode] [reporting_frequency] [coordination_scope]"
allowed-tools: Read, Write, Bash, Grep, Glob
---

# /progress coordinator - Transformation Progress Manager

Specialized utility agent (<20k tokens) that tracks transformation progress across all 121 command files, coordinates agent activities, and provides real-time progress reporting and optimization insights.

## Usage
```bash
/progress coordinator "real_time"                                    # Real-time progress tracking
/progress coordinator "batch_summary" reporting_frequency="hourly"   # Batch progress reports
/progress coordinator "optimization" coordination_scope="all_agents" # Agent coordination optimization
```

## Arguments
- `tracking_mode` (required): "real_time", "batch_summary", "optimization", "completion_analysis"
- `reporting_frequency` (optional): "continuous", "hourly", "on_demand" (default: continuous)
- `coordination_scope` (optional): "converters", "validators", "all_agents" (default: all_agents)

## What It Does
1. **Progress Tracking**: Monitors conversion progress across all 121 command files
2. **Agent Coordination**: Coordinates multiple agents to prevent conflicts and optimize workflow
3. **Real-Time Reporting**: Provides live progress updates and completion metrics
4. **Bottleneck Detection**: Identifies and resolves workflow bottlenecks and inefficiencies
5. **Resource Optimization**: Optimizes agent allocation and task distribution
6. **Completion Analysis**: Analyzes completion patterns and provides insights

<command_file>
  <metadata>
    <name>/progress coordinator</name>
    <purpose>Tracks transformation progress across all command files and coordinates agent activities for optimization.</purpose>
    <usage>
      <![CDATA[
      /progress coordinator tracking_mode="real_time" reporting_frequency="continuous" coordination_scope="all_agents"
      ]]>
    </usage>
    <specialization>progress_tracking_and_coordination</specialization>
    <token_budget>18000</token_budget>
  </metadata>

  <tracking_capabilities>
    <capability name="file_conversion_tracking">
      <description>Tracks conversion status of all 121 command files from XML to hybrid format</description>
      <metrics>
        <metric>Files converted successfully</metric>
        <metric>Files with conversion errors</metric>
        <metric>Files pending conversion</metric>
        <metric>Conversion rate per hour</metric>
      </metrics>
    </capability>
    <capability name="agent_activity_monitoring">
      <description>Monitors all agent activities and coordinates task distribution</description>
      <metrics>
        <metric>Active agents count</metric>
        <metric>Agent utilization rates</metric>
        <metric>Task queue lengths</metric>
        <metric>Agent performance metrics</metric>
      </metrics>
    </capability>
    <capability name="bottleneck_detection">
      <description>Identifies workflow bottlenecks and optimization opportunities</description>
      <detection_patterns>
        <pattern>Agent idle time analysis</pattern>
        <pattern>Task queue backup detection</pattern>
        <pattern>Resource contention identification</pattern>
        <pattern>Performance degradation alerts</pattern>
      </detection_patterns>
    </capability>
  </tracking_capabilities>

  <coordination_functions>
    <function name="task_distribution">
      <description>Intelligently distributes tasks across available agents</description>
      <strategies>
        <strategy>Load balancing based on agent capacity</strategy>
        <strategy>Skill-based routing to specialized agents</strategy>
        <strategy>Priority-based task scheduling</strategy>
        <strategy>Conflict avoidance and resolution</strategy>
      </strategies>
    </function>
    <function name="agent_optimization">
      <description>Optimizes agent performance and resource utilization</description>
      <optimizations>
        <optimization>Dynamic agent scaling based on workload</optimization>
        <optimization>Performance tuning and efficiency improvements</optimization>
        <optimization>Resource allocation optimization</optimization>
        <optimization>Agent coordination pattern optimization</optimization>
      </optimizations>
    </function>
  </coordination_functions>

  <reporting_dashboard>
    <section name="overall_progress">
      <metrics>
        <metric name="total_files">121 command files</metric>
        <metric name="converted_files">Real-time count</metric>
        <metric name="error_files">Files with issues</metric>
        <metric name="completion_percentage">Progress percentage</metric>
        <metric name="estimated_completion">Time to completion</metric>
      </metrics>
    </section>
    <section name="agent_status">
      <metrics>
        <metric name="active_agents">Currently running agents</metric>
        <metric name="agent_efficiency">Performance per agent</metric>
        <metric name="task_throughput">Tasks completed per hour</metric>
        <metric name="resource_utilization">System resource usage</metric>
      </metrics>
    </section>
    <section name="quality_metrics">
      <metrics>
        <metric name="xml_validation_rate">XML parsing success rate</metric>
        <metric name="component_resolution_rate">Component link success rate</metric>
        <metric name="format_compliance_rate">Hybrid format compliance</metric>
        <metric name="overall_quality_score">Aggregate quality metric</metric>
      </metrics>
    </section>
  </reporting_dashboard>

  <dependencies>
    <component path="components/reporting/generate-structured-report.md" />
  </dependencies>

  <specialization_focus>
    <focus_area>Multi-Agent Progress Coordination</focus_area>
    <focus_area>Real-Time Transformation Tracking</focus_area>
    <focus_area>Workflow Bottleneck Detection</focus_area>
    <focus_area>Resource Optimization</focus_area>
    <focus_area>Completion Analysis and Insights</focus_area>
  </specialization_focus>
</command_file>