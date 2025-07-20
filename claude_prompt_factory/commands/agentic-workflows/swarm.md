# /swarm - Multi-Agent Swarm Intelligence

**Purpose**: Coordinate a swarm of specialized AI agents to collaboratively solve complex problems.

## Usage
```bash
/swarm "[problem description]"
```

## Workflow

The `/swarm` command follows a systematic process to coordinate a multi-agent swarm.

```xml
<swarm_workflow>
  <step name="Decompose Problem">
    <description>Decompose the complex problem into a set of smaller, more manageable sub-tasks that can be assigned to specialized agents.</description>
  </step>
  
  <step name="Select & Configure Agents">
    <description>Select a team of specialized AI agents, each with the skills and tools needed to solve a specific sub-task. The agents will be configured with a shared context and a clear set of objectives.</description>
  </step>
  
  <step name="Execute in Parallel">
    <description>The agents will work in parallel on their assigned sub-tasks, communicating and collaborating as needed to solve the problem.</description>
  </step>
  
  <step name="Synthesize Results">
    <description>A coordinator agent will monitor the progress of the swarm, synthesize the results from each agent, and assemble the final solution.</description>
  </step>
</swarm_workflow>
```

## Agent Specializations

The `/swarm` command can leverage a variety of specialized agents, including:

*   **Architect**: Designs the high-level structure of the system.
*   **Developer**: Writes the code for individual components.
*   **Tester**: Creates and runs tests to verify the code.
*   **Security Analyst**: Scans for vulnerabilities and hardens the system.
*   **Performance Optimizer**: Analyzes and improves the performance of the system.
*   **Documentation Writer**: Creates clear and comprehensive documentation.

## Use Cases

*   **Rapid Prototyping**: Quickly build a working prototype of a new application.
*   **Complex System Design**: Design and implement a complex, multi-component system.
*   **Parallelized Problem Solving**: Solve a complex problem by breaking it down into smaller pieces and assigning them to a team of specialized agents. 