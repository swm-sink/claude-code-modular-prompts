<command purpose="AI prompt engineering workflows for creating, evaluating, testing, and improving prompts with systematic methodology">
  
  <delegation target="modules/development/prompt-engineering.md">
    This command delegates ALL implementation to the prompt engineering module which provides comprehensive prompt development workflows including creation patterns, evaluation frameworks, testing methodologies, and iterative improvement cycles.
  </delegation>
  
  <module_integration>
    <primary_module>modules/development/prompt-engineering.md</primary_module>
    <supporting_modules>
      <module>modules/quality/critical-thinking.md</module>
      <module>modules/patterns/research-analysis.md</module>
      <module>modules/patterns/session-management.md</module>
      <module>modules/quality/production-standards.md</module>
    </supporting_modules>
  </module_integration>
  
  <subcommands>
    <subcommand name="create">
      <purpose>Create new prompts with best practices and patterns</purpose>
      <example>/prompt create "user authentication flow" --type system --framework claude</example>
    </subcommand>
    <subcommand name="evaluate">
      <purpose>Analyze prompt effectiveness and identify improvements</purpose>
      <example>/prompt evaluate "existing_prompt.md" --metrics clarity,specificity,robustness</example>
    </subcommand>
    <subcommand name="test">
      <purpose>Test prompts against various scenarios and edge cases</purpose>
      <example>/prompt test "api_generation.md" --scenarios edge-cases --iterations 5</example>
    </subcommand>
    <subcommand name="improve">
      <purpose>Iteratively enhance prompts based on evaluation results</purpose>
      <example>/prompt improve "current_prompt.md" --based-on test-results.json</example>
    </subcommand>
  </subcommands>
  
  <usage_examples>
    <example type="create_system">/prompt create "code review assistant" --type system --style directive</example>
    <example type="create_user">/prompt create "bug report template" --type user --format structured</example>
    <example type="evaluate_existing">/prompt evaluate ".claude/prompts/api-design.md" --comprehensive</example>
    <example type="test_scenarios">/prompt test "refactoring-prompt.md" --scenarios all --output report.md</example>
    <example type="improve_iterative">/prompt improve "assistant-prompt.md" --iterations 3 --target clarity</example>
    <example type="workflow_complete">/prompt create "feature generator" &amp;&amp; /prompt test &amp;&amp; /prompt improve</example>
  </usage_examples>
  
  <parameters>
    <parameter name="--type" values="system|user|assistant|hybrid" default="system">
      <purpose>Specify the type of prompt being created or modified</purpose>
    </parameter>
    <parameter name="--framework" values="claude|gpt|general" default="claude">
      <purpose>Target AI framework for optimization</purpose>
    </parameter>
    <parameter name="--style" values="directive|conversational|structured|narrative" default="directive">
      <purpose>Communication style for the prompt</purpose>
    </parameter>
    <parameter name="--metrics" values="clarity|specificity|robustness|effectiveness|all" default="all">
      <purpose>Evaluation metrics to apply</purpose>
    </parameter>
    <parameter name="--scenarios" values="basic|edge-cases|adversarial|all" default="basic">
      <purpose>Test scenario categories</purpose>
    </parameter>
    <parameter name="--output" values="console|file|both" default="console">
      <purpose>Output format for results</purpose>
    </parameter>
  </parameters>
  
  <escalation_triggers>
    <trigger condition="multi_prompt_system">Complex prompt system design - escalates to /swarm</trigger>
    <trigger condition="framework_prompts">Framework-wide prompt updates - escalates to /swarm</trigger>
    <trigger condition="production_deployment">Production prompt rollout - requires /protocol validation</trigger>
  </escalation_triggers>
  
  <quality_requirements>
    <requirement name="clarity">Prompts must be unambiguous and clear</requirement>
    <requirement name="testability">All prompts must include test scenarios</requirement>
    <requirement name="versioning">Prompt iterations tracked with semantic versioning</requirement>
    <requirement name="documentation">Each prompt includes purpose, usage, and examples</requirement>
    <requirement name="validation">Prompts validated against target framework guidelines</requirement>
  </quality_requirements>
  
  <strict_enforcement target="prompt_engineering_discipline">
    <primary_rule>ALL prompts MUST follow systematic engineering methodology</primary_rule>
    <verification>Pattern compliance + test coverage + evaluation metrics + documentation complete</verification>
    <consequence>Ad-hoc prompt creation violates engineering standards and reduces effectiveness</consequence>
  </strict_enforcement>
  
  <integration_hooks>
    <hook type="pre_create">Validates parameters and loads templates</hook>
    <hook type="post_create">Runs initial evaluation and generates test cases</hook>
    <hook type="pre_test">Prepares test environment and scenarios</hook>
    <hook type="post_test">Analyzes results and suggests improvements</hook>
    <hook type="pre_improve">Backs up current version and plans changes</hook>
    <hook type="post_improve">Validates improvements and updates documentation</hook>
  </integration_hooks>
  
  <reference>
    See modules/development/prompt-engineering.md for complete implementation details including creation patterns, evaluation frameworks, testing methodologies, improvement algorithms, and production deployment workflows.
  </reference>
  
</command>