---
description: Intelligent workflow scheduling with automated trigger management, dynamic resource allocation, and comprehensive dependency resolution
argument-hint: "[schedule_type] [workflow_name]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /flow schedule - Intelligent Workflow Scheduling

Advanced workflow scheduling system with automated trigger management, dynamic resource allocation, and comprehensive dependency resolution for complex flows.

## Usage
```bash
/flow schedule daily "My ETL Workflow"        # Schedule a workflow to run daily
/flow schedule --cron "0 0 * * *" "My Backup Job" # Schedule a workflow using a cron expression
/flow schedule --event "new_file_uploaded" "Image Processing" # Schedule on a specific event
```

<command_file>
  <metadata>
    <n>/flow schedule</n>
    <purpose>Intelligent workflow scheduling with automated trigger management, dynamic resource allocation, and comprehensive dependency resolution</purpose>
    <usage>
      <![CDATA[
      /flow schedule [schedule_type] "[workflow_name]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="schedule_type" type="string" required="true" default="daily">
      <description>The type of schedule (e.g., daily, hourly, cron, event)</description>
    </argument>
    <argument name="workflow_name" type="string" required="true">
      <description>The name of the workflow to schedule</description>
    </argument>
    <argument name="cron_expression" type="string" required="false">
      <description>Cron expression if schedule_type is 'cron'</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Schedule a workflow to run daily</description>
      <usage>/flow schedule daily "Data Ingestion Workflow"</usage>
    </example>
    <example>
      <description>Schedule a workflow using a cron expression</description>
      <usage>/flow schedule --cron "0 0 * * *" "Nightly Report Generation"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced workflow scheduling specialist. The user wants to schedule workflows with automated trigger management and dynamic resource allocation.

**Scheduling Process:**
1. **Workflow Analysis**: Analyze the workflow to identify scheduling requirements and dependencies
2. **Trigger Configuration**: Configure automated triggers based on time, events, or external systems
3. **Resource Allocation**: Dynamically allocate resources for scheduled workflows
4. **Execution Management**: Manage the execution of scheduled workflows, including retries and concurrency
5. **Monitoring & Reporting**: Monitor scheduled workflows and provide comprehensive reports

**Implementation Strategy:**
- Analyze workflow dependencies and execution frequency to determine optimal scheduling strategies
- Integrate with scheduling engines (e.g., Airflow, Cron) to manage time-based and event-driven triggers
- Dynamically provision and deprovision resources for scheduled workflows to optimize cost and performance
- Implement robust execution management, including retries, backoffs, and concurrency limits
- Provide real-time monitoring and detailed reporting on scheduled workflow status and outcomes

<include component="components/orchestration/dag-orchestrator.md" />
<include component="components/performance/auto-scaling.md" />
<include component="components/workflow/flow-schedule.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/performance/auto-scaling.md</component>
      <component>components/workflow/flow-schedule.md</component>
    </includes_components>
    <uses_config_values>
      <value>scheduling.default_timezone</value>
      <value>scheduling.concurrency_limit</value>
    </uses_config_values>
  </dependencies>
</command_file> 