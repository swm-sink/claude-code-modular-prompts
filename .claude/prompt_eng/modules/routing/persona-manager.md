| version | last_updated | status |
|---------|--------------|--------|
| 1.1.0   | 2025-07-11   | stable |

# Persona Manager Module

────────────────────────────────────────────────────────────────────────────────


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
        <!-- Mobile Engineering R&D -->
        <rule>iOS/Swift projects → ios-engineer</rule>
        <rule>Android/Kotlin projects → android-engineer</rule>
        <rule>React Native/Flutter projects → cross-platform-mobile-engineer</rule>
        <rule>Xcode/Android Studio configs → mobile engineering lead</rule>
        <rule>App Store/Play Store configs → mobile engineering lead</rule>
        
        <!-- Platform & Infrastructure Engineering -->
        <rule>Kubernetes/Docker patterns → platform-engineer</rule>
        <rule>CI/CD pipelines → devops-engineer</rule>
        <rule>SLO/monitoring patterns → site-reliability-engineer</rule>
        <rule>AWS/GCP/Azure → cloud-engineer</rule>
        <rule>Infrastructure as Code → platform-engineer</rule>
        <rule>Developer platform tools → platform-engineer</rule>
        <rule>Service mesh configurations → platform-engineer</rule>
        
        <!-- Data & Analytics Engineering -->
        <rule>Data pipelines/ETL → data-engineer</rule>
        <rule>BI/dashboards → analytics-engineer</rule>
        <rule>ML/AI models → ml-engineer</rule>
        <rule>Data warehouses/lakes → data-engineer</rule>
        <rule>Analytics platforms → analytics-engineer</rule>
        <rule>Machine learning pipelines → ml-engineer</rule>
        
        <!-- Backend & API Engineering -->
        <rule>API/backend focus → backend-engineer</rule>
        <rule>Microservices architecture → api-engineer</rule>
        <rule>GraphQL/REST APIs → api-engineer</rule>
        <rule>Database schemas → backend-engineer</rule>
        <rule>Message queues → backend-engineer</rule>
        <rule>Service-oriented architecture → api-engineer</rule>
        
        <!-- Frontend Engineering -->
        <rule>Frontend-heavy project → frontend-engineer</rule>
        <rule>React/Vue/Angular projects → frontend-engineer</rule>
        <rule>UI/UX components → frontend-engineer</rule>
        <rule>Web performance optimization → frontend-engineer</rule>
        
        <!-- Security Engineering -->
        <rule>Security libraries detected → security-engineer</rule>
        <rule>Authentication/authorization → security-engineer</rule>
        <rule>Cryptography implementations → security-engineer</rule>
        <rule>Security scanning tools → security-engineer</rule>
        
        <!-- Quality & Testing Engineering -->
        <rule>Test automation frameworks → test-engineer</rule>
        <rule>Performance testing → test-engineer</rule>
        <rule>Quality assurance → test-engineer</rule>
        <rule>Test coverage tools → test-engineer</rule>
        
        <!-- Research & Innovation -->
        <rule>Experimental code → research-engineer</rule>
        <rule>Prototype development → research-engineer</rule>
        <rule>Research publications → research-engineer</rule>
        <rule>Innovation projects → research-engineer</rule>
        
        <!-- Architecture & Leadership -->
        <rule>Complex architecture → technical-architect</rule>
        <rule>System design docs → technical-architect</rule>
        <rule>Team management → engineering-manager</rule>
        <rule>Strategic planning → engineering-manager</rule>
        
        <!-- Legacy compatibility -->
        <rule>Performance-critical patterns → performance-engineer</rule>
        <rule>Senior architecture → senior-architect</rule>
        <rule>Frontend-expert → frontend-engineer</rule>
        <rule>Backend-expert → backend-engineer</rule>
        <rule>DevOps-expert → devops-engineer</rule>
        <rule>Data-expert → data-engineer</rule>
      </codebase_analysis>
      
      <context_switching>
        <rule>Task type determines persona within project context</rule>
        <rule>Security tasks always engage security-engineer lens</rule>
        <rule>Performance tasks always engage performance-engineer lens</rule>
        <rule>Architecture decisions always engage technical-architect lens</rule>
        <rule>Mobile app development → mobile engineering personas (ios-engineer, android-engineer, cross-platform-mobile-engineer)</rule>
        <rule>Infrastructure tasks → platform/devops/SRE personas (platform-engineer, devops-engineer, site-reliability-engineer, cloud-engineer)</rule>
        <rule>Data processing tasks → data/analytics engineering personas (data-engineer, analytics-engineer, ml-engineer)</rule>
        <rule>API development → api-engineer persona</rule>
        <rule>Backend development → backend-engineer persona</rule>
        <rule>Frontend development → frontend-engineer persona</rule>
        <rule>Testing and QA → test-engineer persona</rule>
        <rule>Research and innovation → research-engineer persona</rule>
        <rule>Team management → engineering-manager persona</rule>
        <rule>Legacy compatibility → senior-architect, performance-engineer, security-specialist</rule>
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
      <!-- Mobile Engineering R&D -->
      <ios_engineer>App Store guidelines → Performance profiling → Accessibility testing</ios_engineer>
      <android_engineer>Play Store compliance → Device testing → Material Design validation</android_engineer>
      <cross_platform_mobile_engineer>Platform parity → Performance consistency → Code reuse optimization</cross_platform_mobile_engineer>
      
      <!-- Platform & Infrastructure Engineering -->
      <platform_engineer>Developer experience → Self-service validation → Infrastructure automation</platform_engineer>
      <devops_engineer>CI/CD pipeline → Deployment automation → Monitoring coverage</devops_engineer>
      <site_reliability_engineer>SLO compliance → Error budget → Incident response</site_reliability_engineer>
      <cloud_engineer>Cost optimization → Security compliance → Performance benchmarking</cloud_engineer>
      
      <!-- Data & Analytics Engineering -->
      <data_engineer>Data quality → Pipeline reliability → Performance optimization</data_engineer>
      <analytics_engineer>Business validation → Data accuracy → User adoption metrics</analytics_engineer>
      <ml_engineer>Model validation → Bias assessment → Production monitoring</ml_engineer>
      
      <!-- Backend & API Engineering -->
      <backend_engineer>API design → Performance benchmarking → Database optimization</backend_engineer>
      <api_engineer>API contract validation → Performance testing → Developer experience</api_engineer>
      
      <!-- Frontend Engineering -->
      <frontend_engineer>UI/UX validation → Performance optimization → Accessibility compliance</frontend_engineer>
      
      <!-- Security Engineering -->
      <security_engineer>Threat modeling → Security scan → Vulnerability assessment</security_engineer>
      
      <!-- Quality & Testing Engineering -->
      <test_engineer>Test coverage → Automation validation → Performance testing</test_engineer>
      
      <!-- Research & Innovation -->
      <research_engineer>Research validation → Prototype testing → Innovation assessment</research_engineer>
      
      <!-- Architecture & Leadership -->
      <technical_architect>Design review → Pattern validation → Scalability assessment</technical_architect>
      <engineering_manager>Team performance → Strategic alignment → Process optimization</engineering_manager>
      
      <!-- Legacy compatibility -->
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