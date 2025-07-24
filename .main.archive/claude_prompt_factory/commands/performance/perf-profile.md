---
description: Application profiling with detailed performance analysis and bottleneck identification
argument-hint: "[profile_type] [depth_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /perf profile - Application Profiler

Advanced application profiler with memory tracking, CPU analysis, and bottleneck identification.

## Usage
```bash
/perf profile cpu                    # CPU usage profiling
/perf profile memory --deep          # Deep memory profiling
/perf profile full --duration 30s    # Complete profile for 30 seconds
```

<command_file>
  <metadata>
    <name>/perf profile</name>
    <purpose>Conducts deep performance profiling to identify bottlenecks, hotspots, and resource usage patterns.</purpose>
    <usage>
      <![CDATA[
      /perf profile "[target_file_or_function]" <type="cpu">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="true">
      <description>The specific file, function, or class to profile.</description>
    </argument>
    <argument name="type" type="string" required="false" default="cpu">
      <description>The type of profiling to perform (e.g., 'cpu', 'memory').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Run a CPU profile on a specific data processing function.</description>
      <usage>/perf profile "src/utils/dataProcessor.js:processLargeFile"</usage>
    </example>
    <example>
      <description>Run a memory profile on an analytics engine.</description>
      <usage>/perf profile "src/analytics/engine.py" type="memory"</usage>
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
      <include>components/performance/profiling-tools.md</include>
      <include>components/analysis/bottleneck-detection.md</include>
      <include>components/visualization/flame-graphs.md</include>
      <include>components/analysis/memory-leak-detection.md</include>
      
      You are a performance engineer. The user wants to profile a specific part of the code.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the project's configured profiling tool.
      2.  **Generate Profiling Script**:
          *   Create a script that initializes the appropriate profiler (CPU or memory).
          *   The script should attach the profiler to the `target` code and execute it.
      3.  **Execute and Collect Data**:
          *   Present the profiling script to the user and, on confirmation, execute it to collect performance samples.
      4.  **Analyze and Report**:
          *   Analyze the collected profiling data to identify performance hotspots and bottlenecks.
          *   Generate a report that includes:
              *   A summary of the most time-consuming function calls (for CPU profiling).
              *   An analysis of memory allocation and potential leaks (for memory profiling).
              *   A flame graph visualization for intuitive analysis.
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>performance.profiling_tool</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>