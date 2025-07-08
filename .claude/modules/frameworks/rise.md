| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# RISE Framework Module (Role, Input, Steps, Expectation)

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="rise_framework" category="frameworks">
  
  <purpose>
    Implement RISE (Role, Input, Steps, Expectation) framework for structured, actionable prompts with clear role clarity and systematic execution patterns optimized for Claude 4 capabilities.
  </purpose>
  
  <framework_definition>
    <name>RISE (Role, Input, Steps, Expectation)</name>
    <origin>Community Framework Analysis - 2025 Advanced Prompting Frameworks</origin>
    <purpose>Structured approach for clear, actionable prompts requiring role clarity</purpose>
    <best_for>Complex multi-step tasks requiring role clarity and systematic execution</best_for>
    <complexity_range>Moderate to Complex (suitable for tasks requiring 3-10 steps)</complexity_range>
  </framework_definition>
  
  <rise_components>
    <role_component>
      <description>Define Claude's specific role and expertise level for the task</description>
      <purpose>Establishes context, authority, and appropriate knowledge depth</purpose>
      <patterns>
        <pattern name="expertise_role">Senior Software Architect, Security Specialist, Performance Engineer</pattern>
        <pattern name="functional_role">Code Reviewer, System Analyst, Technical Writer</pattern>
        <pattern name="hybrid_role">Senior DevOps Engineer with Security Focus</pattern>
      </patterns>
      <claude_4_optimization>
        <thinking_integration>Role selection triggers appropriate domain knowledge activation</thinking_integration>
        <context_efficiency>Role context loads relevant expertise patterns efficiently</context_efficiency>
      </claude_4_optimization>
    </role_component>
    
    <input_component>
      <description>Clearly specify what data/context Claude will work with</description>
      <purpose>Defines scope, constraints, and available information</purpose>
      <patterns>
        <pattern name="codebase_input">Codebase with 50+ microservices and legacy components</pattern>
        <pattern name="data_input">Performance metrics, log files, user feedback data</pattern>
        <pattern name="document_input">Technical specifications, API documentation, requirements</pattern>
      </patterns>
      <claude_4_optimization>
        <parallel_loading>Input analysis can be parallelized for efficiency</parallel_loading>
        <context_management>Hierarchical input loading based on relevance</context_management>
      </claude_4_optimization>
    </input_component>
    
    <steps_component>
      <description>Break down the process into clear, sequential actions</description>
      <purpose>Provides systematic execution path with validation checkpoints</purpose>
      <patterns>
        <pattern name="analysis_steps">1. Analyze dependencies 2. Identify bottlenecks 3. Propose solutions</pattern>
        <pattern name="implementation_steps">1. Design interfaces 2. Write tests 3. Implement 4. Validate</pattern>
        <pattern name="review_steps">1. Security scan 2. Performance check 3. Code review 4. Documentation</pattern>
      </patterns>
      <claude_4_optimization>
        <parallel_execution>Independent steps can be executed in parallel for 70% improvement</parallel_execution>
        <thinking_checkpoints>Each step includes critical thinking validation</thinking_checkpoints>
      </claude_4_optimization>
    </steps_component>
    
    <expectation_component>
      <description>Define exact output format and success criteria</description>
      <purpose>Ensures deliverable clarity and measurable outcomes</purpose>
      <patterns>
        <pattern name="document_output">Architecture diagram + 3-page analysis report</pattern>
        <pattern name="code_output">Implementation with 90%+ test coverage and documentation</pattern>
        <pattern name="analysis_output">Findings summary with recommendations and priority ranking</pattern>
      </patterns>
      <claude_4_optimization>
        <validation_criteria>Measurable success criteria with evidence requirements</validation_criteria>
        <quality_gates>Expectation alignment with quality standards</quality_gates>
      </claude_4_optimization>
    </expectation_component>
  </rise_components>
  
  <implementation_patterns>
    <basic_rise_pattern>
      <structure>
        &lt;rise_framework&gt;
          &lt;role&gt;[Define Claude's expertise and perspective]&lt;/role&gt;
          &lt;input&gt;[Specify available data and context]&lt;/input&gt;
          &lt;steps&gt;
            1. [First systematic action]
            2. [Second systematic action]
            3. [Third systematic action]
            ...
          &lt;/steps&gt;
          &lt;expectation&gt;[Exact output format and success criteria]&lt;/expectation&gt;
        &lt;/rise_framework&gt;
      </structure>
      <usage>Standard RISE implementation for moderate complexity tasks</usage>
    </basic_rise_pattern>
    
    <enhanced_rise_pattern>
      <structure>
        &lt;rise_framework thinking_mode="interleaved" optimization="claude_4"&gt;
          &lt;role expertise_level="senior" domain="[specific_domain]"&gt;[Detailed role definition]&lt;/role&gt;
          &lt;input context_scope="[scope]" priority="[hierarchical]"&gt;[Comprehensive input specification]&lt;/input&gt;
          &lt;steps execution_mode="parallel_where_possible" validation="mandatory"&gt;
            &lt;step id="1" parallel_group="analysis"&gt;[Action with parallel optimization]&lt;/step&gt;
            &lt;step id="2" parallel_group="analysis"&gt;[Independent parallel action]&lt;/step&gt;
            &lt;step id="3" depends_on="1,2"&gt;[Sequential step after parallel completion]&lt;/step&gt;
          &lt;/steps&gt;
          &lt;expectation format="structured" validation="measurable"&gt;[Detailed output specification with success metrics]&lt;/expectation&gt;
        &lt;/rise_framework&gt;
      </structure>
      <usage>Advanced RISE with Claude 4 optimization for complex tasks</usage>
    </enhanced_rise_pattern>
    
    <tdd_integrated_rise_pattern>
      <structure>
        &lt;rise_framework tdd_enforcement="mandatory"&gt;
          &lt;role&gt;Senior Developer with TDD expertise&lt;/role&gt;
          &lt;input&gt;Requirements and existing test suite&lt;/input&gt;
          &lt;steps&gt;
            1. Analyze requirements for testability
            2. Write comprehensive failing tests FIRST
            3. Implement minimal code to pass tests
            4. Refactor while maintaining green tests
            5. Validate 90%+ coverage and quality gates
          &lt;/steps&gt;
          &lt;expectation&gt;Working feature with full test coverage and documentation&lt;/expectation&gt;
        &lt;/rise_framework&gt;
      </structure>
      <usage>RISE framework integrated with mandatory TDD enforcement</usage>
    </tdd_integrated_rise_pattern>
  </implementation_patterns>
  
  <use_case_scenarios>
    <architecture_analysis>
      <scenario>Analyzing complex system architecture for scalability improvements</scenario>
      <rise_application>
        <role>Senior Software Architect with 10+ years distributed systems experience</role>
        <input>Microservices codebase with performance metrics and scaling challenges</input>
        <steps>1. Map service dependencies 2. Identify bottlenecks 3. Design scaling solutions 4. Create implementation roadmap</steps>
        <expectation>Architecture diagram, bottleneck analysis, and 3-phase scaling plan</expectation>
      </rise_application>
    </architecture_analysis>
    
    <security_implementation>
      <scenario>Implementing comprehensive security measures for financial application</scenario>
      <rise_application>
        <role>Security Specialist with financial industry compliance expertise</role>
        <input>Payment processing system with PCI DSS requirements</input>
        <steps>1. Threat modeling 2. Security control design 3. Implementation with tests 4. Compliance validation</steps>
        <expectation>Secure implementation with threat model documentation and compliance report</expectation>
      </rise_application>
    </security_implementation>
    
    <performance_optimization>
      <scenario>Optimizing application performance for 10x user scale</scenario>
      <rise_application>
        <role>Performance Engineer with profiling and optimization expertise</role>
        <input>Application with performance benchmarks and scaling targets</input>
        <steps>1. Profile current performance 2. Identify optimization opportunities 3. Implement improvements 4. Validate performance gains</steps>
        <expectation>Optimized application with performance benchmarks and improvement documentation</expectation>
      </rise_application>
    </performance_optimization>
  </use_case_scenarios>
  
  <claude_4_optimization_features>
    <interleaved_thinking_integration>
      <purpose>Leverage Claude 4's 16K thinking capacity for sophisticated RISE execution</purpose>
      <implementation>
        <role_thinking>Deep analysis of role requirements and expertise activation</role_thinking>
        <input_thinking>Comprehensive context analysis and prioritization</input_thinking>
        <steps_thinking>Critical evaluation of each step's necessity and optimization</steps_thinking>
        <expectation_thinking>Validation of deliverable clarity and success criteria</expectation_thinking>
      </implementation>
      <triggers>Complex scenarios, ambiguous requirements, multi-domain expertise needed</triggers>
    </interleaved_thinking_integration>
    
    <parallel_execution_optimization>
      <purpose>Optimize RISE framework execution for 70% performance improvement</purpose>
      <implementation>
        <role_optimization>Role context loaded efficiently with domain expertise</role_optimization>
        <input_optimization>Parallel input analysis and context building</input_optimization>
        <steps_optimization>Independent steps executed in parallel with dependency management</steps_optimization>
        <expectation_optimization>Concurrent validation against multiple success criteria</expectation_optimization>
      </implementation>
      <performance_targets>70% reduction in execution time through intelligent parallelization</performance_targets>
    </parallel_execution_optimization>
    
    <context_window_efficiency>
      <purpose>Optimize 200K token window usage for comprehensive RISE execution</purpose>
      <implementation>
        <hierarchical_loading>Critical RISE components loaded first, supporting details as needed</hierarchical_loading>
        <token_budgeting>Optimal allocation across Role, Input, Steps, and Expectation components</token_budgeting>
        <lazy_evaluation>Load detailed context only when step execution requires it</lazy_evaluation>
      </implementation>
      <monitoring>Real-time token usage tracking with optimization triggers</monitoring>
    </context_window_efficiency>
  </claude_4_optimization_features>
  
  <integration_interfaces>
    <command_integration>
      <auto_command>Use RISE for complex routing decisions requiring role-based analysis</auto_command>
      <task_command>Apply RISE for structured single-component development tasks</task_command>
      <feature_command>Leverage RISE for comprehensive feature development planning</feature_command>
      <swarm_command>Use RISE for multi-agent coordination and role specialization</swarm_command>
    </command_integration>
    
    <module_integration>
      <thinking_patterns>Enhance thinking-pattern-template.md with RISE checkpoint integration</thinking_patterns>
      <quality_gates>Integrate RISE validation with universal-quality-gates.md</quality_gates>
      <session_management>Apply RISE for structured session planning and execution</session_management>
    </module_integration>
  </integration_interfaces>
  
  <validation_criteria>
    <completeness_check>
      <criterion>All four RISE components (Role, Input, Steps, Expectation) must be clearly defined</criterion>
      <criterion>Role specification must include expertise level and domain knowledge</criterion>
      <criterion>Input must define scope, constraints, and available information</criterion>
      <criterion>Steps must be sequential, actionable, and validation-ready</criterion>
      <criterion>Expectation must include measurable success criteria and output format</criterion>
    </completeness_check>
    
    <quality_validation>
      <criterion>Role matches task complexity and domain requirements</criterion>
      <criterion>Input specification enables successful task execution</criterion>
      <criterion>Steps are logically ordered with clear dependencies</criterion>
      <criterion>Expectations are achievable and measurable</criterion>
      <criterion>Framework application improves task clarity and success rate</criterion>
    </quality_validation>
    
    <claude_4_optimization_validation>
      <criterion>Parallel execution opportunities identified and leveraged</criterion>
      <criterion>Thinking integration enhances framework effectiveness</criterion>
      <criterion>Context efficiency optimized for 200K token window</criterion>
      <criterion>Performance improvement measurable and validated</criterion>
    </claude_4_optimization_validation>
  </validation_criteria>
  
  <usage_guidelines>
    <when_to_use_rise>
      <scenario>Complex tasks requiring role-based expertise</scenario>
      <scenario>Multi-step processes with clear sequential flow</scenario>
      <scenario>Tasks where role clarity significantly impacts output quality</scenario>
      <scenario>Situations requiring systematic approach with measurable outcomes</scenario>
    </when_to_use_rise>
    
    <when_not_to_use_rise>
      <scenario>Simple tasks that don't benefit from role specification</scenario>
      <scenario>Tasks where steps are highly parallel with no clear sequence</scenario>
      <scenario>Scenarios where role is obvious or irrelevant</scenario>
      <scenario>Quick operations where framework overhead exceeds benefits</scenario>
    </when_not_to_use_rise>
    
    <framework_selection_guidance>
      <simple_tasks>Consider APE or CARE frameworks for lighter overhead</simple_tasks>
      <complex_analysis>Use CLEAR or CRISP for more comprehensive structure</complex_analysis>
      <problem_solving>Consider SPARK framework for debugging scenarios</problem_solving>
      <strategic_planning>Use SOAR for high-level planning tasks</strategic_planning>
    </framework_selection_guidance>
  </usage_guidelines>
  
  <performance_metrics>
    <effectiveness_indicators>
      <metric name="task_completion_rate">Percentage of RISE-structured tasks completed successfully</metric>
      <metric name="clarity_improvement">Reduction in clarification requests when using RISE</metric>
      <metric name="execution_efficiency">Time reduction through systematic step execution</metric>
      <metric name="quality_consistency">Consistent output quality across similar RISE tasks</metric>
    </effectiveness_indicators>
    
    <optimization_tracking>
      <metric name="parallel_execution_utilization">Percentage of steps executed in parallel</metric>
      <metric name="context_efficiency">Token usage optimization through RISE structure</metric>
      <metric name="thinking_integration_depth">Quality of role-based thinking integration</metric>
      <metric name="framework_overhead">Time/token cost of RISE implementation vs benefits</metric>
    </optimization_tracking>
  </performance_metrics>
  
  <integration_points>
    <depends_on>
      patterns/thinking-pattern-template.md for checkpoint integration
      quality/universal-quality-gates.md for validation standards
      patterns/module-composition-framework.md for execution orchestration
    </depends_on>
    <provides_to>
      All commands for structured task execution with role clarity
      frameworks/framework-selector.md for automatic framework selection
      quality/framework-metrics.md for RISE effectiveness measurement
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">structured_execution</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">role_based_processing</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">systematic_validation</uses_pattern>
    <implementation_notes>
      RISE framework implements structured_execution pattern for systematic task completion
      Role component uses role_based_processing pattern for expertise activation
      Validation follows systematic_validation pattern for consistent quality
      Framework provides foundation for role-aware task execution
    </implementation_notes>
  </pattern_usage>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Core RISE framework implementation for structured, role-based task execution with Claude 4 optimization and systematic validation patterns.