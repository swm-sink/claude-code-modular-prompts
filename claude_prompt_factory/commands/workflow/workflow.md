---
description: Advanced workflow orchestration with intelligent automation, dynamic adaptation, and comprehensive process management
argument-hint: "[workflow_type] [orchestration_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /workflow - Advanced Workflow Orchestration

Sophisticated workflow orchestration system with intelligent automation, dynamic adaptation, and comprehensive process management.

## Usage
```bash
/workflow create                             # Create advanced workflow
/workflow --automated                        # Automated workflow execution
/workflow --adaptive                         # Adaptive workflow management
/workflow --comprehensive                    # Comprehensive workflow orchestration
```

## Core Concepts

This command provides a powerful orchestration engine that can execute different types of workflows.

```xml
<workflow_concepts>
  <concept name="Chain">
    <description>A sequence of steps that are executed in order. Supports parallel execution of independent steps.</description>
    <keywords>sequence, chain, series</keywords>
  </concept>
  <concept name="Flow">
    <description>A workflow with conditional logic (if/then/else) that can adapt its execution path based on the results of previous steps.</description>
    <keywords>conditional, if/then, flow, decision</keywords>
  </concept>
  <concept name="Swarm">
    <description>A multi-agent workflow where different "agents" (specialized instances of the LLM) work together to solve a complex problem. This is ideal for tasks that require different areas of expertise.</description>
    <keywords>multi-agent, swarm, team, coordinate</keywords>
  </concept>
  <concept name="Pipeline">
    <description>A continuous workflow that processes a stream of data through a series of stages. Ideal for data processing and CI/CD-style workflows.</description>
    <keywords>pipeline, stream, data processing</keywords>
  </concept>
</workflow_concepts>
```

## Workflow Definition Syntax

Workflows are defined using a simple YAML or XML format.

### Chain Workflow Example
```yaml
type: chain
name: Security Audit Workflow
parallel_where_possible: true
steps:
  - name: analyze_codebase
    command: /query
    params: "analyze Python security vulnerabilities"
  - name: fix_issues
    command: /task
    params: "fix security issues found in the analysis"
    depends_on: [analyze_codebase]
  - name: validate_fixes
    command: /test
    params: "run all security tests"
    depends_on: [fix_issues]
```

### Swarm Workflow Example
```yaml
type: swarm
name: Complex Feature Implementation
topology: hierarchical
agents:
  coordinator:
    role: "Task decomposition and synthesis"
    capabilities: [planning, coordination]
  security_specialist:
    role: "Security analysis specialist"
    tools: [/security scan, /query "security patterns"]
  performance_specialist:
    role: "Performance optimization specialist"
    tools: [/perf analyze, /perf optimize]
```

## Orchestration Logic

When you execute a workflow, I will act as the orchestrator, following this process:

```xml
<orchestration_logic>
  <step name="Parse Workflow">
    <description>Parse the workflow definition file (YAML or XML) to understand the steps, dependencies, and logic.</description>
  </step>
  
  <step name="Build Execution Graph (DAG)">
    <description>Construct a Directed Acyclic Graph (DAG) of the workflow steps based on the `depends_on` attributes. This will determine the execution order and identify opportunities for parallel execution.</description>
  </step>
  
  <step name="Execute Graph">
    <description>Execute the workflow by traversing the graph. I will execute all steps with no dependencies in parallel, and then move on to the next set of steps as their dependencies are met.</description>
    <tool_usage>
      <tool>Parallel Command Execution</tool>
      <description>Use parallel execution to run multiple commands at the same time.</description>
    </tool_usage>
  </step>
  
  <step name="Handle Logic & State">
    <description>For `flow` workflows, I will evaluate the conditions at each decision point and take the appropriate path. For `swarm` workflows, I will coordinate the different agents and synthesize their results. I will also manage the state of the workflow and provide it as context to subsequent steps.</description>
  </step>
  
  <step name="Monitor & Report">
    <description>Monitor the progress of the workflow, provide real-time updates, and generate a final report with the results of each step.</description>
  </step>
  <step name="Abort Workflow">
    <description>Safely abort a running workflow, capturing its current state, saving a progress checkpoint, and performing necessary cleanup tasks. This step can be triggered manually or automatically upon critical failure.</description>
    <safety_protocol>graceful_shutdown</safety_protocol>
    <abort_sequence>
      <action>Stop active operations.</action>
      <action>Rollback incomplete changes (if applicable).</action>
      <action>Release resources.</action>
      <action>Update workflow status to aborted.</action>
    </abort_sequence>
    <recovery_options>
      <option name="resume_point">Last successful checkpoint.</option>
      <option name="partial_results">Preserved for analysis.</option>
    </recovery_options>
  </step>
</orchestration_logic>
```

## Monitoring & Analytics

The `/workflow` command provides robust monitoring and analytics capabilities to give you real-time insights into your workflow execution.

### Real-time Metrics
- **Progress Indicators**: Step completion status and overall workflow progress.
- **Token Usage**: Track token consumption with real-time cost projections.
- **Execution Time**: Monitor elapsed time and estimated completion.
- **Resource Utilization**: Track API calls and memory usage.
- **Performance Anomalies**: Detect deviations from baseline execution times.

### Alerting
- **Failure Detection**: Immediate alerts on workflow failures or timeouts.
- **Cost Thresholds**: Alerts when projected costs exceed predefined limits.
- **Performance Degradation**: Notifications if execution time significantly increases.
- **Resource Exhaustion**: Warnings for high resource usage.

### Reporting
- **Comprehensive Output**: Detailed summary of workflow execution, including all metrics and any alerts.
- **Historical Data**: Track trends over time for continuous optimization.

```xml
<monitoring_capabilities>
  <metrics>
    <metric name="progress_percentage" description="Percentage of workflow completed."/>
    <metric name="elapsed_time" description="Time elapsed since workflow start."/>
    <metric name="estimated_completion" description="Estimated time remaining until workflow completion."/>
    <metric name="tokens_used" description="Total tokens consumed during workflow execution."/>
    <metric name="current_cost" description="Current estimated cost of workflow execution."/>
  </metrics>
  <alerts>
    <alert type="failure" description="Triggered on any step failure or workflow timeout."/>
    <alert type="cost_exceeded" description="Triggered if projected cost exceeds a configured threshold."/>
    <alert type="performance_degradation" description="Triggered if step execution time is significantly above baseline."/>
  </alerts>
</monitoring_capabilities>
```

This powerful, prompt-driven orchestration engine replaces the need for a complex, coded solution, making it a true "Claude Code Native" command. 