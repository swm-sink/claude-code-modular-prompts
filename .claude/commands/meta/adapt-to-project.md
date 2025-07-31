---
name: /adapt-to-project
description: Interactive automated project customization with real-time detection (v2.0)
version: 2.0
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
progressive-disclosure:
  layer-integration: "Supports all three layers with intelligent mode selection"
  auto-detection: "Smart project type detection with fallback options"
  error-recovery: "Built-in rollback and error handling throughout process"
performance:
  estimated-time: "2-5 minutes (v1.0) → 1-3 minutes (v2.0 optimized)"
  success-metrics: "Enhanced validation and error prevention"
  batch-processing: "Optimized for large template libraries"
---

# 🚀 Interactive Automated Project Customization (v2.0)

**Enhanced intelligent project detection with progressive disclosure integration and comprehensive validation. No manual work required!**

## v2.0 Enhanced Process

### **Usage Options**:
- **`/adapt-to-project`** - Standard automated customization
- **`/adapt-to-project quick-mode`** - Fast mode for simple projects (1-2 minutes)
- **`/adapt-to-project comprehensive`** - Full analysis with component assembly (3-5 minutes)
- **`/adapt-to-project validate`** - Validation-only mode (check current customization)
- **`/adapt-to-project rollback`** - Revert to previous state with full recovery

## How v2.0 Actually Works

1. **🔍 Smart Auto-detect** - Enhanced project scanning with AI-powered analysis
2. **💬 Intelligent Questions** - Context-aware questions with smart defaults
3. **🔄 Validated Replacement** - Real-time validation during replacement process
4. **🧩 Progressive Integration** - Automatic integration with Layer 1/2/3 system
5. **✅ Comprehensive Validation** - Multi-layer validation with error recovery
6. **📊 Performance Monitoring** - Track optimization and success metrics

**Timeline: 1-3 minutes total (v2.0 optimized)**

---

## 🔍 Phase 1: Enhanced Smart Project Detection

**v2.0 Features: AI-powered analysis with comprehensive project understanding**

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

#### v2.0 Secondary Analysis:
- **Architecture Detection**: Microservices, monolith, serverless patterns
- **CI/CD Integration**: GitHub Actions, GitLab CI, Jenkins detection
- **Database Analysis**: PostgreSQL, MongoDB, Redis configuration detection
- **Container Detection**: Docker, Kubernetes configuration analysis
- **Cloud Platform**: AWS, GCP, Azure infrastructure detection

### 📊 Progressive Disclosure Integration

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

**v2.0 Features: Context-aware questions with smart defaults and validation**

For any details I can't auto-detect, I'll ask intelligent questions with pre-filled smart defaults:

### 🧠 Smart Questioning System

#### Context-Aware Questions:
- **Pre-filled answers** based on detected patterns
- **Skip redundant questions** when confidence is high
- **Progressive complexity** - simple projects get fewer questions
- **Validation during input** - immediate feedback on responses
- **Smart suggestions** - learn from similar projects

### 📊 v2.0 Enhanced Interaction Examples:

#### Standard Mode:
```bash
🤖 I detected a Next.js + TypeScript project called "awesome-dashboard"
🤖 Confidence: 95% - web application, TypeScript ecosystem
🤖 Team size? [default: small] (solo/small/medium/large)  
👤 [Enter] # Uses default
🤖 Progressive Disclosure: Recommending Layer 2 (Guided Customization)
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

### 🎯 v2.0 Question Categories:
- **Architecture Questions**: Validated against detected infrastructure
- **Team & Process**: Smart defaults based on project size and complexity
- **Technology Preferences**: Pre-populated from ecosystem analysis
- **Integration Points**: Automatic detection with confirmation prompts
- **Quality & Testing**: Framework-specific recommendations

---

## 🔄 Phase 3: Enhanced Validated Replacement

**v2.0 Features: Real-time validation with intelligent batch processing and rollback capability**

I'll automatically update **all** templates with comprehensive validation at each step:

### 📁 Enhanced File Coverage:
- **`.claude/commands/**/*.md`** - 88 command templates with validation
- **`.claude/components/**/*.md`** - 94+ component templates with compatibility checking
- **`.claude/assembly-templates/`** - Professional workflow templates
- **`.claude/assembly-config/`** - Component compatibility configurations
- **`.claude/context/*.md`** - Context files with project-specific learning
- **`CLAUDE.md`** - Enhanced project memory with v2.0 features
- **Configuration files** - JSON configs with intelligent defaults

### 🎯 v2.0 Smart Replacements:

#### Core Project Identifiers:
- **`lusaka`** → Your actual project name with validation
- **`software-development`** → Intelligent domain classification (web-dev, data-science, DevOps, etc.)
- **Technology stacks** → Complete ecosystem replacement (React+TypeScript, Django+Postgres, etc.)
- **Framework versions** → Version-aware replacements with compatibility checking

#### Progressive Disclosure Integration:
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

### 🛡️ v2.0 Validation During Replacement:
- **Pre-replacement validation** - File integrity and structure checks
- **Real-time validation** - Each replacement validated before applying
- **Dependency validation** - Ensure component compatibility throughout
- **Post-replacement verification** - Comprehensive functionality testing
- **Automatic rollback** - Revert any failed replacements with full recovery

---

## ✅ Phase 4: Comprehensive Validation & Enhanced Reporting

**v2.0 Features: Multi-layer validation with performance metrics and intelligent recommendations**

I'll perform comprehensive validation with detailed reporting and actionable insights:

### 🔍 v2.0 Validation Suite:

#### Multi-Layer Validation:
- **Structural Validation**: YAML compliance across all 88 commands
- **Component Compatibility**: Validate 94+ components for interaction compatibility
- **Progressive Disclosure**: Verify all three layers function correctly
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
- **🎯 Layer Integration**: Progressive Disclosure configuration status
- **📋 Command Inventory**: 88 customized commands organized by category and complexity
- **🧩 Component Status**: 94+ components with compatibility matrix
- **⚡ Performance Report**: Optimization results and success metrics
- **🔧 Configuration Status**: All JSON configs and their validation status

#### Intelligent Recommendations:

##### Immediate Next Steps (Personalized):
1. **Start Here**: `/welcome [your-experience-level]` - Personalized onboarding
2. **First Command**: Recommended command based on your project type
3. **Layer Navigation**: Suggested Progressive Disclosure layer to begin with
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

## 🚀 Ready to Start v2.0 Enhanced Customization?

**Choose your preferred mode and I'll begin the intelligent automated customization process!**

### 🎯 Quick Start Options:

#### Option 1: Standard Mode
```bash
/adapt-to-project
# Full v2.0 experience with intelligent defaults (1-3 minutes)
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

### 📊 v2.0 Enhanced Session Examples:

#### Standard Mode Session:
```bash
👤 /adapt-to-project
🤖 Starting v2.0 intelligent project detection...
🤖 Found package.json + docker-compose.yml - Next.js + PostgreSQL detected!
🤖 Project: "ecommerce-dashboard" | Confidence: 97% | Domain: web-dev
🤖 Progressive Disclosure: Recommending Layer 2 (Guided Customization)
🤖 Team size? [default: small] 
👤 [Enter]
🤖 ✅ 88 templates + 94 components customized! Layer 2 ready.
🤖 📊 Validation: 100% success | Performance: Optimized | Ready in 2.3 minutes
🤖 🎯 Start with: /welcome intermediate
```

#### Quick Mode Session:
```bash
👤 /adapt-to-project quick-mode
🤖 Quick v2.0 mode: High confidence React project detected
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
🤖 📊 94+ components active | All layers configured | Ready for /assemble-command
```

### 🚀 v2.0 Benefits:
- **⚡ 50% faster** than v1.0 with intelligent defaults
- **🎯 Higher accuracy** with AI-powered project analysis  
- **🔧 Enhanced validation** with automatic error recovery
- **📊 Better reporting** with actionable insights
- **🧩 Progressive integration** with three-layer system

**Ready to experience v2.0 enhanced automated customization?**