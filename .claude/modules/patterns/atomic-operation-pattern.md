| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-12   | stable |

# Atomic Operation Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="atomic_operation_pattern" category="patterns">
  
  <purpose>
    Universal atomic commit pattern for all framework operations, ensuring zero data loss with instant rollback capability across every development workflow.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Any framework operation or development task</condition>
    <condition type="explicit">Quality gate enforcement</condition>
    <condition type="explicit">Module state changes</condition>
    <condition type="explicit">Command execution phases</condition>
  </trigger_conditions>
  
  <atomic_operation_template>
    
    <pre_operation_phase order="1">
      <checkpoint>git add -A && git commit -m "PRE-OP: [operation_name] - backup state before operation"</checkpoint>
      <validation>Current state captured and validated</validation>
      <purpose>Create rollback point before any changes</purpose>
    </pre_operation_phase>
    
    <operation_execution_phase order="2">
      <checkpoint>git add -A && git commit -m "OP-EXEC: [operation_details] - operation executed with validation"</checkpoint>
      <validation_before_commit>Operation success criteria must be met before commit</validation_before_commit>
      <rollback_trigger>Operation failure triggers: git reset --hard HEAD~1</rollback_trigger>
      <purpose>Execute operation with atomic safety</purpose>
    </operation_execution_phase>
    
    <post_operation_validation_phase order="3">
      <checkpoint>git add -A && git commit -m "POST-OP: [operation_name] - validation complete and operation successful"</checkpoint>
      <validation_checks>Quality gates, coverage thresholds, functionality verification</validation_checks>
      <rollback_trigger>Validation failure triggers: git reset --hard HEAD~2 (return to pre-operation)</rollback_trigger>
      <purpose>Validate operation success before finalizing</purpose>
    </post_operation_validation_phase>
    
  </atomic_operation_template>
  
  <rollback_capabilities>
    <immediate_rollback>git reset --hard HEAD~1 # Rollback last operation phase</immediate_rollback>
    <operation_rollback>git reset --hard HEAD~[n] # Rollback entire operation</operation_rollback>
    <selective_rollback>git checkout HEAD~[n] -- [specific_files] # Rollback specific changes</selective_rollback>
    <emergency_rollback>git stash && git reset --hard [safe_commit] # Emergency full rollback</emergency_rollback>
  </rollback_capabilities>
  
  <integration_points>
    <commands>All commands use this pattern for atomic execution phases</commands>
    <modules>All modules use this pattern for state changes</modules>
    <quality_gates>Quality enforcement uses this pattern for validation</quality_gates>
    <tdd_cycle>TDD phases use this pattern for RED-GREEN-REFACTOR commits</tdd_cycle>
  </integration_points>
  
  <safety_guarantees>
    <zero_data_loss>Every operation has rollback capability within 2 seconds</zero_data_loss>
    <state_integrity>Consistent state maintained across all atomic operations</state_integrity>
    <operation_isolation>Failed operations cannot corrupt successful operations</operation_isolation>
    <audit_trail>Complete operation history with rollback points</audit_trail>
  </safety_guarantees>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

**Usage Examples:**

```bash
# Example: Atomic Task Execution
git add -A && git commit -m "PRE-OP: user-authentication - backup state before task"
# ... execute task operations ...
git add -A && git commit -m "OP-EXEC: auth-implementation - tests passing and code implemented"
git add -A && git commit -m "POST-OP: user-authentication - validation complete and production ready"

# Example: Rollback on Failure
git reset --hard HEAD~1  # Rollback to previous safe state
```

────────────────────────────────────────────────────────────────────────────────