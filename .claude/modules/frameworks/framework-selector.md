| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Framework Selector Engine Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="framework_selector" category="frameworks">
  
  <purpose>
    Intelligent framework selection engine that automatically chooses the optimal prompting framework based on task characteristics, complexity, domain requirements, and interaction style preferences, preventing choice paralysis and ensuring optimal execution patterns.
  </purpose>
  
  <selection_engine>
    
    <intelligent_analysis>
      <task_classification>
        <complexity_assessment>
          <simple_tasks>
            <characteristics>1-3 steps, clear requirements, immediate execution, minimal context</characteristics>
            <framework_recommendations>APE (primary), CARE (secondary)</framework_recommendations>
            <decision_criteria>Speed, simplicity, minimal overhead requirements</decision_criteria>
          </simple_tasks>
          
          <moderate_tasks>
            <characteristics>4-12 steps, structured approach needed, moderate context, role clarity important</characteristics>
            <framework_recommendations>RISE (primary), TRACE (secondary), SOAR (tertiary), FOCUS (quaternary)</framework_recommendations>
            <decision_criteria>Structure, clarity, systematic approach, moderate depth</decision_criteria>
          </moderate_tasks>
          
          <complex_tasks>
            <characteristics>13+ steps, extensive context, multiple stakeholders, high precision required</characteristics>
            <framework_recommendations>CLEAR (primary), CRISP (secondary), BRIDGE (tertiary)</framework_recommendations>
            <decision_criteria>Comprehensiveness, precision, stakeholder coordination, extensive documentation</decision_criteria>
          </complex_tasks>
        </complexity_assessment>
        
        <domain_classification>
          <technical_development>
            <precision_work>
              <characteristics>Exact specifications, edge cases, configuration parameters</characteristics>
              <optimal_framework>CRISP - Context, Role, Instructions, Specifics, Parameters</optimal_framework>
              <reasoning>Detailed technical specifications with precise parameter control</reasoning>
            </precision_work>
            
            <problem_solving>
              <characteristics>Debugging, root cause analysis, troubleshooting</characteristics>
              <optimal_framework>SPARK - Scenario, Problem, Action, Result, Knowledge</optimal_framework>
              <reasoning>Systematic problem diagnosis and solution methodology</reasoning>
            </problem_solving>
            
            <integration_work>
              <characteristics>Cross-system implementations, complex coordination</characteristics>
              <optimal_framework>BRIDGE - Background, Requirements, Implementation, Deliverables, Goals, Evaluation</optimal_framework>
              <reasoning>Comprehensive integration planning and execution</reasoning>
            </integration_work>
            
            <research_work>
              <characteristics>Technology learning, capability exploration</characteristics>
              <optimal_framework>LEAP - Learn, Explore, Apply, Produce</optimal_framework>
              <reasoning>Knowledge acquisition and practical application</reasoning>
            </research_work>
          </technical_development>
          
          <business_planning>
            <strategic_planning>
              <characteristics>High-level goals, outcome focus, strategic alignment</characteristics>
              <optimal_framework>SOAR - Situation, Objective, Action, Result</optimal_framework>
              <reasoning>Strategic thinking and goal achievement</reasoning>
            </strategic_planning>
            
            <project_planning>
              <characteristics>Milestone definition, AI assistance, measurable goals</characteristics>
              <optimal_framework>SMART-AI - Specific, Measurable, Achievable, Relevant, Time-bound + AI</optimal_framework>
              <reasoning>Structured planning with AI optimization</reasoning>
            </project_planning>
            
            <comprehensive_analysis>
              <characteristics>Complex decisions, multiple constraints, expert analysis</characteristics>
              <optimal_framework>CLEAR - Context, Limitation, Example, Action, Role</optimal_framework>
              <reasoning>Comprehensive analysis with expert-level insight</reasoning>
            </comprehensive_analysis>
          </business_planning>
          
          <user_experience>
            <interface_design>
              <characteristics>User-centered approach, usability focus, context awareness</characteristics>
              <optimal_framework>FOCUS - Function, Objective, Context, User, Scope</optimal_framework>
              <reasoning>User-centered design with clear scope boundaries</reasoning>
            </interface_design>
            
            <user_research>
              <characteristics>User behavior analysis, needs discovery</characteristics>
              <optimal_framework>LEAP - Learn, Explore, Apply, Produce</optimal_framework>
              <reasoning>Research methodology for user understanding</reasoning>
            </user_research>
            
            <workflow_optimization>
              <characteristics>Process improvement, feedback integration</characteristics>
              <optimal_framework>CARE - Context, Action, Result, Evaluation</optimal_framework>
              <reasoning>Iterative improvement with systematic evaluation</reasoning>
            </workflow_optimization>
          </user_experience>
          
          <research_analysis>
            <knowledge_acquisition>
              <characteristics>Learning focus, synthesis required, capability building</characteristics>
              <optimal_framework>LEAP - Learn, Explore, Apply, Produce</optimal_framework>
              <reasoning>Structured learning and knowledge production</reasoning>
            </knowledge_acquisition>
            
            <comprehensive_research>
              <characteristics>Deep analysis, multiple perspectives, expert insight</characteristics>
              <optimal_framework>CLEAR - Context, Limitation, Example, Action, Role</optimal_framework>
              <reasoning>Thorough analysis with comprehensive context</reasoning>
            </comprehensive_research>
            
            <comparative_analysis>
              <characteristics>Detailed comparison, precise specification</characteristics>
              <optimal_framework>TRACE - Task, Request, Action, Context, Expectation</optimal_framework>
              <reasoning>Precise specification for accurate comparison</reasoning>
            </comparative_analysis>
          </research_analysis>
        </domain_classification>
        
        <interaction_style_classification>
          <directive_approach>
            <characteristics>Clear instructions needed, step-by-step guidance, minimal ambiguity</characteristics>
            <optimal_frameworks>
              <primary>RISE - Role, Input, Steps, Expectation</primary>
              <secondary>TRACE - Task, Request, Action, Context, Expectation</secondary>
              <tertiary>CRISP - Context, Role, Instructions, Specifics, Parameters</tertiary>
            </optimal_frameworks>
            <reasoning>Structured guidance with clear role definition and precise steps</reasoning>
          </directive_approach>
          
          <collaborative_approach>
            <characteristics>Feedback loops, iterative improvement, stakeholder input</characteristics>
            <optimal_frameworks>
              <primary>CARE - Context, Action, Result, Evaluation</primary>
              <secondary>FOCUS - Function, Objective, Context, User, Scope</secondary>
              <tertiary>SMART-AI - Specific, Measurable, Achievable, Relevant, Time-bound + AI</tertiary>
            </optimal_frameworks>
            <reasoning>Iterative approach with built-in feedback and collaborative elements</reasoning>
          </collaborative_approach>
          
          <exploratory_approach>
            <characteristics>Investigation needed, discovery focus, open-ended analysis</characteristics>
            <optimal_frameworks>
              <primary>SPARK - Scenario, Problem, Action, Result, Knowledge</primary>
              <secondary>LEAP - Learn, Explore, Apply, Produce</secondary>
              <tertiary>BRIDGE - Background, Requirements, Implementation, Deliverables, Goals, Evaluation</tertiary>
            </optimal_frameworks>
            <reasoning>Investigation and discovery-oriented frameworks for exploration</reasoning>
          </exploratory_approach>
        </interaction_style_classification>
      </task_classification>
    </intelligent_analysis>
    
    <selection_algorithm>
      <decision_tree>
        <step order="1" name="complexity_assessment">
          <input>Task description, estimated steps, context requirements</input>
          <analysis>
            <simple_indicators>Single action, clear requirements, minimal context</simple_indicators>
            <moderate_indicators>Multiple steps, structured approach, moderate context</moderate_indicators>
            <complex_indicators>Extensive planning, multiple stakeholders, comprehensive documentation</complex_indicators>
          </analysis>
          <output>Complexity classification (simple/moderate/complex)</output>
        </step>
        
        <step order="2" name="domain_identification">
          <input>Task domain, technical requirements, stakeholder types</input>
          <analysis>
            <technical_indicators>Code, systems, debugging, implementation</technical_indicators>
            <business_indicators>Strategy, planning, goals, ROI</business_indicators>
            <ux_indicators>Users, interfaces, workflows, experience</ux_indicators>
            <research_indicators>Learning, analysis, investigation, knowledge</research_indicators>
          </analysis>
          <output>Domain classification (technical/business/ux/research)</output>
        </step>
        
        <step order="3" name="interaction_style_detection">
          <input>User preferences, task nature, collaboration requirements</input>
          <analysis>
            <directive_indicators>Clear instructions needed, structured approach, minimal ambiguity</directive_indicators>
            <collaborative_indicators>Feedback required, iterative improvement, stakeholder input</collaborative_indicators>
            <exploratory_indicators>Investigation needed, discovery focus, open-ended</exploratory_indicators>
          </analysis>
          <output>Interaction style (directive/collaborative/exploratory)</output>
        </step>
        
        <step order="4" name="framework_recommendation">
          <input>Complexity, domain, interaction style classifications</input>
          <processing>
            <weight_factors>
              <complexity_weight>40%</complexity_weight>
              <domain_weight>35%</domain_weight>
              <interaction_style_weight>25%</interaction_style_weight>
            </weight_factors>
            <selection_logic>
              <primary_match>Best fit across all three dimensions</primary_match>
              <secondary_options>Alternative frameworks for flexibility</secondary_options>
              <combination_opportunities>Multi-framework strategies where beneficial</combination_opportunities>
            </selection_logic>
          </processing>
          <output>Primary framework recommendation with alternatives and reasoning</output>
        </step>
      </decision_tree>
      
      <selection_criteria_matrix>
        <framework_scores>
          <ape_framework>
            <complexity_fit>Simple: 95%, Moderate: 20%, Complex: 5%</complexity_fit>
            <domain_fit>Technical: 40%, Business: 60%, UX: 50%, Research: 30%</domain_fit>
            <interaction_fit>Directive: 80%, Collaborative: 30%, Exploratory: 20%</interaction_fit>
          </ape_framework>
          
          <rise_framework>
            <complexity_fit>Simple: 60%, Moderate: 90%, Complex: 40%</complexity_fit>
            <domain_fit>Technical: 80%, Business: 70%, UX: 60%, Research: 50%</domain_fit>
            <interaction_fit>Directive: 95%, Collaborative: 40%, Exploratory: 30%</interaction_fit>
          </rise_framework>
          
          <trace_framework>
            <complexity_fit>Simple: 40%, Moderate: 85%, Complex: 70%</complexity_fit>
            <domain_fit>Technical: 90%, Business: 60%, UX: 50%, Research: 80%</domain_fit>
            <interaction_fit>Directive: 90%, Collaborative: 30%, Exploratory: 40%</interaction_fit>
          </trace_framework>
          
          <care_framework>
            <complexity_fit>Simple: 70%, Moderate: 80%, Complex: 30%</complexity_fit>
            <domain_fit>Technical: 60%, Business: 50%, UX: 90%, Research: 40%</domain_fit>
            <interaction_fit>Directive: 40%, Collaborative: 95%, Exploratory: 50%</interaction_fit>
          </care_framework>
          
          <clear_framework>
            <complexity_fit>Simple: 10%, Moderate: 60%, Complex: 95%</complexity_fit>
            <domain_fit>Technical: 85%, Business: 90%, UX: 70%, Research: 95%</domain_fit>
            <interaction_fit>Directive: 70%, Collaborative: 60%, Exploratory: 80%</interaction_fit>
          </clear_framework>
          
          <soar_framework>
            <complexity_fit>Simple: 30%, Moderate: 85%, Complex: 60%</complexity_fit>
            <domain_fit>Technical: 40%, Business: 95%, UX: 50%, Research: 60%</domain_fit>
            <interaction_fit>Directive: 60%, Collaborative: 70%, Exploratory: 60%</interaction_fit>
          </soar_framework>
          
          <crisp_framework>
            <complexity_fit>Simple: 20%, Moderate: 70%, Complex: 90%</complexity_fit>
            <domain_fit>Technical: 95%, Business: 40%, UX: 30%, Research: 50%</domain_fit>
            <interaction_fit>Directive: 95%, Collaborative: 30%, Exploratory: 40%</interaction_fit>
          </crisp_framework>
          
          <spark_framework>
            <complexity_fit>Simple: 40%, Moderate: 80%, Complex: 50%</complexity_fit>
            <domain_fit>Technical: 90%, Business: 40%, UX: 30%, Research: 70%</domain_fit>
            <interaction_fit>Directive: 60%, Collaborative: 50%, Exploratory: 95%</interaction_fit>
          </spark_framework>
          
          <focus_framework>
            <complexity_fit>Simple: 50%, Moderate: 85%, Complex: 40%</complexity_fit>
            <domain_fit>Technical: 30%, Business: 60%, UX: 95%, Research: 40%</domain_fit>
            <interaction_fit>Directive: 50%, Collaborative: 90%, Exploratory: 60%</interaction_fit>
          </focus_framework>
          
          <smart_ai_framework>
            <complexity_fit>Simple: 30%, Moderate: 80%, Complex: 60%</complexity_fit>
            <domain_fit>Technical: 50%, Business: 90%, UX: 40%, Research: 30%</domain_fit>
            <interaction_fit>Directive: 70%, Collaborative: 85%, Exploratory: 40%</interaction_fit>
          </smart_ai_framework>
          
          <leap_framework>
            <complexity_fit>Simple: 40%, Moderate: 75%, Complex: 50%</complexity_fit>
            <domain_fit>Technical: 70%, Business: 40%, UX: 60%, Research: 95%</domain_fit>
            <interaction_fit>Directive: 40%, Collaborative: 60%, Exploratory: 90%</interaction_fit>
          </leap_framework>
          
          <bridge_framework>
            <complexity_fit>Simple: 5%, Moderate: 40%, Complex: 95%</complexity_fit>
            <domain_fit>Technical: 85%, Business: 70%, UX: 50%, Research: 60%</domain_fit>
            <interaction_fit>Directive: 60%, Collaborative: 70%, Exploratory: 85%</interaction_fit>
          </bridge_framework>
        </framework_scores>
      </selection_criteria_matrix>
    </selection_algorithm>
    
    <combination_strategies>
      
      <sequential_combinations>
        <research_to_implementation>
          <sequence>LEAP → CLEAR → CRISP → CARE</sequence>
          <trigger_conditions>Learning new technology followed by production implementation</trigger_conditions>
          <benefits>Comprehensive knowledge acquisition to validated production delivery</benefits>
          <use_cases>New technology adoption, platform migrations, capability building</use_cases>
        </research_to_implementation>
        
        <problem_to_solution>
          <sequence>SPARK → SOAR → TRACE → CARE</sequence>
          <trigger_conditions>Problem diagnosis requiring strategic solution with precise implementation</trigger_conditions>
          <benefits>Systematic problem solving with strategic alignment and validation</benefits>
          <use_cases>Complex debugging, system redesign, performance optimization</use_cases>
        </problem_to_solution>
        
        <user_focused_development>
          <sequence>FOCUS → RISE → CRISP → CARE</sequence>
          <trigger_conditions>User-centered development requiring technical precision</trigger_conditions>
          <benefits>User needs driving structured technical implementation</benefits>
          <use_cases>Interface development, user experience improvements, workflow optimization</use_cases>
        </user_focused_development>
        
        <strategic_execution>
          <sequence>SOAR → SMART-AI → BRIDGE → CARE</sequence>
          <trigger_conditions>Strategic initiatives requiring comprehensive implementation</trigger_conditions>
          <benefits>Strategic vision translated to operational execution with validation</benefits>
          <use_cases>Major feature development, system transformations, organizational initiatives</use_cases>
        </strategic_execution>
      </sequential_combinations>
      
      <parallel_combinations>
        <multi_perspective_analysis>
          <parallel_frameworks>CLEAR (technical) + FOCUS (user) + SOAR (business)</parallel_frameworks>
          <trigger_conditions>Complex decisions requiring multiple expert perspectives</trigger_conditions>
          <benefits>Holistic analysis and comprehensive decision making</benefits>
          <coordination_strategy>Execute frameworks in parallel, synthesize results for integrated decision</coordination_strategy>
        </multi_perspective_analysis>
        
        <distributed_implementation>
          <parallel_frameworks>CRISP (backend) + FOCUS (frontend) + BRIDGE (integration)</parallel_frameworks>
          <trigger_conditions>Complex system development with multiple specialized teams</trigger_conditions>
          <benefits>Parallel development with specialized expertise and coordination</benefits>
          <coordination_strategy>Team-specific frameworks with integration checkpoints</coordination_strategy>
        </distributed_implementation>
        
        <comprehensive_validation>
          <parallel_frameworks>TRACE (functional) + CRISP (technical) + CARE (quality)</parallel_frameworks>
          <trigger_conditions>Critical implementations requiring multi-dimensional validation</trigger_conditions>
          <benefits>Comprehensive quality assurance across all validation dimensions</benefits>
          <coordination_strategy>Parallel validation streams with integrated reporting</coordination_strategy>
        </comprehensive_validation>
      </parallel_combinations>
      
      <hybrid_approaches>
        <adaptive_combinations>
          <base_framework>Primary framework selected by algorithm</base_framework>
          <contextual_additions>Additional framework elements based on specific requirements</contextual_additions>
          <examples>
            <security_enhanced>CRISP + security considerations for sensitive implementations</security_enhanced>
            <user_validated>TRACE + FOCUS user validation for technical specifications</user_validated>
            <business_aligned>RISE + SOAR strategic alignment for development tasks</business_aligned>
          </examples>
          <customization_triggers>Special requirements, compliance needs, stakeholder preferences</customization_triggers>
        </adaptive_combinations>
        
        <component_mixing>
          <pattern>Best components from multiple frameworks</pattern>
          <examples>
            <precision_with_evaluation>RISE role + TRACE specificity + CARE evaluation</precision_with_evaluation>
            <strategic_with_technical>SOAR objectives + CRISP implementation + CARE validation</strategic_with_technical>
            <user_with_technical>FOCUS user focus + CRISP technical precision + CARE quality</user_with_technical>
          </examples>
          <selection_criteria>Component strengths address specific task requirements</selection_criteria>
        </component_mixing>
      </hybrid_approaches>
      
    </combination_strategies>
    
    <selection_optimization>
      
      <performance_optimization>
        <speed_optimization>
          <rule>For time-critical tasks, prioritize frameworks with minimal overhead</rule>
          <recommendations>APE for immediate execution, CARE for rapid iteration</recommendations>
          <trade_offs>Speed vs comprehensiveness - document conscious choices</trade_offs>
        </speed_optimization>
        
        <quality_optimization>
          <rule>For quality-critical tasks, prioritize frameworks with comprehensive validation</rule>
          <recommendations>CLEAR for thorough analysis, CRISP for precise implementation, BRIDGE for complex integration</recommendations>
          <validation_emphasis>Multiple validation checkpoints and quality gates</validation_emphasis>
        </quality_optimization>
        
        <context_optimization>
          <rule>Optimize framework selection for available context and Claude 4 capabilities</rule>
          <context_awareness>Adjust framework complexity based on available context window</context_awareness>
          <claude_4_leveraging>Use frameworks that maximize Claude 4 thinking and parallel execution benefits</claude_4_leveraging>
        </context_optimization>
      </performance_optimization>
      
      <learning_optimization>
        <user_preference_learning>
          <pattern_recognition>Track successful framework selections for similar tasks</pattern_recognition>
          <preference_adaptation>Adapt recommendations based on user success patterns</preference_adaptation>
          <feedback_integration>Incorporate user feedback for framework effectiveness</feedback_integration>
        </user_preference_learning>
        
        <outcome_optimization>
          <success_tracking>Monitor task completion rates by framework selection</success_tracking>
          <quality_correlation>Correlate framework choice with output quality metrics</quality_correlation>
          <continuous_improvement>Refine selection criteria based on outcome data</continuous_improvement>
        </outcome_optimization>
      </learning_optimization>
      
    </selection_optimization>
    
  </selection_engine>
  
  <implementation_interface>
    
    <selection_api>
      <function name="select_framework">
        <parameters>
          <task_description>string - Description of the task to be performed</task_description>
          <complexity_hint>optional string - User-provided complexity assessment</complexity_hint>
          <domain_preference>optional string - Preferred domain focus (technical/business/ux/research)</domain_preference>
          <interaction_style>optional string - Preferred interaction style (directive/collaborative/exploratory)</interaction_style>
          <time_constraint>optional string - Time sensitivity (immediate/normal/extended)</time_constraint>
          <quality_requirement>optional string - Quality expectations (standard/high/critical)</quality_requirement>
        </parameters>
        <returns>
          <primary_recommendation>Framework object with implementation guidance</primary_recommendation>
          <alternative_options>Array of alternative framework recommendations</alternative_options>
          <combination_suggestions>Optional multi-framework strategies</combination_suggestions>
          <reasoning>Explanation of selection logic and trade-offs</reasoning>
        </returns>
      </function>
      
      <function name="validate_selection">
        <parameters>
          <selected_framework>Framework choice for validation</selected_framework>
          <task_context>Complete task context and requirements</task_context>
        </parameters>
        <returns>
          <validation_result>Boolean indicating framework appropriateness</validation_result>
          <optimization_suggestions>Recommendations for framework optimization</optimization_suggestions>
          <warning_flags>Potential issues or mismatches identified</warning_flags>
        </returns>
      </function>
      
      <function name="recommend_combination">
        <parameters>
          <primary_framework>Base framework selection</primary_framework>
          <task_complexity>Task complexity and scope</task_complexity>
          <stakeholder_requirements>Multi-stakeholder needs and perspectives</stakeholder_requirements>
        </parameters>
        <returns>
          <combination_strategy>Sequential, parallel, or hybrid approach</combination_strategy>
          <coordination_plan>Framework integration and execution plan</coordination_plan>
          <success_metrics>Validation criteria for combined approach</success_metrics>
        </returns>
      </function>
    </selection_api>
    
    <integration_patterns>
      <command_integration>
        <auto_command>Primary entry point for framework selection intelligence</auto_command>
        <task_command>Framework selection for focused development work</task_command>
        <feature_command>Framework selection for comprehensive feature development</feature_command>
        <swarm_command>Multi-framework coordination for complex multi-agent work</swarm_command>
        <query_command>Framework selection for research and analysis tasks</query_command>
      </command_integration>
      
      <module_integration>
        <intelligent_routing>Framework-aware routing decisions</intelligent_routing>
        <task_management>Framework optimization for task execution</task_management>
        <multi_agent>Framework coordination across multiple agents</multi_agent>
        <quality_gates>Framework validation and quality assurance</quality_gates>
      </module_integration>
    </integration_patterns>
    
  </implementation_interface>
  
  <claude_4_optimization>
    
    <selection_thinking_integration>
      <purpose>Leverage Claude 4 thinking capabilities for intelligent framework selection</purpose>
      <implementation>
        <pre_selection_thinking>Analyze task characteristics and requirements before framework selection</pre_selection_thinking>
        <selection_reasoning>Deep analysis of framework trade-offs and optimization opportunities</selection_reasoning>
        <post_selection_validation>Validate framework choice against task requirements and constraints</post_selection_validation>
      </implementation>
      <triggers>Complex task analysis, unclear requirements, multiple viable options</triggers>
    </selection_thinking_integration>
    
    <parallel_selection_optimization>
      <purpose>Optimize framework selection process for Claude 4 parallel execution</purpose>
      <implementation>
        <parallel_analysis>Evaluate multiple frameworks simultaneously during selection</parallel_analysis>
        <concurrent_validation>Validate framework options against multiple criteria in parallel</concurrent_validation>
        <batch_recommendation>Generate multiple recommendation strategies simultaneously</batch_recommendation>
      </implementation>
      <performance_benefits>Faster selection process with comprehensive analysis</performance_benefits>
    </parallel_selection_optimization>
    
    <context_aware_selection>
      <purpose>Optimize framework selection based on available context and constraints</purpose>
      <implementation>
        <context_budget_awareness>Consider available context window for framework complexity</context_budget_awareness>
        <token_optimization>Select frameworks that maximize value within token constraints</token_optimization>
        <adaptive_complexity>Adjust framework recommendation based on context availability</adaptive_complexity>
      </implementation>
      <optimization_targets>Maximum value delivery within context and performance constraints</optimization_targets>
    </context_aware_selection>
    
  </claude_4_optimization>
  
  <validation_criteria>
    
    <selection_accuracy>
      <criterion>Framework recommendations must align with task characteristics and requirements</criterion>
      <criterion>Selection algorithm must be consistent and repeatable for similar tasks</criterion>
      <criterion>Alternative recommendations must provide genuine value and flexibility</criterion>
      <criterion>Combination strategies must offer clear benefits over single framework approaches</criterion>
    </selection_accuracy>
    
    <usability_validation>
      <criterion>Selection interface must be intuitive and easy to use</criterion>
      <criterion>Reasoning explanations must be clear and actionable</criterion>
      <criterion>Framework selection must reduce choice paralysis and decision overhead</criterion>
      <criterion>Integration with commands must be seamless and transparent</criterion>
    </usability_validation>
    
    <performance_validation>
      <criterion>Selection process must complete within reasonable time constraints</criterion>
      <criterion>Framework recommendations must improve task execution efficiency</criterion>
      <criterion>Claude 4 optimizations must provide measurable performance benefits</criterion>
      <criterion>Context utilization must be optimized for maximum effectiveness</criterion>
    </performance_validation>
    
  </validation_criteria>
  
  <integration_points>
    <depends_on>
      frameworks/rise.md for foundational framework patterns and implementation guidance
      frameworks/trace.md for precision framework approaches and technical specifications  
      frameworks/care.md for evaluation patterns and outcome validation methods
      frameworks/advanced-frameworks.md for comprehensive framework ecosystem and selection criteria
      patterns/intelligent-routing.md for routing intelligence and decision patterns
      quality/universal-quality-gates.md for framework validation and quality standards
    </depends_on>
    <provides_to>
      All commands for intelligent framework selection and optimization
      patterns/intelligent-routing.md for framework-aware routing decisions
      development/task-management.md for task-specific framework optimization
      patterns/multi-agent.md for multi-framework coordination strategies
      quality/framework-metrics.md for framework effectiveness measurement and optimization
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">intelligent_selection</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">decision_optimization</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">adaptive_routing</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">performance_optimization</uses_pattern>
    <implementation_notes>
      Framework selector implements intelligent_selection pattern for optimal framework choice
      Selection algorithm uses decision_optimization pattern for consistent and effective choices
      Integration patterns leverage adaptive_routing pattern for context-aware framework selection
      Claude 4 optimization follows performance_optimization pattern for maximum efficiency
      Module provides foundation for intelligent framework ecosystem with reduced choice paralysis
    </implementation_notes>
  </pattern_usage>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Intelligent framework selection engine providing automated framework choice based on task characteristics, complexity, domain, and interaction style, with combination strategies and Claude 4 optimization for optimal prompting framework selection and execution.