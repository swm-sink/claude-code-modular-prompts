| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# TDD Verification Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

<thinking_pattern>
Parse TDD requirements → Verify RED test exists → Check GREEN implementation → Validate REFACTOR → Generate evidence → Report compliance
</thinking_pattern>

<module>
  <name>tdd-verification</name>
  <version>1.0.0</version>
  <description>Automated TDD compliance verification with evidence requirements</description>
  <dependencies>
    <required>tdd.md</required>
    <required>error-recovery.md</required>
    <required>production-standards.md</required>
  </dependencies>
</module>

────────────────────────────────────────────────────────────────────────────────

## Core Verification Pattern

```xml
<tdd_verification>
  <workflow>
    <phase name="RED" required="true">
      <step>1. Detect test file creation/modification BEFORE implementation</step>
      <step>2. Verify test runs and FAILS with expected error</step>
      <step>3. Capture failure evidence (screenshot/output)</step>
      <step>4. Block implementation until RED phase complete</step>
    </phase>
    <phase name="GREEN" required="true">
      <step>1. Detect implementation file creation/modification</step>
      <step>2. Verify test now PASSES</step>
      <step>3. Capture success evidence</step>
      <step>4. Ensure minimal code to pass test</step>
    </phase>
    <phase name="REFACTOR" required="true">
      <step>1. Detect code improvements</step>
      <step>2. Verify tests still PASS</step>
      <step>3. Check code quality metrics</step>
      <step>4. Generate refactoring report</step>
    </phase>
  </workflow>
</tdd_verification>
```

────────────────────────────────────────────────────────────────────────────────

## Automated Evidence Collection

```xml
<evidence_collection>
  <red_phase_evidence>
    <capture>Test failure output with timestamp</capture>
    <capture>Stack trace showing expected failure</capture>
    <capture>File creation order verification</capture>
    <store>evidence/tdd/{task_id}/red-phase-{timestamp}.json</store>
  </red_phase_evidence>
  
  <green_phase_evidence>
    <capture>Test success output</capture>
    <capture>Implementation diff</capture>
    <capture>Coverage report</capture>
    <store>evidence/tdd/{task_id}/green-phase-{timestamp}.json</store>
  </green_phase_evidence>
  
  <refactor_evidence>
    <capture>Before/after code metrics</capture>
    <capture>Test stability confirmation</capture>
    <capture>Performance comparison</capture>
    <store>evidence/tdd/{task_id}/refactor-{timestamp}.json</store>
  </refactor_evidence>
</evidence_collection>
```

────────────────────────────────────────────────────────────────────────────────

## Verification Implementation

```python
# TDD Verification Engine
class TDDVerifier:
    def __init__(self):
        self.current_phase = None
        self.evidence = []
        self.blocked = False
        
    def verify_red_phase(self, test_file, test_output):
        """Verify RED phase compliance"""
        evidence = {
            "phase": "RED",
            "timestamp": datetime.utcnow().isoformat(),
            "test_file": test_file,
            "test_failed": "FAILED" in test_output,
            "error_message": self.extract_error(test_output),
            "implementation_exists": self.check_implementation_exists()
        }
        
        if not evidence["test_failed"]:
            self.blocked = True
            raise TDDViolation("Test must FAIL in RED phase")
            
        if evidence["implementation_exists"]:
            self.blocked = True
            raise TDDViolation("Implementation found before test - TDD violation")
            
        self.evidence.append(evidence)
        self.current_phase = "GREEN"
        return evidence
        
    def verify_green_phase(self, test_output, implementation_diff):
        """Verify GREEN phase compliance"""
        if self.current_phase != "GREEN":
            raise TDDViolation("Must complete RED phase first")
            
        evidence = {
            "phase": "GREEN",
            "timestamp": datetime.utcnow().isoformat(),
            "test_passed": "PASSED" in test_output,
            "implementation_size": len(implementation_diff.split('\n')),
            "minimal_code": self.verify_minimal_implementation(implementation_diff)
        }
        
        if not evidence["test_passed"]:
            self.blocked = True
            raise TDDViolation("Test must PASS in GREEN phase")
            
        self.evidence.append(evidence)
        self.current_phase = "REFACTOR"
        return evidence
```

────────────────────────────────────────────────────────────────────────────────

## Compliance Gates

```xml
<compliance_gates>
  <gate name="PreImplementation">
    <check>Test file exists and fails</check>
    <check>No implementation code present</check>
    <check>Test describes expected behavior</check>
    <action>BLOCK implementation until passed</action>
  </gate>
  
  <gate name="PostImplementation">
    <check>All tests pass</check>
    <check>Code coverage ≥ 90%</check>
    <check>Implementation is minimal</check>
    <action>BLOCK commit until passed</action>
  </gate>
  
  <gate name="PostRefactor">
    <check>Tests still pass</check>
    <check>Code quality improved</check>
    <check>Performance maintained</check>
    <action>Generate compliance certificate</action>
  </gate>
</compliance_gates>
```

────────────────────────────────────────────────────────────────────────────────

## Verification Commands

```bash
# Verify TDD compliance for current task
verify_tdd() {
    local task_id=$1
    local phase=$2
    
    # Collect evidence
    if [[ "$phase" == "red" ]]; then
        pytest tests/test_${task_id}.py 2>&1 | tee evidence/tdd/${task_id}/red-output.txt
        [[ $? -eq 1 ]] || { echo "VIOLATION: Test must fail in RED phase"; return 1; }
    fi
    
    # Generate report
    python -m quality.tdd_verifier \
        --task-id "$task_id" \
        --phase "$phase" \
        --evidence-dir "evidence/tdd/${task_id}"
}

# Block non-compliant commits
pre_commit_tdd_check() {
    local violations=$(find . -name "*.py" -newer .git/tdd_verified -type f)
    if [[ -n "$violations" ]]; then
        echo "TDD VIOLATION: Unverified changes detected"
        echo "Run: verify_tdd <task_id> <phase>"
        exit 1
    fi
}
```

────────────────────────────────────────────────────────────────────────────────

## Integration Points

```xml
<integration>
  <with module="task-management.md">
    <hook>Pre-implementation TDD check</hook>
    <hook>Post-implementation verification</hook>
    <hook>Refactor quality gate</hook>
  </with>
  
  <with module="production-standards.md">
    <hook>Quality gate enforcement</hook>
    <hook>Evidence archival</hook>
    <hook>Compliance reporting</hook>
  </with>
  
  <with module="git-operations.md">
    <hook>Pre-commit TDD verification</hook>
    <hook>PR quality checks</hook>
    <hook>Merge gate enforcement</hook>
  </with>
</integration>
```

────────────────────────────────────────────────────────────────────────────────

## Reporting Template

```markdown
# TDD Compliance Report

**Task ID**: {task_id}
**Date**: {date}
**Developer**: {developer}

## RED Phase ✓
- Test Created: {test_file}
- Test Failed: YES
- Error: {error_message}
- Evidence: [red-phase-evidence.json](evidence/tdd/{task_id}/red-phase.json)

## GREEN Phase ✓
- Implementation: {implementation_file}
- Test Passed: YES
- Coverage: {coverage}%
- Evidence: [green-phase-evidence.json](evidence/tdd/{task_id}/green-phase.json)

## REFACTOR Phase ✓
- Metrics Improved: {metrics}
- Tests Stable: YES
- Performance: {performance}
- Evidence: [refactor-evidence.json](evidence/tdd/{task_id}/refactor.json)

## Compliance Certificate
All TDD requirements met. Quality gate PASSED.
```

────────────────────────────────────────────────────────────────────────────────

## Error Recovery

```xml
<error_recovery>
  <violation type="ImplementationFirst">
    <detect>Implementation file created before test</detect>
    <action>Block commit, require test creation</action>
    <recovery>Move implementation to staging, create test first</recovery>
  </violation>
  
  <violation type="TestNotFailing">
    <detect>Test passes in RED phase</detect>
    <action>Block progression to GREEN</action>
    <recovery>Revise test to properly fail first</recovery>
  </violation>
  
  <violation type="InsufficientCoverage">
    <detect>Coverage below 90% threshold</detect>
    <action>Block merge to main</action>
    <recovery>Add missing test cases</recovery>
  </violation>
</error_recovery>
```