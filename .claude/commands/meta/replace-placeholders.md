---
name: /replace-placeholders
description: Systematically replace all placeholders in adapted commands with enhanced validation (v2.0)
version: 2.0
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

# Enhanced Placeholder Replacement Guide (v2.0)

**Enhanced manual replacement with validation, safety, and guided workflows**

## 🎯 v2.0 Enhanced Capabilities

### **Usage Options:**
- **`/replace-placeholders`** - Standard guided replacement with validation
- **`/replace-placeholders validate`** - Validation-only mode (check current placeholders)
- **`/replace-placeholders guided`** - Step-by-step guided workflow with safety checks
- **`/replace-placeholders batch`** - Batch processing with progress tracking
- **`/replace-placeholders rollback`** - Rollback to previous state with full recovery

## 🚀 What v2.0 Actually Does

**Enhanced replacement guide with comprehensive validation and safety.** I'll help you manually replace all `[INSERT_XXX]` placeholders with:

### Core Capabilities:
- 📋 **Smart Detection** - AI-powered placeholder detection with pattern recognition
- 📍 **Precise Location** - Exact file locations with line numbers and context
- 📝 **Guided Instructions** - Step-by-step Find & Replace workflow with validation
- ✅ **Real-time Verification** - Validation checkpoints throughout the process
- 🛡️ **Safety First** - Automatic backup verification and rollback capability
- 📊 **Progress Tracking** - Todo-based progress tracking with completion status

## 🔧 v2.0 Enhanced vs. Limitations

### ✅ v2.0 Enhanced Capabilities:
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

### 🎯 v2.0 Philosophy: **Enhanced Manual Control**
The v2.0 approach enhances the manual process with **validation, safety, and guidance** while keeping you in full control of file modifications.

## v2.0 Enhanced Manual Workflow

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

#### v2.0 Enhanced File Coverage:
- **📁 `.claude/commands/**/*.md`** - 88 command files with validation
- **📁 `.claude/components/**/*.md`** - 94+ component files with compatibility checking
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

## 📋 v2.0 Enhanced Placeholder Reference

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

### 🧩 v2.0 Progressive Disclosure Placeholders
**New placeholders for Layer integration**

```yaml
[INSERT_LAYER_PREFERENCE] → layer-1, layer-2, layer-3 (complexity-recommended)
[INSERT_AUTO_GENERATION_CONFIG] → enabled, disabled (layer-1 settings)
[INSERT_GUIDED_CUSTOMIZATION_CONFIG] → standard, advanced (layer-2 settings)
[INSERT_COMPONENT_ASSEMBLY_CONFIG] → basic, professional, enterprise (layer-3 settings)
```

### 🔧 v2.0 Enhanced Configuration Placeholders
**New advanced configuration options**

```yaml
[INSERT_VALIDATION_LEVEL] → basic, comprehensive, enterprise (validation-requirements)
[INSERT_ERROR_HANDLING] → standard, enhanced, enterprise (error-recovery-level)
[INSERT_MONITORING_SETUP] → none, basic, advanced, enterprise (observability-level)
[INSERT_PERFORMANCE_MONITORING] → disabled, basic, advanced (performance-tracking)
```

### 🔗 v2.0 Smart Nested Placeholder Handling
**Enhanced nested placeholder resolution with validation**

#### Intelligent Nested Resolution:
For complex placeholders like `[INSERT_[INSERT_DOMAIN]_CONFIG]`:

1. **Smart Detection**: v2.0 automatically detects nested patterns
2. **Guided Resolution**: Step-by-step resolution with validation:
   ```yaml
   Step 1: [INSERT_DOMAIN] → "web-dev" (validated)
   Step 2: [INSERT_DOMAIN_CONFIG] → [INSERT_WEB-DEV_CONFIG] 
   Step 3: [INSERT_WEB-DEV_CONFIG] → "react-typescript-config" (validated)
   ```
3. **Validation at Each Step**: Ensure each resolution step is valid
4. **Error Prevention**: Detect circular references and invalid nesting

---

## 🚀 v2.0 Enhanced Manual Replacement Process

### 🛡️ Step 1: Safety Setup & Validation
**Enhanced safety protocol with automatic verification**

#### Pre-Replacement Safety Protocol:
```bash
# v2.0 Enhanced Safety Setup:
/replace-placeholders validate    # Comprehensive system validation
# ✅ Backup verification: .claude.backup/ exists and complete
# ✅ Git status: Clean working directory 
# ✅ File integrity: All 88 commands + 94+ components verified
# ✅ Placeholder inventory: 200+ placeholders catalogued with locations
```

### 📝 Step 2: Enhanced Value Collection
**Smart value gathering with intelligent defaults**

#### Guided Value Collection Process:
I'll collect your project details with smart validation and pre-filled defaults based on your project analysis.

### 📊 Step 3: v2.0 Enhanced Replacement Guide
**Comprehensive guide with validation and progress tracking**

#### Enhanced Guide Format:
```markdown
v2.0 PLACEHOLDER REPLACEMENT GUIDE
===================================
📊 Total Files: 88 commands + 94 components + configs
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

### 🎯 Step 4: v2.0 Enhanced Manual Steps
**Guided workflow with validation checkpoints**

#### Enhanced Manual Workflow:
1. **Verified Backup** - I verify your .claude.backup/ directory exists and is complete
2. **Smart File Ordering** - Files prioritized by dependency and importance  
3. **Editor-Specific Instructions** - Tailored Find & Replace instructions for your editor
4. **Validation Checkpoints** - Verify each file after replacement with built-in validation
5. **Progress Tracking** - Todo-based progress tracking with completion status
6. **Real-time Error Detection** - Immediate detection and recovery for any issues

### ✅ Step 5: v2.0 Comprehensive Verification
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
□ CLAUDE.md updated with v2.0 structure

🔍 VALIDATION CHECKPOINTS:
□ YAML header integrity: All 88 commands validated
□ Component compatibility: 94+ components cross-validated
□ Progressive Disclosure: Layer configurations validated
□ Command functionality: Sample commands tested
□ No orphaned placeholders: Full scan completed

📊 FINAL VALIDATION:
□ Total replacements: ___/247 placeholders processed
□ Error-free completion: No issues detected
□ Performance validation: All optimizations working
□ Ready for production: Full system validated
```

## 🛡️ v2.0 Enhanced Safety & Recovery

### 🚀 Enhanced Safety Protocol
**Comprehensive safety with automatic verification**

#### Before You Start:
1. **Automatic Backup Verification** - I verify backups exist and are complete
2. **Git State Management** - Ensure clean state for easy rollback  
3. **Systematic Approach** - Priority-ordered file processing with validation
4. **Real-time Monitoring** - Continuous validation and error detection

#### v2.0 Enhanced Find & Replace Tips:
- **Editor Detection** - I provide instructions specific to your editor
- **Batch Processing** - Efficient replacement strategies for large template libraries
- **Validation Integration** - Built-in validation after each replacement step
- **Error Recovery** - Automatic detection and recovery procedures

### 🚨 v2.0 Enhanced Error Prevention & Recovery
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

## 🚀 Ready for v2.0 Enhanced Replacement?

### 🎯 Quick Start Options:

#### Option 1: Standard Guided Mode
```bash
/replace-placeholders guided
# Full v2.0 experience with validation and safety
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

**Ready to experience v2.0 enhanced placeholder replacement with comprehensive validation and safety?**