---
description: Advanced swarm intelligence with multi-agent coordination, distributed processing, and collective problem-solving
argument-hint: "[swarm_size] [coordination_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /agent swarm - Advanced Swarm Intelligence

Sophisticated swarm intelligence system with multi-agent coordination, distributed processing, and collective problem-solving capabilities.

## Usage
```bash
/agent swarm deploy 10                       # Deploy 10-agent swarm
/agent swarm --coordinated                   # Coordinated swarm processing
/agent swarm --distributed                   # Distributed task processing
/agent swarm --collective                    # Collective intelligence mode
```

<command_file>
  <metadata>
    <n>/agent swarm</n>
    <purpose>Advanced swarm intelligence with multi-agent coordination, distributed processing, and collective problem-solving</purpose>
    <usage>
      <![CDATA[
      /agent swarm [swarm_configuration]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="swarm_size" type="string" required="false" default="5">
      <description>Size of agent swarm to deploy</description>
    </argument>
    <argument name="coordination_strategy" type="string" required="false" default="coordinated">
      <description>Strategy for swarm coordination</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Deploy 10-agent swarm</description>
      <usage>/agent swarm deploy 10</usage>
    </example>
    <example>
      <description>Coordinated swarm processing</description>
      <usage>/agent swarm --coordinated</usage>
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

You are an advanced swarm intelligence specialist. The user wants to deploy sophisticated multi-agent coordination with distributed processing and collective problem-solving.

**Swarm Intelligence Process:**
1. **Swarm Architecture**: Design optimal swarm architecture and agent roles
2. **Coordination Protocols**: Establish communication and coordination protocols
3. **Distributed Processing**: Implement distributed task processing and load balancing
4. **Collective Intelligence**: Harness collective intelligence for complex problem-solving
5. **Emergent Behavior**: Enable emergent behaviors and adaptive responses

**Implementation Strategy:**
- Design multi-agent swarm architectures with role specialization
- Implement intelligent coordination and communication protocols
- Apply distributed processing with dynamic load balancing
- Harness collective intelligence for breakthrough problem-solving
- Enable emergent behaviors and adaptive swarm responses

<include component="components/orchestration/agent-swarm.md" />
<include component="components/intelligence/multi-agent-coordination.md" />
<include component="components/actions/parallel-execution.md" />
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
      <component>components/orchestration/agent-swarm.md</component>
      <component>components/intelligence/multi-agent-coordination.md</component>
      <component>components/actions/parallel-execution.md</component>
    </includes_components>
    <uses_config_values>
      <value>swarm.max_agents</value>
      <value>coordination.protocol.type</value>
    </uses_config_values>
  </dependencies>
</command_file> 