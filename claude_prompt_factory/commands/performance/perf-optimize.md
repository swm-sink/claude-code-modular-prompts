---
description: Intelligent performance optimization with automated tuning and validation
argument-hint: "[optimization_target] [scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /perf optimize - Performance Optimization Engine

AI-powered performance optimization with automated tuning, validation, and rollback capabilities.

## Usage
```bash
/perf optimize database              # Database performance optimization
/perf optimize code --scope critical # Code optimization for critical paths
/perf optimize infrastructure       # Infrastructure performance tuning
```

<command_file>
  <metadata>
    <name>/perf optimize</name>
    <purpose>Applies targeted performance optimizations to improve efficiency and reduce memory usage.</purpose>
    <usage>
      <![CDATA[
      /perf optimize "[target_file_or_function]" <focus="cpu">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="true">
      <description>The specific file, function, or class to optimize.</description>
    </argument>
    <argument name="focus" type="string" required="false" default="cpu">
      <description>The optimization focus (e.g., 'cpu', 'memory', 'io').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Analyze and suggest CPU optimizations for a specific function.</description>
      <usage>/perf optimize "src/utils/dataProcessor.js:processLargeFile"</usage>
    </example>
    <example>
      <description>Focus on memory optimizations for a data-intensive module.</description>
      <usage>/perf optimize "src/analytics/engine.py" focus="memory"</usage>
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
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/actions/apply-code-changes.md</include>
      <include>components/performance/optimization-strategies.md</include>
      <include>components/performance/profiling-analysis.md</include>
      
      You are a performance optimization expert. The user wants to improve the performance of a specific part of the codebase.

      1.  **Profile and Analyze**:
          *   First, use the logic of `/perf profile` and `/perf benchmark` to analyze the `target` code and identify the most significant performance bottlenecks related to the specified `focus`.
      2.  **Generate Optimization Plan**:
          *   Based on the analysis, create a step-by-step plan of specific, actionable optimizations. Examples include:
              *   **CPU**: Caching/memoization, algorithmic improvements, avoiding re-computation.
              *   **Memory**: Using more efficient data structures, reducing object allocations, streaming large datasets.
              *   **I/O**: Batching operations, using asynchronous I/O, compressing data.
      3.  **Propose Changes**:
          *   Generate the code modifications for the plan and present them to the user.
      4.  **Apply and Verify**:
          *   On confirmation, apply the changes.
          *   Instruct the user to re-run the benchmark (`/perf benchmark`) to verify the improvement.
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/perf profile</command>
      <command>/perf benchmark</command>
    </chain>
    <includes_components>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>