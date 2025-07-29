---
name: /test-integration
description: "Execute comprehensive integration testing including advanced failure scenarios and emergency response validation"
tools: Read, Bash, Write
usage: "[scenario-type] (e.g., 'advanced-failures', 'emergency-fallback', 'all')"
category: quality
---

# Integration Testing Command

Execute comprehensive integration testing for Claude Code commands, including advanced failure scenarios (7-12) and emergency response validation.

## Usage

```
/test-integration [scenario-type]
```

**Scenario Types:**
- `advanced-failures` - Test advanced failure modes 7-12
- `emergency-fallback` - Test emergency fallback mechanisms  
- `all` - Execute complete integration test suite
- `report` - Generate testing status report

## Testing Framework Components

### Advanced Failure Testing (Errors 7-12)

**Framework**: `tests/advanced_failure_testing.py`

Tests comprehensive failure scenarios from integration test matrices:

1. **ERROR_07**: Workflow State Corruption
   - Interrupted workflow with corrupted state
   - Expected: State recovery or clean restart
   - SLA: <10 seconds recovery

2. **ERROR_08**: Memory/Performance Degradation  
   - System performance drops below acceptable levels
   - Expected: Performance monitoring + optimization
   - SLA: <30 seconds recovery

3. **ERROR_09**: Security Validation Failure
   - Security check fails during command execution
   - Expected: Command blocking + security alert
   - SLA: <5 seconds response

4. **ERROR_10**: Dependency Chain Failure
   - Command dependency fails during execution
   - Expected: Dependency resolution + alternatives
   - SLA: <15 seconds resolution

5. **ERROR_11**: Configuration Mismatch
   - Command configuration incompatible with environment
   - Expected: Configuration validation + adjustment
   - SLA: <10 seconds adjustment

6. **ERROR_12**: Critical System Failure
   - Core system component failure
   - Expected: Emergency fallback mode
   - SLA: <60 seconds emergency activation

### Emergency Fallback Validation

**Framework**: `tests/emergency_fallback_validation.py`

Tests emergency response mechanisms:

1. **Emergency Mode** - Minimal functionality preservation
2. **Safe Mode** - Tool quarantine and read-only operations
3. **Recovery Mode** - Context isolation and resource management
4. **Graceful Degradation** - State recovery with reduced functionality
5. **Minimal Function** - Command blocking with essential services only

### Validation Metrics

**Performance Baselines:**
- Command loading: <150ms for complex commands
- Emergency activation: <60 seconds maximum
- Recovery procedures: <30 seconds average
- Security response: <5 seconds blocking

**Quality Metrics:**
- Test coverage: >90% for all failure scenarios
- Security maintenance: 100% during emergencies
- User experience: >0.7/1.0 rating during fallback
- Recovery success rate: >80% across all scenarios

## Execution Examples

### Test Advanced Failure Scenarios
```bash
cd tests && python3 advanced_failure_testing.py
```

### Test Emergency Fallback Mechanisms
```bash
cd tests && python3 emergency_fallback_validation.py
```

### Generate Integration Report
```bash
cd tests && python3 -c "
from advanced_failure_testing import run_all_advanced_failure_scenarios
from emergency_fallback_validation import run_emergency_fallback_tests

commands_dir = '.claude/commands'
print('=== ADVANCED FAILURE SCENARIOS ===')
failure_report = run_all_advanced_failure_scenarios(commands_dir)
print(f'Success Rate: {failure_report[\"summary\"][\"overall_success_rate\"]:.1f}%')

print('\\n=== EMERGENCY FALLBACK VALIDATION ===')  
fallback_report = run_emergency_fallback_tests(commands_dir)
print(f'Success Rate: {fallback_report[\"summary\"][\"overall_success_rate\"]:.1f}%')
"
```

## Latest Test Results

**Advanced Failure Scenarios**: 83.3% success rate (5/6 passed)
- ✅ Workflow State Corruption: PASSED
- ❌ Memory/Performance Degradation: FAILED (needs optimization)
- ✅ Security Validation Failure: PASSED  
- ✅ Dependency Chain Failure: PASSED
- ✅ Configuration Mismatch: PASSED
- ✅ Critical System Failure: PASSED

**Emergency Fallback Mechanisms**: 80.0% success rate (4/5 passed)
- ✅ Emergency Mode: PASSED (UX: 1.00/1.0)
- ❌ Graceful Degradation: FAILED (UX: 0.80/1.0)
- ✅ Safe Mode: PASSED (UX: 1.00/1.0)
- ✅ Recovery Mode: PASSED (UX: 1.00/1.0)
- ✅ Minimal Function: PASSED (UX: 1.00/1.0)

**Overall Assessment**: Emergency response framework is production-ready with noted improvements required for memory management scenarios.

## Integration with Existing Testing

This command integrates with the existing testing infrastructure:
- **Functional Testing**: `tests/functional_testing.py`
- **Security Testing**: `tests/security_testing.py`
- **Mock Environment**: `tests/mock_environment.py`
- **LLM Evaluation**: `tests/llm_evaluation.py`

## Test Documentation

**Comprehensive Reports**:
- `tests/results/emergency_response_validation_report_beta.md`
- Integration test matrices: `.claude/commands/quality/integration-test-matrices.md`
- Testing methodology: `tests/TESTING-METHODOLOGY.md`

## Error Recovery Procedures

If integration tests fail:

1. **Check Prerequisites**: Ensure all testing dependencies are installed
2. **Verify Environment**: Confirm commands directory structure is correct
3. **Review Logs**: Check execution logs for specific error details
4. **Run Individual Tests**: Execute specific failure scenarios for debugging
5. **Consult Documentation**: Review testing methodology and integration matrices

## Security Considerations

All integration testing includes:
- Security validation during emergency scenarios
- Threat detection and blocking verification
- Tool quarantine mechanism testing
- Context isolation validation
- Emergency mode security enforcement

## Performance Monitoring

Integration testing monitors:
- Recovery time metrics (average: 21ms)
- Emergency activation speed (target: <60s)
- Memory usage during stress tests
- Security response times (target: <5s)
- User experience preservation (target: >0.7/1.0)

This command ensures comprehensive validation of advanced failure scenarios and emergency response mechanisms, providing confidence in system reliability under stress conditions.