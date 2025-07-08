| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Persona Manager Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="persona_manager" category="patterns">
  
  <purpose>
    Orchestrate persona-based agent behavior with seamless propagation through agent chains, ensuring consistent expertise and specialized thinking patterns across all agents in a session.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze request context to determine optimal persona selection</step>
    <step>2. Load and validate persona framework from .claude/personas/</step>
    <step>3. Inject persona context into command thinking patterns</step>
    <step>4. Ensure persona propagation setup for any child agents</step>
    <step>5. Track persona assignments in session management</step>
    <step>6. Apply persona-specific quality gates and validation</step>
    <step>7. Monitor persona consistency across agent interactions</step>
  </thinking_pattern>
  
  <persona_propagation_architecture>
    
    <context_injection>
      <description>Every Task() call receives comprehensive persona context</description>
      <structure>
        ```xml
        <persona_context active="{persona_name}">
          <thinking_framework>{persona_approach}</thinking_framework>
          <quality_standards>{persona_standards}</quality_standards>
          <tool_preferences>{persona_tools}</tool_preferences>
          <communication_style>{persona_communication}</communication_style>
          <error_handling>{persona_recovery}</error_handling>
          <domain_knowledge>{persona_expertise}</domain_knowledge>
        </persona_context>
        ```
      </structure>
      <propagation_rule>All child agents inherit parent persona context automatically</propagation_rule>
    </context_injection>
    
    <swarm_coordination>
      <lead_agent>Inherits command persona, coordinates specialized agents</lead_agent>
      <specialist_agents>Each receives domain-specific persona assignment</specialist_agents>
      <cross_validation>Agents review work through their persona lens</cross_validation>
      <integration_synthesis>Multi-persona perspectives synthesized in final output</integration_synthesis>
    </swarm_coordination>
    
    <session_persistence>
      <persona_tracking>GitHub sessions track active persona and agent assignments</persona_tracking>
      <decision_logging>Persona decisions and rationale logged for continuity</decision_logging>
      <adaptation_learning>Persona effectiveness tracked for optimization</adaptation_learning>
    </session_persistence>
    
  </persona_propagation_architecture>
  
  <persona_selection_logic>
    
    <auto_detection>
      <codebase_analysis>
        <rule>Security libraries detected → security-specialist</rule>
        <rule>Performance-critical patterns → performance-engineer</rule>
        <rule>Complex architecture → senior-architect</rule>
        <rule>Frontend-heavy project → frontend-expert</rule>
        <rule>API/backend focus → backend-expert</rule>
        <rule>Infrastructure/deployment → devops-expert</rule>
        <rule>Data/analytics patterns → data-expert</rule>
      </codebase_analysis>
      
      <context_switching>
        <rule>Task type determines persona within project context</rule>
        <rule>Security tasks always engage security-specialist lens</rule>
        <rule>Performance tasks always engage performance-engineer lens</rule>
        <rule>Architecture decisions always engage senior-architect lens</rule>
      </context_switching>
      
      <user_preferences>
        <rule>Learn from user's preferred persona patterns</rule>
        <rule>Adapt based on project success metrics</rule>
        <rule>Override auto-detection when explicitly specified</rule>
      </user_preferences>
    </auto_detection>
    
    <explicit_selection>
      <command_flags>
        <flag>--persona {persona_name} for single persona</flag>
        <flag>--lead-persona {lead} --agents {specialist_list} for swarm</flag>
        <flag>--auto-persona for intelligent auto-selection</flag>
      </command_flags>
      
      <validation>
        <rule>Verify persona exists in .claude/personas/</rule>
        <rule>Validate persona compatibility with command type</rule>
        <rule>Ensure persona context is complete and valid</rule>
      </validation>
    </explicit_selection>
    
  </persona_selection_logic>
  
  <agent_chain_propagation>
    
    <inheritance_mechanism>
      <parent_to_child>Child agents automatically receive parent persona context</parent_to_child>
      <context_validation>Agents verify correct persona context on initialization</context_validation>
      <behavioral_alignment>Cross-agent checks for persona consistency</behavioral_alignment>
      <state_synchronization>Persona updates propagate to all active agents</state_synchronization>
    </inheritance_mechanism>
    
    <multi_agent_coordination>
      <role_specialization>
        ```xml
        <swarm_personas>
          <lead_agent persona="senior-architect">Overall design and coordination</lead_agent>
          <specialist_agents>
            <agent persona="security-specialist">Security review and threat modeling</agent>
            <agent persona="performance-engineer">Optimization and scaling</agent>
            <agent persona="quality-advocate">Testing and standards enforcement</agent>
          </specialist_agents>
        </swarm_personas>
        ```
      </role_specialization>
      
      <cross_persona_validation>
        <rule>Security specialist reviews all agents' security implications</rule>
        <rule>Performance engineer validates all agents' performance impact</rule>
        <rule>Quality advocate ensures all agents meet testing standards</rule>
        <rule>Architect validates overall design coherence</rule>
      </cross_persona_validation>
    </multi_agent_coordination>
    
  </agent_chain_propagation>
  
  <quality_enhancement>
    
    <persona_specific_gates>
      <security_specialist>Threat modeling → Security scan → Vulnerability assessment</security_specialist>
      <performance_engineer>Benchmarking → Profiling → Optimization validation</performance_engineer>
      <senior_architect>Design review → Pattern validation → Scalability assessment</senior_architect>
      <quality_advocate>Test coverage → Code review → Standards compliance</quality_advocate>
      <product_engineer>User story validation → Business value assessment → UX review</product_engineer>
    </persona_specific_gates>
    
    <enhanced_thinking_patterns>
      <augmentation>Personas enhance existing module thinking patterns</augmentation>
      <specialization>Domain-specific approach overlays on general patterns</specialization>
      <consistency>Same persona produces consistent decisions across contexts</consistency>
    </enhanced_thinking_patterns>
    
  </quality_enhancement>
  
  <integration_points>
    <commands>Feature, Task, Swarm, Query commands enhanced with persona support</commands>
    <modules>All modules become persona-aware through context injection</modules>
    <session_management>Persona tracking integrated with GitHub session system</session_management>
    <multi_agent>Swarm coordination enhanced with persona specialization</multi_agent>
    <quality_standards>Persona-specific standards applied throughout development</quality_standards>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Persona Context Structure

```xml
<persona_context_template>
  <persona_identity>
    <name>{persona_name}</name>
    <expertise_domain>{primary_domain}</expertise_domain>
    <experience_level>{senior|expert|specialist}</experience_level>
    <perspective>{thinking_approach}</perspective>
  </persona_identity>
  
  <thinking_framework>
    <primary_lens>{main_analytical_approach}</primary_lens>
    <decision_priorities>{priority_order}</decision_priorities>
    <problem_solving_method>{methodology}</problem_solving_method>
    <trade_off_preferences>{optimization_targets}</trade_off_preferences>
  </thinking_framework>
  
  <quality_standards>
    <mandatory_gates>{required_validations}</mandatory_gates>
    <success_metrics>{measurement_criteria}</success_metrics>
    <risk_tolerance>{acceptable_risk_levels}</risk_tolerance>
    <validation_approach>{verification_methods}</validation_approach>
  </quality_standards>
  
  <tool_preferences>
    <primary_tools>{preferred_technologies}</primary_tools>
    <analysis_methods>{diagnostic_approaches}</analysis_methods>
    <automation_focus>{automation_priorities}</automation_focus>
    <documentation_style>{communication_preferences}</documentation_style>
  </tool_preferences>
  
  <collaboration_patterns>
    <communication_style>{interaction_approach}</communication_style>
    <knowledge_sharing>{expertise_transfer_method}</knowledge_sharing>
    <conflict_resolution>{disagreement_handling}</conflict_resolution>
    <mentoring_approach>{guidance_style}</mentoring_approach>
  </collaboration_patterns>
  
  <domain_knowledge>
    <core_expertise>{specialized_knowledge}</core_expertise>
    <adjacent_domains>{related_knowledge_areas}</adjacent_domains>
    <blind_spots>{known_limitations}</blind_spots>
    <learning_priorities>{skill_development_focus}</learning_priorities>
  </domain_knowledge>
  
</persona_context_template>
```

────────────────────────────────────────────────────────────────────────────────

## Usage Examples

```xml
<usage_patterns>
  
  <single_agent_enhancement>
    <command>/feature "payment system" --persona security-specialist</command>
    <result>Security-first architecture with threat modeling throughout</result>
  </single_agent_enhancement>
  
  <multi_agent_coordination>
    <command>/swarm "full-stack app" --lead-persona senior-architect --agents "frontend-expert,backend-expert,devops-expert"</command>
    <result>Coordinated development with specialized expertise per domain</result>
  </multi_agent_coordination>
  
  <auto_detection>
    <command>/task "optimize database queries" --auto-persona</command>
    <result>Automatically selects performance-engineer persona based on task type</result>
  </auto_detection>
  
  <context_switching>
    <scenario>Security review within architecture project</scenario>
    <behavior>Temporarily adopts security-specialist lens while maintaining architectural context</behavior>
  </context_switching>
  
</usage_patterns>
```

────────────────────────────────────────────────────────────────────────────────

## Implementation Protocol

```xml
<implementation_steps>
  
  <persona_loading>
    <step>1. Parse command for persona specifications</step>
    <step>2. Load persona framework from .claude/personas/</step>
    <step>3. Validate persona context completeness</step>
    <step>4. Prepare context injection for agent chain</step>
  </persona_loading>
  
  <context_injection>
    <step>1. Inject persona context into command thinking pattern</step>
    <step>2. Enhance module delegation with persona awareness</step>
    <step>3. Configure quality gates for persona-specific standards</step>
    <step>4. Set up propagation for any child agents</step>
  </context_injection>
  
  <agent_coordination>
    <step>1. Assign personas to specialist agents in swarm scenarios</step>
    <step>2. Establish cross-persona validation protocols</step>
    <step>3. Configure knowledge sharing between agents</step>
    <step>4. Set up conflict resolution mechanisms</step>
  </agent_coordination>
  
  <session_tracking>
    <step>1. Log persona assignments in GitHub session</step>
    <step>2. Track persona decisions and rationale</step>
    <step>3. Monitor persona effectiveness metrics</step>
    <step>4. Update persona adaptation learning</step>
  </session_tracking>
  
</implementation_steps>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Core orchestration module for persona-enhanced agent behavior. Used by all commands for specialized expertise injection and agent chain consistency.