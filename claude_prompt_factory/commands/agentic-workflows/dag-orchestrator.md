# /dag-orchestrator - Adaptive DAG-Based Agent Orchestration

**Purpose**: Execute complex, adaptive, DAG-based agentic workflows that follow a sophisticated cycle of exploration, research, synthesis, planning, and implementation.

## Usage
```bash
/dag-orchestrator "[high-level goal]"
```

## Workflow Cycle

The `/dag-orchestrator` follows a recursive, adaptive cycle for each node in the execution graph. This cycle is designed to ensure a deep, thorough, and well-planned execution of complex tasks.

```xml
<dag_orchestration_cycle>
  <step name="Explore">
    <description>Explore the problem space to understand the context, identify the key challenges, and define the scope of the task.</description>
  </step>
  <step name="Research">
    <description>Conduct targeted research to gather information, identify best practices, and explore potential solutions.</description>
  </step>
  <step name="Synthesize">
    <description>Synthesize the results of the exploration and research phases into a coherent understanding of the problem and a set of potential solutions.</description>
  </step>
  <step name="Outline">
    <description>Create a high-level outline of the proposed solution, including the key components and their interactions.</description>
  </step>
  <step name="Critique">
    <description>Critically evaluate the proposed outline, identifying potential weaknesses, risks, and areas for improvement.</description>
  </step>
  <step name="Plan">
    <description>Develop a detailed, atomic plan for implementing the solution, breaking the work down into small, manageable tasks.</description>
  </step>
  <step name="Implement">
    <description>Execute the implementation plan, with each atomic task being handled by a specialized agent.</description>
  </step>
  <step name="Check">
    <description>Verify that the implementation meets the requirements and that the task has been successfully completed.</description>
  </step>
  <step name="Commit">
    <description>Commit the changes to the codebase, with a clear and descriptive commit message.</description>
  </step>
  <step name="Continue">
    <description>Proceed to the next node in the DAG, adapting the plan as needed based on the results of the current node.</description>
  </step>
</dag_orchestration_cycle>
```

## Adaptive Orchestration

The `/dag-orchestrator` is designed to be adaptive. It will:

*   **Dynamically Adjust the DAG**: The orchestrator can add, remove, or modify nodes in the DAG based on the results of the execution.
*   **Learn from Experience**: The orchestrator will learn from its successes and failures, improving its performance over time.
*   **Request Help When Needed**: If the orchestrator encounters a problem it cannot solve, it will ask for help from the user.

## Use Cases

*   **Complex Feature Development**: Orchestrate the development of a complex new feature, from initial design to final implementation.
*   **Large-Scale Refactoring**: Manage a large-scale refactoring of a legacy codebase, ensuring that the work is done safely and efficiently.
*   **Greenfield Project Development**: Guide the development of a new project from scratch, ensuring that it is well-designed and well-engineered. 