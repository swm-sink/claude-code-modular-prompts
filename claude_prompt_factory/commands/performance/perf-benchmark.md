# /perf benchmark - Performance Benchmarking Command

**Purpose**: Run comprehensive performance benchmarks to measure and compare the performance of different implementations across various scenarios.

## Usage
```bash
/perf benchmark <target> [--scenarios=<scenarios>] [--compare]
```

## Workflow

The `/perf benchmark` command follows a systematic process to benchmark code.

```xml
<perf_benchmark_workflow>
  <step name="Setup Benchmark Environment & Scenarios">
    <description>Set up an isolated environment for benchmarking to ensure consistent and reliable results. Load the test scenarios, which can be specified with the `--scenarios` flag (e.g., 'small,medium,large').</description>
    <tool_usage>
      <tool>Benchmarking Tool</tool>
      <description>Use a language-specific benchmarking library (e.g., benchmark.js for Node.js, pytest-benchmark for Python).</description>
    </tool_usage>
  </step>
  
  <step name="Execute Benchmarks & Collect Metrics">
    <description>Execute the benchmarks for each scenario, running the target code a specified number of times to get statistically significant results. Collect key performance metrics, such as execution time, memory usage, and CPU utilization.</description>
    <tool_usage>
      <tool>Benchmarking Tool</tool>
      <description>Run the benchmarks and collect performance data.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Results & Generate Report">
    <description>Analyze the collected metrics to understand the performance characteristics of the code. If the `--compare` flag is used, compare the results against a baseline or previous run. Generate a report that summarizes the findings and highlights any performance regressions.</description>
    <output>A detailed performance benchmark report.</output>
  </step>
</perf_benchmark_workflow>
```

## Configuration

The `/perf benchmark` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/perf benchmark">
  <setting name="default_scenarios" value="small,medium,large" description="The default scenarios to use for benchmarking." />
  <setting name="default_iterations" value="1000" description="The default number of iterations to run for each benchmark." />
</command>
```

## Use Cases

*   **Comparing Implementations**: Objectively compare the performance of different algorithms or implementations.
*   **Preventing Performance Regressions**: Integrate benchmarking into the CI/CD pipeline to automatically detect and prevent performance regressions.
*   **Capacity Planning**: Use benchmark results to understand how the application will perform under different load conditions.