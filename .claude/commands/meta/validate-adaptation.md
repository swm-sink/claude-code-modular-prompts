---
name: /validate-adaptation
description: Check adaptation completeness and calculate readiness score (v1.0)
version: "1.0"
usage: '/validate-adaptation [--verbose] [--auto-run] [--layer=1|2|3] [--export-report]'
category: meta
allowed-tools:
- Read
- Grep
- TodoWrite
- Bash
- Glob
dependencies: [replace-placeholders, quick-command, build-command, assemble-command]
validation:
  pre-execution: Check for .claude/ directory existence
  during-execution: Validate each checklist item systematically
  post-execution: Generate readiness score and action plan
progressive-disclosure:
  layer-integration: Validates adaptations for all 3 layers
  layer-1-checks: Auto-generation template readiness
  layer-2-checks: Customization JSON configs validation
  layer-3-checks: Component assembly framework integrity
error-recovery:
  missing-structure: Provides recovery instructions
  incomplete-adaptation: Generates specific fix commands
  validation-failures: Detailed remediation guidance
export-formats:
  markdown: Full validation report
  json: Machine-readable scores
  checklist: Interactive TODO format
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/commands/meta/validate-adaptation.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>validate-adaptation</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>all</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="adaptation_status_scanning"/>
      <component ref="parameter-parser" role="validation_options_processing"/>
      <component ref="search-files" role="placeholder_detection"/>
      <component ref="response-validator" role="validation_result_assessment"/>
      <component ref="progress-indicator" role="validation_progress_tracking"/>
      <component ref="task-summary" role="validation_report_generation"/>
    </required_components>
    <optional_components>
      <component ref="output-formatter" benefit="multiple_export_formats"/>
      <component ref="error-handler" benefit="validation_failure_recovery"/>
      <component ref="performance-monitoring" benefit="validation_performance_tracking"/>
      <component ref="completion-tracker" benefit="readiness_score_calculation"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="replace-placeholders" context="placeholder_fixing"/>
      <command ref="quick-command" context="layer_1_validation"/>
      <command ref="build-command" context="layer_2_validation"/>
      <command ref="assemble-command" context="layer_3_validation"/>
    </invokable_commands>
    <orchestration_patterns>conditional|diagnostic|remediation|layer_aware</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Comprehensive adaptation validation with layer-aware assessment, automated scanning, and readiness scoring</task_description>
    <implementation_strategy>systematic_scanning|layer_specific_validation|readiness_assessment|remediation_guidance|export_reporting</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>validation_and_quality_assurance</primary_discovery_path>
    <alternative_paths>
      <path>adaptation_verification</path>
      <path>template_readiness_assessment</path>
      <path>progressive_disclosure_validation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="command" ref="replace-placeholders" relation="placeholder_management"/>
      <file type="context" ref=".claude/context/validation-patterns.md" relation="validation_methodology"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="welcome" relation="onboarding_validation"/>
      <file type="command" ref="help-plus" relation="diagnostic_integration"/>
      <file type="context" ref=".claude/context/quality-assessment-report.md" relation="quality_reporting"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="validate-automation" similarity="0.70"/>
      <file type="command" ref="help-plus" similarity="0.45"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>post_adaptation_verification</scenario>
      <scenario>readiness_assessment_before_productive_use</scenario>
      <scenario>troubleshooting_adaptation_issues</scenario>
      <scenario>progressive_disclosure_layer_verification</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>during_active_adaptation_process</scenario>
      <scenario>pre_adaptation_environment_checking</scenario>
      <scenario>routine_template_usage</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>validate adaptation verification readiness assessment quality assurance validation</keywords>
    <semantic_tags>validation_framework adaptation_verification readiness_scoring quality_assurance</semantic_tags>
    <functionality_vectors>[0.9, 1.0, 0.8, 0.9, 0.7]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/validation-patterns.md" importance="critical"/>
      <context_file ref=".claude/context/progressive-disclosure-guide.md" importance="critical"/>
      <context_file ref=".claude/context/quality-assessment-framework.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/adaptation-troubleshooting.md" importance="high"/>
      <context_file ref=".claude/context/template-library-standards.md" importance="high"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>validation_and_qa</workflow_stage>
    <integration_patterns>
      <pattern>systematic_validation_scanning</pattern>
      <pattern>layer_aware_quality_assessment</pattern>
      <pattern>automated_readiness_scoring</pattern>
      <pattern>remediation_guidance_generation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>adaptation_validation_framework</concept_introduction>
    <skill_progression>all_levels</skill_progression>
    <mastery_indicators>
      <indicator>comprehensive_placeholder_detection</indicator>
      <indicator>layer_specific_validation_execution</indicator>
      <indicator>accurate_readiness_score_calculation</indicator>
      <indicator>effective_remediation_guidance_provision</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# Validate Adaptation (v1.0)

## 🎯 Enhanced Validation with Progressive Disclosure Support

**v1.0 Enhancement**: This command now provides layer-aware validation with automated scanning capabilities and comprehensive readiness assessment across all three Progressive Disclosure layers.

### 🚀 What's New in v1.0
- **Layer-Aware Validation**: Specific checks for each Progressive Disclosure layer
- **Automated Scanning**: Uses Bash and Glob tools for systematic validation
- **Export Capabilities**: Generate reports in multiple formats
- **Error Recovery**: Detailed remediation for validation failures
- **Dependency Tracking**: Validates related command configurations

### 📊 Validation Capabilities by Layer

#### Layer 1 Validation (Auto-Generation)
- Quick command template availability
- Auto-generation readiness assessment
- Basic project detection capabilities

#### Layer 2 Validation (Guided Customization)
- Customization JSON config integrity
- Option filtering effectiveness
- Build command configuration

#### Layer 3 Validation (Component Assembly)
- Component library completeness
- Assembly template validation
- Compatibility matrix verification

## Manual Validation Checklist

### 1. Check for Unreplaced Placeholders
Run these commands in your terminal to find placeholders:
```bash
# Find all remaining placeholders
grep -r "\[INSERT_" .claude/commands/
grep -r "\[INSERT_" .claude/components/
grep -r "\[INSERT_" .claude/context/
grep "\[INSERT_" CLAUDE.md
```

**Checklist:**
□ No results from placeholder search
□ All project-specific values replaced
□ Nested placeholders resolved

### 2. Verify Project Configuration
Check these files manually:
```bash
# Check if configuration exists
ls -la .claude/config/project-config.yaml
cat .claude/config/project-config.yaml
```

**Checklist:**
□ project-config.yaml exists
□ All fields have real values (not placeholders)
□ Domain matches your project type
□ Tech stack is accurate

### 3. Review Command Selection
```bash
# List your commands
ls -la .claude/commands/
ls -la .claude/commands/*/
```

**Checklist:**
□ Only commands you need are present
□ Domain-specific commands added
□ Unused commands removed
□ Core commands (help, task) retained

### 4. Check Framework Structure
```bash
# Verify structure
tree .claude/ -L 2
# or
find .claude -type d
```

**Checklist:**
□ .claude/commands/ exists with subfolders
□ .claude/components/ has key components  
□ .claude/context/ has anti-patterns
□ CLAUDE.md exists and is customized

## Manual Readiness Score Calculation

Calculate your score yourself:

### Scoring Guide
Start with 100% and subtract:
- **Each unreplaced placeholder found**: -5%
- **No project-config.yaml**: -20%
- **Using all default commands**: -10%
- **No domain customization**: -15%
- **Default security settings**: -10%

### Score Interpretation
- **0-40%**: Just imported, needs significant work
- **41-70%**: Basic adaptation started
- **71-90%**: Good adaptation progress
- **91-100%**: Fully customized for your project

### Example Calculation
```
Starting score: 100%
Found 6 placeholders: -30%
No domain commands: -15%
Using defaults: -10%
Final score: 45% (Basic adaptation needed)
```

## Enhanced v1.0 Validation Suite

### Automated Validation Commands
```bash
# v1.0 Enhanced validation with layer support
echo "=== Progressive Disclosure Layer Validation ==="

# Layer 1: Auto-Generation Readiness
echo "Layer 1 - Quick Command Templates:"
ls -la .claude/templates/*.template 2>/dev/null | wc -l

# Layer 2: Customization Configs
echo "Layer 2 - Build Configs:"
ls -la .claude/customization/*.json 2>/dev/null | wc -l

# Layer 3: Assembly Framework
echo "Layer 3 - Components:"
find .claude/components -name "*.md" 2>/dev/null | wc -l

# Comprehensive placeholder scan
echo "=== Checking Placeholders ==="
grep -r "\[INSERT_" .claude/ 2>/dev/null | wc -l

# Configuration validation
echo "=== Checking Config ==="
cat .claude/config/project-config.yaml 2>/dev/null || echo "No config found"

# Command inventory
echo "=== Command Count by Category ==="
for dir in .claude/commands/*/; do
  echo "$(basename "$dir"): $(find "$dir" -name "*.md" 2>/dev/null | wc -l)"
done

# v1.0 Feature validation
echo "=== v1.0 Features ==="
grep -l "version: "1.0"" .claude/commands/*/*.md 2>/dev/null | wc -l
```

### Layer-Specific Validation

#### --layer=1 Validation
```bash
# Validate Layer 1 auto-generation readiness
echo "Checking /quick-command availability..."
test -f .claude/commands/core/quick-command.md && echo "✓ Found" || echo "✗ Missing"

echo "Checking templates..."
ls -la .claude/templates/*.template 2>/dev/null
```

#### --layer=2 Validation  
```bash
# Validate Layer 2 customization framework
echo "Checking /build-command..."
test -f .claude/commands/core/build-command.md && echo "✓ Found" || echo "✗ Missing"

echo "Checking customization configs..."
ls -la .claude/customization/*.json 2>/dev/null
```

#### --layer=3 Validation
```bash
# Validate Layer 3 assembly system
echo "Checking /assemble-command..."
test -f .claude/commands/core/assemble-command.md && echo "✓ Found" || echo "✗ Missing"

echo "Checking component library..."
find .claude/components -type f -name "*.md" | head -10
```

## Next Steps Based on Your Findings

### If you found placeholders:
1. Run `/replace-placeholders` for a replacement guide
2. Manually update each file
3. Re-run validation checks

### If configuration is missing:
1. Create `.claude/config/project-config.yaml`
2. Copy the template from project configuration documentation
3. Fill in your project values

### If using all defaults:
1. Remove commands you don't need
2. Add domain-specific commands
3. Customize core commands

## Enhanced v1.0 Validation Report

### Export Options (--export-report)

#### Markdown Format (Default)
```markdown
ADAPTATION VALIDATION REPORT v1.0
=================================
Date: [TODAY'S DATE]
Project: [YOUR PROJECT NAME]
Framework Version: 1.0

PROGRESSIVE DISCLOSURE READINESS
--------------------------------
Layer 1 (Auto-Generation): [READY/NOT READY]
- Quick Command: [✓/✗]
- Templates: [COUNT]
- Readiness: [XX]%

Layer 2 (Customization): [READY/NOT READY]  
- Build Command: [✓/✗]
- JSON Configs: [COUNT]
- Readiness: [XX]%

Layer 3 (Assembly): [READY/NOT READY]
- Assemble Command: [✓/✗]
- Components: [COUNT]
- Readiness: [XX]%

CORE VALIDATION METRICS
-----------------------
Placeholders Found: [NUMBER]
Configuration Status: [EXISTS/MISSING]
Command Count: [NUMBER] ([NUMBER] v1.0)
Customization Level: [BASIC/MODERATE/ADVANCED]

Overall Readiness Score: [XX]%

RECOMMENDED ACTIONS
-------------------
1. [SPECIFIC ACTION WITH COMMAND]
2. [SPECIFIC ACTION WITH COMMAND]
3. [SPECIFIC ACTION WITH COMMAND]
```

#### JSON Format (--export-report --format=json)
```json
{
  "validation_report": {
    "version": "2.0",
    "date": "[ISO_DATE]",
    "project": "[PROJECT_NAME]",
    "progressive_disclosure": {
      "layer1": {
        "ready": false,
        "quick_command": false,
        "templates": 0,
        "score": 0
      },
      "layer2": {
        "ready": false,
        "build_command": false,
        "configs": 0,
        "score": 0
      },
      "layer3": {
        "ready": false,
        "assemble_command": false,
        "components": 0,
        "score": 0
      }
    },
    "core_metrics": {
      "placeholders": 0,
      "configuration": false,
      "commands": {
        "total": 0,
        "v2_0": 0
      },
      "customization_level": "basic"
    },
    "overall_score": 0,
    "actions": []
  }
}
```

### Error Recovery Guidance

#### Missing Progressive Disclosure Commands
```bash
# Quick fix for missing layer commands
echo "Installing Progressive Disclosure commands..."
cp .claude-framework/commands/core/quick-command.md .claude/commands/core/
cp .claude-framework/commands/core/build-command.md .claude/commands/core/
cp .claude-framework/commands/core/assemble-command.md .claude/commands/core/
```

#### v1.0 Migration Path
```bash
# Upgrade existing commands to v1.0
echo "Run these commands to upgrade:"
echo "/convert-to-v2 --batch=all"
echo "/validate-adaptation --layer=all"
```

Would you like me to run the comprehensive validation now?