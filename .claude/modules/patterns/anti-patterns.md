# Anti-Pattern Detection System

## Overview

Comprehensive system for identifying, preventing, and correcting common prompt engineering mistakes that reduce effectiveness, create confusion, or lead to poor outcomes.

## Framework Integration

<delegation_reference>
  This module implements anti-pattern detection and prevention for all Claude Code patterns
</delegation_reference>

## Common Anti-Patterns Catalog

### Reasoning Anti-Patterns

<reasoning_anti_patterns>
  <circular_reasoning>
    <description>Pattern that creates logical loops or circular dependencies in reasoning</description>
    <example>
      "Explain why X is true because X is obviously correct, which proves X is true"
    </example>
    <detection_criteria>
      <indicators>["because X", "obviously", "clearly", "self-evident"]</indicators>
      <structural_markers>Premises that reference conclusions</structural_markers>
      <logical_tests>Dependency cycle detection in reasoning chains</logical_tests>
    </detection_criteria>
    <prevention_strategies>
      <strategy>Require independent evidence for each reasoning step</strategy>
      <strategy>Implement reasoning chain validation</strategy>
      <strategy>Add external validation requirements</strategy>
    </prevention_strategies>
    <severity>High - undermines logical integrity</severity>
  </circular_reasoning>
  
  <false_precision>
    <description>Providing overly specific metrics or claims without sufficient basis</description>
    <example>
      "This optimization will improve performance by exactly 23.7% in all scenarios"
    </example>
    <detection_criteria>
      <indicators>Specific percentages, exact numbers without error margins</indicators>
      <context_mismatch>High precision claims in uncertain domains</context_mismatch>
      <confidence_analysis>Precision level exceeds available evidence</confidence_analysis>
    </detection_criteria>
    <correction_methods>
      <method>Replace with ranges or approximate values</method>
      <method>Add uncertainty qualifiers</method>
      <method>Provide confidence intervals where appropriate</method>
    </correction_methods>
    <severity>Medium - creates false confidence</severity>
  </false_precision>
  
  <assumption_stacking>
    <description>Building conclusions on multiple unvalidated assumptions</description>
    <example>
      "Assuming users prefer feature A, and assuming implementation is simple, and assuming no conflicts..."
    </example>
    <detection_criteria>
      <assumption_counting>More than 3 sequential assumptions</assumption_counting>
      <validation_checking>Assumptions not backed by evidence</validation_checking>
      <cascading_risk>Each assumption increases uncertainty</cascading_risk>
    </detection_criteria>
    <mitigation_approaches>
      <approach>Limit assumption chains to 2-3 maximum</approach>
      <approach>Require validation for critical assumptions</approach>
      <approach>Provide alternative scenarios with different assumptions</approach>
    </mitigation_approaches>
    <severity>High - compounds uncertainty</severity>
  </assumption_stacking>
</reasoning_anti_patterns>

### Learning Anti-Patterns

<learning_anti_patterns>
  <example_pollution>
    <description>Using examples that contradict or confuse the intended pattern</description>
    <example>
      Showing JSON format examples when asking for XML output
    </example>
    <detection_criteria>
      <format_inconsistency>Examples in different format than requested</format_inconsistency>
      <conflicting_patterns>Examples demonstrating contradictory approaches</conflicting_patterns>
      <quality_variance>Dramatic quality differences between examples</quality_variance>
    </detection_criteria>
    <prevention_measures>
      <measure>Validate example consistency before use</measure>
      <measure>Use format-specific example validation</measure>
      <measure>Implement example quality scoring</measure>
    </prevention_measures>
    <severity>High - corrupts pattern learning</severity>
  </example_pollution>
  
  <over_specification>
    <description>Providing so many examples that they constrain creativity or generalization</description>
    <example>
      Providing 15+ examples for a simple formatting task
    </example>
    <detection_criteria>
      <example_count>More than 5-7 examples for simple patterns</example_count>
      <redundancy_analysis>Examples that don't add new information</redundancy_analysis>
      <constraint_creep>Examples that overly narrow the solution space</constraint_creep>
    </detection_criteria>
    <optimization_strategies>
      <strategy>Limit examples to 3-5 high-quality demonstrations</strategy>
      <strategy>Ensure each example adds unique value</strategy>
      <strategy>Focus on edge cases rather than redundant examples</strategy>
    </optimization_strategies>
    <severity>Medium - reduces flexibility</severity>
  </over_specification>
  
  <context_free_examples>
    <description>Examples that don't relate to the actual use case or domain</description>
    <example>
      Using cooking examples when teaching software architecture
    </example>
    <detection_criteria>
      <domain_mismatch>Examples from completely different domains</domain_mismatch>
      <abstraction_failure>Examples too abstract to be useful</abstraction_failure>
      <relevance_scoring>Low relevance to target application</relevance_scoring>
    </detection_criteria>
    <correction_techniques>
      <technique>Use domain-specific examples</technique>
      <technique>Ensure examples match use case complexity</technique>
      <technique>Validate example relevance to task context</technique>
    </correction_techniques>
    <severity>Medium - reduces transfer effectiveness</severity>
  </context_free_examples>
</learning_anti_patterns>

### Structural Anti-Patterns

<structural_anti_patterns>
  <information_soup>
    <description>Mixing different types of information without clear organization</description>
    <example>
      Context, examples, constraints, and instructions all in one unstructured paragraph
    </example>
    <detection_criteria>
      <structure_analysis>Lack of clear sections or organization</structure_analysis>
      <information_mixing>Different information types in same sections</information_mixing>
      <cognitive_load>High mental effort required to parse information</cognitive_load>
    </detection_criteria>
    <restructuring_approaches>
      <approach>Implement clear XML or section-based organization</approach>
      <approach>Separate different information types into distinct sections</approach>
      <approach>Use hierarchical structure for complex information</approach>
    </restructuring_approaches>
    <severity>High - creates confusion and errors</severity>
  </information_soup>
  
  <nested_complexity>
    <description>Excessive nesting or hierarchical depth that becomes difficult to follow</description>
    <example>
      XML structures nested 8+ levels deep without clear purpose
    </example>
    <detection_criteria>
      <depth_analysis>More than 5-6 levels of nesting</depth_analysis>
      <navigation_difficulty>Hard to find specific information</navigation_difficulty>
      <maintenance_burden>Complex to update or modify</maintenance_burden>
    </detection_criteria>
    <simplification_methods>
      <method>Flatten hierarchy where possible</method>
      <method>Use references instead of deep nesting</method>
      <method>Break complex structures into multiple simpler ones</method>
    </simplification_methods>
    <severity>Medium - reduces usability</severity>
  </nested_complexity>
  
  <tag_soup>
    <description>Using XML tags without semantic meaning or consistent naming</description>
    <example>
      &lt;thing&gt;&lt;stuff&gt;&lt;data&gt;content&lt;/data&gt;&lt;/stuff&gt;&lt;/thing&gt;
    </example>
    <detection_criteria>
      <semantic_analysis>Tags that don't convey meaning</semantic_analysis>
      <naming_consistency>Inconsistent tag naming patterns</naming_consistency>
      <tag_utility>Tags that don't add structural value</tag_utility>
    </detection_criteria>
    <improvement_guidelines>
      <guideline>Use semantically meaningful tag names</guideline>
      <guideline>Maintain consistent naming conventions</guideline>
      <guideline>Ensure each tag serves a clear organizational purpose</guideline>
    </improvement_guidelines>
    <severity>Medium - reduces clarity and maintainability</severity>
  </tag_soup>
</structural_anti_patterns>

### Optimization Anti-Patterns

<optimization_anti_patterns>
  <premature_optimization>
    <description>Optimizing for efficiency before establishing effectiveness</description>
    <example>
      Focusing on token reduction when the pattern doesn't work correctly yet
    </example>
    <detection_criteria>
      <effectiveness_baseline>Pattern effectiveness below minimum threshold</effectiveness_baseline>
      <optimization_focus>Disproportionate attention to efficiency metrics</optimization_focus>
      <quality_sacrifice>Trading accuracy for marginal efficiency gains</quality_sacrifice>
    </detection_criteria>
    <corrective_actions>
      <action>Establish minimum effectiveness threshold before optimizing</action>
      <action>Focus on correctness and quality first</action>
      <action>Implement staged optimization approach</action>
    </corrective_actions>
    <severity>Medium - misallocates development effort</severity>
  </premature_optimization>
  
  <false_economy>
    <description>Saving tokens in ways that significantly reduce output quality</description>
    <example>
      Removing all examples to save tokens, making the pattern unclear
    </example>
    <detection_criteria>
      <quality_degradation>Significant drop in output quality</quality_degradation>
      <token_savings>Minimal actual token savings</token_savings>
      <cost_benefit_analysis>Poor efficiency gains vs. quality loss ratio</cost_benefit_analysis>
    </detection_criteria>
    <rebalancing_strategies>
      <strategy>Identify high-value components that shouldn't be optimized away</strategy>
      <strategy>Focus optimization on low-value, verbose elements</strategy>
      <strategy>Measure quality impact of each optimization</strategy>
    </rebalancing_strategies>
    <severity>High - undermines pattern purpose</severity>
  </false_economy>
  
  <over_engineering>
    <description>Adding unnecessary complexity in pursuit of theoretical perfection</description>
    <example>
      Implementing complex multi-stage validation for simple yes/no questions
    </example>
    <detection_criteria>
      <complexity_mismatch>Pattern complexity exceeds task complexity</complexity_mismatch>
      <feature_bloat>Many features that aren't actually used</feature_bloat>
      <maintenance_overhead>Disproportionate effort required to maintain</maintenance_overhead>
    </detection_criteria>
    <simplification_approaches>
      <approach>Apply YAGNI (You Aren't Gonna Need It) principle</approach>
      <approach>Remove features not demonstrably improving outcomes</approach>
      <approach>Focus on core functionality and proven value</approach>
    </simplification_approaches>
    <severity>Medium - wastes resources and reduces maintainability</severity>
  </over_engineering>
</optimization_anti_patterns>

## Detection Algorithm

### Real-Time Anti-Pattern Detection

<detection_system>
  <lexical_analysis>
    <keyword_detection>
      <warning_phrases>["obviously", "clearly", "always works", "never fails", "guaranteed"]</warning_phrases>
      <confidence_indicators>["exactly", "precisely", "definitely", "certainly"]</confidence_indicators>
      <assumption_markers>["assuming", "given that", "if we assume", "obviously"]</assumption_markers>
    </keyword_detection>
    
    <pattern_matching>
      <circular_references>Detect when reasoning references itself</circular_references>
      <assumption_chains>Count sequential assumptions without validation</assumption_chains>
      <precision_analysis>Identify overly specific claims without basis</precision_analysis>
    </pattern_matching>
  </lexical_analysis>
  
  <structural_analysis>
    <organization_assessment>
      <section_clarity>Evaluate clear separation of different information types</section_clarity>
      <hierarchy_depth>Measure nesting levels and complexity</hierarchy_depth>
      <tag_semantics>Analyze XML tag meaningfulness and consistency</tag_semantics>
    </organization_assessment>
    
    <complexity_evaluation>
      <cognitive_load>Estimate mental effort required to process pattern</cognitive_load>
      <maintenance_burden>Assess difficulty of updating or modifying pattern</maintenance_burden>
      <usability_score>Measure practical ease of use</usability_score>
    </complexity_evaluation>
  </structural_analysis>
  
  <semantic_analysis>
    <logical_consistency>
      <premise_validation>Check that premises support conclusions</premise_validation>
      <evidence_sufficiency>Evaluate if claims are adequately supported</evidence_sufficiency>
      <reasoning_soundness>Assess logical validity of argument chains</reasoning_soundness>
    </logical_consistency>
    
    <contextual_appropriateness>
      <domain_alignment>Verify examples and references match domain</domain_alignment>
      <complexity_matching>Ensure pattern complexity matches task complexity</complexity_matching>
      <relevance_assessment>Check that all components serve the main purpose</relevance_assessment>
    </contextual_appropriateness>
  </semantic_analysis>
</detection_system>

### Anti-Pattern Scoring

<scoring_algorithm>
  <severity_weighting>
    <critical_score>1.0 - Pattern fundamentally broken or harmful</critical_score>
    <high_score>0.8 - Significant negative impact on effectiveness</high_score>
    <medium_score>0.5 - Moderate reduction in quality or usability</medium_score>
    <low_score>0.2 - Minor issues that should be addressed</low_score>
  </severity_weighting>
  
  <confidence_calculation>
    <detection_confidence>How certain the system is that an anti-pattern exists</detection_confidence>
    <impact_confidence>How certain the system is about the severity of impact</impact_confidence>
    <overall_confidence>detection_confidence * impact_confidence</overall_confidence>
  </confidence_calculation>
  
  <prioritization_formula>
    priority_score = severity_score * confidence_score * usage_frequency
  </prioritization_formula>
</scoring_algorithm>

## Prevention and Correction System

### Preventive Measures

<prevention_system>
  <template_validation>
    <pre_deployment_checks>
      <structure_validation>Verify proper organization and hierarchy</structure_validation>
      <logic_validation>Check reasoning chains for validity</logic_validation>
      <example_validation>Ensure examples are consistent and relevant</example_validation>
    </pre_deployment_checks>
    
    <quality_gates>
      <minimum_effectiveness>Pattern must achieve 70% effectiveness threshold</minimum_effectiveness>
      <anti_pattern_clearance>No high-severity anti-patterns detected</anti_pattern_clearance>
      <expert_review>Human validation for complex or critical patterns</expert_review>
    </quality_gates>
  </template_validation>
  
  <user_guidance>
    <best_practice_hints>
      <real_time_suggestions>Suggest improvements during pattern creation</real_time_suggestions>
      <example_recommendations>Provide better examples when poor ones detected</example_recommendations>
      <structure_improvements>Suggest organizational improvements</structure_improvements>
    </best_practice_hints>
    
    <educational_resources>
      <anti_pattern_documentation>Clear explanations of what to avoid</anti_pattern_documentation>
      <positive_examples>Demonstrate correct approaches</positive_examples>
      <common_mistakes>Highlight frequent errors and how to avoid them</common_mistakes>
    </educational_resources>
  </user_guidance>
</prevention_system>

### Automated Correction

<correction_system>
  <structure_fixes>
    <organization_improvement>
      <information_separation>Automatically separate mixed information types</information_separation>
      <hierarchy_flattening>Reduce excessive nesting when detected</hierarchy_flattening>
      <tag_enhancement>Suggest semantic improvements for meaningless tags</tag_enhancement>
    </organization_improvement>
    
    <format_standardization>
      <consistent_naming>Apply standard naming conventions</consistent_naming>
      <template_conformance>Ensure patterns follow established templates</template_conformance>
      <accessibility_improvements>Enhance readability and usability</accessibility_improvements>
    </format_standardization>
  </structure_fixes>
  
  <content_improvements>
    <precision_adjustment>
      <uncertainty_addition>Add appropriate uncertainty qualifiers</uncertainty_addition>
      <range_conversion>Convert false precision to appropriate ranges</range_conversion>
      <confidence_indicators>Add confidence levels to claims</confidence_indicators>
    </precision_adjustment>
    
    <reasoning_enhancement>
      <evidence_requirements>Add evidence requirements to unsupported claims</evidence_requirements>
      <assumption_validation>Require validation for critical assumptions</assumption_validation>
      <alternative_consideration>Suggest considering alternative approaches</alternative_consideration>
    </reasoning_enhancement>
  </content_improvements>
</correction_system>

## Integration with Pattern Library

### Quality Assurance Pipeline

<qa_integration>
  <development_workflow>
    <creation_stage>Anti-pattern checking during initial pattern development</creation_stage>
    <review_stage>Comprehensive anti-pattern analysis before approval</review_stage>
    <deployment_stage>Final validation before pattern library inclusion</deployment_stage>
  </development_workflow>
  
  <continuous_monitoring>
    <usage_analysis>Monitor patterns in production for emerging anti-pattern indicators</usage_analysis>
    <effectiveness_correlation>Correlate anti-pattern presence with effectiveness decline</effectiveness_correlation>
    <user_feedback_analysis>Analyze user complaints for anti-pattern indicators</user_feedback_analysis>
  </continuous_monitoring>
  
  <improvement_feedback>
    <pattern_refinement>Use anti-pattern detection to guide pattern improvements</pattern_refinement>
    <library_evolution>Remove or fix patterns with persistent anti-pattern issues</library_evolution>
    <best_practice_development>Develop new best practices based on anti-pattern analysis</best_practice_development>
  </improvement_feedback>
</qa_integration>

### User Experience Enhancement

<ux_enhancement>
  <transparent_feedback>
    <issue_explanations>Clear explanations of detected anti-patterns</issue_explanations>
    <improvement_suggestions>Specific recommendations for fixes</improvement_suggestions>
    <learning_opportunities>Educational content about better approaches</learning_opportunities>
  </transparent_feedback>
  
  <progressive_assistance>
    <gentle_guidance>Start with suggestions rather than hard restrictions</gentle_guidance>
    <skill_development>Help users learn to avoid anti-patterns independently</skill_development>
    <expert_mode>Reduced assistance for experienced users who understand the risks</expert_mode>
  </progressive_assistance>
</ux_enhancement>

---

*This anti-pattern detection system ensures high quality and effectiveness of the prompt pattern library by proactively identifying and correcting common mistakes and ineffective approaches.*