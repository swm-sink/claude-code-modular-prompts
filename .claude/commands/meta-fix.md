| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-16   | stable |

# /meta-fix - Compliance Issue Diagnosis & Self-Correction

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

> **⚡ Clear Purpose**: Diagnoses and fixes compliance issues like TDD violations, date usage errors, and framework non-compliance. Provides root cause analysis and self-correction capabilities.

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Intelligent compliance issue diagnosis and self-correction with root cause analysis and prevention strategies">
  
  <delegation target="modules/meta/compliance-diagnostics.md">
    Issue analysis → Root cause identification → Compliance gap assessment → Corrective action planning → Implementation execution → Validation testing → Prevention strategy deployment
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Deep issue analysis and root cause identification</uses_pattern>
    <uses_pattern from="patterns/error-recovery-pattern.md">Systematic error correction and recovery</uses_pattern>
    <uses_pattern from="patterns/validation-pattern.md">Comprehensive validation of corrections</uses_pattern>
    <uses_pattern from="patterns/quality-validation-pattern.md">Quality assurance for corrections</uses_pattern>
    <uses_pattern from="patterns/tdd-cycle-pattern.md">TDD compliance analysis and correction</uses_pattern>
    <uses_pattern from="patterns/performance-optimization-pattern.md">Parallel diagnostic operations</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Analyze reported compliance issue and identify root causes</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What specific compliance issue or error needs diagnosis and correction?
          - What framework standards or procedures were violated?
          - How does issue analysis connect to root cause identification?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Issue Question: What specific compliance violation or error occurred?]
          - [Context Question: What framework standards or procedures should have been followed?]
          - [Root Cause Question: What underlying factors led to this compliance failure?]
          - [Pattern Question: Is this a recurring issue or isolated incident?]
          - [Impact Question: What are the consequences of this compliance violation?]
          - [Prevention Question: What could have prevented this issue from occurring?]
          - [Systemic Question: Does this indicate a broader framework compliance problem?]
          - [Correction Question: What specific corrective actions are needed?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this root cause analysis optimal for understanding the compliance issue?
          - What evidence supports this diagnosis of the compliance failure?
          - How will this analysis guide effective corrective action?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
    
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Develop and validate corrective action plan with compliance verification</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What corrective actions address the root causes identified?
          - What validation ensures corrections meet framework standards?
          - How does correction planning connect to prevention strategy?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Correction Question: What specific actions will correct the identified compliance issue?]
          - [Standards Question: How do corrective actions align with framework standards?]
          - [Validation Question: What validation ensures corrections are effective?]
          - [Quality Question: How do corrections meet quality gate requirements?]
          - [Safety Question: Are corrective actions safe and within framework boundaries?]
          - [Prevention Question: What prevention strategies avoid similar issues?]
          - [Integration Question: How do corrections integrate with existing framework?]
          - [Effectiveness Question: What measures validate correction effectiveness?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this corrective action plan optimal for addressing the compliance issue?
          - What evidence supports the effectiveness of these corrections?
          - How will this approach prevent similar issues in the future?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
    
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Execute corrections with validation and deploy prevention strategies</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What execution approach ensures safe and effective correction implementation?
          - What validation confirms corrections meet compliance standards?
          - How does execution connect to prevention strategy deployment?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Execution Question: Are corrections being implemented safely and effectively?]
          - [Validation Question: Are corrections meeting expected compliance standards?]
          - [Quality Question: Are corrections passing all quality gates?]
          - [Integration Question: Are corrections integrating properly with framework?]
          - [Prevention Question: Are prevention strategies being deployed effectively?]
          - [Monitoring Question: Are correction results being monitored for effectiveness?]
          - [Learning Question: Are lessons learned being integrated into framework?]
          - [Sustainability Question: Are corrections sustainable and maintainable?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this execution approach optimal for safe and effective correction?
          - What evidence validates the success of corrective actions?
          - How will this approach ensure long-term compliance improvement?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
  </thinking_pattern>
  
  <compliance_diagnostics enforcement="MANDATORY">
    <common_issues>
      <tdd_violations>
        <issue>TDD cycle not followed (RED→GREEN→REFACTOR)</issue>
        <diagnosis>Analyze why TDD process was bypassed or incorrectly implemented</diagnosis>
        <correction>Implement proper TDD cycle with test-first approach</correction>
        <prevention>Enforce TDD quality gates and validation checkpoints</prevention>
      </tdd_violations>
      
      <temporal_standards_violations>
        <issue>Current date not used (2025-07-11 required)</issue>
        <diagnosis>Identify why system date generation was not used</diagnosis>
        <correction>Update to current date using $(date '+%Y-%m-%d') format</correction>
        <prevention>Enforce temporal standards validation in all operations</prevention>
      </temporal_standards_violations>
      
      <quality_gate_failures>
        <issue>Quality gates not passed or enforced</issue>
        <diagnosis>Analyze which quality gates failed and why</diagnosis>
        <correction>Address quality gate failures and ensure compliance</correction>
        <prevention>Strengthen quality gate enforcement and monitoring</prevention>
      </quality_gate_failures>
      
      <pattern_integration_failures>
        <issue>Pattern integration missing or incorrect</issue>
        <diagnosis>Identify missing or improperly integrated patterns</diagnosis>
        <correction>Implement proper pattern integration per framework standards</correction>
        <prevention>Validate pattern integration in all components</prevention>
      </pattern_integration_failures>
    </common_issues>
    
    <framework_compliance_analysis>
      <structure_violations>
        <xml_structure>Non-compliant XML structure in commands or modules</xml_structure>
        <thinking_patterns>Missing or incorrect thinking pattern implementation</thinking_patterns>
        <version_tables>Incorrect version table format or outdated versions</version_tables>
        <documentation_standards>Non-compliant documentation format or content</documentation_standards>
      </structure_violations>
      
      <behavioral_violations>
        <safety_boundary_violations>Actions that violate framework safety boundaries</safety_boundary_violations>
        <approval_process_bypasses>Bypassing required human approval processes</approval_process_bypasses>
        <rollback_capability_missing>Missing rollback capability for changes</rollback_capability_missing>
        <monitoring_gaps>Inadequate monitoring or validation of operations</monitoring_gaps>
      </behavioral_violations>
      
      <performance_violations>
        <response_time_failures>Operations exceeding response time requirements</response_time_failures>
        <resource_inefficiency>Inefficient resource usage or waste</resource_inefficiency>
        <parallel_execution_missed>Missed opportunities for parallel execution</parallel_execution_missed>
        <optimization_gaps>Missed optimization opportunities</optimization_gaps>
      </performance_violations>
    </framework_compliance_analysis>
  </compliance_diagnostics>
  
  <self_correction_capabilities enforcement="MANDATORY">
    <automated_corrections>
      <date_corrections>
        <current_date_update>Automatically update to current date (2025-07-11)</current_date_update>
        <temporal_format_correction>Fix temporal format to YYYY-MM-DD standard</temporal_format_correction>
        <version_table_update>Update version tables with current date</version_table_update>
      </date_corrections>
      
      <structure_corrections>
        <xml_structure_fix>Correct XML structure violations automatically</xml_structure_fix>
        <pattern_integration_fix>Add missing pattern integrations</pattern_integration_fix>
        <thinking_pattern_addition>Add missing thinking patterns to commands</thinking_pattern_addition>
        <quality_gate_integration>Integrate missing quality gates</quality_gate_integration>
      </structure_corrections>
      
      <compliance_corrections>
        <tdd_cycle_implementation>Implement proper TDD cycle where missing</tdd_cycle_implementation>
        <validation_addition>Add missing validation steps</validation_addition>
        <documentation_completion>Complete missing documentation</documentation_completion>
        <approval_process_integration>Integrate missing approval processes</approval_process_integration>
      </compliance_corrections>
    </automated_corrections>
    
    <guided_corrections>
      <complex_issue_resolution>
        <root_cause_analysis>Provide detailed root cause analysis for complex issues</root_cause_analysis>
        <step_by_step_correction>Provide step-by-step correction guidance</step_by_step_correction>
        <validation_procedures>Outline validation procedures for corrections</validation_procedures>
        <prevention_strategies>Recommend prevention strategies</prevention_strategies>
      </complex_issue_resolution>
      
      <systemic_improvements>
        <framework_enhancement>Recommend framework enhancements to prevent issues</framework_enhancement>
        <process_improvements>Suggest process improvements for compliance</process_improvements>
        <training_recommendations>Recommend training or documentation improvements</training_recommendations>
        <monitoring_enhancements>Suggest monitoring improvements</monitoring_enhancements>
      </systemic_improvements>
    </guided_corrections>
  </self_correction_capabilities>
  
  <prevention_strategies enforcement="MANDATORY">
    <proactive_prevention>
      <compliance_monitoring>
        <real_time_monitoring>Monitor compliance in real-time</real_time_monitoring>
        <early_warning_systems>Implement early warning for compliance issues</early_warning_systems>
        <automated_validation>Automate validation of compliance requirements</automated_validation>
        <compliance_dashboards>Provide visibility into compliance status</compliance_dashboards>
      </compliance_monitoring>
      
      <process_improvements>
        <workflow_enhancement>Enhance workflows to prevent common issues</workflow_enhancement>
        <checkpoint_integration>Integrate compliance checkpoints into processes</checkpoint_integration>
        <validation_automation>Automate validation to catch issues early</validation_automation>
        <quality_gate_strengthening>Strengthen quality gates to prevent issues</quality_gate_strengthening>
      </process_improvements>
      
      <education_and_training>
        <compliance_guidance>Provide clear compliance guidance</compliance_guidance>
        <best_practice_documentation>Document best practices for compliance</best_practice_documentation>
        <training_materials>Develop training materials for common issues</training_materials>
        <learning_integration>Integrate learning from issues into training</learning_integration>
      </education_and_training>
    </proactive_prevention>
    
    <reactive_improvements>
      <issue_learning>
        <pattern_recognition>Recognize patterns in compliance issues</pattern_recognition>
        <root_cause_database>Maintain database of root causes and solutions</root_cause_database>
        <solution_library>Build library of proven solutions</solution_library>
        <prevention_knowledge>Accumulate prevention knowledge</prevention_knowledge>
      </issue_learning>
      
      <continuous_improvement>
        <feedback_integration>Integrate feedback from issue resolution</feedback_integration>
        <process_refinement>Refine processes based on issue patterns</process_refinement>
        <framework_evolution>Evolve framework to prevent recurring issues</framework_evolution>
        <culture_development>Develop culture of compliance and quality</culture_development>
      </continuous_improvement>
    </reactive_improvements>
  </prevention_strategies>
  
  <validation_framework enforcement="MANDATORY">
    <correction_validation>
      <effectiveness_verification>Verify corrections address root causes</effectiveness_verification>
      <compliance_confirmation>Confirm corrections meet framework standards</compliance_confirmation>
      <integration_testing>Test corrections integrate properly</integration_testing>
      <prevention_validation>Validate prevention strategies are effective</prevention_validation>
    </correction_validation>
    
    <quality_assurance>
      <correction_quality>Ensure corrections meet quality standards</correction_quality>
      <solution_sustainability>Verify solutions are sustainable long-term</solution_sustainability>
      <impact_assessment>Assess impact of corrections on framework</impact_assessment>
      <continuous_monitoring>Monitor corrections for ongoing effectiveness</continuous_monitoring>
    </quality_assurance>
  </validation_framework>
  
  <success_criteria>
    <immediate_success>
      <issue_resolution>Reported compliance issue fully resolved</issue_resolution>
      <root_cause_addressed>Root causes identified and addressed</root_cause_addressed>
      <standards_compliance>Full compliance with framework standards achieved</standards_compliance>
      <validation_passed>All validation tests passed</validation_passed>
    </immediate_success>
    
    <long_term_success>
      <recurrence_prevention>Similar issues prevented from recurring</recurrence_prevention>
      <process_improvement>Processes improved to prevent future issues</process_improvement>
      <compliance_culture>Culture of compliance and quality strengthened</compliance_culture>
      <continuous_learning>Learning integrated into framework evolution</continuous_learning>
    </long_term_success>
  </success_criteria>
  
  <quality_gates enforcement="MANDATORY">
    <gate name="root_cause_identification" requirement="Clear root cause identified">
      <validation>Root cause must be clearly identified and evidence-based</validation>
      <remediation>Deepen analysis until root cause is clear</remediation>
    </gate>
    <gate name="correction_effectiveness" requirement="Corrections address root causes">
      <validation>Corrections must directly address identified root causes</validation>
      <remediation>Refine corrections to ensure root cause resolution</remediation>
    </gate>
    <gate name="compliance_achievement" requirement="Full framework compliance">
      <validation>Corrected state must meet all applicable framework standards</validation>
      <remediation>Continue corrections until full compliance achieved</remediation>
    </gate>
    <gate name="prevention_implementation" requirement="Prevention strategies deployed">
      <validation>Prevention strategies must be implemented to avoid recurrence</validation>
      <remediation>Develop and implement prevention strategies</remediation>
    </gate>
  </quality_gates>
  
  <restrictions>
    <restriction>SAFETY: Must respect all framework safety boundaries during corrections</restriction>
    <restriction>VALIDATION: All corrections must be validated before implementation</restriction>
    <restriction>EVIDENCE: All diagnoses must be evidence-based and verifiable</restriction>
    <restriction>PREVENTION: Must implement prevention strategies to avoid recurrence</restriction>
  </restrictions>
</command>
```