| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-16 | template | N/A      |

# [Command Name] - [Brief Description]

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="[command_name]" category="[development|analysis|meta|utility]" enforcement="[BLOCKING|CONDITIONAL|WARNING]">
  
  <purpose>
    [Clear, concise statement of what this command does and why it exists]
  </purpose>
  
  <scope>
    <includes>[What this command handles - be specific]</includes>
    <excludes>[What this command does NOT handle - important boundaries]</excludes>
    <boundaries>[When to use other commands instead]</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>[What the user must provide]</required_arguments>
    <context_requirements>[What must exist in the environment]</context_requirements>
    <preconditions>[What must be true before execution]</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>[What this command produces]</deliverables>
    <success_criteria>[How to know the command succeeded]</success_criteria>
    <artifacts>[Files, reports, or outputs created]</artifacts>
  </output_specification>
</command>
```

[One-line summary of what the command does]

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>[First major step - usually analysis or validation]</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - [Key question 1 to consider]
        - [Key question 2 to consider]
        - [Key question 3 to consider]
      </pre_analysis>
      <execution_criteria>
        - [Criteria for successful completion]
        - [Validation requirements]
        - [Quality standards]
      </execution_criteria>
      <risk_assessment>
        - [Potential issues to watch for]
        - [Mitigation strategies]
        - [Rollback procedures]
      </risk_assessment>
    </interleaved_thinking>
    <validation>
      <success_criteria>[How to verify this step succeeded]</success_criteria>
      <failure_triggers>[What indicates failure]</failure_triggers>
      <next_actions>[What to do after success]</next_actions>
    </validation>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>[Second major step - usually implementation or execution]</action>
    <interleaved_thinking enforcement="MANDATORY">
      <implementation_strategy>
        - [Key implementation considerations]
        - [Technical approach]
        - [Quality requirements]
      </implementation_strategy>
      <parallel_optimization>
        - [Opportunities for parallel execution]
        - [Tool batching strategies]
        - [Performance optimizations]
      </parallel_optimization>
      <quality_gates>
        - [Quality checks to perform]
        - [Validation requirements]
        - [Success criteria]
      </quality_gates>
    </interleaved_thinking>
    <validation>
      <success_criteria>[How to verify this step succeeded]</success_criteria>
      <failure_triggers>[What indicates failure]</failure_triggers>
      <next_actions>[What to do after success]</next_actions>
    </validation>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>[Third major step - usually validation or finalization]</action>
    <interleaved_thinking enforcement="MANDATORY">
      <validation_strategy>
        - [How to validate the complete solution]
        - [Quality assurance steps]
        - [Integration testing]
      </validation_strategy>
      <completion_criteria>
        - [Final success criteria]
        - [Deliverable requirements]
        - [Documentation needs]
      </completion_criteria>
      <error_recovery>
        - [Recovery procedures if issues found]
        - [Rollback strategies]
        - [Alternative approaches]
      </error_recovery>
    </interleaved_thinking>
    <validation>
      <success_criteria>[How to verify complete success]</success_criteria>
      <failure_triggers>[What indicates overall failure]</failure_triggers>
      <next_actions>[What to do after completion]</next_actions>
    </validation>
  </checkpoint>
  
</thinking_pattern>
```

## Module Runtime - Core Integration

```xml
<module_runtime enforcement="CRITICAL">
  
  <core_modules enforcement="MANDATORY">
    <module>patterns/critical-thinking-pattern.md</module>
    <module>quality/universal-quality-gates.md</module>
    <module>patterns/thinking-pattern-template.md</module>
  </core_modules>
  
  <contextual_modules enforcement="CONDITIONAL">
    <module>[specific module for this command's domain]</module>
    <module>[related pattern module]</module>
  </contextual_modules>
  
  <support_modules enforcement="CONDITIONAL">
    <module>development/session-management.md</module>
    <module>system/git/git-operations.md</module>
    <module>development/error-recovery.md</module>
  </support_modules>
  
  <quality_gates enforcement="BLOCKING">
    <gate>TDD Cycle Completion</gate>
    <gate>Test Coverage ≥90%</gate>
    <gate>Security Validation</gate>
    <gate>Performance Standards</gate>
  </quality_gates>
  
  <atomic_safety enforcement="CRITICAL">
    <pre_execution>git add -A && git commit -m "Pre-[command_name] backup"</pre_execution>
    <checkpoints>Atomic commits at each major milestone</checkpoints>
    <rollback>Instant rollback capability via git reset</rollback>
  </atomic_safety>
  
</module_runtime>
```

## Command-Specific Implementation

### Step 1: [Major Step 1]

```xml
<implementation_step id="1">
  <objective>[What this step accomplishes]</objective>
  <modules_required>
    <module>[module1.md]</module>
    <module>[module2.md]</module>
  </modules_required>
  <execution_pattern>
    <parallel_tools>[Tools to run in parallel]</parallel_tools>
    <validation_checks>[Validation after execution]</validation_checks>
    <error_handling>[How to handle failures]</error_handling>
  </execution_pattern>
</implementation_step>
```

### Step 2: [Major Step 2]

```xml
<implementation_step id="2">
  <objective>[What this step accomplishes]</objective>
  <dependencies>
    <step>Step 1 completion</step>
    <validation>[Required validation state]</validation>
  </dependencies>
  <execution_pattern>
    <sequential_actions>[Actions that must be sequential]</sequential_actions>
    <quality_gates>[Quality checks to perform]</quality_gates>
    <success_criteria>[How to know this step succeeded]</success_criteria>
  </execution_pattern>
</implementation_step>
```

### Step 3: [Major Step 3]

```xml
<implementation_step id="3">
  <objective>[What this step accomplishes]</objective>
  <finalization>
    <deliverables>[Final outputs to produce]</deliverables>
    <validation>[Final validation requirements]</validation>
    <documentation>[Documentation to update]</documentation>
  </finalization>
</implementation_step>
```

## Error Recovery Protocols

```xml
<error_recovery>
  <recovery_levels>
    <level name="step">Rollback to previous step checkpoint</level>
    <level name="command">Rollback entire command execution</level>
    <level name="system">Escalate to framework error handler</level>
  </recovery_levels>
  
  <common_errors>
    <error type="[ErrorType1]">
      <cause>[What causes this error]</cause>
      <detection>[How to detect it]</detection>
      <recovery>[How to recover]</recovery>
    </error>
    <error type="[ErrorType2]">
      <cause>[What causes this error]</cause>
      <detection>[How to detect it]</detection>
      <recovery>[How to recover]</recovery>
    </error>
  </common_errors>
  
  <escalation_procedures>
    <trigger>[When to escalate to human]</trigger>
    <information>[What info to provide]</information>
    <rollback>[How to safely rollback]</rollback>
  </escalation_procedures>
</error_recovery>
```

## Integration Points

### Command Relationships

- **Delegates to**: [List commands this might delegate to]
- **Delegated from**: [List commands that might delegate to this]
- **Alternatives**: [When to use other commands instead]

### Module Dependencies

- **Core dependencies**: [Essential modules this command needs]
- **Optional dependencies**: [Modules that enhance functionality]
- **Provides to**: [What this command provides to other modules]

### Framework Integration

- **Quality gates**: [How this integrates with quality system]
- **Session management**: [How this integrates with session tracking]
- **Error reporting**: [How errors are reported to framework]

## Performance Characteristics

- **Typical execution time**: [Expected duration]
- **Resource requirements**: [Memory, CPU, disk needs]
- **Scalability limits**: [When performance degrades]
- **Optimization opportunities**: [How to improve performance]

## Testing Requirements

### Unit Testing
- **Test coverage**: Minimum 90% with meaningful assertions
- **Test categories**: [Types of tests required]
- **Mock requirements**: [What needs to be mocked]

### Integration Testing
- **Integration points**: [What integrations to test]
- **End-to-end scenarios**: [Complete workflows to test]
- **Failure scenarios**: [Error conditions to test]

### Performance Testing
- **Load testing**: [Performance under load]
- **Stress testing**: [Behavior at limits]
- **Benchmarking**: [Performance baselines]

## Documentation Standards

### User Documentation
- **Usage examples**: [Clear examples of how to use]
- **Common patterns**: [Typical use cases]
- **Troubleshooting**: [Common issues and solutions]

### Developer Documentation
- **Architecture**: [How the command is structured]
- **Extension points**: [How to extend functionality]
- **Maintenance**: [How to maintain and update]

## Changelog

### Version 3.0.0 - 2025-07-16
- Initial command template creation
- Claude 4 optimization integrated
- Thinking pattern standardized
- Module runtime integration completed

## Related Commands

- **[Related Command 1]**: [How it relates and when to use instead]
- **[Related Command 2]**: [How it relates and when to use instead]
- **[Parent Command]**: [Command this might be delegated from]

## TODO

- [ ] Implement command-specific logic
- [ ] Add comprehensive test coverage
- [ ] Optimize performance for large inputs
- [ ] Add telemetry and monitoring
- [ ] Create integration examples