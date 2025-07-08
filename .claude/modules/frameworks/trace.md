| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# TRACE Framework Module (Task, Request, Action, Context, Expectation)

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="trace_framework" category="frameworks">
  
  <purpose>
    Implement TRACE (Task, Request, Action, Context, Expectation) framework for comprehensive, detailed prompts with explicit context management and systematic execution patterns optimized for Claude 4 capabilities.
  </purpose>
  
  <framework_definition>
    <name>TRACE (Task, Request, Action, Context, Expectation)</name>
    <origin>Community Framework Analysis - 2025 Advanced Prompting Frameworks</origin>
    <purpose>Comprehensive approach for complex, context-heavy prompts requiring detailed specification</purpose>
    <best_for>Complex multi-step tasks requiring explicit context management and detailed execution</best_for>
    <complexity_range>Moderate to Very Complex (suitable for tasks requiring 5-20 steps with rich context)</complexity_range>
  </framework_definition>
  
  <trace_components>
    <task_component>
      <description>Define the overall objective and scope with clear boundaries</description>
      <purpose>Establishes high-level goal and success criteria for the entire workflow</purpose>
      <patterns>
        <pattern name="development_task">Implement secure payment processing system with compliance validation</pattern>
        <pattern name="analysis_task">Comprehensive security audit of microservices architecture</pattern>
        <pattern name="optimization_task">Performance optimization for real-time data processing pipeline</pattern>
      </patterns>
      <claude_4_optimization>
        <thinking_integration>Task clarity triggers appropriate domain-specific reasoning patterns</thinking_integration>
        <scope_management>Clear task boundaries prevent scope creep and optimize context usage</scope_management>
      </claude_4_optimization>
    </task_component>
    
    <request_component>
      <description>Specify exact deliverables and requirements in granular detail</description>
      <purpose>Defines precise outputs, constraints, and quality standards</purpose>
      <patterns>
        <pattern name="code_request">Working implementation with 90%+ test coverage, security validation, and documentation</pattern>
        <pattern name="analysis_request">Comprehensive report with findings, recommendations, and implementation roadmap</pattern>
        <pattern name="design_request">Architecture diagrams, API specifications, and integration documentation</pattern>
      </patterns>
      <claude_4_optimization>
        <parallel_validation>Request components can be validated independently for efficiency</parallel_validation>
        <quality_alignment>Request specifications directly map to quality gate requirements</quality_alignment>
      </claude_4_optimization>
    </request_component>
    
    <action_component>
      <description>Define specific, executable steps with dependencies and validation</description>
      <purpose>Provides detailed execution roadmap with checkpoints and error recovery</purpose>
      <patterns>
        <pattern name="implementation_actions">1. Design interfaces 2. Write comprehensive tests 3. Implement core logic 4. Integration testing 5. Security validation</pattern>
        <pattern name="analysis_actions">1. Data collection 2. Pattern analysis 3. Vulnerability assessment 4. Risk evaluation 5. Recommendation synthesis</pattern>
        <pattern name="coordination_actions">1. Team synchronization 2. Work stream setup 3. Progress monitoring 4. Integration management 5. Quality validation</pattern>
      </patterns>
      <claude_4_optimization>
        <parallel_execution>Independent actions identified for concurrent execution (70% improvement)</parallel_execution>
        <dependency_management>Clear action dependencies for optimal execution sequencing</dependency_management>
      </claude_4_optimization>
    </action_component>
    
    <context_component>
      <description>Comprehensive environmental and situational information</description>
      <purpose>Provides all necessary background, constraints, and operational context</purpose>
      <patterns>
        <pattern name="technical_context">Current architecture, technology stack, performance requirements, security constraints</pattern>
        <pattern name="business_context">User requirements, business goals, compliance needs, timeline constraints</pattern>
        <pattern name="operational_context">Team structure, resource availability, deployment environment, maintenance requirements</pattern>
      </patterns>
      <claude_4_optimization>
        <hierarchical_context>Context loaded in priority order for optimal token utilization</hierarchical_context>
        <dynamic_expansion>Context details loaded as needed during execution</dynamic_expansion>
      </claude_4_optimization>
    </context_component>
    
    <expectation_component>
      <description>Detailed success criteria, deliverable formats, and validation methods</description>
      <purpose>Ensures clear understanding of success metrics and output requirements</purpose>
      <patterns>
        <pattern name="implementation_expectations">Working code with tests, performance benchmarks, security validation, and deployment guide</pattern>
        <pattern name="analysis_expectations">Executive summary, detailed findings, risk assessment, and prioritized recommendations</pattern>
        <pattern name="coordination_expectations">Project timeline, milestone tracking, team assignments, and progress reports</pattern>
      </patterns>
      <claude_4_optimization>
        <measurable_criteria>Quantifiable success metrics with automated validation where possible</measurable_criteria>
        <progressive_validation">Incremental expectation validation throughout execution</progressive_validation>
      </claude_4_optimization>
    </expectation_component>
  </trace_components>
  
  <implementation_patterns>
    <basic_trace_pattern>
      <structure>
        &lt;trace_framework&gt;
          &lt;task&gt;[Overall objective and scope definition]&lt;/task&gt;
          &lt;request&gt;[Specific deliverables and requirements]&lt;/request&gt;
          &lt;action&gt;
            1. [First detailed action with validation]
            2. [Second detailed action with dependencies]
            3. [Third detailed action with checkpoints]
            ...
          &lt;/action&gt;
          &lt;context&gt;[Comprehensive environmental and situational information]&lt;/context&gt;
          &lt;expectation&gt;[Detailed success criteria and deliverable formats]&lt;/expectation&gt;
        &lt;/trace_framework&gt;
      </structure>
      <usage>Standard TRACE implementation for comprehensive task specification</usage>
    </basic_trace_pattern>
    
    <enhanced_trace_pattern>
      <structure>
        &lt;trace_framework thinking_mode="interleaved" optimization="claude_4"&gt;
          &lt;task scope="[defined]" complexity="[assessed]"&gt;[Detailed objective with success boundaries]&lt;/task&gt;
          &lt;request deliverables="[count]" quality_level="[standard]"&gt;[Granular requirement specification]&lt;/request&gt;
          &lt;action execution_mode="parallel_optimized" validation="comprehensive"&gt;
            &lt;action_group id="preparation" parallel="true"&gt;
              &lt;action id="1" type="setup"&gt;[Parallel preparation action]&lt;/action&gt;
              &lt;action id="2" type="analysis"&gt;[Independent analysis action]&lt;/action&gt;
            &lt;/action_group&gt;
            &lt;action_group id="implementation" depends_on="preparation"&gt;
              &lt;action id="3" type="core"&gt;[Sequential implementation after preparation]&lt;/action&gt;
              &lt;action id="4" type="validation"&gt;[Quality validation and testing]&lt;/action&gt;
            &lt;/action_group&gt;
          &lt;/action&gt;
          &lt;context priority="hierarchical" loading="dynamic"&gt;[Rich contextual information with priority ordering]&lt;/context&gt;
          &lt;expectation metrics="measurable" validation="automated"&gt;[Comprehensive success criteria with measurable outcomes]&lt;/expectation&gt;
        &lt;/trace_framework&gt;
      </structure>
      <usage>Advanced TRACE with Claude 4 optimization for complex, context-heavy tasks</usage>
    </enhanced_trace_pattern>
    
    <tdd_integrated_trace_pattern>
      <structure>
        &lt;trace_framework tdd_enforcement="mandatory"&gt;
          &lt;task&gt;Test-driven implementation of feature with comprehensive validation&lt;/task&gt;
          &lt;request&gt;Working implementation with 90%+ test coverage, documentation, and security validation&lt;/request&gt;
          &lt;action&gt;
            1. Analyze requirements for comprehensive testability
            2. Design test strategy covering all requirement aspects
            3. Write failing tests for all functionality FIRST
            4. Implement minimal code to achieve green tests
            5. Refactor implementation while maintaining test coverage
            6. Validate quality gates and security requirements
            7. Generate comprehensive documentation
          &lt;/action&gt;
          &lt;context&gt;Current codebase, testing frameworks, quality standards, security requirements&lt;/context&gt;
          &lt;expectation&gt;Production-ready feature with comprehensive test suite, security validation, and documentation&lt;/expectation&gt;
        &lt;/trace_framework&gt;
      </structure>
      <usage>TRACE framework with mandatory TDD enforcement for development tasks</usage>
    </tdd_integrated_trace_pattern>
    
    <multi_agent_trace_pattern>
      <structure>
        &lt;trace_framework coordination="multi_agent" orchestration="intelligent"&gt;
          &lt;task&gt;[Complex task requiring specialized expertise coordination]&lt;/task&gt;
          &lt;request&gt;[Deliverables requiring multiple domain expertise areas]&lt;/request&gt;
          &lt;action&gt;
            &lt;agent_coordination&gt;
              1. Analyze task complexity and domain requirements
              2. Assign specialized agents with appropriate expertise
              3. Coordinate parallel work streams with dependencies
              4. Monitor progress and manage integration points
              5. Validate cross-agent consistency and quality
              6. Synthesize results into coherent deliverable
            &lt;/agent_coordination&gt;
          &lt;/action&gt;
          &lt;context&gt;[Rich context with agent-specific information and coordination requirements]&lt;/context&gt;
          &lt;expectation&gt;[Coordinated deliverable meeting all quality standards with expert validation]&lt;/expectation&gt;
        &lt;/trace_framework&gt;
      </structure>
      <usage>TRACE framework for complex multi-agent coordination tasks</usage>
    </multi_agent_trace_pattern>
  </implementation_patterns>
  
  <use_case_scenarios>
    <comprehensive_system_development>
      <scenario>Building enterprise-grade microservices platform with security and compliance</scenario>
      <trace_application>
        <task>Implement secure, scalable microservices platform with full compliance validation</task>
        <request>Working platform with security audit, performance benchmarks, compliance documentation, and deployment automation</request>
        <action>1. Architecture design 2. Security framework implementation 3. Core services development 4. Integration testing 5. Compliance validation 6. Performance optimization 7. Documentation generation</action>
        <context>Enterprise requirements, compliance standards (SOC2, PCI DSS), existing infrastructure, team expertise, timeline constraints</context>
        <expectation>Production-ready platform with security certification, performance benchmarks meeting SLA requirements, comprehensive documentation, and automated deployment pipeline</expectation>
      </trace_application>
    </comprehensive_system_development>
    
    <complex_data_analysis>
      <scenario>Comprehensive security and performance analysis of distributed system</scenario>
      <trace_application>
        <task>Conduct thorough security audit and performance analysis of distributed microservices architecture</task>
        <request>Security assessment report, performance optimization recommendations, compliance gap analysis, and implementation roadmap</request>
        <action>1. System mapping and inventory 2. Security vulnerability assessment 3. Performance profiling and bottleneck identification 4. Compliance review against standards 5. Risk assessment and prioritization 6. Recommendation synthesis 7. Implementation roadmap creation</action>
        <context>Current architecture documentation, security policies, performance requirements, compliance frameworks, budget constraints, team capabilities</context>
        <expectation>Executive summary with risk ratings, detailed technical findings, prioritized recommendations with cost-benefit analysis, implementation timeline, and monitoring strategy</expectation>
      </trace_application>
    </complex_data_analysis>
    
    <multi_team_coordination>
      <scenario>Coordinating complex feature development across multiple specialized teams</scenario>
      <trace_application>
        <task>Orchestrate cross-team development of integrated payment and notification system</task>
        <request>Coordinated implementation with team synchronization, progress tracking, integration validation, and quality assurance</request>
        <action>1. Team capability assessment and assignment 2. Work stream definition and dependency mapping 3. Communication protocol establishment 4. Progress monitoring and coordination 5. Integration point management 6. Quality gate enforcement 7. Final validation and delivery</action>
        <context>Team structures, individual expertise, technology preferences, existing systems, integration requirements, timeline pressures</context>
        <expectation>Successful feature delivery with all teams synchronized, integration points validated, quality standards met, and comprehensive documentation of coordination decisions</expectation>
      </trace_application>
    </multi_team_coordination>
  </use_case_scenarios>
  
  <claude_4_optimization_features>
    <interleaved_thinking_integration>
      <purpose>Leverage Claude 4's 16K thinking capacity for sophisticated TRACE execution</purpose>
      <implementation>
        <task_thinking>Deep analysis of task scope and complexity assessment</task_thinking>
        <request_thinking>Comprehensive requirement breakdown and feasibility analysis</request_thinking>
        <action_thinking>Critical evaluation of action sequences, dependencies, and optimization opportunities</action_thinking>
        <context_thinking>Thorough context analysis and priority-based information structuring</context_thinking>
        <expectation_thinking>Detailed validation of success criteria and deliverable specifications</expectation_thinking>
      </implementation>
      <triggers>Very complex scenarios, multi-domain requirements, ambiguous specifications, high-stakes deliverables</triggers>
    </interleaved_thinking_integration>
    
    <parallel_execution_optimization>
      <purpose>Optimize TRACE framework execution for 70% performance improvement through intelligent coordination</purpose>
      <implementation>
        <task_optimization>Task scope analysis concurrent with resource assessment</task_optimization>
        <request_optimization>Parallel requirement validation and feasibility checking</request_optimization>
        <action_optimization>Independent action groups executed simultaneously with dependency management</action_optimization>
        <context_optimization>Hierarchical context loading with priority-based access patterns</context_optimization>
        <expectation_optimization">Concurrent validation against multiple success criteria and quality standards</expectation_optimization>
      </implementation>
      <performance_targets>70% reduction in execution time through intelligent parallelization and context optimization</performance_targets>
    </parallel_execution_optimization>
    
    <context_window_efficiency>
      <purpose>Optimize 200K token window usage for comprehensive TRACE execution with rich context</purpose>
      <implementation>
        <hierarchical_loading>Critical TRACE components loaded first, detailed context loaded as needed</hierarchical_loading>
        <token_budgeting>Optimal allocation across Task, Request, Action, Context, and Expectation components</token_budgeting>
        <dynamic_context_expansion>Context details loaded incrementally based on execution requirements</dynamic_context_expansion>
        <context_compression>Efficient context representation using structured XML for maximum information density</context_compression>
      </implementation>
      <monitoring>Real-time token usage tracking with adaptive context loading and optimization triggers</monitoring>
    </context_window_efficiency>
    
    <advanced_dependency_management>
      <purpose>Sophisticated action dependency tracking and optimization for complex workflows</purpose>
      <implementation>
        <dependency_analysis>Automated dependency discovery and validation</dependency_analysis>
        <execution_sequencing">Optimal action ordering based on dependency constraints</execution_sequencing>
        <parallel_identification>Automatic identification of parallelizable action groups</parallel_identification>
        <bottleneck_optimization>Dynamic bottleneck identification and resolution</bottleneck_optimization>
      </implementation>
      <benefits>Optimal execution paths with minimal wait times and maximum parallelization</benefits>
    </advanced_dependency_management>
  </claude_4_optimization_features>
  
  <integration_interfaces>
    <command_integration>
      <auto_command>Use TRACE for comprehensive complex routing requiring detailed context analysis</auto_command>
      <task_command>Apply TRACE for complex single-component tasks requiring rich context</task_command>
      <feature_command>Leverage TRACE for comprehensive feature development with detailed requirements</feature_command>
      <swarm_command>Use TRACE for complex multi-agent coordination with extensive context sharing</swarm_command>
      <query_command>Apply TRACE for comprehensive analysis tasks requiring detailed context consideration</query_command>
    </command_integration>
    
    <module_integration>
      <thinking_patterns>Enhance thinking-pattern-template.md with TRACE checkpoint integration and context management</thinking_patterns>
      <quality_gates>Integrate TRACE validation with universal-quality-gates.md for comprehensive quality assurance</quality_gates>
      <session_management>Apply TRACE for complex session planning with rich context preservation</session_management>
      <multi_agent>Integrate TRACE with multi-agent coordination for context-rich collaboration</multi_agent>
    </module_integration>
  </integration_interfaces>
  
  <validation_criteria>
    <completeness_check>
      <criterion>All five TRACE components (Task, Request, Action, Context, Expectation) must be comprehensively defined</criterion>
      <criterion>Task must include clear scope boundaries and success definitions</criterion>
      <criterion>Request must specify detailed deliverables with quality standards</criterion>
      <criterion>Action must provide executable steps with dependencies and validation</criterion>
      <criterion>Context must include all relevant environmental and situational information</criterion>
      <criterion>Expectation must define measurable success criteria and output formats</criterion>
    </completeness_check>
    
    <quality_validation>
      <criterion>Task scope matches complexity and available resources</criterion>
      <criterion>Request specifications are achievable within context constraints</criterion>
      <criterion>Actions are logically sequenced with clear dependencies and validation points</criterion>
      <criterion>Context provides sufficient information for successful task execution</criterion>
      <criterion>Expectations are measurable, achievable, and aligned with task objectives</criterion>
      <criterion>Framework application significantly improves task clarity and execution success</criterion>
    </quality_validation>
    
    <claude_4_optimization_validation>
      <criterion>Parallel execution opportunities identified and leveraged across all TRACE components</criterion>
      <criterion>Interleaved thinking integration enhances framework effectiveness for complex scenarios</criterion>
      <criterion>Context efficiency optimized for 200K token window with hierarchical loading</criterion>
      <criterion>Performance improvement measurable and validated through execution metrics</criterion>
      <criterion>Dependency management optimized for minimal bottlenecks and maximum parallelization</criterion>
    </claude_4_optimization_validation>
  </validation_criteria>
  
  <usage_guidelines>
    <when_to_use_trace>
      <scenario>Complex tasks requiring comprehensive context management</scenario>
      <scenario>Multi-step processes with rich environmental requirements</scenario>
      <scenario>Tasks where detailed specification significantly impacts success</scenario>
      <scenario>Situations requiring explicit dependency management and validation</scenario>
      <scenario>Complex coordination tasks requiring detailed context sharing</scenario>
    </when_to_use_trace>
    
    <when_not_to_use_trace>
      <scenario>Simple tasks where context is obvious or minimal</scenario>
      <scenario>Quick operations where TRACE overhead exceeds benefits</scenario>
      <scenario>Tasks with clear, simple requirements not requiring detailed specification</scenario>
      <scenario>Scenarios where simpler frameworks provide sufficient structure</scenario>
    </when_not_to_use_trace>
    
    <framework_selection_guidance>
      <simple_tasks>Consider RISE or CARE frameworks for lighter specification overhead</simple_tasks>
      <moderate_complexity>Use CLEAR or CRISP for balanced structure without full TRACE complexity</moderate_complexity>
      <rapid_execution>Consider APE or SMART-AI for speed-optimized approaches</rapid_execution>
      <strategic_planning>Use SOAR for high-level planning without detailed implementation context</strategic_planning>
    </framework_selection_guidance>
  </usage_guidelines>
  
  <performance_metrics>
    <effectiveness_indicators>
      <metric name="task_completion_rate">Percentage of TRACE-structured tasks completed successfully</metric>
      <metric name="context_utilization">Effectiveness of context information in task execution</metric>
      <metric name="dependency_optimization">Improvement in execution efficiency through dependency management</metric>
      <metric name="quality_consistency">Consistent high-quality outputs across complex TRACE tasks</metric>
      <metric name="coordination_efficiency">Success rate in multi-agent coordination using TRACE</metric>
    </effectiveness_indicators>
    
    <optimization_tracking>
      <metric name="parallel_execution_utilization">Percentage of actions executed in parallel vs sequential</metric>
      <metric name="context_efficiency">Token usage optimization through hierarchical context loading</metric>
      <metric name="thinking_integration_depth">Quality and depth of interleaved thinking integration</metric>
      <metric name="framework_overhead">Time/token cost of TRACE implementation vs benefits achieved</metric>
      <metric name="dependency_resolution_speed">Time required for dependency analysis and optimization</metric>
    </optimization_tracking>
  </performance_metrics>
  
  <integration_points>
    <depends_on>
      patterns/thinking-pattern-template.md for advanced checkpoint integration
      quality/universal-quality-gates.md for comprehensive validation standards
      patterns/module-composition-framework.md for execution orchestration
      patterns/multi-agent.md for coordination and context sharing
    </depends_on>
    <provides_to>
      All commands for comprehensive task execution with rich context management
      frameworks/framework-selector.md for automatic framework selection based on complexity
      quality/framework-metrics.md for TRACE effectiveness measurement and optimization
      patterns/session-management.md for complex session coordination with context preservation
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">comprehensive_execution</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">context_management</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">dependency_optimization</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">systematic_validation</uses_pattern>
    <implementation_notes>
      TRACE framework implements comprehensive_execution pattern for detailed task management
      Context component uses context_management pattern for rich environmental information
      Action component leverages dependency_optimization pattern for efficient execution sequencing
      Validation follows systematic_validation pattern for comprehensive quality assurance
      Framework provides foundation for context-rich, dependency-aware task execution
    </implementation_notes>
  </pattern_usage>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Core TRACE framework implementation for comprehensive, context-rich task execution with Claude 4 optimization and sophisticated dependency management patterns.