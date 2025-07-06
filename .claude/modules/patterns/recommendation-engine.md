# Pattern Recommendation Engine

## Overview

Intelligent recommendation system that analyzes task context, user preferences, and historical performance to suggest optimal prompt engineering patterns. This engine learns from usage patterns and continuously improves recommendations.

## Framework Integration

<delegation_reference>
  This module implements intelligent pattern recommendations for all Claude Code commands
</delegation_reference>

## Recommendation Architecture

### Context Analysis Framework

<context_analyzer>
  <task_characterization>
    <input_complexity>
      <simple_tasks>
        <indicators>["basic query", "simple request", "straightforward task"]</indicators>
        <recommended_patterns>["zero-shot", "template-based"]</recommended_patterns>
        <complexity_score>0.1-0.3</complexity_score>
      </simple_tasks>
      
      <moderate_tasks>
        <indicators>["multi-step", "requires analysis", "format conversion"]</indicators>
        <recommended_patterns>["few-shot", "chain-of-thought", "xml-structured"]</recommended_patterns>
        <complexity_score>0.4-0.6</complexity_score>
      </moderate_tasks>
      
      <complex_tasks>
        <indicators>["strategic thinking", "creative problem-solving", "system design"]</indicators>
        <recommended_patterns>["tree-of-thought", "self-consistency", "meta-learning"]</recommended_patterns>
        <complexity_score>0.7-1.0</complexity_score>
      </complex_tasks>
    </input_complexity>
    
    <domain_classification>
      <technical_domains>
        <identifiers>["code", "programming", "algorithm", "system", "technical", "engineering"]</identifiers>
        <preferred_patterns>["chain-of-thought", "xml-structured", "few-shot"]</preferred_patterns>
        <reasoning>Technical tasks benefit from logical reasoning and structured output</reasoning>
      </technical_domains>
      
      <creative_domains>
        <identifiers>["creative", "design", "content", "story", "marketing", "artistic"]</identifiers>
        <preferred_patterns>["tree-of-thought", "role-based", "few-shot"]</preferred_patterns>
        <reasoning>Creative tasks benefit from exploration and persona-based approaches</reasoning>
      </creative_domains>
      
      <analytical_domains>
        <identifiers>["analyze", "research", "evaluate", "compare", "assess", "study"]</identifiers>
        <preferred_patterns>["self-consistency", "chain-of-thought", "xml-structured"]</preferred_patterns>
        <reasoning>Analytical tasks require systematic reasoning and validation</reasoning>
      </analytical_domains>
      
      <operational_domains>
        <identifiers>["process", "workflow", "manage", "organize", "plan", "execute"]</identifiers>
        <preferred_patterns>["template-based", "xml-structured", "few-shot"]</preferred_patterns>
        <reasoning>Operational tasks benefit from structure and proven formats</reasoning>
      </operational_domains>
    </domain_classification>
    
    <intent_recognition>
      <information_seeking>
        <patterns>["question", "what", "how", "why", "explain", "describe"]</patterns>
        <recommended_approach>["zero-shot", "role-based"] with domain expertise</recommended_approach>
      </information_seeking>
      
      <problem_solving>
        <patterns>["solve", "fix", "resolve", "debug", "troubleshoot", "optimize"]</patterns>
        <recommended_approach>["chain-of-thought", "tree-of-thought"] for systematic exploration</recommended_approach>
      </problem_solving>
      
      <content_creation>
        <patterns>["create", "generate", "write", "design", "build", "develop"]</patterns>
        <recommended_approach>["few-shot", "template-based"] with clear examples</recommended_approach>
      </content_creation>
      
      <analysis_evaluation>
        <patterns>["analyze", "evaluate", "compare", "assess", "review", "critique"]</patterns>
        <recommended_approach>["self-consistency", "xml-structured"] for thorough analysis</recommended_approach>
      </analysis_evaluation>
    </intent_recognition>
  </task_characterization>
  
  <user_profile_analysis>
    <experience_level>
      <novice_users>
        <indicators>["simple language", "basic requests", "help-seeking"]</indicators>
        <recommended_patterns>["template-based", "few-shot"] with clear examples</recommended_patterns>
        <explanation_level>detailed with reasoning</explanation_level>
      </novice_users>
      
      <intermediate_users>
        <indicators>["specific terminology", "moderate complexity", "efficiency-focused"]</indicators>
        <recommended_patterns>["chain-of-thought", "xml-structured"] with optimization</recommended_patterns>
        <explanation_level>balanced detail</explanation_level>
      </intermediate_users>
      
      <expert_users>
        <indicators>["advanced concepts", "complex requests", "customization needs"]</indicators>
        <recommended_patterns>["tree-of-thought", "meta-learning"] with advanced techniques</recommended_patterns>
        <explanation_level>minimal, focus on results</explanation_level>
      </expert_users>
    </experience_level>
    
    <preference_patterns>
      <verbosity_preference>
        <concise>Prefer token-efficient patterns</concise>
        <detailed>Accept verbose patterns for thoroughness</detailed>
        <adaptive>Adjust based on task complexity</adaptive>
      </verbosity_preference>
      
      <structure_preference>
        <highly_structured>Strong preference for XML and template patterns</highly_structured>
        <moderately_structured>Balanced approach to organization</moderately_structured>
        <flexible_structure>Adaptive to task requirements</flexible_structure>
      </structure_preference>
      
      <reasoning_preference>
        <explicit_reasoning>Always show logical steps</explicit_reasoning>
        <implicit_reasoning>Focus on results over process</implicit_reasoning>
        <context_dependent>Reasoning detail based on task type</context_dependent>
      </reasoning_preference>
    </preference_patterns>
  </user_profile_analysis>
</context_analyzer>

## Recommendation Algorithm

### Multi-Factor Scoring System

<scoring_algorithm>
  <factor_weights>
    <task_complexity_match>0.25</task_complexity_match>
    <domain_alignment>0.20</domain_alignment>
    <intent_compatibility>0.15</intent_compatibility>
    <user_preference_fit>0.15</user_preference_fit>
    <historical_performance>0.15</historical_performance>
    <constraint_satisfaction>0.10</constraint_satisfaction>
  </factor_weights>
  
  <scoring_calculation>
    <complexity_score>
      pattern_complexity_score = 1.0 - abs(task_complexity - pattern_optimal_complexity)
    </complexity_score>
    
    <domain_score>
      domain_score = pattern_domain_affinity[detected_domain] || 0.5
    </domain_score>
    
    <intent_score>
      intent_score = pattern_intent_compatibility[detected_intent] || 0.5
    </intent_score>
    
    <preference_score>
      preference_score = weighted_average(user_preferences_match)
    </preference_score>
    
    <performance_score>
      performance_score = (success_rate * 0.6) + (efficiency_score * 0.4)
    </performance_score>
    
    <constraint_score>
      constraint_score = min(token_fit, time_fit, accuracy_fit)
    </constraint_score>
    
    <final_score>
      final_score = (complexity_score * 0.25) + 
                   (domain_score * 0.20) + 
                   (intent_score * 0.15) + 
                   (preference_score * 0.15) + 
                   (performance_score * 0.15) + 
                   (constraint_score * 0.10)
    </final_score>
  </scoring_calculation>
</scoring_algorithm>

### Recommendation Generation

<recommendation_generator>
  <primary_recommendation>
    <selection_criteria>
      <minimum_score>0.7</minimum_score>
      <confidence_threshold>0.8</confidence_threshold>
      <performance_requirement>success_rate > 0.75</performance_requirement>
    </selection_criteria>
    
    <recommendation_format>
      <pattern_name>Selected pattern identifier</pattern_name>
      <confidence_score>0.0-1.0 confidence level</confidence_score>
      <reasoning>Why this pattern was selected</reasoning>
      <expected_benefits>Anticipated advantages for this task</expected_benefits>
      <customization_suggestions>Specific adaptations for optimal results</customization_suggestions>
    </recommendation_format>
  </primary_recommendation>
  
  <alternative_recommendations>
    <secondary_patterns>
      <selection_criteria>score >= 0.6 AND score < primary_score</selection_criteria>
      <max_alternatives>3</max_alternatives>
      <differentiation_requirement>Must offer meaningfully different approaches</differentiation_requirement>
    </secondary_patterns>
    
    <recommendation_rationale>
      <when_to_use>Specific scenarios where alternative might be better</when_to_use>
      <trade_offs>Advantages and disadvantages compared to primary</trade_offs>
      <combination_potential>How alternative could complement primary pattern</combination_potential>
    </recommendation_rationale>
  </alternative_recommendations>
  
  <hybrid_recommendations>
    <combination_detection>
      <compatible_pairs>Identify patterns that work well together</compatible_pairs>
      <synergy_analysis>Calculate combined effectiveness potential</synergy_analysis>
      <complexity_assessment>Ensure combination doesn't exceed complexity limits</complexity_assessment>
    </combination_detection>
    
    <hybrid_benefits>
      <enhanced_capabilities>What the combination achieves beyond individual patterns</enhanced_capabilities>
      <use_case_scenarios>Specific situations where hybrid approach excels</use_case_scenarios>
      <implementation_guidance>How to effectively combine the patterns</implementation_guidance>
    </hybrid_benefits>
  </hybrid_recommendations>
</recommendation_generator>

## Adaptive Learning System

### Performance Tracking

<learning_system>
  <feedback_collection>
    <implicit_feedback>
      <success_indicators>Task completion, user satisfaction, output quality</success_indicators>
      <efficiency_metrics>Token usage, processing time, iteration count</efficiency_metrics>
      <quality_metrics>Accuracy, relevance, completeness of results</quality_metrics>
    </implicit_feedback>
    
    <explicit_feedback>
      <user_ratings>Direct pattern effectiveness ratings</user_ratings>
      <preference_updates>Changes in user preferences and requirements</preference_updates>
      <outcome_assessments>Success/failure evaluation of recommendations</outcome_assessments>
    </explicit_feedback>
  </feedback_collection>
  
  <pattern_performance_updates>
    <effectiveness_tracking>
      <success_rate_calculation>
        new_success_rate = (old_rate * decay_factor) + (current_outcome * learning_rate)
      </success_rate_calculation>
      
      <efficiency_optimization>
        <token_efficiency>Track average tokens used vs. output quality</token_efficiency>
        <time_efficiency>Monitor processing time and user satisfaction</time_efficiency>
        <accuracy_efficiency>Balance speed vs. correctness for different domains</accuracy_efficiency>
      </efficiency_optimization>
    </effectiveness_tracking>
    
    <contextual_refinement>
      <domain_specialization>Improve pattern recommendations for specific domains</domain_specialization>
      <user_personalization>Adapt to individual user preferences and patterns</user_personalization>
      <task_optimization>Refine pattern selection for specific task types</task_optimization>
    </contextual_refinement>
  </pattern_performance_updates>
</learning_system>

### Recommendation Evolution

<evolution_engine>
  <pattern_discovery>
    <emerging_patterns>
      <pattern_mining>Identify successful novel pattern combinations</pattern_mining>
      <effectiveness_validation>Test new patterns against established benchmarks</effectiveness_validation>
      <community_contribution>Incorporate community-discovered patterns</community_contribution>
    </emerging_patterns>
    
    <pattern_retirement>
      <obsolescence_detection>Identify patterns with declining effectiveness</obsolescence_detection>
      <graceful_deprecation>Gradually phase out underperforming patterns</graceful_deprecation>
      <migration_guidance>Help users transition to better alternatives</migration_guidance>
    </pattern_retirement>
  </pattern_discovery>
  
  <recommendation_refinement>
    <algorithm_improvement>
      <weight_optimization>Adjust factor weights based on performance data</weight_optimization>
      <threshold_tuning>Optimize confidence and selection thresholds</threshold_tuning>
      <bias_correction>Address systematic biases in recommendations</bias_correction>
    </algorithm_improvement>
    
    <context_expansion>
      <new_domains>Add support for emerging task domains</new_domains>
      <edge_cases>Improve handling of unusual or complex scenarios</edge_cases>
      <integration_enhancement>Better alignment with Claude Code framework evolution</integration_enhancement>
    </context_expansion>
  </recommendation_refinement>
</evolution_engine>

## Integration with Framework Commands

### Command-Specific Optimization

<command_optimization>
  <auto_command_integration>
    <intelligent_routing_support>
      <pattern_selection>Patterns that produce structured, parseable output</pattern_selection>
      <decision_transparency>Clear reasoning for downstream routing decisions</decision_transparency>
      <fallback_reliability>Robust patterns that rarely fail</fallback_reliability>
    </intelligent_routing_support>
    
    <module_composition_guidance>
      <compatibility_analysis>Ensure patterns work well with selected modules</compatibility_analysis>
      <orchestration_optimization>Patterns that facilitate multi-module coordination</orchestration_optimization>
    </module_composition_guidance>
  </auto_command_integration>
  
  <task_command_integration>
    <development_workflow_optimization>
      <code_generation>Patterns optimized for programming tasks</code_generation>
      <debugging_support>Patterns that excel at problem diagnosis</debugging_support>
      <documentation_creation>Patterns for clear technical writing</documentation_creation>
    </development_workflow_optimization>
    
    <quality_assurance_alignment>
      <testing_pattern_integration>Patterns that work well with TDD workflows</testing_pattern_integration>
      <security_consideration>Patterns that support security-conscious development</security_consideration>
      <performance_awareness>Patterns that consider performance implications</performance_awareness>
    </quality_assurance_alignment>
  </task_command_integration>
  
  <swarm_command_integration>
    <multi_agent_coordination>
      <communication_patterns>Patterns that facilitate agent-to-agent communication</communication_patterns>
      <task_distribution>Patterns that support work breakdown and assignment</task_distribution>
      <result_aggregation>Patterns that enable effective result combination</result_aggregation>
    </multi_agent_coordination>
    
    <session_management_support>
      <progress_tracking>Patterns that support systematic progress monitoring</progress_tracking>
      <context_preservation>Patterns that maintain context across agent handoffs</context_preservation>
      <outcome_documentation>Patterns that facilitate comprehensive result documentation</outcome_documentation>
    </session_management_support>
  </swarm_command_integration>
</command_optimization>

### Real-Time Recommendation API

<recommendation_api>
  <request_processing>
    <input_format>
      {
        "user_input": "task description",
        "context": {
          "command": "auto|task|query|swarm",
          "constraints": {
            "token_limit": number,
            "time_limit": number,
            "accuracy_requirement": number
          },
          "user_preferences": {
            "verbosity": "concise|detailed|adaptive",
            "structure": "high|medium|flexible",
            "reasoning": "explicit|implicit|contextual"
          }
        },
        "history": [
          {
            "pattern": "pattern_id",
            "effectiveness": number,
            "user_satisfaction": number
          }
        ]
      }
    </input_format>
    
    <response_format>
      {
        "primary_recommendation": {
          "pattern_id": "string",
          "pattern_name": "string",
          "confidence": number,
          "reasoning": "string",
          "expected_benefits": ["string"],
          "customizations": ["string"]
        },
        "alternatives": [
          {
            "pattern_id": "string",
            "pattern_name": "string",
            "score": number,
            "use_cases": ["string"],
            "trade_offs": "string"
          }
        ],
        "hybrid_options": [
          {
            "primary_pattern": "string",
            "secondary_pattern": "string",
            "synergy_benefits": "string",
            "implementation_guidance": "string"
          }
        ]
      }
    </response_format>
  </request_processing>
  
  <performance_requirements>
    <response_time>< 100ms for standard recommendations</response_time>
    <accuracy_target>85% user satisfaction with primary recommendations</accuracy_target>
    <learning_rate>Continuous improvement with each interaction</learning_rate>
  </performance_requirements>
</recommendation_api>

---

*This recommendation engine provides intelligent, adaptive pattern selection that learns from usage and continuously improves the effectiveness of prompt engineering within the Claude Code framework.*