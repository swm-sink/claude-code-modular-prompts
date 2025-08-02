---
name: /replace-placeholders
description: Systematically replace all placeholders in adapted commands with enhanced validation (v1.0)
version: "1.0"
usage: '/replace-placeholders [validate|guided|batch|rollback] [--dry-run] [--config-file project-config.yaml]'
category: meta
allowed-tools:
- Read
- Write
- MultiEdit
- Grep
- TodoWrite
- Bash
- LS
dependencies:
- adapt-to-project
- validate-adaptation
- welcome
validation:
  pre-execution: validate_placeholder_integrity
  during-execution: validate_each_replacement_step
  post-execution: comprehensive_placeholder_validation
progressive-disclosure:
  layer-integration: "Supports Layer 2 guided customization with intelligent defaults"
  validation-points: "Real-time validation during manual replacement process"
  error-recovery: "Built-in rollback and verification at each step"
safety:
  backup-requirement: "Automatic backup verification before any changes"
  rollback-capability: "Complete rollback to previous state with validation"
  verification-checkpoints: "Multi-step verification throughout process"
enhancement:
  smart-detection: "AI-powered placeholder detection and pattern recognition"
  guided-workflow: "Step-by-step guided replacement with validation"
  batch-processing: "Efficient batch replacement with progress tracking"
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/commands/meta/replace-placeholders.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>replace-placeholders</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>2</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="placeholder_detection"/>
      <component ref="search-files" role="systematic_placeholder_scanning"/>
      <component ref="parameter-parser" role="replacement_mode_processing"/>
      <component ref="progress-indicator" role="replacement_progress_tracking"/>
      <component ref="user-confirmation" role="safety_verification"/>
      <component ref="task-summary" role="replacement_completion_reporting"/>
    </required_components>
    <optional_components>
      <component ref="input-validation" benefit="replacement_value_validation"/>
      <component ref="error-handler" benefit="rollback_and_recovery"/>
      <component ref="completion-tracker" benefit="comprehensive_progress_tracking"/>
      <component ref="git-operations" benefit="backup_verification"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="adapt-to-project" context="integration_workflow"/>
      <command ref="validate-adaptation" context="post_replacement_validation"/>
      <command ref="welcome" context="onboarding_integration"/>
    </invokable_commands>
    <orchestration_patterns>guided|batch_processing|validation_checkpoints|safety_first</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Enhanced placeholder replacement with validation, safety measures, and guided workflows for manual template customization</task_description>
    <implementation_strategy>smart_detection|guided_workflow|validation_checkpoints|progress_tracking|safety_verification</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>placeholder_management_system</primary_discovery_path>
    <alternative_paths>
      <path>template_customization</path>
      <path>guided_replacement_workflow</path>
      <path>manual_template_adaptation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="command" ref="adapt-to-project" relation="customization_source"/>
      <file type="context" ref=".claude/context/placeholder-patterns.md" relation="detection_methodology"/>
      <file type="context" ref=".claude/context/replacement-validation-patterns.md" relation="validation_framework"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="validate-adaptation" relation="validation_workflow"/>
      <file type="command" ref="build-command" relation="layer_2_integration"/>
      <file type="context" ref=".claude/context/template-customization-guide.md" relation="guidance_documentation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="adapt-to-project" similarity="0.80"/>
      <file type="command" ref="sync-from-reference" similarity="0.55"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>systematic_placeholder_replacement</scenario>
      <scenario>manual_template_customization</scenario>
      <scenario>guided_adaptation_workflow</scenario>
      <scenario>layer_2_customization_process</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>fully_automated_replacement_needed</scenario>
      <scenario>validation_only_requirements</scenario>
      <scenario>initial_project_detection_phase</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>replace placeholders template customization guided workflow validation safety</keywords>
    <semantic_tags>placeholder_replacement manual_customization guided_workflow validation_safety</semantic_tags>
    <functionality_vectors>[0.9, 0.8, 1.0, 0.9, 0.8]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/placeholder-patterns.md" importance="critical"/>
      <context_file ref=".claude/context/replacement-validation-patterns.md" importance="critical"/>
      <context_file ref=".claude/context/template-customization-guide.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/progressive-disclosure-guide.md" importance="high"/>
      <context_file ref=".claude/context/safety-procedures.md" importance="high"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>template_customization</workflow_stage>
    <integration_patterns>
      <pattern>guided_manual_replacement</pattern>
      <pattern>validation_checkpoint_system</pattern>
      <pattern>safety_first_approach</pattern>
      <pattern>progress_tracking_workflow</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>enhanced_placeholder_management</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>comprehensive_placeholder_detection</indicator>
      <indicator>systematic_guided_replacement</indicator>
      <indicator>validation_checkpoint_execution</indicator>
      <indicator>safe_rollback_capability</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# Enhanced Placeholder Replacement Guide (v1.0)

**Enhanced manual replacement with validation, safety, and guided workflows**

## 🎯 v1.0 Enhanced Capabilities

### **Usage Options:**
- **`/replace-placeholders`** - Standard guided replacement with validation
- **`/replace-placeholders validate`** - Validation-only mode (check current placeholders)
- **`/replace-placeholders guided`** - Step-by-step guided workflow with safety checks
- **`/replace-placeholders batch`** - Batch processing with progress tracking
- **`/replace-placeholders rollback`** - Rollback to previous state with full recovery

## 🚀 What v1.0 Actually Does

**Enhanced replacement guide with comprehensive validation and safety.** I'll help you manually replace all `[INSERT_XXX]` placeholders with:

### Core Capabilities:
- 📋 **Smart Detection** - AI-powered placeholder detection with pattern recognition
- 📍 **Precise Location** - Exact file locations with line numbers and context
- 📝 **Guided Instructions** - Step-by-step Find & Replace workflow with validation
- ✅ **Real-time Verification** - Validation checkpoints throughout the process
- 🛡️ **Safety First** - Automatic backup verification and rollback capability
- 📊 **Progress Tracking** - Todo-based progress tracking with completion status

## 🔧 v1.0 Enhanced vs. Limitations

### ✅ v1.0 Enhanced Capabilities:
- **Validation & Safety**: Comprehensive validation with backup verification
- **Guided Workflows**: Step-by-step process with validation checkpoints
- **Progress Tracking**: Todo-based tracking with completion status
- **Error Recovery**: Built-in rollback and recovery procedures
- **Smart Detection**: AI-powered placeholder pattern recognition
- **Batch Processing**: Efficient handling of multiple files simultaneously

### ⚠️ Current Limitations (Manual Process Required):
- ❌ **Cannot automatically replace text** - You still do manual Find & Replace in your editor
- ❌ **Cannot modify files directly** - You maintain control over all file changes
- ❌ **Cannot read existing configs** - You provide values during the guided process  
- ❌ **Cannot create backups automatically** - You create backups (but I verify they exist)

### 🎯 v1.0 Philosophy: **Enhanced Manual Control**
The v1.0 approach enhances the manual process with **validation, safety, and guidance** while keeping you in full control of file modifications.

## v1.0 Enhanced Manual Workflow

### 🛡️ Phase 1: Safety & Validation Setup
**Enhanced safety with automatic validation**

#### Pre-Flight Safety Checks:
1. **Backup Verification**: I'll verify you have created backups (.claude.backup/)
2. **Git Status Check**: Ensure you have clean git state for rollback capability
3. **File Integrity**: Scan all template files for corruption or issues
4. **Placeholder Inventory**: Complete scan and cataloging of all placeholders

### 📝 Phase 2: Enhanced Value Collection
**Smart value collection with validation and defaults**

#### Intelligent Value Gathering:
- **Project Context**: Name, domain, tech stack with intelligent detection
- **Smart Defaults**: Pre-filled values based on project analysis
- **Validation During Input**: Real-time validation of provided values
- **Cross-Reference Checking**: Ensure values are consistent and compatible
- **Progressive Disclosure Integration**: Determine appropriate layer recommendations

### 📁 Phase 3: Enhanced File Coverage
**Comprehensive file analysis with validation**

#### v1.0 Enhanced File Coverage:
- **📁 `.claude/commands/**/*.md`** - 88 command files with validation
- **📁 `.claude/components/**/*.md`** - 91 component files with compatibility checking
- **📁 `.claude/assembly-templates/`** - Professional workflow templates
- **📁 `.claude/assembly-config/`** - Component compatibility configurations
- **📁 `.claude/context/*.md`** - Context files with validation
- **📁 `CLAUDE.md`** - Project memory with enhanced structure
- **📁 Configuration files** - JSON configs with validation

### 🎯 Phase 4: Guided Replacement Process
**Step-by-step workflow with validation checkpoints**

#### Enhanced Manual Process:
1. **Smart File Prioritization** - Files ordered by importance and dependency
2. **Guided Editor Instructions** - Specific instructions for your editor type
3. **Validation Checkpoints** - Verify each file after replacement
4. **Progress Tracking** - Todo-based tracking with completion status
5. **Error Detection** - Real-time detection of replacement issues
6. **Recovery Options** - Immediate recovery if issues are detected

## 📋 v1.0 Enhanced Placeholder Reference

### 🎯 Core Project Placeholders
**Enhanced with validation and smart defaults**

#### Primary Identifiers:
```yaml
[INSERT_PROJECT_NAME] → Your actual project name (validated against git/package.json)
[INSERT_DOMAIN] → web-dev, data-science, devops, enterprise (AI-classified)
[INSERT_TECH_STACK] → React+TypeScript+Node, Python+FastAPI+PostgreSQL (ecosystem-detected)
[INSERT_COMPANY_NAME] → Your organization (optional, defaults to project name)
[INSERT_TEAM_SIZE] → solo, small, medium, large (project-complexity-inferred)
```

#### Architecture & Workflow:
```yaml
[INSERT_WORKFLOW_TYPE] → agile, waterfall, hybrid (project-pattern-detected)
[INSERT_PRIMARY_LANGUAGE] → JavaScript, Python, Go, etc. (ecosystem-analyzed)
[INSERT_TESTING_FRAMEWORK] → Jest, pytest, JUnit (framework-detected)
[INSERT_CI_CD_PLATFORM] → GitHub Actions, GitLab CI, Jenkins (config-detected)
[INSERT_DEPLOYMENT_TARGET] → AWS, Azure, Kubernetes, Docker (infrastructure-detected)
```

#### Data & Integration:
```yaml
[INSERT_DATABASE_TYPE] → PostgreSQL, MongoDB, Redis (config-detected)
[INSERT_API_STYLE] → REST, GraphQL, gRPC (architecture-analyzed)
[INSERT_SECURITY_LEVEL] → basic, standard, high, enterprise (compliance-assessed)
[INSERT_PERFORMANCE_PRIORITY] → balanced, optimized, scalable (requirements-analyzed)
[INSERT_USER_BASE] → internal, b2b, b2c, enterprise (domain-classified)
```

### 🧩 v1.0 Progressive Disclosure Placeholders
**New placeholders for Layer integration**

```yaml
[INSERT_LAYER_PREFERENCE] → layer-1, layer-2, layer-3 (complexity-recommended)
[INSERT_AUTO_GENERATION_CONFIG] → enabled, disabled (layer-1 settings)
[INSERT_GUIDED_CUSTOMIZATION_CONFIG] → standard, advanced (layer-2 settings)
[INSERT_COMPONENT_ASSEMBLY_CONFIG] → basic, professional, enterprise (layer-3 settings)
```

### 🔧 v1.0 Enhanced Configuration Placeholders
**New advanced configuration options**

```yaml
[INSERT_VALIDATION_LEVEL] → basic, comprehensive, enterprise (validation-requirements)
[INSERT_ERROR_HANDLING] → standard, enhanced, enterprise (error-recovery-level)
[INSERT_MONITORING_SETUP] → none, basic, advanced, enterprise (observability-level)
[INSERT_PERFORMANCE_MONITORING] → disabled, basic, advanced (performance-tracking)
```

### 🔗 v1.0 Smart Nested Placeholder Handling
**Enhanced nested placeholder resolution with validation**

#### Intelligent Nested Resolution:
For complex placeholders like `[INSERT_[INSERT_DOMAIN]_CONFIG]`:

1. **Smart Detection**: v1.0 automatically detects nested patterns
2. **Guided Resolution**: Step-by-step resolution with validation:
   ```yaml
   Step 1: [INSERT_DOMAIN] → "web-dev" (validated)
   Step 2: [INSERT_DOMAIN_CONFIG] → [INSERT_WEB-DEV_CONFIG] 
   Step 3: [INSERT_WEB-DEV_CONFIG] → "react-typescript-config" (validated)
   ```
3. **Validation at Each Step**: Ensure each resolution step is valid
4. **Error Prevention**: Detect circular references and invalid nesting

---

## 🚀 v1.0 Enhanced Manual Replacement Process

### 🛡️ Step 1: Safety Setup & Validation
**Enhanced safety protocol with automatic verification**

#### Pre-Replacement Safety Protocol:
```bash
# v1.0 Enhanced Safety Setup:
/replace-placeholders validate    # Comprehensive system validation
# ✅ Backup verification: .claude.backup/ exists and complete
# ✅ Git status: Clean working directory 
# ✅ File integrity: All 88 commands + 91 components verified
# ✅ Placeholder inventory: 200+ placeholders catalogued with locations
```

### 📝 Step 2: Enhanced Value Collection
**Smart value gathering with intelligent defaults**

#### Guided Value Collection Process:
I'll collect your project details with smart validation and pre-filled defaults based on your project analysis.

### 📊 Step 3: v1.0 Enhanced Replacement Guide
**Comprehensive guide with validation and progress tracking**

#### Enhanced Guide Format:
```markdown
v1.0 PLACEHOLDER REPLACEMENT GUIDE
===================================
📊 Total Files: 88 commands + 91 components + configs
📋 Total Replacements: 247 placeholders detected
🎯 Estimated Time: 15-25 minutes (with validation)
🛡️ Safety: Backups verified, rollback ready

🚀 PRIORITY 1 - CORE COMMANDS (Critical)
File: .claude/commands/core/task.md (✅ backup verified)
- Line 8: "[INSERT_PROJECT_NAME]" → "MyAwesomeApp" (✅ validated)
- Line 24: "[INSERT_TESTING_FRAMEWORK]" → "Jest" (✅ ecosystem-detected)
  🔍 Validation: After replacement, verify YAML header integrity

File: .claude/commands/core/query.md (✅ backup verified)  
- Line 12: "[INSERT_DOMAIN]" → "web-dev" (✅ AI-classified)
- Line 45: "[INSERT_TECH_STACK]" → "React + TypeScript + Node.js" (✅ ecosystem-analyzed)
  🔍 Validation: Test command execution after replacement

🧩 PRIORITY 2 - COMPONENTS (Layer Integration)
[... detailed component-by-component guide with validation points ...]

📊 Progress Tracking: Todo checklist for each file
✅ Built-in validation points throughout process
🔄 Rollback instructions if issues are detected
```

### 🎯 Step 4: v1.0 Enhanced Manual Steps
**Guided workflow with validation checkpoints**

#### Enhanced Manual Workflow:
1. **Verified Backup** - I verify your .claude.backup/ directory exists and is complete
2. **Smart File Ordering** - Files prioritized by dependency and importance  
3. **Editor-Specific Instructions** - Tailored Find & Replace instructions for your editor
4. **Validation Checkpoints** - Verify each file after replacement with built-in validation
5. **Progress Tracking** - Todo-based progress tracking with completion status
6. **Real-time Error Detection** - Immediate detection and recovery for any issues

### ✅ Step 5: v1.0 Comprehensive Verification
**Multi-layer validation with automatic error detection**

#### Enhanced Verification Checklist:
```markdown
🛡️ PRE-REPLACEMENT SAFETY:
□ Backup verified: .claude.backup/ directory complete
□ Git status: Clean working directory for rollback capability  
□ File integrity: All template files validated for corruption

📋 REPLACEMENT PROGRESS:
□ Priority 1 - Core commands (12 files): ___/12 complete
□ Priority 2 - Components (94+ files): ___/94+ complete  
□ Priority 3 - Context files (15+ files): ___/15+ complete
□ Priority 4 - Configuration files: ___/X complete
□ CLAUDE.md updated with v1.0 structure

🔍 VALIDATION CHECKPOINTS:
□ YAML header integrity: All 88 commands validated
□ Component compatibility: 91 components cross-validated
□ Progressive Disclosure: Layer configurations validated
□ Command functionality: Sample commands tested
□ No orphaned placeholders: Full scan completed

📊 FINAL VALIDATION:
□ Total replacements: ___/247 placeholders processed
□ Error-free completion: No issues detected
□ Performance validation: All optimizations working
□ Ready for production: Full system validated
```

## 🛡️ v1.0 Enhanced Safety & Recovery

### 🚀 Enhanced Safety Protocol
**Comprehensive safety with automatic verification**

#### Before You Start:
1. **Automatic Backup Verification** - I verify backups exist and are complete
2. **Git State Management** - Ensure clean state for easy rollback  
3. **Systematic Approach** - Priority-ordered file processing with validation
4. **Real-time Monitoring** - Continuous validation and error detection

#### v1.0 Enhanced Find & Replace Tips:
- **Editor Detection** - I provide instructions specific to your editor
- **Batch Processing** - Efficient replacement strategies for large template libraries
- **Validation Integration** - Built-in validation after each replacement step
- **Error Recovery** - Automatic detection and recovery procedures

### 🚨 v1.0 Enhanced Error Prevention & Recovery
**Comprehensive error handling with automatic rollback**

#### Advanced Error Prevention:
- **Pre-validation** - Detect issues before replacement begins
- **Real-time Monitoring** - Continuous validation during replacement process
- **Smart Pattern Detection** - Avoid common replacement errors automatically
- **Dependency Validation** - Ensure component compatibility throughout

#### Automatic Recovery Options:
- **File-level Rollback** - Revert individual files if issues detected
- **Batch Rollback** - Revert entire batches with validation
- **Complete System Rollback** - Full restoration to previous state with verification

---

## 🚀 Ready for v1.0 Enhanced Replacement?

### 🎯 Quick Start Options:

#### Option 1: Standard Guided Mode
```bash
/replace-placeholders guided
# Full v1.0 experience with validation and safety
```

#### Option 2: Validation Only
```bash  
/replace-placeholders validate
# Check current placeholder status without changes
```

#### Option 3: Batch Processing Mode
```bash
/replace-placeholders batch
# Efficient batch processing with progress tracking
```

### 📝 Enhanced Value Collection:
When you're ready, I'll collect your project details with:
- **🎯 Smart defaults** based on project analysis
- **🔍 Real-time validation** of provided values  
- **🧩 Progressive Disclosure integration** with layer recommendations
- **📊 Comprehensive reporting** with actionable insights

**Ready to experience v1.0 enhanced placeholder replacement with comprehensive validation and safety?**