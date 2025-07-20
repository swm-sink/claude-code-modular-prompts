# /error trace - Error Tracing Command

**Purpose**: Trace error propagation paths and analyze error flow patterns to identify root causes and prevent recurrence.

## Usage
```bash
/error trace [--stack] [--flow] [--depth=<depth>]
```

## Workflow

The `/error trace` command follows a systematic process to trace errors.

```xml
<error_trace_workflow>
  <step name="Collect Trace Data">
    <description>Collect trace data from various sources, including stack traces, application logs, and distributed tracing systems. The depth of the trace can be controlled with the `--depth` flag.</description>
    <tool_usage>
      <tool>Log/Trace Reader</tool>
      <description>Read and parse trace data from various sources.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Trace & Build Flow Map">
    <description>Analyze the collected trace data to build a map of the error flow through the system. This involves identifying the origin of the error and tracing its propagation path across different components and services.</description>
    <tool_usage>
      <tool>Graph Analysis</tool>
      <description>Use graph analysis techniques to model and visualize the error flow.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Trace Report">
    <description>Generate a report that summarizes the error trace analysis. The report includes a visualization of the error flow, an identification of the root cause, and recommendations for preventing similar errors in the future.</description>
    <output>A detailed error trace report.</output>
  </step>
</error_trace_workflow>
```

## Configuration

The `/error trace` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/error trace">
  <setting name="default_trace_depth" value="5" description="The default depth for error traces." />
  <setting name="trace_output_format" value="diagram" description="The default format for the trace report (e.g., 'diagram', 'json')." />
</command>
```

## Use Cases

*   **Complex Bug Analysis**: Understand how errors propagate in a complex, distributed system.
*   **System Hardening**: Identify and fix weaknesses in error handling and propagation.
*   **Performance Optimization**: Analyze how error handling affects application performance.