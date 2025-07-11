| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# /meta-govern - Governance & Compliance Framework Management

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

> **⚡ Clear Purpose**: Enforces governance policies, compliance standards, and safety boundaries across the entire framework. Provides centralized oversight and control with human authority integration.

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Comprehensive governance and compliance framework with safety enforcement, human oversight, and policy management">
  
  <delegation target="modules/meta/governance-enforcer.md">
    Compliance monitoring → Policy enforcement → Safety validation → Human oversight integration → Audit trail management → Emergency controls → Violation detection → Remediation orchestration
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Strategic governance analysis</uses_pattern>
    <uses_pattern from="patterns/validation-pattern.md">Compliance validation methodology</uses_pattern>
    <uses_pattern from="patterns/error-recovery-pattern.md">Governance failure recovery</uses_pattern>
    <uses_pattern from="patterns/session-management-pattern.md">Governance session coordination</uses_pattern>
    <uses_pattern from="patterns/quality-validation-pattern.md">Governance quality assurance</uses_pattern>
    <uses_pattern from="patterns/enforcement-verification.md">Policy enforcement verification</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Assess governance compliance and identify policy violations</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What governance policies and compliance standards need enforcement?
          - What potential violations or non-compliance issues require attention?
          - How does compliance assessment connect to policy enforcement strategy?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Policy Question: What governance policies apply to current framework operations?]
          - [Compliance Question: What compliance standards need verification and enforcement?]
          - [Violation Question: What potential violations or non-compliance issues exist?]
          - [Safety Question: Are safety boundaries being respected across all operations?]
          - [Authority Question: What human oversight requirements apply to current operations?]
          - [Audit Question: What audit trail and monitoring capabilities are needed?]
          - [Emergency Question: What emergency controls and override capabilities are required?]
          - [Remediation Question: What remediation strategies address identified violations?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this governance assessment optimal for compliance enforcement?
          - What evidence supports these policy enforcement priorities?
          - How will this analysis guide effective governance management?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
    
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Enforce governance policies with human oversight integration</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What policy enforcement mechanisms ensure compliance without disrupting operations?
          - What human oversight integration maintains ultimate authority and control?
          - How does enforcement connect to violation detection and remediation?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Enforcement Question: Are governance policies being enforced consistently and effectively?]
          - [Authority Question: Is human oversight properly integrated with ultimate authority?]
          - [Control Question: Are appropriate controls in place for different governance scenarios?]
          - [Monitoring Question: Are compliance violations being detected and addressed promptly?]
          - [Emergency Question: Are emergency controls and override mechanisms functioning?]
          - [Audit Question: Is complete audit trail being maintained for all governance actions?]
          - [Transparency Question: Are governance decisions and actions fully transparent?]
          - [Escalation Question: Are proper escalation procedures in place for violations?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this enforcement approach optimal for governance compliance?
          - What evidence supports the effectiveness of policy enforcement mechanisms?
          - How will this enforcement maintain human authority while ensuring compliance?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
    
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Monitor compliance and provide governance reporting with remediation</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What continuous monitoring ensures ongoing compliance and governance effectiveness?
          - What reporting mechanisms provide transparency and accountability?
          - How does monitoring connect to proactive remediation and improvement?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Monitoring Question: Are governance compliance metrics being tracked continuously?]
          - [Reporting Question: Are governance reports providing clear visibility and accountability?]
          - [Remediation Question: Are remediation actions being implemented effectively?]
          - [Improvement Question: Are governance processes being continuously improved?]
          - [Transparency Question: Are all governance actions and decisions fully documented?]
          - [Effectiveness Question: Are governance mechanisms achieving intended compliance outcomes?]
          - [Learning Question: Are governance learnings being integrated into framework evolution?]
          - [Proactive Question: Are potential compliance issues being identified and prevented?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this monitoring approach optimal for governance effectiveness?
          - What evidence validates the success of governance compliance management?
          - How will this monitoring ensure continuous governance improvement?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
  </thinking_pattern>
  
  <governance_policies enforcement="CRITICAL">
    <safety_boundaries>
      <immutable_zones>Core commands, core modules, quality gates, CLAUDE.md core sections</immutable_zones>
      <modification_limits>5% framework changes per week maximum</modification_limits>
      <approval_requirements>Human approval for changes affecting >2 modules</approval_requirements>
      <rollback_mandate>All changes reversible within 60 seconds</rollback_mandate>
    </safety_boundaries>
    <compliance_standards>
      <quality_gates>Universal quality gates must be maintained</quality_gates>
      <tdd_enforcement>RED→GREEN→REFACTOR cycle mandatory</tdd_enforcement>
      <security_standards>Threat modeling and security validation required</security_standards>
      <performance_standards>200ms p95 response time, 90% test coverage</performance_standards>
    </compliance_standards>
    <operational_policies>
      <file_discipline>Strict file creation and modification controls</file_discipline>
      <version_control>Temporal standards and version alignment enforcement</version_control>
      <documentation_standards>Comprehensive documentation requirements</documentation_standards>
      <testing_requirements>Mandatory testing and validation procedures</testing_requirements>
    </operational_policies>
  </governance_policies>
  
  <human_oversight_integration enforcement="MANDATORY">
    <ultimate_authority>
      <decision_override>Human decisions override all automated governance</decision_override>
      <emergency_control>Immediate human control over all framework operations</emergency_control>
      <policy_modification>Human authority to modify governance policies</policy_modification>
      <system_shutdown>Human capability to halt any framework operation</system_shutdown>
    </ultimate_authority>
    <approval_workflows>
      <automatic_approval>Single-module optimizations within safety boundaries</automatic_approval>
      <human_approval>Multi-module changes, policy modifications, safety boundary changes</human_approval>
      <escalation_procedures>Clear escalation paths for governance violations</escalation_procedures>
      <transparency_requirements>Complete visibility into all governance decisions</transparency_requirements>
    </approval_workflows>
  </human_oversight_integration>
  
  <violation_detection enforcement="MANDATORY">
    <monitoring_systems>
      <real_time_monitoring>Continuous monitoring of all framework operations</real_time_monitoring>
      <policy_compliance>Automated detection of policy violations</policy_compliance>
      <safety_boundary_violations>Immediate detection of safety boundary breaches</safety_boundary_violations>
      <performance_degradation>Monitoring for performance and stability issues</performance_degradation>
    </monitoring_systems>
    <response_procedures>
      <immediate_response>Automatic violation detection and immediate response</immediate_response>
      <escalation_protocols>Clear escalation procedures for different violation types</escalation_protocols>
      <remediation_actions>Automated remediation for standard violations</remediation_actions>
      <human_notification>Immediate human notification for critical violations</human_notification>
    </response_procedures>
  </violation_detection>
  
  <emergency_controls enforcement="CRITICAL">
    <emergency_stop>
      <immediate_halt>Capability to immediately halt all framework operations</immediate_halt>
      <human_trigger>Human-initiated emergency stop with immediate effect</human_trigger>
      <automated_trigger>Automated emergency stop for critical violations</automated_trigger>
    </emergency_stop>
    <rollback_systems>
      <sixty_second_rollback>All changes reversible within 60 seconds</sixty_second_rollback>
      <state_restoration>Complete framework state restoration capability</state_restoration>
      <data_protection>Protection of critical data during emergency operations</data_protection>
    </rollback_systems>
  </emergency_controls>
  
  <audit_trail enforcement="MANDATORY">
    <comprehensive_logging>
      <governance_actions>Complete log of all governance actions and decisions</governance_actions>
      <policy_enforcement>Detailed records of policy enforcement actions</policy_enforcement>
      <human_oversight>Complete audit trail of human oversight activities</human_oversight>
      <violation_responses>Detailed records of violation detection and responses</violation_responses>
    </comprehensive_logging>
    <transparency_reporting>
      <governance_reports>Regular governance compliance and effectiveness reports</governance_reports>
      <violation_summaries>Comprehensive summaries of violations and remediation</violation_summaries>
      <performance_metrics>Governance effectiveness and performance metrics</performance_metrics>
      <improvement_recommendations>Proactive recommendations for governance improvement</improvement_recommendations>
    </transparency_reporting>
  </audit_trail>
  
  <quality_gates enforcement="MANDATORY">
    <gate name="policy_compliance" requirement="100% compliance with governance policies">
      <validation>All operations must comply with established governance policies</validation>
      <remediation>Immediate remediation of policy violations</remediation>
    </gate>
    <gate name="safety_boundary_protection" requirement="No safety boundary violations">
      <validation>Immutable zones and safety boundaries fully protected</validation>
      <remediation>Immediate rollback and remediation of safety violations</remediation>
    </gate>
    <gate name="human_oversight_integration" requirement="Proper human authority integration">
      <validation>Human oversight properly integrated with ultimate authority</validation>
      <remediation>Enhance human oversight integration as needed</remediation>
    </gate>
    <gate name="audit_trail_completeness" requirement="Complete audit trail maintenance">
      <validation>All governance actions fully documented and traceable</validation>
      <remediation>Enhance audit trail capabilities for complete transparency</remediation>
    </gate>
  </quality_gates>
  
  <restrictions>
    <restriction>AUTHORITY: Human oversight maintains ultimate authority over all operations</restriction>
    <restriction>SAFETY: Must protect all immutable zones and safety boundaries</restriction>
    <restriction>TRANSPARENCY: All governance actions must be fully documented and traceable</restriction>
    <restriction>EMERGENCY: Emergency controls must be immediately available and functional</restriction>
  </restrictions>
</command>
```