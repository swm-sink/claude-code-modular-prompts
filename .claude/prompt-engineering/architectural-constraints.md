# Architectural Constraints Framework

| module | version | last_updated | status |
|--------|---------|--------------|--------|
| architectural-constraints | 1.0.0 | 2025-07-20 | production |

## Purpose

Enforce architectural discipline in LLM-generated code through mandatory constraints that prevent common anti-patterns and ensure maintainable, readable code structures.

## Core Constraints

### File Size Limits

```xml
<file_size_constraints enforcement="BLOCKING">
  <max_file_size>500 lines</max_file_size>
  <critical_threshold>300 lines - requires justification</critical_threshold>
  <emergency_threshold>200 lines - preferred maximum</emergency_threshold>
  
  <enforcement_rules>
    <rule>Files >500 lines BLOCKED from creation</rule>
    <rule>Files >300 lines require architectural justification</rule>
    <rule>Files >200 lines trigger refactoring suggestions</rule>
  </enforcement_rules>
  
  <exemptions>
    <config_files>XML, JSON configuration files up to 1000 lines</config_files>
    <test_files>Integration tests up to 800 lines with justification</test_files>
    <generated_code>Auto-generated files marked with headers</generated_code>
  </exemptions>
</file_size_constraints>
```

### Class Size Limits

```xml
<class_size_constraints enforcement="BLOCKING">
  <max_methods>15 methods per class</max_methods>
  <max_lines>200 lines per class</max_lines>
  <max_public_methods>10 public methods</max_public_methods>
  
  <enforcement_rules>
    <rule>Classes >15 methods BLOCKED</rule>
    <rule>Classes >200 lines require refactoring</rule>
    <rule>Classes >10 public methods trigger interface extraction</rule>
  </enforcement_rules>
  
  <refactoring_triggers>
    <composition>Extract collaborator objects</composition>
    <inheritance>Use template method pattern</inheritance>
    <strategy>Extract algorithms to strategy classes</strategy>
    <facade>Create facade for complex subsystems</facade>
  </refactoring_triggers>
</class_size_constraints>
```

### Method Size Limits

```xml
<method_size_constraints enforcement="BLOCKING">
  <max_lines>25 lines per method</max_lines>
  <max_parameters>5 parameters per method</max_parameters>
  <max_complexity>10 cyclomatic complexity</max_complexity>
  
  <enforcement_rules>
    <rule>Methods >25 lines BLOCKED</rule>
    <rule>Methods >5 parameters require parameter objects</rule>
    <rule>Methods >10 complexity require decomposition</rule>
  </enforcement_rules>
  
  <decomposition_patterns>
    <extract_method>Break into smaller focused methods</extract_method>
    <parameter_object>Group related parameters</parameter_object>
    <command_pattern>Encapsulate operations</command_pattern>
    <state_machine>Extract state transitions</state_machine>
  </decomposition_patterns>
</method_size_constraints>
```

## Constraint Enforcement Patterns

### Pre-Implementation Validation

```xml
<pre_implementation_validation>
  <thinking_pattern>
    <step>1. Analyze planned implementation size</step>
    <step>2. Check against constraint limits</step>
    <step>3. Plan decomposition if needed</step>
    <step>4. Design interfaces and contracts</step>
    <step>5. Validate architectural compliance</step>
  </thinking_pattern>
  
  <validation_checklist>
    <file_size>Will this file exceed 200 lines?</file_size>
    <class_design>Will this class have >10 methods?</class_design>
    <method_design>Will any method exceed 25 lines?</method_design>
    <complexity>Will any method be complex?</complexity>
    <responsibilities>Does each class have single responsibility?</responsibilities>
  </validation_checklist>
</pre_implementation_validation>
```

### Decomposition Strategies

```xml
<decomposition_strategies>
  <large_files>
    <strategy>Split by functional domains</strategy>
    <strategy>Extract utilities to separate files</strategy>
    <strategy>Create focused modules</strategy>
    <strategy>Use composition over inheritance</strategy>
  </large_files>
  
  <large_classes>
    <strategy>Extract collaborator objects</strategy>
    <strategy>Use delegation patterns</strategy>
    <strategy>Apply single responsibility principle</strategy>
    <strategy>Create focused interfaces</strategy>
  </large_classes>
  
  <large_methods>
    <strategy>Extract helper methods</strategy>
    <strategy>Use parameter objects</strategy>
    <strategy>Apply command pattern</strategy>
    <strategy>Create focused algorithms</strategy>
  </large_methods>
</decomposition_strategies>
```

### Real Framework Examples

```xml
<framework_examples>
  <good_example>
    <file>.claude/modules/patterns/tdd-cycle-pattern.md</file>
    <size>180 lines</size>
    <structure>Single responsibility, clear sections, focused content</structure>
    <compliance>Meets all size constraints</compliance>
  </good_example>
  
  <needs_refactoring>
    <file>Large command modules</file>
    <issue>Multiple responsibilities in single file</issue>
    <solution>Split into command + execution + validation modules</solution>
  </needs_refactoring>
  
  <anti_pattern>
    <description>God modules with 1000+ lines</description>
    <detection>Files with mixed concerns</detection>
    <prevention>Enforce single responsibility</prevention>
  </anti_pattern>
</framework_examples>
```

## Validation Mechanisms

### Automated Checking

```xml
<automated_checking>
  <pre_commit_hooks>
    <line_count_check>Block files >500 lines</line_count_check>
    <complexity_check>Analyze cyclomatic complexity</complexity_check>
    <structure_check>Validate single responsibility</structure_check>
  </pre_commit_hooks>
  
  <real_time_validation>
    <size_monitoring>Track file growth during development</size_monitoring>
    <complexity_alerts>Warn when approaching limits</complexity_alerts>
    <refactoring_suggestions>Propose decomposition strategies</refactoring_suggestions>
  </real_time_validation>
</automated_checking>
```

### Manual Review Points

```xml
<manual_review_points>
  <checkpoint_1>Before implementing new features</checkpoint_1>
  <checkpoint_2>During code review process</checkpoint_2>
  <checkpoint_3>Before merging to main branch</checkpoint_3>
  <checkpoint_4>During architecture reviews</checkpoint_4>
</manual_review_points>
```

## Integration with TDD

```xml
<tdd_integration>
  <red_phase>
    <constraint>Write minimal failing test</constraint>
    <validation>Test should be <50 lines</validation>
    <focus>Single responsibility testing</focus>
  </red_phase>
  
  <green_phase>
    <constraint>Implement minimal passing code</constraint>
    <validation>Implementation should be <100 lines</validation>
    <decomposition>Split if approaching limits</decomposition>
  </green_phase>
  
  <refactor_phase>
    <constraint>Maintain or improve structure</constraint>
    <validation>Ensure all constraints still met</validation>
    <opportunity>Apply decomposition patterns</opportunity>
  </refactor_phase>
</tdd_integration>
```

## Error Prevention

```xml
<error_prevention>
  <common_mistakes>
    <mistake>Creating monolithic files</mistake>
    <prevention>Enforce size limits early</prevention>
    
    <mistake>God objects with many responsibilities</mistake>
    <prevention>Single responsibility validation</prevention>
    
    <mistake>Complex methods with many branches</mistake>
    <prevention>Complexity monitoring</prevention>
  </common_mistakes>
  
  <early_detection>
    <threshold_warnings>Alert at 80% of limits</threshold_warnings>
    <architectural_review>Required for large implementations</architectural_review>
    <decomposition_planning>Mandatory for complex features</decomposition_planning>
  </early_detection>
</error_prevention>
```

## Metrics and Monitoring

```xml
<metrics_monitoring>
  <size_metrics>
    <files>Average file size, distribution, outliers</files>
    <classes>Method count distribution, size trends</classes>
    <methods>Line count, parameter count, complexity</methods>
  </size_metrics>
  
  <quality_metrics>
    <maintainability>Code readability scores</maintainability>
    <testability>Test coverage by component size</testability>
    <modularity>Coupling and cohesion measurements</modularity>
  </quality_metrics>
  
  <trend_analysis>
    <growth_patterns>Track file size growth over time</growth_patterns>
    <refactoring_impact>Measure improvement after decomposition</refactoring_impact>
    <constraint_violations>Monitor and trend violations</constraint_violations>
  </trend_analysis>
</metrics_monitoring>
```

## Framework Integration

```xml
<framework_integration>
  <command_integration>
    <task_command>Enforce constraints during single-task development</task_command>
    <feature_command>Apply constraints to feature implementation</feature_command>
    <swarm_command>Coordinate constraint enforcement across agents</swarm_command>
  </command_integration>
  
  <quality_gates>
    <gate_1>Size constraint validation</gate_1>
    <gate_2>Complexity threshold checking</gate_2>
    <gate_3>Single responsibility verification</gate_3>
    <gate_4>Decomposition requirement assessment</gate_4>
  </quality_gates>
  
  <enforcement_workflow>
    <pre_implementation>Constraint planning and validation</pre_implementation>
    <during_implementation>Real-time monitoring and alerts</during_implementation>
    <post_implementation>Compliance verification and reporting</post_implementation>
  </enforcement_workflow>
</framework_integration>
```

## Success Criteria

```xml
<success_criteria>
  <quantitative>
    <constraint>95% of files under 300 lines</constraint>
    <constraint>90% of classes under 10 methods</constraint>
    <constraint>95% of methods under 20 lines</constraint>
    <constraint>Zero blocking violations in production</constraint>
  </quantitative>
  
  <qualitative>
    <maintainability>Code is easy to understand and modify</maintainability>
    <testability>Components are easily testable in isolation</testability>
    <modularity>Clear separation of concerns</modularity>
    <reliability>Consistent enforcement across all development</reliability>
  </qualitative>
</success_criteria>
```