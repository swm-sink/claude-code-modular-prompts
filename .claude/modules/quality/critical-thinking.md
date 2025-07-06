<module name="critical_thinking" category="quality">
  
  <purpose>
    Enforce forensic-level critical thinking to prevent framework disasters, duplication, and hasty decisions that create complexity.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">ALL operations without exceptions - universal enforcement</condition>
    <condition type="explicit">Any framework modification, file creation, or implementation decision</condition>
  </trigger_conditions>
  
  <implementation enforcement="mandatory">
    
    <phase name="pre_action_analysis" order="1">
      <requirements>
        Minimum 30 seconds deep thinking before ANY action
        All assumptions verified with concrete evidence
        Duplication prevention scan completed
      </requirements>
      <actions>
        Apply mandatory analysis checklist: what, why, risk, assumptions, complexity, alternatives, evidence
        Scan existing system for duplicate functionality or competing solutions
        Verify all claims against actual filesystem state
        Document complete decision rationale with evidence chain
      </actions>
      <validation>
        Analysis documented with specific evidence for each decision
        Zero duplication detected through comprehensive system scan
        All assumptions verified with concrete proof
      </validation>
    </phase>
    
    <phase name="implementation_monitoring" order="2">
      <requirements>
        Continuous verification of each step against planned outcome
        Immediate halt on unexpected results or assumption violations
        DRY principle validation throughout implementation process
      </requirements>
      <actions>
        Verify each step outcome matches expected result before proceeding
        Monitor complexity growth and justify any increases
        Validate against duplication prevention protocols continuously
        Document any deviations from plan with corrective actions
      </actions>
      <validation>
        Each implementation step verified before next step begins
        Zero tolerance for assumption violations or duplication creation
        Complete audit trail of decisions and course corrections
      </validation>
    </phase>
    
    <phase name="post_action_validation" order="3">
      <requirements>
        Comprehensive verification that all references remain valid
        File count reconciliation against expected changes
        Functionality regression testing completed
      </requirements>
      <actions>
        Count and verify all files match expected outcomes
        Test all module references and integration points
        Verify no functionality lost through systematic testing
        Document actual vs expected results with lessons learned
      </actions>
      <validation>
        System integrity verified with zero broken references
        Functionality confirmed maintained or enhanced
        Complete post-action analysis documented for future prevention
      </validation>
    </phase>
    
  </implementation>
  
  <catastrophic_lesson origin="previous_framework_disaster">
    <failures>262+ duplicate files created, contradictory claims of simplification, broken references, lost capabilities</failures>
    <root_cause>Thinking failure - acting without deep analysis and verification</root_cause>
    <prevention>Mandatory 30-second analysis, DRY enforcement, forensic verification</prevention>
  </catastrophic_lesson>
  
  <enforcement_rules tolerance="zero">
    <deep_thinking minimum_time="30_seconds">
      <checklist>What exactly am I doing? Why this specific approach? What could go wrong? What assumptions? Will this add complexity? What alternatives? What evidence?</checklist>
      <violations>Acting without analysis, surface understanding, unverified assumptions, rushed implementation</violations>
    </deep_thinking>
    <dry_principle enforcement="absolute">
      <prevention>Scan before file creation, enhance vs create new, move vs copy, clean up original locations</prevention>
      <violations>Creating competing solutions, duplicating existing functionality, copying instead of referencing</violations>
    </dry_principle>
    <forensic_verification requirement="every_step">
      <protocols>Read paths character by character, verify references, check claims against reality, count files, test changes</protocols>
      <violations>Broken references, incorrect claims, missing verification, untested changes</violations>
    </forensic_verification>
  </enforcement_rules>
  
  <critical_decision_questions mandatory="true">
    <primary>Problem definition, scope verification, simplicity test, evidence check, failure impact</primary>
    <secondary>Duplication scan, reference integrity, maintenance burden, user impact, rollback plan</secondary>
  </critical_decision_questions>
  
  <aware_framework_enhancement>
    <assess_analyze multiplier="3x">Spend 3x longer on assessment, question assumptions, map dependencies</assess_analyze>
    <watch_assumptions mode="active_hunting">Seek hidden assumptions, challenge obvious conclusions, verify with evidence</watch_assumptions>
    <architect_approach constraint="dry_primary">DRY prevention as #1 priority, reuse over recreation, document necessity</architect_approach>
    <run_verification requirement="every_step">Verify each operation, stop on unexpected results, validate against gates</run_verification>
    <evaluate_evolve method="forensic">Forensic analysis of outcomes, compare to predictions, update prevention</evaluate_evolve>
  </aware_framework_enhancement>
  
  <failure_pattern_recognition>
    <warning_signs>Creating unnecessary directories, copying vs referencing, unverified claims, duplicating existing features, rushed analysis, dismissing complexity</warning_signs>
    <disaster_examples>Surface thinking creating 262 duplicates, reality disconnect leaving scattered code, evidence ignoring keeping theoretical features</disaster_examples>
    <prevention_approach>Count actual files, check duplicates, verify references, test impact, document before acting</prevention_approach>
  </failure_pattern_recognition>
  
  <session_integration>
    <mandatory_documentation>
      Decision rationale for major changes with evidence
      Assumption verification with concrete proof
      Duplication prevention measures and scans
      Alternative approaches considered and rejection rationale
    </mandatory_documentation>
  </session_integration>
  
  <survival_principles>
    <rule_1>THINK DEEPLY - Minimum 30 seconds analysis before any action</rule_1>
    <rule_2>CHECK EVERYTHING - Verify every claim, count, and assumption</rule_2>
    <rule_3>DUPLICATE NOTHING - Reuse and reference, never recreate</rule_3>
  </survival_principles>
  
  <integration_points>
    <depends_on>
      None - foundational quality enforcement for all operations
    </depends_on>
    <provides_to>
      ALL modules for critical thinking enforcement
      patterns/session-management.md for decision documentation
      ALL commands for implementation verification
    </provides_to>
  </integration_points>
  
</module>