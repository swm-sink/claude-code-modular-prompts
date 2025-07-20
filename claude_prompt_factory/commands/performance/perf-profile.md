# /perf profile - Performance Profiling Command

**Purpose**: Conduct deep performance profiling to identify bottlenecks, hotspots, and resource usage patterns in the code.

## Usage
```bash
/perf profile <target> [--type=<type>] [--depth=<depth>] [--flamegraph]
```

## Workflow

The `/perf profile` command follows a systematic process to profile code.

```xml
<perf_profile_workflow>
  <step name="Initialize & Attach Profiler">
    <description>Initialize the appropriate profiler (e.g., CPU, memory, I/O) and attach it to the target process or application. The type of profiling can be specified with the `--type` flag.</description>
    <tool_usage>
      <tool>Profiler Tool</tool>
      <description>Use a language-specific profiler (e.g., cProfile for Python, V8 profiler for Node.js).</description>
    </tool_usage>
  </step>
  
  <step name="Collect Performance Samples">
    <description>Run the target code and collect performance samples over a specified duration. The `--depth` flag can control the stack depth of the collected samples.</description>
    <tool_usage>
      <tool>Profiler Tool</tool>
      <description>Collect performance data while the code is running.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Hotspots & Generate Visualizations">
    <description>Analyze the collected samples to identify performance hotspots, memory leaks, and other bottlenecks. If the `--flamegraph` flag is used, generate a flame graph visualization to make the data easier to understand.</description>
    <tool_usage>
      <tool>Analysis & Visualization Tools</tool>
      <description>Use tools to analyze the profiling data and generate visualizations.</description>
    </tool_usage>
  </step>
</perf_profile_workflow>
```

## Configuration

The `/perf profile` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/perf profile">
  <setting name="default_profiling_type" value="cpu" description="The default type of profiling to perform." />
  <setting name="default_sampling_rate" value="100" description="The default sampling rate in Hz." />
</command>
```

## Use Cases

*   **Identifying Performance Bottlenecks**: Pinpoint the exact lines of code that are causing performance issues.
*   **Memory Leak Detection**: Analyze memory usage patterns to identify and fix memory leaks.
*   **Optimizing Resource Usage**: Understand how the application is using resources like CPU and I/O to optimize its performance.