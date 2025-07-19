# /meta - Unified Meta-Framework Command

```xml
<meta_command version="3.0.0" type="unified_routing">
  <purpose>Unified meta-framework operations with intelligent routing to specialized capabilities</purpose>
  
  <command_signature>/meta [operation] [context]</command_signature>
  
  <operations>
    <review>
      <usage>/meta review "audit framework compliance"</usage>
      <routes_to>@.claude/modules/meta/framework-auditor.md</routes_to>
      <purpose>Comprehensive framework audit and validation</purpose>
    </review>
    
    <optimize>
      <usage>/meta optimize "improve token efficiency"</usage>
      <routes_to>@.claude/modules/meta/continuous-optimizer.md</routes_to>
      <purpose>Performance enhancement and optimization</purpose>
    </optimize>
    
    <evolve>
      <usage>/meta evolve "adapt to new patterns"</usage>
      <routes_to>@.claude/modules/meta/update-cycle-manager.md</routes_to>
      <purpose>Intelligent framework evolution</purpose>
    </evolve>
    
    <govern>
      <usage>/meta govern "enforce quality standards"</usage>
      <routes_to>@.claude/modules/meta/governance-enforcer.md</routes_to>
      <purpose>Governance and compliance enforcement</purpose>
    </govern>
    
    <fix>
      <usage>/meta fix "TDD not followed"</usage>
      <routes_to>@.claude/modules/meta/compliance-diagnostics.md</routes_to>
      <purpose>Compliance issue diagnosis and correction</purpose>
    </fix>
    
    <auto>
      <usage>/meta "analyze and improve framework"</usage>
      <routes_to>@.claude/meta/meta-prompting-orchestration.md</routes_to>
      <purpose>Intelligent routing to optimal meta-operation</purpose>
    </auto>
  </operations>
  
  <routing_intelligence>
    <context_analysis>Analyze user input to determine optimal meta-operation</context_analysis>
    <capability_matching>Match request to most appropriate meta-module</capability_matching>
    <safety_validation>Ensure all operations respect safety boundaries</safety_validation>
  </routing_intelligence>
  
  <safety_framework>
    <canonical_source>@.claude/meta/meta-framework-control.md</canonical_source>
    <boundaries>5% weekly limit | Human approval | 60s rollback | 99.9% stability</boundaries>
    <oversight>Ultimate human authority | Emergency override | Full transparency</oversight>
  </safety_framework>
  
  <execution_workflow>
    <step order="1">Parse operation and context from user input</step>
    <step order="2">Route to appropriate meta-module for implementation</step>
    <step order="3">Execute with safety boundaries and monitoring</step>
    <step order="4">Report results with actionable recommendations</step>
    <step order="5">Update learning data for future optimization</step>
  </execution_workflow>
  
  <integration_points>
    <framework_control>@.claude/meta/meta-framework-control.md</framework_control>
    <meta_modules>@.claude/modules/meta/</meta_modules>
    <quality_gates>@.claude/system/quality/universal-quality-gates.md</quality_gates>
    <atomic_rollback>@.claude/system/git/atomic-rollback-protocol.md</atomic_rollback>
  </integration_points>
</meta_command>
```