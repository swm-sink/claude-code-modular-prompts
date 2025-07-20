# God Object Prevention Module

| module | version | last_updated | status |
|--------|---------|--------------|--------|
| god-object-prevention | 1.0.0 | 2025-07-20 | production |

## Purpose

Detect, prevent, and refactor god objects in LLM-generated code through pattern recognition, early detection, and automated refactoring suggestions.

## God Object Detection Rules

### Primary Detection Patterns

```xml
<god_object_patterns enforcement="BLOCKING">
  <size_indicators>
    <lines_of_code>Classes >200 lines</lines_of_code>
    <method_count>Classes >15 methods</method_count>
    <public_interface>Classes >10 public methods</public_interface>
    <field_count>Classes >12 instance variables</field_count>
  </size_indicators>
  
  <responsibility_indicators>
    <mixed_concerns>Multiple unrelated responsibilities</mixed_concerns>
    <data_and_behavior>Both data container and business logic</data_and_behavior>
    <coordination_and_implementation>Both orchestration and execution</coordination_and_implementation>
    <ui_and_business>Both presentation and business logic</ui_and_business>
  </responsibility_indicators>
  
  <coupling_indicators>
    <high_fan_out>Dependencies on >10 other classes</high_fan_out>
    <central_dependency>Many classes depend on this one</central_dependency>
    <import_explosion>Imports from >8 different modules</import_explosion>
    <parameter_proliferation>Methods with >5 parameters</parameter_proliferation>
  </coupling_indicators>
</god_object_patterns>
```

### Detection Algorithm

```xml
<detection_algorithm>
  <scoring_system>
    <size_score>
      <lines>1 point per 50 lines over 100</lines>
      <methods>2 points per method over 8</methods>
      <fields>1 point per field over 6</fields>
    </size_score>
    
    <responsibility_score>
      <concerns>5 points per additional concern</concerns>
      <abstraction_levels>3 points per level mixed</abstraction_levels>
      <domain_mixing>4 points per domain boundary crossed</domain_mixing>
    </responsibility_score>
    
    <coupling_score>
      <dependencies>1 point per dependency over 5</dependencies>
      <dependents>2 points per dependent over 3</dependents>
      <circular_refs>10 points per circular dependency</circular_refs>
    </coupling_score>
  </scoring_system>
  
  <thresholds>
    <warning>Score 8-15: Review recommended</warning>
    <critical>Score 16-25: Refactoring required</critical>
    <blocking>Score >25: Implementation blocked</blocking>
  </thresholds>
</detection_algorithm>
```

## Refactoring Triggers

### Automatic Triggers

```xml
<automatic_triggers>
  <size_triggers>
    <trigger threshold="200_lines">
      <action>Suggest class decomposition</action>
      <patterns>Extract class, Extract subclass</patterns>
    </trigger>
    
    <trigger threshold="15_methods">
      <action>Identify method groupings</action>
      <patterns>Extract class, Strategy pattern</patterns>
    </trigger>
    
    <trigger threshold="10_public_methods">
      <action>Analyze interface complexity</action>
      <patterns>Facade pattern, Interface segregation</patterns>
    </trigger>
  </size_triggers>
  
  <complexity_triggers>
    <trigger threshold="mixed_concerns">
      <action>Separate concerns</action>
      <patterns>Single responsibility principle</patterns>
    </trigger>
    
    <trigger threshold="high_coupling">
      <action>Reduce dependencies</action>
      <patterns>Dependency injection, Observer pattern</patterns>
    </trigger>
    
    <trigger threshold="central_control">
      <action>Distribute responsibilities</action>
      <patterns>Command pattern, Event-driven architecture</patterns>
    </trigger>
  </complexity_triggers>
</automatic_triggers>
```

### Manual Review Triggers

```xml
<manual_review_triggers>
  <code_review_points>
    <new_class_creation>Review any new class >100 lines</new_class_creation>
    <method_addition>Review when adding method to large class</method_addition>
    <responsibility_change>Review when changing class purpose</responsibility_change>
  </code_review_points>
  
  <architectural_reviews>
    <feature_completion>Review major feature implementations</feature_completion>
    <integration_points>Review system integration classes</integration_points>
    <performance_optimization>Review after performance changes</performance_optimization>
  </architectural_reviews>
</manual_review_triggers>
```

## Refactoring Patterns

### Extract Class Pattern

```xml
<extract_class_pattern>
  <identification>
    <step>Identify cohesive method groups</step>
    <step>Find related data and behavior</step>
    <step>Locate natural boundaries</step>
    <step>Assess coupling between groups</step>
  </identification>
  
  <extraction_process>
    <step>Create new class for extracted functionality</step>
    <step>Move related methods and fields</step>
    <step>Establish communication interface</step>
    <step>Update original class to delegate</step>
    <step>Test extraction thoroughly</step>
  </extraction_process>
  
  <validation>
    <single_responsibility>Each class has one reason to change</single_responsibility>
    <loose_coupling>Minimal dependencies between classes</loose_coupling>
    <high_cohesion>Related functionality grouped together</high_cohesion>
  </validation>
</extract_class_pattern>
```

### Strategy Pattern Application

```xml
<strategy_pattern>
  <when_to_apply>
    <multiple_algorithms>Class contains different ways to do same thing</multiple_algorithms>
    <conditional_complexity>Many if-else or switch statements</conditional_complexity>
    <algorithm_variation>Behavior varies based on context</algorithm_variation>
  </when_to_apply>
  
  <implementation_steps>
    <step>Define strategy interface</step>
    <step>Extract each algorithm to strategy class</step>
    <step>Update context to use strategy</step>
    <step>Enable strategy switching</step>
    <step>Test all strategy combinations</step>
  </implementation_steps>
  
  <benefits>
    <flexibility>Easy to add new algorithms</flexibility>
    <testability>Each algorithm testable in isolation</testability>
    <maintainability>Changes isolated to specific strategies</maintainability>
  </benefits>
</strategy_pattern>
```

### Facade Pattern for Complexity

```xml
<facade_pattern>
  <when_to_apply>
    <complex_subsystem>Class manages many complex interactions</complex_subsystem>
    <client_simplification>Clients need simple interface</client_simplification>
    <layered_architecture>Need to hide lower-level complexity</layered_architecture>
  </when_to_apply>
  
  <implementation_approach>
    <step>Identify client use cases</step>
    <step>Design simplified interface</step>
    <step>Create facade class</step>
    <step>Delegate to subsystem components</step>
    <step>Hide complex interactions</step>
  </implementation_approach>
  
  <design_principles>
    <simplicity>Facade provides simple methods for complex operations</simplicity>
    <delegation>Facade delegates to specialized components</delegation>
    <abstraction>Hide implementation details from clients</abstraction>
  </design_principles>
</facade_pattern>
```

## Prevention Protocols

### Design-Time Prevention

```xml
<design_time_prevention>
  <planning_phase>
    <single_responsibility>Plan each class with one clear purpose</single_responsibility>
    <size_estimation>Estimate implementation size before coding</size_estimation>
    <interface_design>Design minimal, focused interfaces</interface_design>
    <dependency_planning>Plan dependencies and collaborations</dependency_planning>
  </planning_phase>
  
  <architectural_patterns>
    <use_composition>Favor composition over inheritance</use_composition>
    <apply_solid>Follow SOLID design principles</apply_solid>
    <domain_modeling>Model domain concepts explicitly</domain_modeling>
    <layered_design>Separate concerns into layers</layered_design>
  </architectural_patterns>
</design_time_prevention>
```

### Implementation-Time Prevention

```xml
<implementation_time_prevention>
  <continuous_monitoring>
    <size_tracking>Monitor class size during development</size_tracking>
    <responsibility_review>Regular responsibility assessment</responsibility_review>
    <coupling_analysis>Track dependencies as they're added</coupling_analysis>
  </continuous_monitoring>
  
  <refactoring_discipline>
    <early_extraction>Extract classes when patterns emerge</early_extraction>
    <test_driven_design>Use TDD to guide class design</test_driven_design>
    <incremental_improvement>Regular refactoring sessions</incremental_improvement>
  </refactoring_discipline>
</implementation_time_prevention>
```

## Framework Integration

### Command Integration

```xml
<command_integration>
  <task_command>
    <validation>Check for god object patterns before implementation</validation>
    <guidance>Suggest decomposition if complexity detected</guidance>
    <enforcement>Block creation of obvious god objects</enforcement>
  </task_command>
  
  <feature_command>
    <planning>Include god object prevention in feature planning</planning>
    <architecture>Design multiple collaborating classes</architecture>
    <validation>Review feature architecture for god objects</validation>
  </feature_command>
  
  <swarm_command>
    <coordination>Distribute responsibilities across agents</coordination>
    <boundaries>Establish clear class boundaries</boundaries>
    <integration>Ensure proper separation of concerns</integration>
  </swarm_command>
</command_integration>
```

### Quality Gate Integration

```xml
<quality_gate_integration>
  <pre_implementation>
    <architectural_review>Review class design for god object risk</architectural_review>
    <size_estimation>Estimate final class size</size_estimation>
    <responsibility_planning>Plan single responsibility adherence</responsibility_planning>
  </pre_implementation>
  
  <during_implementation>
    <size_monitoring>Track class growth in real-time</size_monitoring>
    <complexity_alerts>Alert when approaching thresholds</complexity_alerts>
    <refactoring_suggestions>Suggest improvements immediately</refactoring_suggestions>
  </during_implementation>
  
  <post_implementation>
    <god_object_scan>Full analysis for god object patterns</god_object_scan>
    <refactoring_requirements>Mandate refactoring if detected</refactoring_requirements>
    <architectural_documentation>Document class responsibilities</architectural_documentation>
  </post_implementation>
</quality_gate_integration>
```

## Real Framework Examples

### Framework God Objects Detected

```xml
<framework_examples>
  <potential_god_objects>
    <example>
      <class>Large command modules with mixed concerns</class>
      <issues>Command parsing, execution, and validation mixed</issues>
      <refactoring>Split into CommandParser, CommandExecutor, CommandValidator</refactoring>
    </example>
    
    <example>
      <class>Meta-framework control modules</class>
      <issues>Multiple meta-operations in single class</issues>
      <refactoring>Extract strategy classes for each operation type</refactoring>
    </example>
  </potential_god_objects>
  
  <good_examples>
    <example>
      <class>TDD cycle pattern module</class>
      <strength>Single responsibility: TDD workflow</strength>
      <size>Under 200 lines with clear structure</size>
    </example>
    
    <example>
      <class>Session management components</class>
      <strength>Focused on session concerns only</strength>
      <design>Uses composition for complex functionality</design>
    </example>
  </good_examples>
</framework_examples>
```

## Metrics and Reporting

### Detection Metrics

```xml
<detection_metrics>
  <god_object_count>Number of classes exceeding thresholds</god_object_count>
  <severity_distribution>Breakdown by warning/critical/blocking levels</severity_distribution>
  <refactoring_success>Classes successfully refactored</refactoring_success>
  <prevention_effectiveness>God objects prevented vs. created</prevention_effectiveness>
</detection_metrics>
```

### Quality Improvement Tracking

```xml
<quality_tracking>
  <before_after_analysis>
    <maintainability>Code maintainability improvements</maintainability>
    <testability>Testing ease improvements</testability>
    <performance>Performance impact of refactoring</performance>
  </before_after_analysis>
  
  <trend_analysis>
    <god_object_trends>Trends in god object creation</god_object_trends>
    <refactoring_patterns>Most effective refactoring approaches</refactoring_patterns>
    <prevention_success>Prevention strategy effectiveness</prevention_success>
  </trend_analysis>
</quality_tracking>
```

## Success Criteria

```xml
<success_criteria>
  <quantitative_targets>
    <detection_rate>95% of god objects detected automatically</detection_rate>
    <prevention_rate>80% reduction in god object creation</prevention_rate>
    <refactoring_success>90% of detected god objects successfully refactored</refactoring_success>
    <false_positive_rate><5% false positive detection rate</false_positive_rate>
  </quantitative_targets>
  
  <qualitative_targets>
    <code_quality>Improved maintainability and readability</code_quality>
    <architectural_health>Better separation of concerns</architectural_health>
    <development_velocity>Faster development through better structure</development_velocity>
    <team_adoption>High adoption of prevention practices</team_adoption>
  </qualitative_targets>
</success_criteria>
```