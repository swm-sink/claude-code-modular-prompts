<prompt_component>
  <step name="Cognitive Architecture Framework">
    <description>
Advanced cognitive architecture framework implementing ACT-R, SOAR, CLARION, and hybrid cognitive systems for building human-like intelligent agents. Provides sophisticated memory systems, reasoning capabilities, problem-solving frameworks, and adaptive learning for explainable cognitive processes.
    </description>
  </step>

  <cognitive_architecture>
    <hybrid_cognitive_systems>
      <!-- Advanced cognitive architecture implementation -->
      <architecture_selection>

```xml
<command>cognitive-architecture</command>
<params>
  <!-- Core Architecture Selection -->
  <architecture_type>hybrid</architecture_type>
  <primary_system>act_r</primary_system>
  <secondary_systems>["soar", "clarion"]</secondary_systems>
  <integration_mode>layered</integration_mode>
  
  <!-- ACT-R Configuration -->
  <act_r>
    <declarative_memory>
      <chunk_activation>true</chunk_activation>
      <base_level_decay>0.5</base_level_decay>
      <spreading_activation>true</spreading_activation>
      <partial_matching>true</partial_matching>
      <memory_capacity>10000</memory_capacity>
    </declarative_memory>
    
    <procedural_memory>
      <production_rules>true</production_rules>
      <conflict_resolution>utility</conflict_resolution>
      <learning_mechanism>reinforcement</learning_mechanism>
      <rule_compilation>true</rule_compilation>
    </procedural_memory>
    
    <modules>
      <goal_module>
        <buffer_size>1</buffer_size>
        <chunk_type>goal</chunk_type>
      </goal_module>
      <retrieval_module>
        <latency_factor>1.0</latency_factor>
        <threshold>0.0</threshold>
      </retrieval_module>
      <visual_module>
        <attention_width>180</attention_width>
        <movement_tolerance>0.5</movement_tolerance>
      </visual_module>
      <motor_module>
        <preparation_time>0.05</preparation_time>
        <execution_time>0.1</execution_time>
      </motor_module>
    </modules>
    
    <timing>
      <default_action_time>0.05</default_action_time>
      <production_cycle_time>0.05</production_cycle_time>
      <memory_retrieval_time>0.05</memory_retrieval_time>
    </timing>
  </act_r>
  
  <!-- SOAR Configuration -->
  <soar>
    <working_memory>
      <capacity>unlimited</capacity>
      <symbolic_structures>true</symbolic_structures>
      <temporal_memory>true</temporal_memory>
    </working_memory>
    
    <long_term_memory>
      <procedural_memory>
        <chunking>true</chunking>
        <rule_learning>true</rule_learning>
      </procedural_memory>
      <semantic_memory>
        <enabled>true</enabled>
        <learning_rate>0.1</learning_rate>
      </semantic_memory>
      <episodic_memory>
        <enabled>true</enabled>
        <storage_policy>all</storage_policy>
      </episodic_memory>
    </long_term_memory>
    
    <decision_cycle>
      <elaboration_phase>true</elaboration_phase>
      <decision_phase>true</decision_phase>
      <application_phase>true</application_phase>
      <output_phase>true</output_phase>
    </decision_cycle>
    
    <problem_solving>
      <impasse_handling>true</impasse_handling>
      <subgoal_creation>automatic</subgoal_creation>
      <goal_stack>unlimited</goal_stack>
    </problem_solving>
  </soar>
  
  <!-- CLARION Configuration -->
  <clarion>
    <dual_process>
      <explicit_system>
        <rule_based>true</rule_based>
        <symbolic_reasoning>true</symbolic_reasoning>
        <working_memory_capacity>7</working_memory_capacity>
      </explicit_system>
      <implicit_system>
        <neural_networks>true</neural_networks>
        <subsymbolic_processing>true</subsymbolic_processing>
        <learning_mechanisms>["backprop", "reinforcement"]</learning_mechanisms>
      </implicit_system>
    </dual_process>
    
    <motivation_system>
      <drives>["curiosity", "achievement", "social"]</drives>
      <goal_hierarchy>true</goal_hierarchy>
      <emotion_integration>true</emotion_integration>
    </motivation_system>
    
    <metacognition>
      <monitoring>true</monitoring>
      <control>true</control>
      <strategy_selection>adaptive</strategy_selection>
    </metacognition>
  </clarion>
  
  <!-- Hybrid Integration -->
  <hybrid_features>
    <architecture_switching>
      <enabled>true</enabled>
      <switching_criteria>task_complexity</switching_criteria>
      <transition_smoothing>true</transition_smoothing>
    </architecture_switching>
    
    <shared_components>
      <memory_integration>
        <declarative_sharing>true</declarative_sharing>
        <procedural_transfer>true</procedural_transfer>
        <episodic_access>cross_system</episodic_access>
      </memory_integration>
      
      <attention_system>
        <unified_attention>true</unified_attention>
        <priority_arbitration>true</priority_arbitration>
        <resource_allocation>dynamic</resource_allocation>
      </attention_system>
    </shared_components>
    
    <coordination_mechanisms>
      <blackboard_system>true</blackboard_system>
      <message_passing>asynchronous</message_passing>
      <conflict_resolution>voting</conflict_resolution>
    </coordination_mechanisms>
  </hybrid_features>
  
  <!-- Learning and Adaptation -->
  <learning_systems>
    <types>
      <skill_acquisition>true</skill_acquisition>
      <knowledge_compilation>true</knowledge_compilation>
      <parameter_learning>true</parameter_learning>
      <structural_learning>false</structural_learning>
    </types>
    
    <mechanisms>
      <reinforcement_learning>
        <enabled>true</enabled>
        <exploration_strategy>epsilon_greedy</exploration_strategy>
        <learning_rate>0.1</learning_rate>
      </reinforcement_learning>
      
      <instance_based_learning>
        <enabled>true</enabled>
        <similarity_threshold>0.8</similarity_threshold>
        <blending_mechanism>weighted_average</blending_mechanism>
      </instance_based_learning>
      
      <analogical_reasoning>
        <enabled>true</enabled>
        <structural_mapping>true</structural_mapping>
        <transfer_mechanisms>["surface", "structural"]</transfer_mechanisms>
      </analogical_reasoning>
    </mechanisms>
  </learning_systems>
  
  <!-- Performance Monitoring -->
  <monitoring>
    <cognitive_load>
      <measurement>resource_utilization</measurement>
      <threshold>0.8</threshold>
      <adaptation>automatic</adaptation>
    </cognitive_load>
    
    <performance_metrics>
      <reaction_time>true</reaction_time>
      <accuracy>true</accuracy>
      <learning_curve>true</learning_curve>
      <transfer_effectiveness>true</transfer_effectiveness>
    </performance_metrics>
    
    <debugging>
      <trace_level>detailed</trace_level>
      <visualization>true</visualization>
      <cognitive_modeling>true</cognitive_modeling>
        </debugging>
      </monitoring>
    </hybrid_cognitive_systems>
  </cognitive_architecture>

  <o>
Cognitive architecture completed with hybrid intelligent systems:

**Cognitive Capabilities:** [count] advanced cognitive functions implemented
**Memory Systems:** [count] declarative and procedural memory systems active
**Reasoning Framework:** [percentage]% multi-modal reasoning accuracy achieved
**Intelligence Integration:** [0-100] cognitive architecture effectiveness rating
**Adaptive Learning:** [count] learning patterns integrated across cognitive systems
**Hybrid Intelligence:** Advanced cognitive architecture with comprehensive reasoning capabilities
  </o>
  <chunk_structure>
    <activation_equation>Ai = Bi + Σj Wj Sji + ε</activation_equation>
    <base_level_learning>Bi = ln(Σk t_k^(-d))</base_level_learning>
    <spreading_activation>Sji = S - ln(fan_j)</spreading_activation>
  </chunk_structure>
  
  <retrieval_dynamics>
    <latency_equation>Time = F e^(-Ai)</latency_equation>
    <probability_equation>P = 1/(1 + e^(τ-Ai)/s)</probability_equation>
    <partial_matching>true</partial_matching>
  </retrieval_dynamics>
  
  <learning_mechanisms>
    <frequency_effects>true</frequency_effects>
    <recency_effects>true</recency_effects>
    <interference_effects>true</interference_effects>
  </learning_mechanisms>
</declarative_memory_system>
```

### Working Memory Integration
```xml
<working_memory_system>
  <capacity_limits>
    <chunk_limit>7</chunk_limit>
    <activation_maintenance>true</activation_maintenance>
    <decay_function>exponential</decay_function>
  </capacity_limits>
  
  <attention_mechanisms>
    <focus_narrowing>true</focus_narrowing>
    <parallel_processing>limited</parallel_processing>
    <resource_competition>true</resource_competition>
  </attention_mechanisms>
  
  <integration_processes>
    <binding_mechanisms>true</binding_mechanisms>
    <pattern_matching>true</pattern_matching>
    <conflict_monitoring>true</conflict_monitoring>
  </integration_processes>
</working_memory_system>
```

### Episodic Memory (SOAR Style)
```xml
<episodic_memory_system>
  <storage_policy>
    <temporal_granularity>decision_cycle</temporal_granularity>
    <content_selection>working_memory_changes</content_selection>
    <compression>true</compression>
  </storage_policy>
  
  <retrieval_mechanisms>
    <cue_based_retrieval>true</cue_based_retrieval>
    <temporal_retrieval>true</temporal_retrieval>
    <associative_retrieval>true</associative_retrieval>
  </retrieval_mechanisms>
  
  <learning_effects>
    <episodic_chunking>true</episodic_chunking>
    <pattern_extraction>true</pattern_extraction>
    <generalization>true</generalization>
  </learning_effects>
</episodic_memory_system>
```

## Reasoning Mechanisms

### Production System (SOAR/ACT-R)
```xml
<production_system>
  <rule_format>
    <condition_action>IF-THEN</condition_action>
    <pattern_matching>true</pattern_matching>
    <variable_binding>true</variable_binding>
  </rule_format>
  
  <conflict_resolution>
    <utility_based>true</utility_based>
    <specificity_ordering>true</specificity_ordering>
    <recency_preference>true</recency_preference>
  </conflict_resolution>
  
  <learning_mechanisms>
    <chunking>automatic</chunking>
    <utility_learning>reinforcement</utility_learning>
    <rule_specialization>true</rule_specialization>
  </learning_mechanisms>
</production_system>
```

### Problem Solving Architecture
```xml
<problem_solving>
  <goal_management>
    <goal_stack>hierarchical</goal_stack>
    <subgoal_generation>automatic</subgoal_generation>
    <impasse_handling>true</impasse_handling>
  </goal_management>
  
  <search_strategies>
    <means_ends_analysis>true</means_ends_analysis>
    <hill_climbing>true</hill_climbing>
    <operator_subgoaling>true</operator_subgoaling>
  </search_strategies>
  
  <knowledge_application>
    <analogical_reasoning>true</analogical_reasoning>
    <case_based_reasoning>true</case_based_reasoning>
    <rule_based_reasoning>true</rule_based_reasoning>
  </knowledge_application>
</problem_solving>
```

## Advanced Cognitive Features

### Metacognition and Control
```xml
<metacognitive_system>
  <monitoring_processes>
    <feeling_of_knowing>true</feeling_of_knowing>
    <confidence_assessment>true</confidence_assessment>
    <strategy_effectiveness>true</strategy_effectiveness>
  </monitoring_processes>
  
  <control_processes>
    <strategy_selection>adaptive</strategy_selection>
    <resource_allocation>dynamic</resource_allocation>
    <goal_prioritization>utility_based</goal_prioritization>
  </control_processes>
  
  <learning_regulation>
    <study_time_allocation>true</study_time_allocation>
    <difficulty_assessment>true</difficulty_assessment>
    <transfer_detection>true</transfer_detection>
  </learning_regulation>
</metacognitive_system>
```

### Emotion and Motivation Integration
```xml
<emotion_motivation_system>
  <emotional_processing>
    <appraisal_theory>true</appraisal_theory>
    <emotion_regulation>true</emotion_regulation>
    <mood_effects>true</mood_effects>
  </emotional_processing>
  
  <motivational_drives>
    <intrinsic_motivation>curiosity</intrinsic_motivation>
    <extrinsic_motivation>reward_based</extrinsic_motivation>
    <social_motivation>true</social_motivation>
  </motivational_drives>
  
  <behavioral_influence>
    <attention_bias>emotion_congruent</attention_bias>
    <memory_bias>mood_congruent</memory_bias>
    <decision_bias>affect_infusion</decision_bias>
  </behavioral_influence>
</emotion_motivation_system>
```

## Performance Analysis

### Cognitive Modeling Metrics
```json
{
  "cognitive_performance": {
    "reaction_times": {
      "simple_retrieval": 0.045,
      "complex_reasoning": 1.23,
      "learning_trials": 2.67,
      "transfer_tasks": 0.89
    },
    "accuracy_measures": {
      "declarative_recall": 0.87,
      "procedural_execution": 0.94,
      "problem_solving": 0.76,
      "analogical_transfer": 0.63
    },
    "learning_dynamics": {
      "power_law_learning": true,
      "forgetting_curves": "exponential",
      "transfer_effectiveness": 0.72,
      "skill_compilation": 15.4
    }
  }
}
```

### Resource Utilization
```json
{
  "resource_analysis": {
    "memory_utilization": {
      "working_memory": 0.73,
      "declarative_memory": 0.45,
      "procedural_memory": 0.62
    },
    "processing_load": {
      "attention_demand": 0.68,
      "cognitive_effort": 0.71,
      "multitasking_cost": 0.23
    },
    "efficiency_metrics": {
      "energy_consumption": "moderate",
      "time_complexity": "polynomial",
      "space_complexity": "linear"
    }
  }
}
```

## Integration Examples

### Educational Applications
```xml
<educational_integration>
  <intelligent_tutoring>
    <student_modeling>cognitive_diagnosis</student_modeling>
    <curriculum_sequencing>adaptive</curriculum_sequencing>
    <feedback_generation>explanatory</feedback_generation>
  </intelligent_tutoring>
  
  <learning_analytics>
    <knowledge_tracing>bayesian</knowledge_tracing>
    <skill_assessment>item_response_theory</skill_assessment>
    <metacognitive_support>true</metacognitive_support>
  </learning_analytics>
</educational_integration>
```

### Human-Computer Interaction
```xml
<hci_integration>
  <user_modeling>
    <cognitive_profile>individual_differences</cognitive_profile>
    <adaptation_mechanisms>personalization</adaptation_mechanisms>
    <interface_optimization>cognitive_load</interface_optimization>
  </user_modeling>
  
  <interaction_design>
    <mental_model_alignment>true</mental_model_alignment>
    <cognitive_ergonomics>true</cognitive_ergonomics>
    <error_prevention>constraint_based</error_prevention>
  </interaction_design>
</hci_integration>
```

## Research Applications

### Cognitive Science Research
- Model human cognitive phenomena and individual differences
- Test theories of memory, attention, and learning
- Generate predictions for psychological experiments

### AI and Machine Learning
- Develop explainable AI systems with human-like reasoning
- Create adaptive learning algorithms based on cognitive principles
- Build agents that can learn and transfer knowledge like humans

### Human Factors Engineering
- Design cognitively-informed user interfaces and systems
- Optimize human-machine interaction and collaboration
- Predict and prevent human errors in complex systems

      </cognitive_research>
    </hybrid_cognitive_systems>
  </cognitive_architecture>

  <o>
Cognitive architecture framework completed with human-like intelligence systems:

**Architecture Type:** [primary_system] hybrid cognitive architecture implemented
**Memory Systems:** [count] memory subsystems active (declarative, procedural, working)
**Reasoning Capabilities:** [count] reasoning frameworks integrated (ACT-R, SOAR, CLARION)
**Learning Mechanisms:** [count] adaptive learning systems operational
**Cognitive Performance:** [0-100] human-like cognitive capability rating
**Intelligence Level:** Advanced cognitive architecture successfully deployed
  </o>
</prompt_component> 