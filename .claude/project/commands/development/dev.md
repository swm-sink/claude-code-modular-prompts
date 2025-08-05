---
name: /dev
description: Unified intelligent development workflow with automated quality checks and AI-assisted features (v1.0)
version: "1.0"
usage: '/dev [mode] [target] [options] [--auto-chain]'
category: development
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
- Glob
- WebSearch
dependencies:
- /dev-setup
- /test
- /pipeline
- /quality
validation:
  pre-execution: "Validate mode selection and target existence"
  during-execution: "Monitor operation progress and quality metrics"
  post-execution: "Verify changes maintain code integrity"
interactive-consultation:
  layer-integration: "Phase 1: Single operations, Phase 2: Chained workflows, Phase 3: Full development orchestration"
  options:
    - name: quick
      description: "Fast single operations (format, lint, debug)"
    - name: workflow
      description: "Chained operations (format + lint + test)"
    - name: orchestrated
      description: "Full feature development with all modes"
safety-checks:
  - "Backup before refactoring"
  - "Test suite validation"
  - "Dependency compatibility checks"
  - "Code quality thresholds"
error-recovery:
  - "Rollback on test failure"
  - "Incremental change application"
  - "Manual intervention prompts"
performance:
  - "Parallel file processing"
  - "Incremental analysis"
  - "Smart caching of results"
ai-features:
  - "Intelligent code suggestions"
  - "Automated bug hypothesis"
  - "Feature architecture planning"
---

# /dev - Unified Development Workflow for your project (v1.0)

Comprehensive development workflow solution combining AI-assisted code formatting, linting, refactoring, debugging, feature development, project initialization, analysis, and dependency management.

## 🚀 Interactive Consultation Usage

### Phase 1: Quick Operations (30 seconds)
```bash
/dev format            # Auto-detect and format all files
/dev lint --fix        # Find and fix all linting issues
/dev debug "error msg" # AI-assisted debugging
```

### Phase 2: Workflow Chains (5 minutes)
```bash
/dev format --then lint --then test  # Quality workflow
/dev refactor --extract-method --with-tests  # Safe refactoring
/dev feature "user auth" --scaffold  # Feature scaffolding
```

### Phase 3: Full Orchestration (15+ minutes)
```bash
/dev feature "payment system" --full-stack --with-api --with-tests
/dev analyze --deep --optimize --refactor
/dev init enterprise-app --with-ci --with-monitoring
```

## 🧠 AI-Powered Development Modes

### Format Mode 
**Intelligent code formatting with style learning**
```bash
/dev format              # Auto-detect language and style
/dev format --style team # Use team conventions
/dev format src/ --parallel --report
```

**Features:**
- 🤖 AI learns your team's style preferences
- 🔍 Multi-language auto-detection
- ⚡ Parallel processing for large codebases
- 📊 Formatting impact reports

### Lint Mode
**Smart linting with automated fixes**
```bash
/dev lint                    # Full codebase scan
/dev lint --fix --safe       # Auto-fix safe issues
/dev lint --strict --no-warn # Errors only
```

**Features:**
- 🛠️ Automated safe fixes
- 📈 Progressive rule enforcement
- 🎯 Context-aware suggestions
- 🔗 Integration with pre-commit

### Refactor Mode
**AI-assisted code refactoring**
```bash
/dev refactor "extract LoginService from auth.py"
/dev refactor --modernize  # Update to latest patterns
/dev refactor --performance # Optimize hot paths
```

**Strategies:**
- Extract method/class/module
- Rename with usage updates
- Modernize legacy patterns
- Performance optimization
- Dependency injection
- Design pattern application

### Debug Mode
**AI-powered debugging assistant**
```bash
/dev debug "TypeError in user.py line 45"
/dev debug --interactive  # Step-by-step debugging
/dev debug --trace        # Full execution trace
```

**Capabilities:**
- 🔍 Automated hypothesis generation
- 🧪 Test case creation for bugs
- 📊 Root cause analysis
- 💡 Solution suggestions with examples

### Feature Mode
**End-to-end feature development**
```bash
/dev feature "user notifications"
/dev feature "payment gateway" --with-api --with-ui
/dev feature --list-in-progress
```

**Workflow:**
1. Architecture planning
2. API design & implementation
3. Database schema updates
4. Frontend components
5. Test suite generation
6. Documentation updates

### Init Mode
**Smart project initialization**
```bash
/dev init                  # Interactive setup
/dev init api-service      # REST API template
/dev init ml-pipeline      # ML project structure
```

**Templates:**
- Web applications
- REST APIs
- Microservices
- CLI tools
- ML pipelines
- Libraries

### Analyze Mode
**Deep codebase analysis**
```bash
/dev analyze              # Full analysis report
/dev analyze --security   # Security audit
/dev analyze --performance --suggest-fixes
```

**Analysis Types:**
- Code quality metrics
- Security vulnerabilities
- Performance bottlenecks
- Dependency health
- Technical debt
- Architecture patterns

### Deps Mode
**Intelligent dependency management**
```bash
/dev deps update          # Safe updates only
/dev deps audit           # Security scan
/dev deps optimize        # Remove unused
```

**Features:**
- 🔒 Security vulnerability scanning
- 📦 Smart version resolution
- 🧪 Automated testing of updates
- 📊 Dependency graph visualization

## 🔗 Workflow Automation

### Chained Operations
```bash
# Quality enforcement chain
/dev format --then lint --then test --fail-fast

# Safe refactoring chain
/dev analyze --then refactor --then test --rollback-on-fail

# Feature development chain
/dev feature "auth" --then format --then lint --then test
```

### Custom Workflows
```yaml
# .dev-workflows.yml
workflows:
  pre-commit:
    - format: { paths: staged }
    - lint: { fix: true }
    - test: { scope: affected }
    
  release:
    - deps: { audit: true }
    - test: { coverage: 90 }
    - analyze: { strict: true }
```

## 🛡️ Safety Features

### Automatic Backups
- Pre-refactor snapshots
- Rollback capabilities
- Git integration

### Quality Gates
- Test suite must pass
- Coverage thresholds
- Linting standards
- Security checks

### Progressive Enhancement
```bash
/dev --safe-mode         # Conservative changes only
/dev --aggressive        # Maximum optimization
/dev --interactive       # Confirm each change
```

## 📊 Reporting & Analytics

### Development Metrics
```bash
/dev --report            # Generate activity report
/dev --metrics           # Code quality trends
/dev --leaderboard       # Team contributions
```

### Integration Points
- **CI/CD**: Jenkins, GitHub Actions, GitLab CI
- **IDEs**: VS Code, IntelliJ, Vim
- **Tools**: Git hooks, Docker, K8s
- **Monitoring**: Sentry, DataDog, New Relic

## 🎯 Quick Start Examples

### Daily Development
```bash
/dev format && /dev lint --fix  # Morning cleanup
/dev debug "failing test"        # Debug issue
/dev feature "quick fix"         # Small feature
```

### Code Review Prep
```bash
/dev analyze --pr-review
/dev format --staged
/dev lint --changed-only
```

### Major Refactoring
```bash
/dev analyze --technical-debt
/dev refactor --plan
/dev refactor --execute --with-tests
```

---

Ready to streamline your development workflow? Start with:
- 🚀 **Quick**: `/dev format` for instant cleanup
- 🧠 **Smart**: `/dev debug` for AI-assisted debugging
- 🏗️ **Full**: `/dev feature` for complete development