---
name: /help-plus
description: Enhanced help system with error handling, troubleshooting, and user guidance (v1.0)
version: "1.0"
usage: '[command] [error] [troubleshoot]'
category: meta
allowed-tools:
- Read
- LS
- Grep
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/meta/help-plus.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>help-plus</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="help_request_processing"/>
      <component ref="file-reader" role="documentation_access"/>
      <component ref="search-files" role="command_discovery"/>
      <component ref="error-handler" role="troubleshooting_guidance"/>
      <component ref="user-confirmation" role="interactive_help"/>
    </required_components>
    <optional_components>
      <component ref="examples-library" benefit="contextual_usage_examples"/>
      <component ref="progress-indicator" benefit="troubleshooting_progress"/>
      <component ref="context-optimization" benefit="personalized_help"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="help" context="basic_help_integration"/>
      <command ref="welcome" context="onboarding_guidance"/>
      <command ref="validate-adaptation" context="diagnostic_validation"/>
      <command ref="replace-placeholders" context="placeholder_troubleshooting"/>
    </invokable_commands>
    <orchestration_patterns>diagnostic|interactive|contextual|escalation</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Enhanced help system with error handling, troubleshooting guides, and contextual user guidance</task_description>
    <implementation_strategy>parameter_analysis|contextual_help_provision|error_diagnosis|troubleshooting_guidance|interactive_support</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>enhanced_help_and_support</primary_discovery_path>
    <alternative_paths>
      <path>troubleshooting_system</path>
      <path>error_handling_guide</path>
      <path>user_support_interface</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="command" ref="help" relation="basic_help_foundation"/>
      <file type="command" ref="welcome" relation="onboarding_integration"/>
      <file type="context" ref=".claude/context/troubleshooting-guide.md" relation="troubleshooting_knowledge"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="validate-adaptation" relation="diagnostic_workflow"/>
      <file type="command" ref="replace-placeholders" relation="error_resolution"/>
      <file type="context" ref=".claude/context/user-support-patterns.md" relation="support_documentation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="help" similarity="0.85"/>
      <file type="command" ref="welcome" similarity="0.50"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>troubleshooting_command_issues</scenario>
      <scenario>error_diagnosis_and_resolution</scenario>
      <scenario>enhanced_help_requirements</scenario>
      <scenario>user_guidance_and_support</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>basic_command_reference_lookup</scenario>
      <scenario>initial_onboarding_process</scenario>
      <scenario>automated_workflows</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>help enhanced troubleshooting error handling user support guidance</keywords>
    <semantic_tags>enhanced_help troubleshooting_system error_diagnosis user_support</semantic_tags>
    <functionality_vectors>[0.8, 0.9, 0.7, 1.0, 0.8]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>global</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>7</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/troubleshooting-guide.md" importance="critical"/>
      <context_file ref=".claude/context/error-patterns.md" importance="critical"/>
      <context_file ref=".claude/context/user-support-patterns.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/command-usage-patterns.md" importance="high"/>
      <context_file ref=".claude/context/common-issues-solutions.md" importance="high"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>support_and_troubleshooting</workflow_stage>
    <integration_patterns>
      <pattern>contextual_help_provision</pattern>
      <pattern>error_diagnosis_and_resolution</pattern>
      <pattern>interactive_troubleshooting</pattern>
      <pattern>escalation_to_appropriate_resources</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>enhanced_help_system</concept_introduction>
    <skill_progression>all_levels</skill_progression>
    <mastery_indicators>
      <indicator>effective_error_diagnosis</indicator>
      <indicator>contextual_help_provision</indicator>
      <indicator>successful_troubleshooting_guidance</indicator>
      <indicator>appropriate_resource_escalation</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /help-plus - Enhanced Help & Troubleshooting

Enhanced help system with error handling, troubleshooting guides, and user guidance for the template library.

## Usage Patterns

### Get Help for Specific Command
```
/help-plus /task              # Get detailed help for /task command
/help-plus /adapt-to-project  # Get help for adaptation command
```

### Troubleshoot Common Errors
```
/help-plus error placeholder   # Help with placeholder-related errors
/help-plus error permission    # Help with permission errors
/help-plus error validation    # Help with validation failures
```

### General Troubleshooting
```
/help-plus troubleshoot       # Show common issues and solutions
```

## Common Error Categories & Solutions

### 1. Placeholder Errors ⚠️
**Symptoms**: Commands fail with [INSERT_XXX] references
**Solution**:
1. Run `/replace-placeholders` to see all placeholders
2. Use Find & Replace in your editor to replace them
3. Run `/validate-adaptation` to verify fixes

### 2. Permission Errors 🔒
**Symptoms**: "Permission denied" or file access errors
**Solution**:
1. Check `.claude/settings.json` allowedPaths configuration
2. Ensure files are in allowed directories
3. Verify file permissions (readable/writable)

### 3. Validation Failures ❌
**Symptoms**: `/validate-adaptation` shows failures
**Solution**:
1. Check specific validation error messages
2. Fix issues one at a time
3. Re-run validation after each fix
4. Use `/help-plus error validation` for specific guidance

### 4. Setup Issues 🔧
**Symptoms**: Commands not found, setup script failures
**Solution**:
1. Verify installation method was completed
2. Check `.claude/commands/` directory exists
3. Verify setup script ran without errors
4. Use `/welcome` to restart onboarding process

### 5. Customization Confusion 🤔
**Symptoms**: Unsure how to customize templates
**Solution**:
1. Start with `/welcome` for experience-level guidance
2. Use `/adapt-to-project` for step-by-step help
3. Check `CUSTOMIZATION-WORKFLOW-GUIDE.md`
4. Start with fewer commands, expand gradually

## Troubleshooting Workflow

### Step 1: Identify Error Type
- **Template Error**: Contains [INSERT_XXX] placeholders
- **File Error**: Permission or path issues
- **Validation Error**: Command structure or content issues
- **Usage Error**: Incorrect command usage or expectations

### Step 2: Apply Specific Solution
- Use the relevant section above
- Follow step-by-step instructions
- Test after each fix

### Step 3: Verify Resolution
- Re-run the failing command
- Use validation commands to confirm fix
- Document what worked for future reference

## Quick Reference: Essential Commands

### For New Users
- `/welcome` - Start here for onboarding
- `/adapt-to-project` - Get customization guidance
- `/help-plus troubleshoot` - When things go wrong

### For Customization
- `/replace-placeholders` - See what needs replacement
- `/validate-adaptation` - Check your work
- `/find-commands [category]` - Discover relevant templates

### For Advanced Users  
- `/sync-from-reference` - Update templates
- `/share-adaptation` - Document your customization patterns

## When to Get Additional Help

If you're still stuck after following troubleshooting steps:
1. Check the SECURITY-GUIDELINES.md for security-related issues
2. Review the DOCUMENTATION-ACCURACY-REPORT.md for current project stats
3. Look at examples/ directory for working implementation patterns
4. Consider if your use case requires custom command development

## Pro Tips for Better UX

1. **Start Simple**: Begin with 3-5 core commands, expand gradually
2. **Document Changes**: Keep notes on your customizations
3. **Test Early**: Validate commands as you customize them
4. **Use Categories**: Focus on one command category at a time
5. **Backup Work**: Create backups before major customization sessions

**Remember**: This template library is designed for customization. The initial setup work pays off with months of saved prompt engineering time.
