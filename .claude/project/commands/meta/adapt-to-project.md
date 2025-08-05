---
name: /adapt-to-project
description: Interactive automated project customization with real-time detection (v1.0)
version: "1.0"
usage: '/adapt-to-project [validate|quick-mode|comprehensive|rollback]'
category: meta
allowed-tools:
- Bash
- Read
- Write
- Edit
- MultiEdit
- Glob
- LS
- TodoWrite
- Grep
dependencies:
- welcome
- validate-adaptation
- replace-placeholders
validation:
  pre-execution: validate_project_structure
  during-execution: validate_each_replacement
  post-execution: comprehensive_validation_suite
interactive-consultation:
  layer-integration: "Supports all three consultation phases with intelligent mode selection"
  auto-detection: "Smart project type detection with fallback options"
  error-recovery: "Built-in rollback and error handling throughout process"
performance:
  estimated-time: "2-5 minutes (v1.0) → 1-3 minutes (v1.0 optimized)"
  success-metrics: "Enhanced validation and error prevention"
  batch-processing: "Optimized for large template libraries"
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/meta/adapt-to-project.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>adapt-to-project</command_id>
  <command_count>88</command_count>
  <interactive_consultation_layer>all</interactive_consultation_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="project_structure_analysis"/>
      <component ref="parameter-parser" role="mode_selection"/>
      <component ref="data-transformer" role="configuration_processing"/>
      <component ref="dependency-resolver" role="technology_stack_detection"/>
      <component ref="workflow-coordinator" role="multi_phase_orchestration"/>
      <component ref="progress-indicator" role="adaptation_progress_tracking"/>
      <component ref="user-confirmation" role="validation_prompts"/>
    </required_components>
    <optional_components>
      <component ref="framework-validation" benefit="technology_stack_validation"/>
      <component ref="performance-monitoring" benefit="adaptation_performance_tracking"/>
      <component ref="error-handler" benefit="rollback_and_recovery"/>
      <component ref="context-compression" benefit="optimized_template_processing"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="welcome" context="user_onboarding"/>
      <command ref="validate-adaptation" context="post_adaptation_validation"/>
      <command ref="replace-placeholders" context="placeholder_management"/>
      <command ref="quick-command" context="layer_1_integration"/>
      <command ref="build-command" context="layer_2_integration"/>
      <command ref="assemble-command" context="layer_3_integration"/>
    </invokable_commands>
    <orchestration_patterns>conditional|progressive|batch_processing|error_recovery</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Intelligent automated project customization with real-time detection, progressive disclosure integration, and comprehensive validation</task_description>
    <implementation_strategy>auto_detect_project|interactive_questions|validated_replacement|progressive_integration|comprehensive_validation</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>project_customization_automation</primary_discovery_path>
    <alternative_paths>
      <path>context_engineering_adaptation</path>
      <path>automated_project_setup</path>
      <path>intelligent_customization</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/project-detection-patterns.md" relation="detection_methodology"/>
      <file type="context" ref=".claude/context/interactive-consultation-guide.md" relation="phase_integration"/>
      <file type="context" ref=".claude/context/replacement-validation-patterns.md" relation="validation_framework"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="validate-adaptation" relation="validation_workflow"/>
      <file type="command" ref="replace-placeholders" relation="replacement_execution"/>
      <file type="command" ref="quick-command" relation="layer_1_path"/>
      <file type="command" ref="build-command" relation="layer_2_path"/>
      <file type="command" ref="assemble-command" relation="layer_3_path"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="replace-placeholders" similarity="0.75"/>
      <file type="command" ref="sync-from-reference" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>first_time_context_engineering_setup</scenario>
      <scenario>new_project_template_adaptation</scenario>
      <scenario>comprehensive_project_customization</scenario>
      <scenario>interactive_consultation_phase_integration</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>minor_template_adjustments</scenario>
      <scenario>single_placeholder_replacement</scenario>
      <scenario>validation_only_requirements</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>adapt project customize automation detection progressive disclosure validation</keywords>
    <semantic_tags>project_adaptation automated_customization intelligent_detection progressive_integration</semantic_tags>
    <functionality_vectors>[1.0, 0.9, 0.8, 0.9, 0.7]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>10</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/project-detection-patterns.md" importance="critical"/>
      <context_file ref=".claude/context/progressive-disclosure-guide.md" importance="critical"/>
      <context_file ref=".claude/context/replacement-validation-patterns.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/technology-stack-patterns.md" importance="high"/>
      <context_file ref=".claude/context/framework-detection-guide.md" importance="high"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>project_setup</workflow_stage>
    <integration_patterns>
      <pattern>intelligent_project_detection</pattern>
      <pattern>progressive_layer_integration</pattern>
      <pattern>automated_replacement_with_validation</pattern>
      <pattern>comprehensive_quality_assurance</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>automated_project_adaptation</concept_introduction>
    <skill_progression>beginner_to_advanced</skill_progression>
    <mastery_indicators>
      <indicator>successful_project_type_detection</indicator>
      <indicator>appropriate_progressive_disclosure_layer_selection</indicator>
      <indicator>validated_template_customization</indicator>
      <indicator>error_free_adaptation_with_rollback_capability</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# 🚀 Interactive Automated Project Customization (v1.0)

**Enhanced intelligent project detection with progressive disclosure integration and comprehensive validation. No manual work required!**

## v1.0 Enhanced Process

### **Usage Options**:
- **`/adapt-to-project`** - Standard automated customization
- **`/adapt-to-project quick-mode`** - Fast mode for simple projects (1-2 minutes)
- **`/adapt-to-project comprehensive`** - Full analysis with component assembly (3-5 minutes)
- **`/adapt-to-project validate`** - Validation-only mode (check current customization)
- **`/adapt-to-project rollback`** - Revert to previous state with full recovery

## How v1.0 Actually Works

1. **🔍 Smart Auto-detect** - Enhanced project scanning with AI-powered analysis
2. **💬 Intelligent Questions** - Context-aware questions with smart defaults
3. **🔄 Validated Replacement** - Real-time validation during replacement process
4. **🧩 Progressive Integration** - Automatic integration with Layer 1/2/3 system
5. **✅ Comprehensive Validation** - Multi-layer validation with error recovery
6. **📊 Performance Monitoring** - Track optimization and success metrics

**Timeline: 1-3 minutes total (v1.0 optimized)**

---

## 🔍 Phase 1: Enhanced Smart Project Detection

**v1.0 Features: AI-powered analysis with comprehensive project understanding**

I'll perform multi-layer scanning of your project with enhanced detection capabilities:

### 🧠 Intelligent Project Analysis

#### Primary Detection (Enhanced):
- `package.json` → JavaScript/TypeScript ecosystem analysis (React, Vue, Next.js, etc.)
- `requirements.txt`, `setup.py`, `pyproject.toml` → Python ecosystem (Django, FastAPI, Flask, etc.)
- `pom.xml`, `build.gradle` → Java/Kotlin (Spring Boot, Micronaut, etc.)
- `go.mod` → Go ecosystem analysis
- `Cargo.toml` → Rust project analysis
- `composer.json` → PHP ecosystem (Laravel, Symfony, etc.)
- `Gemfile` → Ruby ecosystem (Rails, Sinatra, etc.)
- `.csproj`, `.sln` → C#/.NET ecosystem

#### v1.0 Secondary Analysis:
- **Architecture Detection**: Microservices, monolith, serverless patterns
- **CI/CD Integration**: GitHub Actions, GitLab CI, Jenkins detection
- **Database Analysis**: PostgreSQL, MongoDB, Redis configuration detection
- **Container Detection**: Docker, Kubernetes configuration analysis
- **Cloud Platform**: AWS, GCP, Azure infrastructure detection

### 📊 Interactive Consultation Integration

Based on detected complexity, I'll automatically recommend the appropriate layer:
- **Simple Projects** → Layer 1 (Auto-generation with `/quick-command`)
- **Standard Projects** → Layer 2 (Guided customization with `/build-command`)
- **Complex Projects** → Layer 3 (Professional assembly with `/assemble-command`)

### 🎯 Enhanced Auto-Determination:
- **Project Name**: Multi-source analysis (package files, git remote, directory)
- **Primary Technologies**: Complete ecosystem mapping with version detection  
- **Framework/Stack**: Intelligent framework detection with configuration analysis
- **Domain Classification**: AI-powered domain classification (web-dev, data-science, DevOps, etc.)
- **Testing Ecosystem**: Complete testing framework and tool detection
- **Development Workflow**: Detected development patterns and practices

---

## 💬 Phase 2: Enhanced Interactive Questions

**v1.0 Features: Context-aware questions with smart defaults and validation**

For any details I can't auto-detect, I'll ask intelligent questions with pre-filled smart defaults:

### 🧠 Smart Questioning System

#### Context-Aware Questions:
- **Pre-filled answers** based on detected patterns
- **Skip redundant questions** when confidence is high
- **Progressive complexity** - simple projects get fewer questions
- **Validation during input** - immediate feedback on responses
- **Smart suggestions** - learn from similar projects

### 📊 v1.0 Enhanced Interaction Examples:

#### Standard Mode:
```bash
🤖 I detected a Next.js + TypeScript project called "awesome-dashboard"
🤖 Confidence: 95% - web application, TypeScript ecosystem
🤖 Team size? [default: small] (solo/small/medium/large)  
👤 [Enter] # Uses default
🤖 Interactive Consultation: Recommending Phase 2 (Guided Customization)
🤖 ✅ Customizing 88 templates for small team web development with TypeScript...
```

#### Quick Mode:
```bash
🤖 Quick mode: High confidence detection (React + Node.js)
🤖 Using intelligent defaults for simple project customization...
🤖 ✅ 45-second customization complete! Layer 1 templates ready.
```

#### Comprehensive Mode:
```bash
🤖 Comprehensive analysis: Complex microservices architecture detected
🤖 Found: Docker, Kubernetes, PostgreSQL, Redis, GitHub Actions
🤖 Recommending Layer 3 (Professional Assembly) with enterprise components
🤖 Database strategy? [PostgreSQL + Redis] (confirmed/modify)
👤 confirmed
🤖 ✅ Enterprise-grade templates configured with full component assembly
```

### 🎯 v1.0 Question Categories:
- **Architecture Questions**: Validated against detected infrastructure
- **Team & Process**: Smart defaults based on project size and complexity
- **Technology Preferences**: Pre-populated from ecosystem analysis
- **Integration Points**: Automatic detection with confirmation prompts
- **Quality & Testing**: Framework-specific recommendations

---

## 🔄 Phase 3: Enhanced Validated Replacement

**v1.0 Features: Real-time validation with intelligent batch processing and rollback capability**

I'll automatically update **all** templates with comprehensive validation at each step:

### 📁 Enhanced File Coverage:
- **`.claude/commands/**/*.md`** - 88 command templates with validation
- **`.claude/components/**/*.md`** - 96 component templates with compatibility checking
- **`.claude/assembly-templates/`** - Professional workflow templates
- **`.claude/assembly-config/`** - Component compatibility configurations
- **`.claude/context/*.md`** - Context files with project-specific learning
- **`CLAUDE.md`** - Enhanced project memory with v1.0 features
- **Configuration files** - JSON configs with intelligent defaults

### 🎯 v1.0 Smart Replacements:

#### Core Project Identifiers:
- **`[PROJECT_NAME]`** → Your actual project name with validation
- **`software-development`** → Intelligent domain classification (web-dev, data-science, DevOps, etc.)
- **Technology stacks** → Complete ecosystem replacement (React+TypeScript, Django+Postgres, etc.)
- **Framework versions** → Version-aware replacements with compatibility checking

#### Interactive Consultation Integration:
- **Layer 1 configs** → Quick-command templates with your project context
- **Layer 2 configs** → Build-command configurations with smart filtering
- **Layer 3 configs** → Assembly templates with enterprise components
- **Cross-layer navigation** → Seamless escalation/de-escalation paths

#### Enhanced Technology Mapping:
- **Frontend**: React → Next.js, Vue → Nuxt.js, Angular ecosystem
- **Backend**: Node.js → Express/Fastify, Python → Django/FastAPI/Flask
- **Database**: PostgreSQL, MongoDB, Redis with connection configurations
- **Testing**: Jest, pytest, JUnit with framework-specific configurations
- **CI/CD**: GitHub Actions, GitLab CI with project-specific workflows
- **Infrastructure**: Docker, Kubernetes, AWS/GCP/Azure configurations

### 🛡️ v1.0 Validation During Replacement:
- **Pre-replacement validation** - File integrity and structure checks
- **Real-time validation** - Each replacement validated before applying
- **Dependency validation** - Ensure component compatibility throughout
- **Post-replacement verification** - Comprehensive functionality testing
- **Automatic rollback** - Revert any failed replacements with full recovery

---

## ✅ Phase 4: Comprehensive Validation & Enhanced Reporting

**v1.0 Features: Multi-layer validation with performance metrics and intelligent recommendations**

I'll perform comprehensive validation with detailed reporting and actionable insights:

### 🔍 v1.0 Validation Suite:

#### Multi-Layer Validation:
- **Structural Validation**: YAML compliance across all 88 commands
- **Component Compatibility**: Validate 96 components for interaction compatibility
- **Interactive Consultation**: Verify all three phases function correctly
- **Performance Validation**: Ensure optimizations don't break functionality
- **Integration Testing**: Test cross-command functionality and workflows

#### Real-Time Quality Assurance:
- **Template Integrity**: Verify all placeholders properly replaced
- **Configuration Validity**: Test all JSON configs and settings
- **Dependency Resolution**: Confirm all command dependencies are satisfied
- **Error Handling**: Validate error recovery and rollback functionality

### 📊 Enhanced Reporting Dashboard:

#### Comprehensive Success Metrics:
- **📊 Replacement Summary**: Detailed breakdown of all 200+ replacements made
- **🎯 Phase Integration**: Interactive Consultation configuration status
- **📋 Command Inventory**: 88 customized commands organized by category and complexity
- **🧩 Component Status**: 96 components with compatibility matrix
- **⚡ Performance Report**: Optimization results and success metrics
- **🔧 Configuration Status**: All JSON configs and their validation status

#### Intelligent Recommendations:

##### Immediate Next Steps (Personalized):
1. **Start Here**: `/welcome [your-experience-level]` - Personalized onboarding
2. **First Command**: Recommended command based on your project type
3. **Phase Navigation**: Suggested Interactive Consultation phase to begin with
4. **Quick Wins**: 3-5 commands that provide immediate value
5. **Advanced Features**: Relevant advanced commands for your tech stack

##### Optimization Opportunities:
- **Performance Improvements**: Identified optimization opportunities
- **Component Assembly**: Suggestions for powerful component combinations  
- **Workflow Integration**: CI/CD and automation recommendations
- **Security Enhancements**: Project-specific security configurations
- **Monitoring Setup**: Relevant monitoring and observability recommendations

#### 🚨 Enhanced Issue Detection & Resolution:
- **⚠️ Issues Detected**: Detailed issues with specific resolution steps
- **🔧 Auto-Fix Available**: Issues that can be automatically resolved
- **📝 Manual Actions**: Clear instructions for any required manual steps
- **🔄 Rollback Options**: Easy rollback instructions if needed
- **📞 Support Paths**: Escalation paths for complex issues

---

## 🚀 Ready to Start v1.0 Enhanced Customization?

**Choose your preferred mode and I'll begin the intelligent automated customization process!**

### 🎯 Quick Start Options:

#### Option 1: Standard Mode
```bash
/adapt-to-project
# Full v1.0 experience with intelligent defaults (1-3 minutes)
```

#### Option 2: Quick Mode  
```bash
/adapt-to-project quick-mode
# Fast customization for simple projects (45 seconds)
```

#### Option 3: Comprehensive Mode
```bash
/adapt-to-project comprehensive  
# Enterprise-grade customization with full component assembly (3-5 minutes)
```

#### Option 4: Validation Only
```bash
/adapt-to-project validate
# Check current customization status without changes
```

### 📊 v1.0 Enhanced Session Examples:

#### Standard Mode Session:
```bash
👤 /adapt-to-project
🤖 Starting v1.0 intelligent project detection...
🤖 Found package.json + docker-compose.yml - Next.js + PostgreSQL detected!
🤖 Project: "ecommerce-dashboard" | Confidence: 97% | Domain: web-dev
🤖 Interactive Consultation: Recommending Phase 2 (Guided Customization)
🤖 Team size? [default: small] 
👤 [Enter]
🤖 ✅ 88 templates + 96 components customized! Layer 2 ready.
🤖 📊 Validation: 100% success | Performance: Optimized | Ready in 2.3 minutes
🤖 🎯 Start with: /welcome intermediate
```

#### Quick Mode Session:
```bash
👤 /adapt-to-project quick-mode
🤖 Quick v1.0 mode: High confidence React project detected
🤖 Using intelligent defaults + Layer 1 auto-generation...  
🤖 ✅ 45-second customization complete! Try /quick-command
```

#### Comprehensive Mode Session:
```bash
👤 /adapt-to-project comprehensive
🤖 Enterprise analysis: Microservices + Kubernetes + CI/CD detected
🤖 Complex architecture - recommending Layer 3 (Professional Assembly)
🤖 Found: Docker, K8s, PostgreSQL, Redis, GitHub Actions, AWS
🤖 Database strategy? [PostgreSQL + Redis] 
👤 confirmed
🤖 ✅ Enterprise templates configured with full component assembly
🤖 📊 96 components active | All layers configured | Ready for /assemble-command
```

### 🚀 v1.0 Benefits:
- **⚡ 50% faster** than v1.0 with intelligent defaults
- **🎯 Higher accuracy** with AI-powered project analysis  
- **🔧 Enhanced validation** with automatic error recovery
- **📊 Better reporting** with actionable insights
- **🧩 Progressive integration** with three-layer system

**Ready to experience v1.0 enhanced automated customization?**