# Comprehensive Usage Guide for /prompt Command

<guide_metadata>
  <purpose>Complete documentation for /prompt command usage in Claude Code framework</purpose>
  <audience>Developers, prompt engineers, and AI practitioners</audience>
  <version>1.0.0</version>
  <last_updated>2025-07-06</last_updated>
</guide_metadata>

## Overview

The `/prompt` command is a powerful tool within the Claude Code framework designed for systematic prompt engineering. It provides a complete workflow for creating, evaluating, testing, and improving AI prompts using proven methodologies and best practices.

<framework_integration>
  <command_delegation>Delegates to modules/development/prompt-engineering.md</command_delegation>
  <supporting_modules>
    <module>modules/quality/critical-thinking.md</module>
    <module>modules/patterns/research-analysis.md</module>
    <module>modules/patterns/session-management.md</module>
    <module>modules/quality/production-standards.md</module>
  </supporting_modules>
</framework_integration>

## Command Structure

```bash
/prompt <subcommand> [options] [parameters]
```

### Available Subcommands

<subcommands>
  <subcommand name="create">
    <purpose>Create new prompts with best practices and patterns</purpose>
    <syntax>/prompt create "prompt_name" [options]</syntax>
  </subcommand>
  
  <subcommand name="evaluate">
    <purpose>Analyze prompt effectiveness and identify improvements</purpose>
    <syntax>/prompt evaluate "prompt_file" [options]</syntax>
  </subcommand>
  
  <subcommand name="test">
    <purpose>Test prompts against various scenarios and edge cases</purpose>
    <syntax>/prompt test "prompt_file" [options]</syntax>
  </subcommand>
  
  <subcommand name="improve">
    <purpose>Iteratively enhance prompts based on evaluation results</purpose>
    <syntax>/prompt improve "prompt_file" [options]</syntax>
  </subcommand>
</subcommands>

## Quick Start Guide

### 1. Creating Your First Prompt

```bash
# Create a basic system prompt
/prompt create "code_reviewer" --type system --style directive

# Create a user prompt with examples
/prompt create "bug_report_template" --type user --format structured
```

### 2. Evaluating Existing Prompts

```bash
# Comprehensive evaluation
/prompt evaluate "prompts/my_prompt.md" --metrics all

# Focus on specific metrics
/prompt evaluate "prompts/my_prompt.md" --metrics clarity,specificity
```

### 3. Testing Prompt Behavior

```bash
# Basic testing scenarios
/prompt test "prompts/my_prompt.md" --scenarios basic

# Comprehensive testing with edge cases
/prompt test "prompts/my_prompt.md" --scenarios all --output report.md
```

### 4. Improving Prompts

```bash
# Auto-improve based on test results
/prompt improve "prompts/my_prompt.md" --based-on test-results.json

# Targeted improvement with specific iterations
/prompt improve "prompts/my_prompt.md" --iterations 3 --target clarity
```

## Parameters Reference

<parameters_detailed>
  <parameter name="--type">
    <values>system|user|assistant|hybrid</values>
    <default>system</default>
    <description>Specifies the type of prompt being created or modified</description>
    <examples>
      <example>--type system (for system-level instructions)</example>
      <example>--type user (for user interaction prompts)</example>
      <example>--type hybrid (for complex multi-role prompts)</example>
    </examples>
  </parameter>
  
  <parameter name="--framework">
    <values>claude|gpt|general</values>
    <default>claude</default>
    <description>Target AI framework for optimization</description>
    <optimization_notes>
      <note>Claude: Uses XML structure and specific techniques for Claude models</note>
      <note>GPT: Optimizes for OpenAI models with appropriate formatting</note>
      <note>General: Framework-agnostic prompts with universal best practices</note>
    </optimization_notes>
  </parameter>
  
  <parameter name="--style">
    <values>directive|conversational|structured|narrative</values>
    <default>directive</default>
    <description>Communication style for the prompt</description>
    <style_guidance>
      <style name="directive">Clear, command-like instructions with explicit steps</style>
      <style name="conversational">Natural, dialogue-like interaction style</style>
      <style name="structured">Formal, organized format with clear sections</style>
      <style name="narrative">Story-like progression with context building</style>
    </style_guidance>
  </parameter>
  
  <parameter name="--metrics">
    <values>clarity|specificity|robustness|effectiveness|all</values>
    <default>all</default>
    <description>Evaluation metrics to apply during assessment</description>
    <metric_definitions>
      <metric name="clarity">Measures how unambiguous and clear the prompt is</metric>
      <metric name="specificity">Evaluates the level of detail and precision</metric>
      <metric name="robustness">Tests prompt performance under edge cases</metric>
      <metric name="effectiveness">Assesses goal achievement likelihood</metric>
    </metric_definitions>
  </parameter>
  
  <parameter name="--scenarios">
    <values>basic|edge-cases|adversarial|all</values>
    <default>basic</default>
    <description>Test scenario categories to execute</description>
    <scenario_types>
      <scenario name="basic">Standard use cases and expected inputs</scenario>
      <scenario name="edge-cases">Boundary conditions and unusual inputs</scenario>
      <scenario name="adversarial">Potential misuse and attack scenarios</scenario>
    </scenario_types>
  </parameter>
  
  <parameter name="--output">
    <values>console|file|both</values>
    <default>console</default>
    <description>Output format for results and reports</description>
  </parameter>
</parameters_detailed>

## Workflow Examples

### Complete Prompt Development Lifecycle

```bash
# 1. Create initial prompt
/prompt create "api_documentation_generator" --type system --style structured

# 2. Evaluate the created prompt
/prompt evaluate "prompts/api_documentation_generator_v1.0.md" --metrics all

# 3. Test with various scenarios
/prompt test "prompts/api_documentation_generator_v1.0.md" --scenarios all --output both

# 4. Improve based on results
/prompt improve "prompts/api_documentation_generator_v1.0.md" --based-on test_results.json

# 5. Re-evaluate improved version
/prompt evaluate "prompts/api_documentation_generator_v1.1.md" --metrics all
```

### Collaborative Prompt Development

```bash
# Create base prompt
/prompt create "code_review_assistant" --type system --framework claude

# Test with team scenarios
/prompt test "prompts/code_review_assistant_v1.0.md" --scenarios basic,edge-cases

# Improve for production readiness
/prompt improve "prompts/code_review_assistant_v1.0.md" --iterations 2 --target robustness

# Final validation
/prompt evaluate "prompts/code_review_assistant_v1.2.md" --metrics all --output report.md
```

### A/B Testing Different Approaches

```bash
# Create variant A
/prompt create "user_onboarding_v1" --style conversational

# Create variant B
/prompt create "user_onboarding_v2" --style directive

# Test both variants
/prompt test "prompts/user_onboarding_v1.md" --scenarios all
/prompt test "prompts/user_onboarding_v2.md" --scenarios all

# Compare results and improve the better performer
/prompt improve "prompts/user_onboarding_v1.md" --based-on comparative_analysis.json
```

## Integration with Other Commands

<command_integration>
  <integration name="auto_command">
    <purpose>Automatic prompt pattern selection based on context</purpose>
    <usage>/auto "create documentation prompts" triggers intelligent prompt creation</usage>
  </integration>
  
  <integration name="task_command">
    <purpose>Task-specific prompt application in development workflows</purpose>
    <usage>/task incorporates prompt engineering patterns automatically</usage>
  </integration>
  
  <integration name="swarm_command">
    <purpose>Multi-agent prompt coordination for complex scenarios</purpose>
    <usage>/swarm uses specialized prompts for each agent role</usage>
  </integration>
  
  <integration name="session_command">
    <purpose>Session-based prompt tracking and improvement</purpose>
    <usage>/session manages prompt evolution across development cycles</usage>
  </integration>
</command_integration>

## File Structure and Organization

<file_organization>
  <directory_structure>
    <directory name=".claude/prompts/">
      <subdirectory name="templates/">Reusable prompt templates</subdirectory>
      <subdirectory name="active/">Currently used prompts</subdirectory>
      <subdirectory name="versions/">Historical prompt versions</subdirectory>
      <subdirectory name="evaluations/">Evaluation reports and metrics</subdirectory>
      <subdirectory name="tests/">Test results and scenarios</subdirectory>
    </directory>
  </directory_structure>
  
  <naming_conventions>
    <convention>prompts/{name}_{version}.md for prompt files</convention>
    <convention>evaluations/{name}_{timestamp}_eval.md for evaluation reports</convention>
    <convention>tests/{name}_{timestamp}_test.json for test results</convention>
    <convention>templates/{category}_{type}_template.md for templates</convention>
  </naming_conventions>
</file_organization>

## Quality Standards

<quality_requirements>
  <requirement name="clarity">
    <description>Prompts must be unambiguous and clear in their instructions</description>
    <validation>Evaluated through clarity metrics and human review</validation>
  </requirement>
  
  <requirement name="testability">
    <description>All prompts must include comprehensive test scenarios</description>
    <validation>Minimum 3 test scenarios per prompt category</validation>
  </requirement>
  
  <requirement name="versioning">
    <description>Prompt iterations tracked with semantic versioning</description>
    <validation>Automatic version increment with change documentation</validation>
  </requirement>
  
  <requirement name="documentation">
    <description>Each prompt includes purpose, usage, and examples</description>
    <validation>Complete metadata and usage examples required</validation>
  </requirement>
  
  <requirement name="validation">
    <description>Prompts validated against target framework guidelines</description>
    <validation>Framework-specific optimization checks</validation>
  </requirement>
</quality_requirements>

## Escalation and Complex Scenarios

<escalation_handling>
  <trigger condition="multi_prompt_system">
    <description>Complex prompt system design requiring multiple coordinated prompts</description>
    <escalation>Automatically escalates to /swarm for multi-agent coordination</escalation>
    <example>Enterprise chatbot with multiple specialized prompt roles</example>
  </trigger>
  
  <trigger condition="framework_prompts">
    <description>Framework-wide prompt updates affecting multiple components</description>
    <escalation>Escalates to /swarm for systematic framework modification</escalation>
    <example>Updating all system prompts for new AI capabilities</example>
  </trigger>
  
  <trigger condition="production_deployment">
    <description>Production prompt rollout requiring validation protocols</description>
    <escalation>Requires /protocol validation before deployment</escalation>
    <example>Customer-facing prompt changes requiring compliance review</example>
  </trigger>
</escalation_handling>

## Common Use Cases

<use_cases>
  <use_case name="system_prompt_creation">
    <description>Creating system-level prompts for AI assistants</description>
    <example_command>/prompt create "technical_writer" --type system --style directive</example>
    <best_practices>
      <practice>Define clear role and capabilities</practice>
      <practice>Include behavioral guidelines</practice>
      <practice>Specify output formatting requirements</practice>
      <practice>Add error handling instructions</practice>
    </best_practices>
  </use_case>
  
  <use_case name="user_interaction_prompts">
    <description>Designing prompts for user-facing interactions</description>
    <example_command>/prompt create "onboarding_flow" --type user --style conversational</example>
    <best_practices>
      <practice>Use natural, friendly language</practice>
      <practice>Anticipate user confusion points</practice>
      <practice>Provide clear next steps</practice>
      <practice>Include example interactions</practice>
    </best_practices>
  </use_case>
  
  <use_case name="code_generation_prompts">
    <description>Prompts specifically for code generation and review</description>
    <example_command>/prompt create "code_reviewer" --type system --framework claude --style structured</example>
    <best_practices>
      <practice>Specify coding standards and conventions</practice>
      <practice>Include security and performance considerations</practice>
      <practice>Define review criteria and priorities</practice>
      <practice>Provide code examples and anti-patterns</practice>
    </best_practices>
  </use_case>
  
  <use_case name="workflow_automation">
    <description>Prompts for automating development workflows</description>
    <example_command>/prompt create "ci_cd_assistant" --type system --style directive</example>
    <best_practices>
      <practice>Define clear workflow steps</practice>
      <practice>Include error recovery procedures</practice>
      <practice>Specify validation criteria</practice>
      <practice>Provide troubleshooting guidance</practice>
    </best_practices>
  </use_case>
</use_cases>

## Next Steps

After reading this guide:

1. **Start with Simple Examples**: Begin with basic prompt creation using the quick start examples
2. **Practice Evaluation**: Use the evaluation features to understand prompt quality metrics
3. **Experiment with Testing**: Run test scenarios to see how prompts perform under different conditions
4. **Iterate and Improve**: Use the improvement workflows to enhance prompt effectiveness
5. **Explore Advanced Features**: Move on to advanced features and complex workflows
6. **Integrate with Other Commands**: Learn how /prompt works with other framework commands

<next_documentation>
  <reference>See PROMPT_PATTERNS_GUIDE.md for detailed pattern documentation</reference>
  <reference>See PROMPT_TROUBLESHOOTING.md for common issues and solutions</reference>
  <reference>See PROMPT_BEST_PRACTICES.md for optimization guidelines</reference>
</next_documentation>

---

*This comprehensive usage guide provides the foundation for effective prompt engineering within the Claude Code framework. For questions or contributions, see the community guidelines in PROMPT_CONTRIBUTION_GUIDE.md.*