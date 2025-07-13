| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Enforcement Verification Templates

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

**PURPOSE**: Standardized checkpoint outputs that prove framework pattern adherence

────────────────────────────────────────────────────────────────────────────────

```xml
<module purpose="Enforcement verification templates and checkpoint validation">
  
  <checkpoint_output_format>
    <header>
      ┌─────────────────────────────────────────────────────────────┐
      │ CHECKPOINT: {checkpoint_name}                                │
      │ Status: {PENDING|IN_PROGRESS|VERIFIED|FAILED}              │
      │ Time: {timestamp}                                           │
      └─────────────────────────────────────────────────────────────┘
    </header>
    
    <verification_section>
      ✓ Verification Steps:
        □ {step_1_description} - {status}
        □ {step_2_description} - {status}
        □ {step_3_description} - {status}
    </verification_section>
    
    <output_section>
      📊 Output Evidence:
        • {key_output_1}: {value}
        • {key_output_2}: {value}
        • {key_output_3}: {value}
    </output_section>
    
    <validation_section>
      ✅ Validation Results:
        • {validation_1}: {PASS|FAIL} - {details}
        • {validation_2}: {PASS|FAIL} - {details}
        • {validation_3}: {PASS|FAIL} - {details}
    </validation_section>
  </checkpoint_output_format>
  
  <standard_checkpoints>
    <checkpoint name="CRITICAL_THINKING">
      <template>
        ┌─────────────────────────────────────────────────────────────┐
        │ CHECKPOINT: CRITICAL THINKING                               │
        │ Status: VERIFIED                                            │
        │ Time: {timestamp}                                           │
        └─────────────────────────────────────────────────────────────┘
        
        ⏸️ CRITICAL THINKING: Analyzing for 30 seconds...
        
        ✓ Verification Steps:
          ☑ 30-second analysis completed
          ☑ Assumptions challenged and documented
          ☑ Existing implementations searched
          ☑ Consequence mapping completed
          ☑ Alternative approaches evaluated
        
        📊 Analysis Results:
          • Assumptions Found: {list_of_assumptions}
          • Similar Code: {existing_implementations}
          • Key Risks: {identified_risks}
          • Alternatives: {approach_1} vs {approach_2} vs {approach_3}
        
        ✅ Validation Results:
          • Duplication Check: PASS - No significant overlap found
          • Complexity Analysis: PASS - Within acceptable bounds
          • Risk Assessment: PASS - Mitigation strategies defined
      </template>
    </checkpoint>
    
    <checkpoint name="TDD_COMPLIANCE">
      <template>
        ┌─────────────────────────────────────────────────────────────┐
        │ CHECKPOINT: TDD COMPLIANCE                                  │
        │ Status: VERIFIED                                            │
        │ Time: {timestamp}                                           │
        └─────────────────────────────────────────────────────────────┘
        
        ✓ Verification Steps:
          ☑ Tests written before implementation
          ☑ Tests fail for correct reasons
          ☑ Implementation makes tests pass
          ☑ Refactoring preserves test success
        
        📊 TDD Evidence:
          • Test Files: {test_file_paths}
          • Initial Status: 🔴 RED - {failing_test_count} tests failing
          • Failure Reasons: {failure_descriptions}
          • Final Status: 🟢 GREEN - All tests passing
          • Coverage: {coverage_percentage}%
        
        ✅ Validation Results:
          • Test-First: PASS - Tests created before code
          • Meaningful Tests: PASS - Tests validate behavior
          • Coverage Target: PASS - Exceeds 90% requirement
      </template>
    </checkpoint>
    
    <checkpoint name="QUALITY_GATES">
      <template>
        ┌─────────────────────────────────────────────────────────────┐
        │ CHECKPOINT: QUALITY GATES                                   │
        │ Status: VERIFIED                                            │
        │ Time: {timestamp}                                           │
        └─────────────────────────────────────────────────────────────┘
        
        ✓ Gate Verification:
          ☑ Security gate evaluated
          ☑ Performance benchmarks tested
          ☑ Code quality metrics calculated
          ☑ Documentation completeness checked
        
        📊 Gate Results:
          • Security: ✅ No vulnerabilities detected
            - Threat model: Complete
            - Auth/AuthZ: Implemented
            - Input validation: Verified
          
          • Performance: ✅ Within targets
            - Response time: {response_ms}ms (target: <200ms)
            - Memory usage: {memory_mb}MB
            - CPU utilization: {cpu_percent}%
          
          • Code Quality: ✅ Standards met
            - Test coverage: {coverage}% (target: >90%)
            - Cyclomatic complexity: {complexity} (target: <10)
            - Linting: 0 errors, 0 warnings
          
          • Documentation: ✅ Complete
            - API docs: Generated
            - README: Updated
            - Code comments: Adequate
        
        ✅ Overall Status: ALL GATES PASSED
      </template>
    </checkpoint>
    
    <checkpoint name="DECISION_RECORDED">
      <template>
        ┌─────────────────────────────────────────────────────────────┐
        │ CHECKPOINT: DECISION RECORDED                               │
        │ Status: VERIFIED                                            │
        │ Time: {timestamp}                                           │
        └─────────────────────────────────────────────────────────────┘
        
        📊 Decision Details:
          • ID: {decision_id}
          • Type: {ARCHITECTURE|TECHNOLOGY|SECURITY|PERFORMANCE|DESIGN}
          • Context: {decision_context}
          
        🤔 Options Considered:
          1. {option_1} - {pros_and_cons}
          2. {option_2} - {pros_and_cons}
          3. {option_3} - {pros_and_cons}
        
        ✅ Decision Made:
          • Choice: {selected_option}
          • Rationale: {detailed_reasoning}
          • Consequences: {downstream_impacts}
          • Reversibility: {HIGH|MEDIUM|LOW}
        
        📝 Recorded In:
          • GitHub Issue: {issue_url}#{comment_id}
          • Decision Log: {log_entry_id}
          • Session Context: Preserved for child agents
      </template>
    </checkpoint>
  </standard_checkpoints>
  
  <enforcement_rules>
    <rule priority="CRITICAL">All checkpoints MUST produce visible output</rule>
    <rule priority="CRITICAL">Output format MUST match templates exactly</rule>
    <rule priority="HIGH">Failed checkpoints MUST block progress</rule>
    <rule priority="HIGH">Checkpoint results MUST be logged to session</rule>
    <rule priority="MEDIUM">Timing data MUST be collected for analysis</rule>
  </enforcement_rules>
  
  <integration_patterns>
    <pattern name="command_integration">
      Commands call checkpoint templates at verification points
    </pattern>
    <pattern name="module_verification">
      Modules output checkpoint data during execution
    </pattern>
    <pattern name="session_logging">
      All checkpoint results logged to GitHub session
    </pattern>
    <pattern name="failure_handling">
      Failed checkpoints trigger error recovery protocols
    </pattern>
  </integration_patterns>
  
  <usage_example>
    <!-- In a command's execution flow -->
    <checkpoint_usage>
      // After critical thinking phase
      output_checkpoint("CRITICAL_THINKING", {
        assumptions: ["User wants REST API", "Single tenant"],
        existing_code: ["api/base.py", "utils/auth.py"],
        risks: ["Scalability", "Token management"],
        alternatives: ["REST", "GraphQL", "gRPC"]
      });
      
      // After TDD phase
      output_checkpoint("TDD_COMPLIANCE", {
        test_files: ["tests/test_feature.py"],
        failing_tests: 5,
        failures: ["Auth not implemented", "DB not mocked"],
        coverage: 95
      });
    </checkpoint_usage>
  </usage_example>
  
</module>
</module>
</standard_checkpoints>
</checkpoint>
</template>
</200ms)>
</10)>
```

────────────────────────────────────────────────────────────────────────────────

## Checkpoint Categories

### 1. Process Checkpoints
- CRITICAL_THINKING - 30-second analysis verification
- TDD_COMPLIANCE - Test-first development proof
- DECISION_RECORDED - Critical decision documentation

### 2. Quality Checkpoints  
- QUALITY_GATES - Security, performance, coverage validation
- CODE_STANDARDS - Style and convention compliance
- DOCUMENTATION - Completeness verification

### 3. Coordination Checkpoints
- CONTEXT_TRANSFER - Inter-agent handoff validation
- SESSION_UPDATE - GitHub tracking verification
- DEPENDENCY_CHECK - Module integration validation

### 4. Error Recovery Checkpoints
- FAILURE_DETECTED - Error identification
- RECOVERY_ATTEMPTED - Mitigation action taken
- FALLBACK_EXECUTED - Alternative approach used

────────────────────────────────────────────────────────────────────────────────

## Implementation Guidelines

1. **Visibility First**: Every checkpoint MUST produce user-visible output
2. **Template Compliance**: Use exact formatting from templates
3. **Failure Blocking**: Failed checkpoints prevent progression
4. **Session Integration**: All results logged to active session
5. **Timing Tracking**: Collect performance data for optimization

────────────────────────────────────────────────────────────────────────────────

*Making framework enforcement visible, verifiable, and effective.*