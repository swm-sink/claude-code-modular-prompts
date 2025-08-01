---
description: Performance benchmarking with comprehensive metrics collection and analysis
argument-hint: "[benchmark_type] [duration]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /perf benchmark - Performance Benchmarking System

Advanced benchmarking system with load testing, metrics collection, and performance analysis.

## Usage
```bash
/perf benchmark api                  # API performance benchmarking
/perf benchmark database            # Database performance testing
/perf benchmark full --duration 5m  # Complete system benchmark for 5 minutes
```

<command_file>
  <metadata>
    <name>/perf benchmark</name>
    <purpose>Runs comprehensive performance benchmarks to measure and compare implementations.</purpose>
    <usage>
      <![CDATA[
      /perf benchmark "[target_file_or_function]" <compare_to_branch="main">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="true">
      <description>The specific file, function, or class to benchmark.</description>
    </argument>
    <argument name="compare_to" type="string" required="false" default="main">
      <description>The git branch to compare the performance results against.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Benchmark the main 'processData' function and compare its performance against the 'main' branch.</description>
      <usage>/perf benchmark "src/utils/processing.js:processData"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/performance/benchmark-harness.md</include>
      <include>components/analysis/performance-metrics.md</include>
      <include>components/testing/load-testing.md</include>
      <include>components/visualization/performance-charts.md</include>
      
      You are a performance engineer. The user wants to run a benchmark.

      1.  **Identify Target**: Locate the `target` file or function to be benchmarked.
      2.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to find the project's benchmarking tool and configuration.
      3.  **Generate Benchmark Harness**:
          *   Create a new benchmark test file.
          *   Write the necessary setup code to run the target function within the benchmark tool's harness.
          *   Include scenarios for different data sizes (e.g., small, medium, large) to get a comprehensive profile.
      4.  **Execute Benchmarks**:
          *   Run the benchmark for the current code.
          *   If `compare_to` is provided, switch to that branch and run the same benchmark to establish a baseline.
      5.  **Generate Report**:
          *   Create a detailed report comparing the performance.
          *   Highlight any significant regressions or improvements in execution time, memory usage, etc.
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>performance.benchmark_tool</value>
      <value>performance.benchmark_scenarios</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>