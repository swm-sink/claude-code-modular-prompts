---
name: /workflow
description: [DEPRECATED] Intelligent workflow management with automated task execution, dynamic resource allocation, and comprehensive progress tracking - use /project workflow instead
argument-hint: "[workflow_name] [action]"
allowed-tools: Read, Write, Edit, Bash, Grep
test_coverage: 0%
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/project workflow"
reason: "Consolidated into unified /project command for better consistency and cross-mode integration"
removal_date: "2025-08-25"
---
# ⚠️ DEPRECATED: /workflow

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Please use `/project workflow` instead:**
```
# Old command:
/workflow start "My Development Workflow"

# New command:
/project workflow start "My Development Workflow"
```

The new unified `/project` command provides:
- ✅ All legacy workflow functionality in workflow mode
- ✅ Enhanced cross-mode integration with setup, provisioning, and tracking
- ✅ Improved state management and progress reporting
- ✅ Better error handling and recovery mechanisms
- ✅ Unified configuration and monitoring across all project operations

---

# /workflow - Intelligent Workflow Management
Advanced workflow management system with automated task execution, dynamic resource allocation, and comprehensive progress tracking.
## Usage
```bash
/workflow start "My Development Workflow"   # Start a new workflow
/workflow --pause "My Deployment Workflow" # Pause a running workflow
/workflow --status "All Workflows"         # Get the status of all workflows
/workflow --log "My CI/CD Workflow"        # View logs for a specific workflow
```
<command_file>
  <metadata>
    <n>/workflow</n>
    <purpose>Intelligent workflow management with automated task execution, dynamic resource allocation, and comprehensive progress tracking</purpose>
    <usage>
      <![CDATA[
      /workflow [action] "[workflow_name]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="action" type="string" required="true" default="start">
      <description>The action to perform on the workflow (e.g., start, pause, resume, stop, status, log)</description>
    </argument>
    <argument name="workflow_name" type="string" required="true">
      <description>The name of the workflow to manage</description>
    </argument>
    <argument name="resource_allocation" type="string" required="false" default="dynamic">
      <description>Strategy for resource allocation (e.g., static, dynamic)</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Start a new development workflow</description>
      <usage>/workflow start "Feature Branch Development"</usage>
    </example>
    <example>
      <description>Get the status of all running workflows</description>
      <usage>/workflow --status "All running workflows"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced workflow management specialist. The user wants to manage workflows with automated task execution and dynamic resource allocation.
**Workflow Management Process:**
1. **Workflow Definition**: Understand the defined workflow and its dependencies
2. **Task Execution**: Automate the execution of tasks within the workflow
3. **Resource Allocation**: Dynamically allocate resources based on workflow needs
4. **Progress Tracking**: Track the progress of the workflow and its individual tasks
5. **Error Handling**: Implement robust error handling and recovery mechanisms
**Implementation Strategy:**
- Parse workflow definitions (e.g., DAGs, sequential steps) to understand task dependencies and execution order
- Automate task execution, integrating with various tools and services as needed
- Dynamically allocate and deallocate compute, memory, and storage resources based on real-time workflow demands
- Implement comprehensive progress tracking and visualization, providing real-time updates to the user
- Design robust error handling and retry mechanisms to ensure workflow resilience and completion
<include component="components/orchestration/dag-orchestrator.md" />
<include component="components/performance/auto-scaling.md" />
<include component="components/interaction/progress-reporting.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/performance/auto-scaling.md</component>
      <component>components/interaction/progress-reporting.md</component>
    </includes_components>
    <uses_config_values>
      <value>workflow.default_executor</value>
      <value>resource.dynamic_allocation.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file>
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