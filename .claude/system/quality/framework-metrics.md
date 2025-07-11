| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Framework Metrics Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="framework_metrics" category="quality">
  
  <purpose>
    Framework-specific quality metrics that measure the effectiveness of the modular command-module architecture and Claude Code integration patterns.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Collect framework-specific usage and performance data</step>
    <step>2. Analyze command delegation success patterns</step>
    <step>3. Measure module composition effectiveness</step>
    <step>4. Evaluate session management and context preservation</step>
    <step>5. Assess thinking pattern adherence and outcomes</step>
    <step>6. Calculate framework evolution and adaptation metrics</step>
    <step>7. Generate improvement recommendations specific to framework architecture</step>
    <step>8. Track user satisfaction and productivity impact</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="automatic">Framework usage analysis, command effectiveness evaluation</condition>
    <condition type="explicit">User requests framework performance assessment or optimization</condition>
  </trigger_conditions>
  
  <implementation>
    
    <framework_specific_metrics>
      
      <command_effectiveness_metrics>
        <metric name="command_delegation_success_rate" target=">95%">
          <description>Percentage of commands that successfully delegate to appropriate modules</description>
          <measurement>
            (Successful delegations / Total command invocations) * 100
            Success = Command finds correct module + Module executes thinking pattern + Desired outcome achieved
          </measurement>
          <failure_indicators>
            <indicator>Command routes to wrong module</indicator>
            <indicator>Module fails to execute thinking pattern</indicator>
            <indicator>User must manually correct or retry</indicator>
            <indicator>Session escalation required due to command failure</indicator>
          </failure_indicators>
        </metric>
        
        <metric name="command_routing_accuracy" target=">98%">
          <description>Accuracy of intelligent command routing based on request analysis</description>
          <measurement>
            (Correctly routed commands / Total routing decisions) * 100
            Correct = Command matches user intent without requiring re-routing
          </measurement>
          <quality_factors>
            <factor>Request complexity analysis accuracy</factor>
            <factor>Context-aware routing decisions</factor>
            <factor>Learning from past routing successes/failures</factor>
          </quality_factors>
        </metric>
        
        <metric name="thinking_pattern_adherence" target=">95%">
          <description>Commands and modules follow prescribed thinking patterns</description>
          <measurement>
            (Pattern steps executed correctly / Total required pattern steps) * 100
            Includes verification of step order, completeness, and quality
          </measurement>
          <compliance_checks>
            <check>All mandatory thinking steps executed in sequence</check>
            <check>Evidence of critical thinking and assumption challenging</check>
            <check>Proper module delegation and integration</check>
            <check>Quality gates applied appropriately</check>
          </compliance_checks>
        </metric>
        
        <metric name="command_completion_efficiency" target="<2_iterations">
          <description>Average iterations required to complete user requests</description>
          <measurement>
            Sum(command iterations per request) / Total requests
            Iteration = Any command invocation or manual correction needed
          </measurement>
          <efficiency_factors>
            <factor>First-time-right execution rate</factor>
            <factor>Error recovery speed</factor>
            <factor>User clarification requirements</factor>
            <factor>Context preservation across interactions</factor>
          </efficiency_factors>
        </metric>
      </command_effectiveness_metrics>
      
      <module_composition_metrics>
        <metric name="module_coupling_coefficient" target="<0.2">
          <description>Measure of inappropriate dependencies between modules</description>
          <measurement>
            (Cross-module dependencies / Total possible module pairs)
            Only count dependencies that violate isolation principles
          </measurement>
          <coupling_violations>
            <violation>Direct state sharing between modules</violation>
            <violation>Hardcoded module references</violation>
            <violation>Circular dependencies</violation>
            <violation>Shared mutable state</violation>
          </coupling_violations>
        </metric>
        
        <metric name="module_cohesion_score" target=">0.8">
          <description>Internal consistency and single-responsibility adherence</description>
          <measurement>
            Average cohesion score across all modules
            Module cohesion = (Related functionality / Total functionality)
          </measurement>
          <cohesion_factors>
            <factor>Single responsibility principle adherence</factor>
            <factor>Related functionality grouping</factor>
            <factor>Clear module purpose and boundaries</factor>
            <factor>Minimal external interface surface</factor>
          </cohesion_factors>
        </metric>
        
        <metric name="pattern_reusability_index" target=">0.75">
          <description>How effectively patterns are reused across modules</description>
          <measurement>
            (Reused patterns / Total patterns defined) * Pattern usage frequency
            Higher score indicates better pattern abstraction and adoption
          </measurement>
          <reusability_indicators>
            <indicator>Pattern usage across multiple modules</indicator>
            <indicator>Pattern composition effectiveness</indicator>
            <indicator>Pattern evolution and versioning success</indicator>
            <indicator>New pattern creation vs reuse ratio</indicator>
          </reusability_indicators>
        </metric>
        
        <metric name="interface_stability_score" target=">0.9">
          <description>Stability of module interfaces over time</description>
          <measurement>
            (Unchanged interfaces / Total interfaces) over rolling 30-day window
            Breaking changes reduce score more than additive changes
          </measurement>
          <stability_factors>
            <factor>Backward compatibility maintenance</factor>
            <factor>Breaking change frequency</factor>
            <factor>Interface versioning effectiveness</factor>
            <factor>Migration path quality</factor>
          </stability_factors>
        </metric>
      </module_composition_metrics>
      
      <session_management_metrics>
        <metric name="context_preservation_rate" target=">95%">
          <description>How well context is maintained across session boundaries</description>
          <measurement>
            (Sessions with full context recovery / Total session resumptions) * 100
            Full recovery = User can continue without re-explaining context
          </measurement>
          <context_elements>
            <element>Previous decisions and rationale</element>
            <element>Work-in-progress state</element>
            <element>Quality gate status</element>
            <element>Architectural choices</element>
            <element>Error recovery state</element>
          </context_elements>
        </metric>
        
        <metric name="session_completion_rate" target=">90%">
          <description>Percentage of sessions that achieve their stated objectives</description>
          <measurement>
            (Successfully completed sessions / Total sessions created) * 100
            Success = All acceptance criteria met and session properly closed
          </measurement>
          <completion_factors>
            <factor>Clear objective definition at session start</factor>
            <factor>Progress tracking throughout session</factor>
            <factor>Quality gate compliance</factor>
            <factor>Proper session closure with documentation</factor>
          </completion_factors>
        </metric>
        
        <metric name="session_efficiency_score" target=">0.8">
          <description>Ratio of value-adding activities vs overhead in sessions</description>
          <measurement>
            (Productive session time / Total session time)
            Productive = Direct work on objectives, not setup/recovery
          </measurement>
          <efficiency_drains>
            <drain>Context reconstruction time</drain>
            <drain>Session setup overhead</drain>
            <drain>Tool switching or manual processes</drain>
            <drain>Error recovery and debugging time</drain>
          </efficiency_drains>
        </metric>
        
        <metric name="cross_session_knowledge_transfer" target=">0.85">
          <description>How well lessons learned propagate across sessions</description>
          <measurement>
            (Applied lessons from previous sessions / Applicable lesson opportunities)
            Measures learning and improvement over time
          </measurement>
          <knowledge_transfer_indicators>
            <indicator>Pattern improvements applied retroactively</indicator>
            <indicator>Error prevention based on past failures</indicator>
            <indicator>Best practice adoption across teams</indicator>
            <indicator>Documentation quality improvements</indicator>
          </knowledge_transfer_indicators>
        </metric>
      </session_management_metrics>
      
      <framework_evolution_metrics>
        <metric name="adaptation_velocity" target="<7_days">
          <description>Time from identifying improvement opportunity to implementation</description>
          <measurement>
            Average(Implementation date - Identification date) for framework improvements
            Tracks how quickly framework evolves to meet changing needs
          </measurement>
          <velocity_factors>
            <factor>Change impact assessment speed</factor>
            <factor>Backward compatibility verification time</factor>
            <factor>Testing and validation duration</factor>
            <factor>Deployment and rollout efficiency</factor>
          </velocity_factors>
        </metric>
        
        <metric name="user_adoption_rate" target=">80%">
          <description>Percentage of eligible users actively using framework features</description>
          <measurement>
            (Active framework users / Total eligible users) * 100
            Active = Regular usage of commands and modules
          </measurement>
          <adoption_barriers>
            <barrier>Learning curve complexity</barrier>
            <barrier>Integration friction with existing workflows</barrier>
            <barrier>Performance or reliability issues</barrier>
            <barrier>Limited perceived value vs alternatives</barrier>
          </adoption_barriers>
        </metric>
        
        <metric name="framework_health_index" target=">0.85">
          <description>Composite measure of framework sustainability and growth</description>
          <measurement>
            Weighted average of: code quality (30%), user satisfaction (25%), 
            feature velocity (20%), technical debt (15%), community engagement (10%)
          </measurement>
          <health_indicators>
            <indicator>Code quality trend over time</indicator>
            <indicator>User satisfaction and retention rates</indicator>
            <indicator>Feature development velocity</indicator>
            <indicator>Technical debt accumulation rate</indicator>
            <indicator>Community contributions and engagement</indicator>
          </health_indicators>
        </metric>
        
        <metric name="quality_gate_effectiveness" target=">0.9">
          <description>How well quality gates prevent defects and improve outcomes</description>
          <measurement>
            (Defects prevented / Total potential defects) based on gate enforcement
            Measured through retrospective analysis of gate bypasses vs outcomes
          </measurement>
          <gate_effectiveness_factors>
            <factor>Gate coverage of critical quality dimensions</factor>
            <factor>False positive rate (unnecessary blocks)</factor>
            <factor>False negative rate (missed issues)</factor>
            <factor>Time cost vs quality benefit ratio</factor>
          </gate_effectiveness_factors>
        </metric>
      </framework_evolution_metrics>
      
    </framework_specific_metrics>
    
    <measurement_infrastructure>
      <data_collection>
        <automated_telemetry>
          <event>Command invocations with routing decisions</event>
          <event>Module execution patterns and completion status</event>
          <event>Session lifecycle events and context transitions</event>
          <event>Quality gate results and enforcement actions</event>
          <event>Error occurrences and recovery patterns</event>
        </automated_telemetry>
        
        <user_feedback_mechanisms>
          <mechanism>Post-command completion satisfaction surveys</mechanism>
          <mechanism>Session retrospective feedback collection</mechanism>
          <mechanism>Framework usability testing sessions</mechanism>
          <mechanism>Feature request and improvement suggestion tracking</mechanism>
        </user_feedback_mechanisms>
        
        <code_analysis_integration>
          <analysis>Static analysis of module coupling and cohesion</analysis>
          <analysis>Pattern usage mining from codebase history</analysis>
          <analysis>Interface stability tracking over time</analysis>
          <analysis>Technical debt accumulation measurement</analysis>
        </code_analysis_integration>
      </data_collection>
      
      <analytics_processing>
        <real_time_dashboards>
          <dashboard>Command effectiveness and routing accuracy trends</dashboard>
          <dashboard>Module composition health and evolution</dashboard>
          <dashboard>Session management efficiency metrics</dashboard>
          <dashboard>Framework adoption and user satisfaction</dashboard>
        </real_time_dashboards>
        
        <predictive_analytics>
          <prediction>Framework quality degradation early warning</prediction>
          <prediction>User adoption bottleneck identification</prediction>
          <prediction>Module refactoring necessity prediction</prediction>
          <prediction>Session complexity and success probability</prediction>
        </predictive_analytics>
        
        <comparative_analysis>
          <comparison>Historical performance trends and regression detection</comparison>
          <comparison>Cross-team framework usage pattern analysis</comparison>
          <comparison>Feature effectiveness before/after comparisons</comparison>
          <comparison>Framework metrics vs external quality benchmarks</comparison>
        </comparative_analysis>
      </analytics_processing>
    </measurement_infrastructure>
    
    <improvement_recommendations>
      <automated_recommendations>
        <trigger condition="command_delegation_success_rate < 95%">
          <action>Analyze routing failures and update command patterns</action>
          <action>Improve module interface clarity and documentation</action>
          <action>Enhance user feedback for failed delegations</action>
        </trigger>
        
        <trigger condition="module_coupling_coefficient > 0.2">
          <action>Identify and refactor problematic inter-module dependencies</action>
          <action>Create interface abstractions to reduce coupling</action>
          <action>Update module isolation guidelines and enforcement</action>
        </trigger>
        
        <trigger condition="context_preservation_rate < 95%">
          <action>Enhance session state serialization mechanisms</action>
          <action>Improve context reconstruction algorithms</action>
          <action>Add validation for context completeness</action>
        </trigger>
        
        <trigger condition="user_adoption_rate < 80%">
          <action>Conduct user experience research to identify barriers</action>
          <action>Develop targeted onboarding and training materials</action>
          <action>Simplify most common use cases and workflows</action>
        </trigger>
      </automated_recommendations>
      
      <continuous_optimization>
        <optimization_cycle>
          <phase>Monthly metric collection and analysis</phase>
          <phase>Quarterly framework health assessment</phase>
          <phase>Semi-annual user satisfaction survey</phase>
          <phase>Annual framework architecture review</phase>
        </optimization_cycle>
        
        <feedback_integration>
          <integration>User feedback directly influences metric weightings</integration>
          <integration>Performance data drives automatic framework tuning</integration>
          <integration>Quality trends trigger proactive improvement initiatives</integration>
          <integration>Competitive analysis updates target benchmarks</integration>
        </feedback_integration>
      </continuous_optimization>
    </improvement_recommendations>
    
  </implementation>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for session lifecycle tracking
      quality/production-standards.md for general quality gate integration
      development/task-management.md for command execution patterns
      patterns/intelligent-routing.md for routing effectiveness analysis
    </depends_on>
    <provides_to>
      quality/production-standards.md for framework-specific quality gates
      patterns/pattern-library.md for pattern effectiveness metrics
      development/prompt-engineering.md for prompt quality measurement
      All commands for framework effectiveness feedback
    </provides_to>
  </integration_points>
  
</module>
```