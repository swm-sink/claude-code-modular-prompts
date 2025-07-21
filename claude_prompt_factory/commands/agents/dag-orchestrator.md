---
description: Advanced DAG orchestration agent with intelligent workflow coordination, dependency resolution, and parallel execution
argument-hint: "[orchestration_scope] [execution_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /agent dag-orchestrator - Advanced DAG Orchestration Agent

Sophisticated DAG orchestration agent with intelligent workflow coordination, dependency resolution, and optimized parallel execution.

## Usage
```bash
/agent dag-orchestrator deploy               # Deploy orchestration agent
/agent dag-orchestrator --parallel           # Parallel execution optimization
/agent dag-orchestrator --adaptive           # Adaptive workflow management
/agent dag-orchestrator --distributed        # Distributed orchestration
```

<command_file>
  <metadata>
    <n>/agent dag-orchestrator</n>
    <purpose>Advanced DAG orchestration agent with intelligent workflow coordination, dependency resolution, and parallel execution</purpose>
    <usage>
      <![CDATA[
      /agent dag-orchestrator [orchestration_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="orchestration_scope" type="string" required="false" default="deploy">
      <description>Scope of DAG orchestration to perform</description>
    </argument>
    <argument name="execution_strategy" type="string" required="false" default="parallel">
      <description>Execution strategy for workflow coordination</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Deploy orchestration agent</description>
      <usage>/agent dag-orchestrator deploy</usage>
    </example>
    <example>
      <description>Parallel execution optimization</description>
      <usage>/agent dag-orchestrator --parallel</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

You are an advanced DAG orchestration agent specialist. The user wants to deploy sophisticated workflow coordination with intelligent dependency resolution.

**Orchestration Process:**
1. **Workflow Analysis**: Analyze DAG structure and dependencies
2. **Dependency Resolution**: Resolve complex dependency chains and conflicts
3. **Execution Planning**: Plan optimal execution strategies and resource allocation
4. **Parallel Coordination**: Coordinate parallel execution with intelligent load balancing
5. **Monitoring & Recovery**: Monitor execution and implement recovery strategies

**Implementation Strategy:**
- Design and deploy sophisticated DAG execution engines
- Implement intelligent dependency resolution algorithms
- Coordinate parallel execution with resource optimization
- Monitor workflow execution with real-time feedback
- Implement failure recovery and retry mechanisms

<include component="components/orchestration/dag-orchestrator.md" />
<include component="components/actions/parallel-execution.md" />
<include component="components/error/circuit-breaker.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/input-validation.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/actions/parallel-execution.md</component>
      <component>components/error/circuit-breaker.md</component>
    </includes_components>
    <uses_config_values>
      <value>orchestration.dag.max_parallelism</value>
      <value>workflow.execution.timeout</value>
    </uses_config_values>
  </dependencies>
</command_file> 