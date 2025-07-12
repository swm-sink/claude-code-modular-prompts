| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-12   | stable |

# Command-Module Atomic Delegation Pattern

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="command_module_atomic_delegation" category="patterns">
  
  <purpose>
    Standardized atomic delegation patterns between commands and modules ensuring consistent rollback capability, state preservation, and error recovery across the entire framework architecture.
  </purpose>
  
  <delegation_architecture>
    <command_role>
      <responsibility>Orchestration, atomic safety, user interface</responsibility>
      <atomic_safety>PRE-OP commits before module delegation</atomic_safety>
      <delegation>Structured handoff to appropriate modules</delegation>
      <validation>POST-OP commits after module completion</validation>
    </command_role>
    
    <module_role>
      <responsibility>Implementation, domain expertise, detailed execution</responsibility>
      <atomic_integration>Integration with command atomic patterns</atomic_integration>
      <state_preservation>Maintain atomic safety during execution</state_preservation>
      <error_handling>Graceful failure with rollback capability</error_handling>
    </module_role>
  </delegation_architecture>
  
  <atomic_delegation_patterns>
    
    <pattern name="simple_delegation" complexity="low">
      <description>Single module delegation with atomic safety</description>
      <command_side>
        <pre_delegation>git add -A && git commit -m "PRE-OP: [command] - backup before [module] delegation"</pre_delegation>
        <delegation>Invoke module with structured input and context</delegation>
        <validation>Validate module output and results</validation>
        <post_delegation>git add -A && git commit -m "POST-OP: [command] - [module] delegation complete"</post_delegation>
      </command_side>
      <module_side>
        <atomic_integration>Leverage command atomic context for internal safety</atomic_integration>
        <execution>Execute module logic with atomic checkpoints</execution>
        <result_validation>Validate results before returning to command</result_validation>
        <error_handling>Return structured error for command rollback</error_handling>
      </module_side>
      <rollback_strategy>
        <command_failure>git reset --hard HEAD~1 # Return to pre-delegation</command_failure>
        <module_failure>Module reports failure, command initiates rollback</module_failure>
      </rollback_strategy>
    </pattern>
    
    <pattern name="multi_module_delegation" complexity="medium">
      <description>Sequential module delegation with progressive atomic safety</description>
      <command_side>
        <pre_delegation>git add -A && git commit -m "PRE-OP: [command] - backup before multi-module delegation"</pre_delegation>
        <progressive_delegation>
          <step>Delegate to module A with atomic checkpoint</step>
          <step>git add -A && git commit -m "CHECKPOINT: [command] - module A complete"</step>
          <step>Validate module A results before proceeding</step>
          <step>Delegate to module B with atomic checkpoint</step>
          <step>git add -A && git commit -m "CHECKPOINT: [command] - module B complete"</step>
          <step>Continue pattern for all modules</step>
        </progressive_delegation>
        <post_delegation>git add -A && git commit -m "POST-OP: [command] - all modules complete"</post_delegation>
      </command_side>
      <rollback_strategy>
        <progressive_rollback>Rollback to last successful module checkpoint</progressive_rollback>
        <selective_rollback>Rollback specific module while preserving others</selective_rollback>
        <complete_rollback>git reset --hard HEAD~[n] # Return to pre-delegation</complete_rollback>
      </rollback_strategy>
    </pattern>
    
    <pattern name="parallel_delegation" complexity="high">
      <description>Parallel module execution with atomic coordination</description>
      <command_side>
        <pre_delegation>git add -A && git commit -m "PRE-OP: [command] - backup before parallel delegation"</pre_delegation>
        <parallel_coordination>
          <step>Initialize parallel execution context</step>
          <step>Delegate to multiple modules simultaneously</step>
          <step>Monitor parallel execution progress</step>
          <step>Coordinate results and atomic safety</step>
          <step>Validate all parallel results before proceeding</step>
        </parallel_coordination>
        <synchronization>
          <step>Wait for all parallel modules to complete</step>
          <step>Validate cross-module consistency</step>
          <step>git add -A && git commit -m "SYNC-POINT: [command] - parallel modules synchronized"</step>
        </synchronization>
        <post_delegation>git add -A && git commit -m "POST-OP: [command] - parallel delegation complete"</post_delegation>
      </command_side>
      <rollback_strategy>
        <parallel_rollback>Rollback all parallel modules atomically</parallel_rollback>
        <selective_recovery>Recover individual module failures without affecting others</selective_recovery>
        <coordination_failure>Complete rollback if coordination fails</coordination_failure>
      </rollback_strategy>
    </pattern>
    
    <pattern name="nested_delegation" complexity="high">
      <description>Module-to-module delegation with hierarchical atomic safety</description>
      <command_side>
        <pre_delegation>git add -A && git commit -m "PRE-OP: [command] - backup before nested delegation"</pre_delegation>
        <delegation>Delegate to primary module with nested capability</delegation>
        <monitoring>Monitor nested delegation chain</monitoring>
        <post_delegation>git add -A && git commit -m "POST-OP: [command] - nested delegation complete"</post_delegation>
      </command_side>
      <module_side>
        <nested_safety>
          <step>Inherit atomic context from parent command</step>
          <step>Create nested atomic checkpoint before sub-delegation</step>
          <step>git add -A && git commit -m "NESTED-PRE: [module] - before sub-module delegation"</step>
          <step>Delegate to sub-module with inherited safety</step>
          <step>git add -A && git commit -m "NESTED-POST: [module] - sub-module complete"</step>
        </nested_safety>
      </module_side>
      <rollback_strategy>
        <hierarchical_rollback>Rollback nested delegation chain in reverse order</hierarchical_rollback>
        <level_specific>Rollback to specific nesting level</level_specific>
        <cascade_prevention>Prevent rollback cascades affecting parent levels</cascade_prevention>
      </rollback_strategy>
    </pattern>
    
  </atomic_delegation_patterns>
  
  <interface_contracts>
    
    <command_module_interface>
      <input_specification>
        <required>operation_type, parameters, atomic_context</required>
        <optional>validation_requirements, performance_constraints, error_handling_preferences</optional>
      </input_specification>
      <output_specification>
        <success>results, validation_status, atomic_checkpoints, execution_metadata</success>
        <failure>error_type, failure_reason, rollback_recommendation, recovery_suggestions</failure>
      </output_specification>
      <atomic_context>
        <inheritance>Modules inherit atomic context from commands</inheritance>
        <preservation>Atomic state preserved across delegation boundaries</preservation>
        <coordination>Atomic operations coordinated between command and module</coordination>
      </atomic_context>
    </command_module_interface>
    
    <error_handling_protocol>
      <graceful_failure>
        <module_side>Return structured error without corrupting state</module_side>
        <command_side>Interpret error and initiate appropriate rollback</command_side>
      </graceful_failure>
      <rollback_coordination>
        <module_initiated>Module requests rollback through error response</module_initiated>
        <command_initiated>Command decides rollback based on module results</command_initiated>
        <automatic>Automatic rollback on critical failures</automatic>
      </rollback_coordination>
    </error_handling_protocol>
    
  </interface_contracts>
  
  <delegation_examples>
    
    <example name="task_command_to_task_management_module">
      <scenario>Task command delegates to task-management module</scenario>
      <command_code>
        ```
        # PRE-OP atomic commit
        git add -A && git commit -m "PRE-OP: task - backup before task-management delegation"
        
        # Delegate to task-management module
        result = delegate_to_module("task-management", {
          task_description: user_input,
          atomic_context: current_atomic_context,
          validation_requirements: ["tdd_compliance", "coverage_90+"]
        })
        
        # Validate results
        if result.success:
          git add -A && git commit -m "POST-OP: task - task-management delegation complete"
          return result
        else:
          git reset --hard HEAD~1  # Rollback to PRE-OP
          return error_response(result.error)
        ```
      </command_code>
      <module_response>
        ```
        # Module inherits atomic context and executes with safety
        execute_with_atomic_safety(task_implementation)
        
        # Return structured result
        return {
          success: true,
          results: {implementation, tests, coverage_report},
          atomic_checkpoints: [pre_op, implementation, post_validation],
          validation_status: "all_passed"
        }
        ```
      </module_response>
    </example>
    
    <example name="swarm_multi_module_delegation">
      <scenario>Swarm command delegates to multiple modules progressively</scenario>
      <command_code>
        ```
        # PRE-OP atomic commit
        git add -A && git commit -m "PRE-OP: swarm - backup before multi-module delegation"
        
        # Progressive delegation with checkpoints
        for module in [planning, implementation, testing, documentation]:
          result = delegate_to_module(module, params)
          if result.success:
            git add -A && git commit -m "CHECKPOINT: swarm - {module} complete"
          else:
            # Rollback to last successful checkpoint
            rollback_to_last_checkpoint()
            return error_response(result.error)
        
        # Final commit
        git add -A && git commit -m "POST-OP: swarm - all modules complete"
        ```
      </command_code>
    </example>
    
  </delegation_examples>
  
  <validation_and_monitoring>
    <delegation_tracking>
      <call_chain>Track complete delegation call chain</call_chain>
      <timing>Monitor delegation timing and performance</timing>
      <success_rate>Track delegation success rates by pattern</success_rate>
      <failure_analysis>Analyze delegation failure patterns</failure_analysis>
    </delegation_tracking>
    
    <atomic_consistency>
      <state_validation>Validate atomic state consistency across delegation</state_validation>
      <checkpoint_verification>Verify atomic checkpoints are properly created</checkpoint_verification>
      <rollback_testing>Regular testing of rollback procedures</rollback_testing>
      <integration_validation>Validate command-module integration integrity</integration_validation>
    </atomic_consistency>
  </validation_and_monitoring>
  
  <integration_points>
    <atomic_operation_pattern>Leverages core atomic operation patterns</atomic_operation_pattern>
    <emergency_procedures>Integrates with emergency rollback procedures</emergency_procedures>
    <framework_operations_safety>Coordinates with framework operations safety</framework_operations_safety>
    <command_orchestration>Enhances command orchestration with atomic safety</command_orchestration>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Delegation Pattern Usage Examples

### Simple Command-Module Delegation
```xml
<delegation>
  <command>task</command>
  <module>task-management</module>
  <pattern>simple_delegation</pattern>
  <atomic_safety>PRE-OP → DELEGATION → POST-OP</atomic_safety>
</delegation>
```

### Multi-Module Progressive Delegation
```xml
<delegation>
  <command>feature</command>
  <modules>["prd-generation", "mvp-strategy", "implementation", "validation"]</modules>
  <pattern>multi_module_delegation</pattern>
  <atomic_safety>PRE-OP → CHECKPOINT → CHECKPOINT → CHECKPOINT → POST-OP</atomic_safety>
</delegation>
```

### Parallel Module Delegation
```xml
<delegation>
  <command>swarm</command>
  <modules>["documentation", "testing", "performance"] # parallel</modules>
  <pattern>parallel_delegation</pattern>
  <atomic_safety>PRE-OP → PARALLEL → SYNC-POINT → POST-OP</atomic_safety>
</delegation>
```

────────────────────────────────────────────────────────────────────────────────