---
version: 1.0.0
last_updated: 2025-07-07
status: stable
---

<module name="prompt_evaluation" category="patterns">
  
  <purpose>
    Implement native Claude Code multi-agent evaluation system for comprehensive prompt analysis using Task() patterns for parallel evaluation across multiple specialized dimensions.
  </purpose>
  
  <trigger_conditions>
    <condition type="explicit">User requests prompt evaluation or improvement</condition>
    <condition type="automatic">Quality gates require prompt validation</condition>
    <condition type="comparative">Multiple prompt versions need comparison</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="evaluation_initialization" order="1">
      <requirements>
        Prompt content validated and prepared for evaluation
        Evaluation criteria configuration loaded
        Specialized evaluator agents instantiated
        GitHub session created for tracking evaluation progress
      </requirements>
      <actions>
        Validate prompt content for completeness and structure
        Load evaluation criteria templates and scoring methodology
        Initialize four specialized evaluator agents with distinct focuses
        Create GitHub session for evaluation coordination and results tracking
      </actions>
      <validation>
        Prompt content properly formatted and ready for evaluation
        All evaluation criteria defined with clear scoring rubrics
        All four evaluator agents properly instantiated and assigned
        Session created with evaluation tracking labels and structure
      </validation>
    </phase>
    
    <phase name="parallel_evaluation" order="2">
      <requirements>
        All evaluator agents execute in parallel using single message
        Each agent evaluates independent criteria without dependencies
        Session serves as coordination hub for evaluation progress
        Results collected in standardized format for aggregation
      </requirements>
      <actions>
        Execute all Task() evaluations in single message for true parallelism
        Clarity evaluator assesses prompt clarity and specificity
        Efficiency analyzer evaluates token usage and conciseness
        Model optimizer determines optimal Claude model selection
        Improvement generator creates enhanced prompt variations
      </actions>
      <validation>
        All evaluator agents working in parallel coordination
        No blocking dependencies between evaluation tasks
        Session actively tracking evaluation progress from all agents
        Results formatted consistently for downstream processing
      </validation>
    </phase>
    
    <phase name="result_aggregation" order="3">
      <requirements>
        All evaluator results successfully collected and validated
        Consensus mechanism applied to resolve scoring conflicts
        Comprehensive evaluation report generated in markdown format
        Session documentation complete with evaluation outcomes
      </requirements>
      <actions>
        Collect and validate all evaluator agent results
        Apply weighted consensus algorithm to aggregate scores
        Generate comprehensive evaluation report with improvement recommendations
        Document evaluation process and outcomes in session
      </actions>
      <validation>
        All evaluator results integrated without conflicts
        Final scores reflect accurate consensus across all evaluators
        Evaluation report complete with actionable recommendations
        Session documentation captures full evaluation process
      </validation>
    </phase>
    
  </implementation>
  
  <evaluation_criteria>
    <clarity_assessment>
      <focus>Language clarity, instruction specificity, ambiguity elimination</focus>
      <scoring_factors>
        <factor weight="30">Instruction specificity and detail level</factor>
        <factor weight="25">Language clarity and comprehensibility</factor>
        <factor weight="25">Ambiguity detection and elimination</factor>
        <factor weight="20">Context completeness and relevance</factor>
      </scoring_factors>
      <score_range>1-10 (1=extremely unclear, 10=crystal clear)</score_range>
    </clarity_assessment>
    
    <efficiency_analysis>
      <focus>Token optimization, redundancy elimination, conciseness</focus>
      <scoring_factors>
        <factor weight="35">Token usage efficiency and optimization</factor>
        <factor weight="30">Redundancy elimination and conciseness</factor>
        <factor weight="25">Information density and relevance</factor>
        <factor weight="10">Structural organization and flow</factor>
      </scoring_factors>
      <score_range>1-10 (1=extremely inefficient, 10=perfectly optimized)</score_range>
    </efficiency_analysis>
    
    <model_optimization>
      <focus>Claude model selection, capability matching, cost optimization</focus>
      <analysis_factors>
        <factor>Task complexity assessment for model requirements</factor>
        <factor>Claude Opus vs Sonnet capability matching</factor>
        <factor>Cost-benefit analysis for model selection</factor>
        <factor>Performance requirements vs model capabilities</factor>
      </analysis_factors>
      <output_format>Recommended model with detailed rationale</output_format>
    </model_optimization>
    
    <improvement_generation>
      <focus>Enhanced prompt creation, optimization implementation</focus>
      <improvement_areas>
        <area>Clarity enhancements with specific language improvements</area>
        <area>Efficiency optimizations with token reduction strategies</area>
        <area>Structure improvements with better organization</area>
        <area>Context additions for better Claude understanding</area>
      </improvement_areas>
      <output_format>Enhanced prompt with detailed improvement explanations</output_format>
    </improvement_generation>
  </evaluation_criteria>
  
  <evaluator_agents>
    <clarity_evaluator>
      <specialization>Language clarity, instruction specificity, ambiguity detection</specialization>
      <evaluation_process>
        Analyze prompt language for clarity and precision
        Identify ambiguous phrasing and unclear instructions
        Assess context completeness and relevance
        Score clarity factors with detailed justification
      </evaluation_process>
      <output_format>
        Clarity score (1-10) with detailed breakdown
        Specific ambiguity issues identified
        Language clarity recommendations
        Context completeness assessment
      </output_format>
    </clarity_evaluator>
    
    <efficiency_analyzer>
      <specialization>Token optimization, redundancy elimination, information density</specialization>
      <evaluation_process>
        Count tokens and assess usage efficiency
        Identify redundant phrases and unnecessary content
        Evaluate information density and relevance
        Recommend conciseness improvements
      </evaluation_process>
      <output_format>
        Efficiency score (1-10) with token analysis
        Redundancy elimination suggestions
        Conciseness improvement recommendations
        Information density optimization
      </output_format>
    </efficiency_analyzer>
    
    <model_optimizer>
      <specialization>Claude model selection, capability matching, performance optimization</specialization>
      <evaluation_process>
        Assess task complexity for model requirements
        Compare Claude Opus vs Sonnet capabilities
        Analyze cost-benefit for model selection
        Recommend optimal model with rationale
      </evaluation_process>
      <output_format>
        Recommended Claude model (Opus/Sonnet/Haiku)
        Detailed rationale for model selection
        Capability matching analysis
        Cost-benefit assessment
      </output_format>
    </model_optimizer>
    
    <improvement_generator>
      <specialization>Enhanced prompt creation, optimization implementation</specialization>
      <evaluation_process>
        Synthesize feedback from other evaluators
        Create enhanced prompt incorporating improvements
        Explain each improvement with rationale
        Validate enhanced version against original
      </evaluation_process>
      <output_format>
        Enhanced prompt with all improvements applied
        Detailed improvement explanations
        Before/after comparison analysis
        Validation against original requirements
      </output_format>
    </improvement_generator>
  </evaluator_agents>
  
  <consensus_mechanism>
    <aggregation_method>
      <scoring_consensus>
        Weighted average of all evaluator scores
        Conflict resolution through detailed analysis
        Outlier detection and investigation
        Final score validation against criteria
      </scoring_consensus>
      <recommendation_synthesis>
        Combine all evaluator recommendations
        Prioritize improvements by impact and feasibility
        Create comprehensive improvement plan
        Validate recommendations against evaluation criteria
      </recommendation_synthesis>
    </aggregation_method>
    
    <conflict_resolution>
      <score_discrepancy>
        Identify significant score differences (>2 points)
        Analyze underlying reasoning for discrepancies
        Apply weighted consensus based on evaluator expertise
        Document resolution rationale for transparency
      </score_discrepancy>
      <recommendation_conflicts>
        Identify conflicting improvement recommendations
        Assess feasibility and impact of each recommendation
        Prioritize based on evaluation criteria weights
        Create consolidated improvement plan
      </recommendation_conflicts>
    </conflict_resolution>
  </consensus_mechanism>
  
  <evaluation_report_template>
    <markdown_structure>
      # Prompt Evaluation Report
      **Date**: {timestamp}
      **Prompt**: {prompt_name}
      **Evaluator Session**: {session_id}
      
      ## Executive Summary
      - **Overall Score**: {composite_score}/10
      - **Recommended Model**: {model_recommendation}
      - **Key Improvements**: {top_3_improvements}
      
      ## Detailed Scores
      ### Clarity Assessment
      - **Score**: {clarity_score}/10
      - **Strengths**: {clarity_strengths}
      - **Issues**: {clarity_issues}
      - **Recommendations**: {clarity_recommendations}
      
      ### Efficiency Analysis
      - **Score**: {efficiency_score}/10
      - **Token Count**: {token_count}
      - **Optimization Potential**: {optimization_potential}
      - **Recommendations**: {efficiency_recommendations}
      
      ### Model Optimization
      - **Recommended Model**: {recommended_model}
      - **Rationale**: {model_rationale}
      - **Performance Impact**: {performance_impact}
      - **Cost Analysis**: {cost_analysis}
      
      ## Enhanced Prompt
      ```
      {enhanced_prompt}
      ```
      
      ## Improvement Explanations
      {improvement_explanations}
      
      ## Evaluation Methodology
      - **Evaluator Agents**: 4 specialized agents
      - **Evaluation Criteria**: {criteria_summary}
      - **Consensus Method**: {consensus_method}
      - **Quality Assurance**: {qa_process}
      
      ## Appendix
      ### Original Prompt
      ```
      {original_prompt}
      ```
      
      ### Individual Evaluator Reports
      {individual_reports}
    </markdown_structure>
  </evaluation_report_template>
  
  <comparison_functionality>
    <version_comparison>
      <process>
        Execute parallel evaluation for all prompt versions
        Generate comparative analysis across all versions
        Identify improvements and regressions between versions
        Recommend optimal version with detailed justification
      </process>
      <output_format>
        Comparison matrix with scores across all versions
        Detailed analysis of improvements and regressions
        Recommended version with comprehensive rationale
        Evolution analysis showing prompt development progress
      </output_format>
    </version_comparison>
    
    <benchmark_comparison>
      <process>
        Compare evaluation results against established benchmarks
        Identify performance gaps and improvement opportunities
        Track evaluation trends over time
        Generate benchmark compliance reports
      </process>
      <output_format>
        Benchmark compliance score and analysis
        Performance gap identification with recommendations
        Trend analysis with historical comparison
        Compliance report with improvement roadmap
      </output_format>
    </benchmark_comparison>
  </comparison_functionality>
  
  <evaluation_api>
    <interface_definition>
      <function name="evaluate_prompt">
        <parameters>
          <parameter name="prompt_content" type="string" required="true">Prompt to evaluate</parameter>
          <parameter name="criteria_config" type="object" required="false">Custom evaluation criteria</parameter>
          <parameter name="session_id" type="string" required="false">Existing session for tracking</parameter>
        </parameters>
        <returns>
          <return name="evaluation_results" type="object">Complete evaluation results</return>
          <return name="enhanced_prompt" type="string">Improved version</return>
          <return name="session_url" type="string">Session tracking URL</return>
        </returns>
      </function>
      
      <function name="compare_prompts">
        <parameters>
          <parameter name="prompt_versions" type="array" required="true">Array of prompt versions</parameter>
          <parameter name="comparison_criteria" type="object" required="false">Custom comparison criteria</parameter>
        </parameters>
        <returns>
          <return name="comparison_matrix" type="object">Detailed comparison results</return>
          <return name="recommended_version" type="string">Optimal prompt version</return>
          <return name="improvement_analysis" type="object">Evolution analysis</return>
        </returns>
      </function>
    </interface_definition>
  </evaluation_api>
  
  <evaluation_benchmarks>
    <quality_benchmarks>
      <clarity_benchmark>
        <excellent>9-10 points: Crystal clear, no ambiguity</excellent>
        <good>7-8 points: Clear with minor ambiguity</good>
        <acceptable>5-6 points: Generally clear with some issues</acceptable>
        <poor>3-4 points: Significant clarity problems</poor>
        <unacceptable>1-2 points: Extremely unclear or ambiguous</unacceptable>
      </clarity_benchmark>
      
      <efficiency_benchmark>
        <excellent>9-10 points: Highly optimized, minimal tokens</excellent>
        <good>7-8 points: Well optimized with minor redundancy</good>
        <acceptable>5-6 points: Reasonably efficient</acceptable>
        <poor>3-4 points: Significant inefficiency</poor>
        <unacceptable>1-2 points: Extremely inefficient</unacceptable>
      </efficiency_benchmark>
    </quality_benchmarks>
    
    <performance_benchmarks>
      <evaluation_speed>Maximum 30 seconds for standard prompt evaluation</evaluation_speed>
      <accuracy_target>95% consistency across repeated evaluations</accuracy_target>
      <coverage_requirement>100% evaluation criteria coverage</coverage_requirement>
    </performance_benchmarks>
  </evaluation_benchmarks>
  
  <automated_triggers>
    <quality_gate_integration>
      <trigger>Before prompt deployment in production workflows</trigger>
      <action>Automatic evaluation with minimum quality thresholds</action>
      <escalation>Manual review required for scores below benchmarks</escalation>
    </quality_gate_integration>
    
    <continuous_improvement>
      <trigger>Weekly batch evaluation of all production prompts</trigger>
      <action>Trend analysis and improvement recommendations</action>
      <escalation>Proactive prompt optimization based on analysis</escalation>
    </continuous_improvement>
  </automated_triggers>
  
  <session_integration>
    <mandatory_creation>
      All multi-agent evaluations automatically create GitHub session
      Session provides coordination hub for evaluator communication
      Progress tracking enables visibility into parallel evaluation streams
    </mandatory_creation>
    <session_documentation>
      Evaluator assignments and specialized responsibilities
      Progress milestones and completion status tracking
      Evaluation decisions requiring cross-evaluator coordination
      Final results and improvement recommendations
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/multi-agent.md for Task() parallel execution patterns
      patterns/session-management.md for automatic session creation
      quality/production-standards.md for evaluation benchmarks
    </depends_on>
    <provides_to>
      development/prompt-engineering.md for prompt optimization
      All commands for prompt quality validation
      patterns/intelligent-routing.md for evaluation-based routing
    </provides_to>
  </integration_points>
  
</module>