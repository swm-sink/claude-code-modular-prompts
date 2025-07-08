| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Module Composition Framework

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="module_composition_framework" category="patterns">
  
  <purpose>
    Define standardized module composition, loading, and execution patterns for deterministic Claude 4 interpretation with explicit dependency management and runtime orchestration.
  </purpose>
  
  <composition_architecture>
    <module_lifecycle>
      <phase name="discovery" order="1">
        <description>Identify required modules based on command context and requirements</description>
        <responsibilities>
          <responsibility>Parse command requirements for module dependencies</responsibility>
          <responsibility>Map requirements to appropriate module categories</responsibility>
          <responsibility>Identify conditional modules based on execution context</responsibility>
          <responsibility>Validate module availability and compatibility</responsibility>
        </responsibilities>
        <output>Validated module dependency graph</output>
      </phase>
      
      <phase name="loading" order="2">
        <description>Load modules in correct dependency order with interface validation</description>
        <responsibilities>
          <responsibility>Resolve module dependencies and load order</responsibility>
          <responsibility>Validate module interfaces and compatibility</responsibility>
          <responsibility>Initialize module contexts and configurations</responsibility>
          <responsibility>Establish inter-module communication channels</responsibility>
        </responsibilities>
        <output>Loaded and initialized module execution environment</output>
      </phase>
      
      <phase name="orchestration" order="3">
        <description>Execute modules in coordinated sequence with state management</description>
        <responsibilities>
          <responsibility>Execute core modules in defined sequence</responsibility>
          <responsibility>Manage module state and context passing</responsibility>
          <responsibility>Handle conditional module execution</responsibility>
          <responsibility>Coordinate module outputs and inputs</responsibility>
        </responsibilities>
        <output>Executed module stack with accumulated results</output>
      </phase>
      
      <phase name="integration" order="4">
        <description>Integrate module results into coherent command output</description>
        <responsibilities>
          <responsibility>Consolidate module outputs into command result</responsibility>
          <responsibility>Validate integration consistency and completeness</responsibility>
          <responsibility>Apply post-execution validation and quality gates</responsibility>
          <responsibility>Generate execution summary and artifacts</responsibility>
        </responsibilities>
        <output>Integrated command execution result</output>
      </phase>
    </module_lifecycle>
  </composition_architecture>
  
  <module_classification>
    <core_modules>
      <description>Essential modules required for command execution</description>
      <characteristics>
        <characteristic>MANDATORY execution for command success</characteristic>
        <characteristic>BLOCKING enforcement on failure</characteristic>
        <characteristic>Sequential execution order dependency</characteristic>
        <characteristic>State propagation between modules</characteristic>
      </characteristics>
      <examples>
        <example>quality/critical-thinking.md - Analysis foundation</example>
        <example>quality/tdd.md - Development methodology enforcement</example>
        <example>patterns/session-management.md - Coordination tracking</example>
      </examples>
    </core_modules>
    
    <contextual_modules>
      <description>Conditional modules loaded based on execution context</description>
      <characteristics>
        <characteristic>CONDITIONAL execution based on runtime conditions</characteristic>
        <characteristic>OPTIONAL or BLOCKING enforcement depending on context</characteristic>
        <characteristic>Dynamic loading based on requirement evaluation</characteristic>
        <characteristic>Context-sensitive configuration and behavior</characteristic>
      </characteristics>
      <examples>
        <example>security/threat-modeling.md - WHEN security implications detected</example>
        <example>patterns/multi-agent.md - WHEN multi-component coordination needed</example>
        <example>quality/error-recovery.md - WHEN failures or issues occur</example>
      </examples>
    </contextual_modules>
    
    <support_modules>
      <description>Utility modules providing supporting functionality</description>
      <characteristics>
        <characteristic>OPTIONAL execution for enhanced capabilities</characteristic>
        <characteristic>WARNING enforcement on failure (non-blocking)</characteristic>
        <characteristic>Parallel execution where possible</characteristic>
        <characteristic>Independent operation without state dependencies</characteristic>
      </characteristics>
      <examples>
        <example>development/code-review.md - Code quality enhancement</example>
        <example>git/conventional-commits.md - Git workflow optimization</example>
        <example>quality/pre-commit.md - Automated quality validation</example>
      </examples>
    </support_modules>
  </module_classification>
  
  <dependency_management>
    <dependency_resolution>
      <algorithm name="topological_sort">
        <description>Resolve module dependencies using topological sorting</description>
        <steps>
          <step>Build dependency graph from module declarations</step>
          <step>Identify circular dependencies and flag as errors</step>
          <step>Sort modules in execution order respecting dependencies</step>
          <step>Validate that all dependencies are satisfiable</step>
        </steps>
        <error_handling>BLOCK execution if circular dependencies or missing modules</error_handling>
      </algorithm>
      
      <dependency_types>
        <hard_dependency>
          <description>Module cannot function without this dependency</description>
          <resolution>MUST be loaded before dependent module</resolution>
          <failure_impact>BLOCK dependent module execution</failure_impact>
        </hard_dependency>
        
        <soft_dependency>
          <description>Module can function with degraded capability</description>
          <resolution>SHOULD be loaded if available</resolution>
          <failure_impact>WARN but continue with limited functionality</failure_impact>
        </soft_dependency>
        
        <conditional_dependency>
          <description>Module needed only under specific conditions</description>
          <resolution>Load ONLY if conditions are met</resolution>
          <failure_impact>CONDITIONAL based on context criticality</failure_impact>
        </conditional_dependency>
      </dependency_types>
    </dependency_resolution>
    
    <interface_contracts>
      <input_contracts>
        <specification>Define expected input format and validation rules</specification>
        <validation>Validate inputs against contract before module execution</validation>
        <error_handling>BLOCK execution if input contract violations detected</error_handling>
      </input_contracts>
      
      <output_contracts>
        <specification>Define guaranteed output format and content</specification>
        <validation>Validate outputs against contract after module execution</validation>
        <error_handling>BLOCK dependent modules if output contract violations</error_handling>
      </output_contracts>
      
      <state_contracts>
        <specification>Define state modifications and side effects</specification>
        <validation>Validate state consistency after module execution</validation>
        <error_handling>ROLLBACK state changes if consistency violations</error_handling>
      </state_contracts>
    </interface_contracts>
  </dependency_management>
  
  <execution_patterns>
    <sequential_execution>
      <description>Execute modules one after another with state propagation</description>
      <use_cases>
        <use_case>Core module stack with inter-dependencies</use_case>
        <use_case>Quality gates requiring previous module results</use_case>
        <use_case>State-dependent workflow progression</use_case>
      </use_cases>
      <implementation>
        <step>Execute module N</step>
        <step>Validate module N output contract</step>
        <step>Propagate state to module N+1</step>
        <step>Continue until stack completion</step>
      </implementation>
      <error_handling>HALT execution on any module failure in sequence</error_handling>
    </sequential_execution>
    
    <parallel_execution>
      <description>Execute independent modules simultaneously for performance</description>
      <use_cases>
        <use_case>Support modules without inter-dependencies</use_case>
        <use_case>Analysis modules operating on same input</use_case>
        <use_case>Validation modules checking different aspects</use_case>
      </use_cases>
      <implementation>
        <step>Identify modules without dependencies</step>
        <step>Execute modules in parallel using batch operations</step>
        <step>Collect and validate all outputs</step>
        <step>Consolidate results for next sequential step</step>
      </implementation>
      <error_handling>COLLECT all errors, continue if non-critical modules fail</error_handling>
    </parallel_execution>
    
    <conditional_execution>
      <description>Execute modules based on runtime condition evaluation</description>
      <use_cases>
        <use_case>Context-specific modules (security, performance, etc.)</use_case>
        <use_case>Error recovery and escalation modules</use_case>
        <use_case>Optional enhancement and optimization modules</use_case>
      </use_cases>
      <implementation>
        <step>Evaluate condition triggers for each conditional module</step>
        <step>Load and execute modules where conditions are met</step>
        <step>Skip modules where conditions are not satisfied</step>
        <step>Document conditional execution decisions</step>
      </implementation>
      <error_handling>EVALUATE criticality of failed conditional modules</error_handling>
    </conditional_execution>
  </execution_patterns>
  
  <module_execution_framework>
    <standard_module_block>
      <structure>
        &lt;module_execution enforcement="MANDATORY"&gt;
          &lt;core_stack order="sequential"&gt;
            &lt;module&gt;[category/module.md] - [description]&lt;/module&gt;
            &lt;module&gt;[category/module.md] - [description]&lt;/module&gt;
            &lt;module&gt;[category/module.md] - [description]&lt;/module&gt;
          &lt;/core_stack&gt;
          &lt;contextual_modules&gt;
            &lt;conditional module="[path]" condition="[trigger_condition]"/&gt;
            &lt;conditional module="[path]" condition="[trigger_condition]"/&gt;
          &lt;/contextual_modules&gt;
          &lt;support_modules order="parallel"&gt;
            &lt;module&gt;[category/module.md] - [description]&lt;/module&gt;
            &lt;module&gt;[category/module.md] - [description]&lt;/module&gt;
          &lt;/support_modules&gt;
        &lt;/module_execution&gt;
      </structure>
      
      <implementation_requirements>
        <requirement>Core stack MUST execute sequentially in defined order</requirement>
        <requirement>Contextual modules evaluated and loaded conditionally</requirement>
        <requirement>Support modules execute in parallel where possible</requirement>
        <requirement>Module failures handled according to enforcement level</requirement>
      </implementation_requirements>
    </standard_module_block>
    
    <command_specific_patterns>
      <task_command_pattern>
        <core_stack>
          <module>quality/critical-thinking.md - 30-second analysis foundation</module>
          <module>quality/tdd.md - Strict RED-GREEN-REFACTOR enforcement</module>
          <module>development/task-management.md - Task execution workflow</module>
          <module>quality/production-standards.md - Quality gate validation</module>
        </core_stack>
        <contextual_modules>
          <conditional module="patterns/session-management.md" condition="complex_task OR multiple_files"/>
          <conditional module="git/conventional-commits.md" condition="task_complete"/>
          <conditional module="quality/pre-commit.md" condition="code_changes"/>
        </contextual_modules>
      </task_command_pattern>
      
      <swarm_command_pattern>
        <core_stack>
          <module>quality/critical-thinking.md - 30-second multi-agent analysis</module>
          <module>patterns/session-management.md - GitHub coordination tracking</module>
          <module>patterns/multi-agent.md - Task() and Batch() coordination</module>
          <module>quality/tdd.md - Multi-agent TDD coordination</module>
          <module>patterns/git-operations.md - Worktree isolation and merge</module>
          <module>quality/production-standards.md - Cross-agent quality validation</module>
        </core_stack>
        <contextual_modules>
          <conditional module="quality/error-recovery.md" condition="agent_failures OR coordination_issues"/>
          <conditional module="development/code-review.md" condition="complex_integration"/>
        </contextual_modules>
      </swarm_command_pattern>
      
      <protocol_command_pattern>
        <core_stack>
          <module>quality/critical-thinking.md - Production-level analysis</module>
          <module>patterns/session-management.md - Compliance tracking session</module>
          <module>quality/production-standards.md - Comprehensive quality gates</module>
          <module>quality/tdd.md - Strictest TDD enforcement</module>
          <module>security/threat-modeling.md - Security analysis and testing</module>
          <module>quality/pre-commit.md - Production-grade validation</module>
        </core_stack>
        <contextual_modules>
          <conditional module="security/financial-compliance.md" condition="financial_system"/>
          <conditional module="patterns/multi-agent.md" condition="complex_system OR escalation_needed"/>
        </contextual_modules>
      </protocol_command_pattern>
    </command_specific_patterns>
  </module_execution_framework>
  
  <state_management>
    <execution_context>
      <context_components>
        <component name="command_state">Current command execution status and progress</component>
        <component name="module_results">Accumulated outputs from executed modules</component>
        <component name="quality_metrics">Quality gate results and compliance status</component>
        <component name="error_state">Error conditions and recovery actions taken</component>
        <component name="user_context">User requirements and preferences</component>
      </context_components>
      
      <state_propagation>
        <method name="context_passing">Pass execution context between modules</method>
        <method name="result_accumulation">Accumulate module outputs for later use</method>
        <method name="state_validation">Validate state consistency at each step</method>
        <method name="rollback_capability">Enable state rollback on critical failures</method>
      </state_propagation>
    </execution_context>
    
    <module_isolation>
      <isolation_principles>
        <principle>Modules cannot directly modify other module's state</principle>
        <principle>Inter-module communication through defined interfaces only</principle>
        <principle>Module failures isolated to prevent cascade failures</principle>
        <principle>Module state changes are atomic and reversible</principle>
      </isolation_principles>
      
      <communication_mechanisms>
        <mechanism name="input_contracts">Structured inputs validated before execution</mechanism>
        <mechanism name="output_contracts">Structured outputs validated after execution</mechanism>
        <mechanism name="event_system">Module events for coordination and monitoring</mechanism>
        <mechanism name="shared_resources">Controlled access to shared state and resources</mechanism>
      </communication_mechanisms>
    </module_isolation>
  </state_management>
  
  <error_handling_and_recovery>
    <error_classification>
      <module_load_errors>
        <description>Failures during module discovery or loading</description>
        <causes>Missing modules, dependency conflicts, interface mismatches</causes>
        <recovery>Fallback to alternative modules, graceful degradation</recovery>
        <escalation>BLOCK execution if core modules unavailable</escalation>
      </module_load_errors>
      
      <module_execution_errors>
        <description>Failures during module execution</description>
        <causes>Invalid inputs, runtime errors, resource constraints</causes>
        <recovery>Module retry, alternative execution paths, error isolation</recovery>
        <escalation>CONDITIONAL based on module criticality</escalation>
      </module_execution_errors>
      
      <integration_errors>
        <description>Failures during module result integration</description>
        <causes>Contract violations, state inconsistencies, resource conflicts</causes>
        <recovery>State rollback, conflict resolution, manual intervention</recovery>
        <escalation>BLOCK until integration consistency restored</escalation>
      </integration_errors>
    </error_classification>
    
    <recovery_strategies>
      <graceful_degradation>
        <description>Continue execution with reduced functionality</description>
        <application>Non-critical module failures, optional feature unavailability</application>
        <implementation>Skip failed modules, use alternative implementations</implementation>
      </graceful_degradation>
      
      <retry_mechanisms>
        <description>Attempt module execution multiple times</description>
        <application>Transient failures, resource contention, network issues</application>
        <implementation>Exponential backoff, circuit breaker patterns</implementation>
      </retry_mechanisms>
      
      <escalation_protocols>
        <description>Transfer to higher-level error handling</description>
        <application>Critical failures, unrecoverable errors, system-wide issues</application>
        <implementation>Command-level error handling, user notification, manual intervention</implementation>
      </escalation_protocols>
    </recovery_strategies>
  </error_handling_and_recovery>
  
  <performance_optimization>
    <execution_optimization>
      <parallel_module_execution>
        <description>Execute independent modules simultaneously</description>
        <benefits>70% faster execution for parallel-eligible modules</benefits>
        <implementation>Identify dependency-free modules, batch execution</implementation>
      </parallel_module_execution>
      
      <module_caching>
        <description>Cache module results for repeated executions</description>
        <benefits>Avoid redundant computation for identical inputs</benefits>
        <implementation>Content-based caching, cache invalidation strategies</implementation>
      </module_caching>
      
      <lazy_loading>
        <description>Load modules only when needed</description>
        <benefits>Reduced memory usage, faster startup times</benefits>
        <implementation>Conditional module loading, just-in-time resolution</implementation>
      </lazy_loading>
    </execution_optimization>
    
    <resource_management>
      <memory_efficiency>
        <strategy>Release module resources after execution</strategy>
        <strategy>Share common resources between compatible modules</strategy>
        <strategy>Use streaming for large data processing</strategy>
      </memory_efficiency>
      
      <cpu_optimization>
        <strategy>Optimize module execution order for CPU cache efficiency</strategy>
        <strategy>Use CPU-bound vs I/O-bound module classification</strategy>
        <strategy>Implement module execution time limits</strategy>
      </cpu_optimization>
    </resource_management>
  </performance_optimization>
  
  <monitoring_and_metrics>
    <execution_metrics>
      <metric name="module_execution_time">Time taken for each module execution</metric>
      <metric name="module_success_rate">Success/failure rate for each module</metric>
      <metric name="dependency_resolution_time">Time to resolve module dependencies</metric>
      <metric name="parallel_execution_efficiency">Speedup achieved through parallelization</metric>
    </execution_metrics>
    
    <quality_metrics>
      <metric name="module_compliance_rate">Percentage of modules passing quality gates</metric>
      <metric name="error_recovery_effectiveness">Success rate of error recovery mechanisms</metric>
      <metric name="state_consistency_validation">Frequency of state validation failures</metric>
      <metric name="integration_success_rate">Success rate of module result integration</metric>
    </quality_metrics>
    
    <continuous_improvement>
      <feedback_collection>Gather execution data for performance analysis</feedback_collection>
      <bottleneck_identification">Identify performance bottlenecks in module execution</bottleneck_identification>
      <optimization_opportunities">Discover opportunities for execution optimization</optimization_opportunities>
      <quality_enhancement">Improve module interfaces and execution patterns</quality_enhancement>
    </continuous_improvement>
  </monitoring_and_metrics>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for execution patterns and mechanisms
      quality/production-standards.md for quality gate integration
      quality/critical-thinking.md for analysis module integration
      patterns/intelligent-routing.md for dynamic module selection
    </depends_on>
    <provides_to>
      All commands for standardized module composition and execution
      quality/framework-metrics.md for execution metrics and monitoring
      patterns/pattern-library.md for composition pattern implementations
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">modular_composition</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">dependency_injection</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">execution_orchestration</uses_pattern>
    <implementation_notes>
      Module composition follows modular_composition pattern for clean separation
      Dependencies managed through dependency_injection pattern for flexibility
      Execution orchestrated using execution_orchestration pattern for consistency
      Framework provides foundation for deterministic module execution
    </implementation_notes>
  </pattern_usage>
  
</module>
```