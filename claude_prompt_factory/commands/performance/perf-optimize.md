# /perf optimize - Performance Optimization Command

**Purpose**: Apply targeted performance optimizations to improve algorithm efficiency, reduce memory usage, and enhance overall system performance.

## Usage
```bash
/perf optimize <target> [--focus=<focus>] [--safe]
```

## Workflow

The `/perf optimize` command follows a systematic process to optimize performance.

```xml
<perf_optimize_workflow>
  <step name="Profile & Analyze Bottlenecks">
    <description>First, run the `/perf profile` command to gather detailed performance data and identify the primary bottlenecks (e.g., CPU, memory, I/O).</description>
    <tool_usage>
      <tool>/perf profile</tool>
      <description>Use the performance profiling command to identify bottlenecks.</description>
    </tool_usage>
  </step>
  
  <step name="Identify & Apply Optimizations">
    <description>Based on the profiling data, identify and apply the most effective optimization techniques. The `--focus` flag can be used to target a specific area (e.g., 'cpu', 'memory'). The `--safe` flag ensures that only low-risk optimizations are applied.</description>
    <tool_usage>
      <tool>AI/Code Refactoring</tool>
      <description>Apply performance optimization patterns to the code.</description>
    </tool_usage>
  </step>
  
  <step name="Benchmark & Verify">
    <description>Run the `/perf benchmark` command to compare the before and after performance and verify that the optimizations have had the desired effect without introducing any regressions.</description>
    <tool_usage>
      <tool>/perf benchmark</tool>
      <description>Use the performance benchmark command to verify the improvements.</description>
    </tool_usage>
  </step>
</perf_optimize_workflow>
```

## Configuration

The `/perf optimize` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/perf optimize">
  <setting name="default_focus" value="auto" description="The default optimization focus (e.g., 'auto', 'cpu', 'memory')." />
  <setting name="default_optimization_level" value="safe" description="The default optimization level to apply (e.g., 'safe', 'aggressive')." />
</command>
```

## Use Cases

*   **Improving Application Speed**: Optimize critical code paths to reduce latency and improve user experience.
*   **Reducing Infrastructure Costs**: Reduce memory and CPU usage to lower hosting costs.
*   **Scaling Applications**: Proactively optimize code to handle increasing traffic and data volumes.