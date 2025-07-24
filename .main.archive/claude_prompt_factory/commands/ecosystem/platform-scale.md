---
description: Advanced platform scaling with ecosystem orchestration, network effects optimization, and community governance
argument-hint: "[scaling_strategy] [platform_type]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /ecosystem platform-scale - Advanced Platform Scaling

Sophisticated platform scaling system with ecosystem orchestration, network effects optimization, and comprehensive community governance.

## Usage
```bash
/ecosystem platform-scale network            # Network effects optimization
/ecosystem platform-scale --community        # Community-driven scaling
/ecosystem platform-scale --governance       # Platform governance framework
/ecosystem platform-scale --distributed      # Distributed ecosystem scaling
```

<command_file>
  <metadata>
    <n>/ecosystem platform-scale</n>
    <purpose>Advanced platform scaling with ecosystem orchestration, network effects optimization, and community governance</purpose>
    <usage>
      <![CDATA[
      /ecosystem platform-scale [scaling_strategy]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="scaling_strategy" type="string" required="false" default="network">
      <description>Platform scaling strategy to implement</description>
    </argument>
    <argument name="platform_type" type="string" required="false" default="marketplace">
      <description>Type of platform to scale</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Network effects optimization</description>
      <usage>/ecosystem platform-scale network --marketplace</usage>
    </example>
    <example>
      <description>Community-driven scaling</description>
      <usage>/ecosystem platform-scale --community --social</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are a platform scaling specialist. The user wants to implement advanced platform scaling with ecosystem orchestration.

**Analysis Process:**
1. **Ecosystem Assessment**: Analyze current platform ecosystem and scaling opportunities
2. **Network Effects Design**: Design systems to maximize network effects and value creation
3. **Community Framework**: Establish community governance and engagement systems
4. **Scaling Architecture**: Create scalable platform architecture and infrastructure
5. **Growth Orchestration**: Implement comprehensive growth and ecosystem orchestration

**Implementation Strategy:**
- Design multi-sided platform architectures with network effects
- Implement community governance frameworks and participation incentives
- Create ecosystem partner programs and API strategies
- Establish platform monetization and value distribution models
- Design scalable infrastructure with microservices and federation
- Implement analytics and growth measurement systems

<include component="components/orchestration/agent-orchestration.md" />
<include component="components/community/community-platform.md" />
<include component="components/analytics/business-intelligence.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/orchestration/agent-orchestration.md</component>
      <component>components/community/community-platform.md</component>
      <component>components/analytics/business-intelligence.md</component>
    </includes_components>
    <uses_config_values>
      <value>ecosystem.scaling.network_effects</value>
      <value>platform.governance.community</value>
    </uses_config_values>
  </dependencies>
</command_file> 