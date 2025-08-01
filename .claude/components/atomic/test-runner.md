# Test Runner Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/test-runner.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>test-runner</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>testing</subcategory>
  <complexity_metrics>
    <usage_complexity>medium</usage_complexity>
    <implementation_effort>hours_6</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  <assembly_compatibility>
    <compatible_components>
      <component>command-security-wrapper</component>
      <component>error-handler</component>
      <component>progress-indicator</component>
      <component>output-formatter</component>
    </compatible_components>
    <incompatible_components>
      <component>none</component>
    </incompatible_components>
  </assembly_compatibility>
  <usage_patterns>
    <primary_use_case>Automated test execution and result analysis</primary_use_case>
    <common_combinations>test-runner + command-security-wrapper + progress-indicator</common_combinations>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>testing_operations</primary_discovery_path>
    <alternative_discovery_path>quality_assurance</alternative_discovery_path>
    <key_concepts>testing test_execution test_results coverage quality_assurance</key_concepts>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <dependency type="input">Test configuration and project context</dependency>
    </upstream_dependencies>
    <downstream_dependencies>
      <dependency type="output">Test results, coverage metrics, and recommendations</dependency>
    </downstream_dependencies>
    <peer_alternatives>
      <alternative>command-security-wrapper (broader command execution vs test-specific)</alternative>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Automated testing workflows</scenario>
      <scenario>CI/CD pipeline integration</scenario>
      <scenario>Quality assurance validation</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Manual interactive testing</scenario>
      <scenario>Simple validation scripts</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>testing test_execution test_results coverage quality_assurance validation automated_testing</keywords>
    <semantic_tags>atomic_component testing_operations quality_assurance development_operations</semantic_tags>
    <functionality_vectors>
      <vector>testing_operations</vector>
      <vector>quality_assurance</vector>
      <vector>validation_operations</vector>
    </functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>component</scope_level>
    <context_retention>moderate</context_retention>
    <memory_priority>7</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file>.claude/components/security/command-security-wrapper.md</context_file>
    </required_context>
    <helpful_context>
      <context_file>.claude/components/atomic/error-handler.md</context_file>
      <context_file>.claude/components/atomic/progress-indicator.md</context_file>
      <context_file>.claude/components/atomic/output-formatter.md</context_file>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <typical_workflow_position>quality_assurance_stage</typical_workflow_position>
    <integration_patterns>
      <pattern>development → test-runner → error-handler</pattern>
      <pattern>test-runner → progress-indicator → output-formatter</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>Automated testing principles and execution strategies</concept_introduction>
    <skill_progression>Basic test running → Advanced result analysis → Custom testing frameworks</skill_progression>
    <mastery_indicator>Ability to design comprehensive testing workflows with intelligent failure analysis</mastery_indicator>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Execute tests and validate results:
- Accept and parse input data or parameters
- Run appropriate test commands for project type
- Capture and analyze test output
- Report test results and coverage metrics
- process test failures and error conditions
- Generate test summary and recommendations
```