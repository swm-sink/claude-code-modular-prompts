# Prompt Engineering Framework

| framework | version | last_updated | status |
|-----------|---------|--------------|--------|
| prompt-engineering-framework | 1.0.0 | 2025-07-20 | production |

## Overview

The Prompt Engineering Framework provides comprehensive security-first components and architectural constraints for Claude Code environments. This framework combines enterprise-grade security controls with coding discipline enforcement, ensuring both secure and maintainable LLM-generated code.

## Framework Structure

### 🔒 Security-First Components (I11-I15)

#### I11 - [Input Validation Framework](./input-validation-framework.md)
- **Purpose**: First line of defense - comprehensive input validation
- **Features**: Whitelist validation, schema enforcement, context-aware sanitization
- **Coverage**: All user inputs, file operations, command parameters
- **Status**: ✅ Production Ready

#### I12 - [Authentication & Authorization Framework](./authentication-authorization-framework.md)
- **Purpose**: Identity verification and access control
- **Features**: Multi-factor auth, RBAC, rate limiting, audit logging
- **Coverage**: User identity, access control, session management
- **Status**: ✅ Production Ready

#### I13 - [Data Protection Module](./data-protection-module.md)
- **Purpose**: Protect sensitive data at rest and in transit
- **Features**: AES-256-GCM encryption, PII handling, secrets management
- **Coverage**: Data encryption, privacy compliance, secure error handling
- **Status**: ✅ Production Ready

#### I14 - [Security Scanning Integration](./security-scanning-integration.md)
- **Purpose**: Continuous security testing and vulnerability management
- **Features**: SAST/DAST, dependency scanning, infrastructure scanning
- **Coverage**: Vulnerability detection, compliance monitoring, quality gates
- **Status**: ✅ Production Ready

#### I15 - [Prompt Injection Prevention](./prompt-injection-prevention.md)
- **Purpose**: LLM-specific security controls
- **Features**: Injection detection, output validation, context escape prevention
- **Coverage**: All LLM interactions, prompt templates, user input processing
- **Status**: ✅ Production Ready

#### 📋 [Security Framework Overview](./security-framework-overview.md)
- **Purpose**: Comprehensive framework documentation and integration guide
- **Features**: Defense-in-depth architecture, OWASP 2025 compliance, zero-trust implementation
- **Coverage**: Complete security ecosystem with metrics and monitoring
- **Status**: ✅ Production Ready

### 🏗️ Architectural Constraints Framework

#### [Architectural Constraints](./architectural-constraints.md)
- **Purpose**: Mandatory file, class, and method size limits
- **Features**: Constraint enforcement patterns, validation mechanisms
- **Integration**: TDD workflows, real-time monitoring
- **Status**: ✅ Production Ready

#### [God Object Prevention](./god-object-prevention.md)
- **Purpose**: Anti-pattern detection and prevention
- **Features**: Scoring system, automatic refactoring triggers
- **Integration**: Design-time guidance, pattern recognition
- **Status**: ✅ Production Ready

#### [Module Structure Constraints](./module-structure-constraints.md)
- **Purpose**: Single responsibility enforcement
- **Features**: Interface contracts, dependency management
- **Integration**: Naming conventions, circular dependency prevention
- **Status**: ✅ Production Ready

#### [Constraint Validation Engine](./constraint-validation-engine.md)
- **Purpose**: Automated constraint checking pipeline
- **Features**: Pre-commit hooks, real-time monitoring
- **Integration**: Threshold alerting, comprehensive reporting
- **Status**: ✅ Production Ready

#### [Command Constraint Integration](./command-constraint-integration.md)
- **Purpose**: Framework command integration
- **Features**: Constraint-aware templates, automatic enforcement
- **Integration**: Fallback mechanisms, emergency procedures
- **Status**: ✅ Production Ready

### 🧪 Testing and Quality Assurance

#### [Integration-First Testing](./integration-first-testing.md)
- **Purpose**: Comprehensive testing framework integration
- **Features**: TDD enforcement, test quality gates
- **Integration**: Framework commands, quality validation
- **Status**: ✅ Production Ready

#### [TDD Enforcement Engine](./tdd-enforcement-engine.md)
- **Purpose**: Test-driven development enforcement
- **Features**: RED-GREEN-REFACTOR cycle, automated validation
- **Integration**: Quality gates, test coverage monitoring
- **Status**: ✅ Production Ready

#### [Test Framework Integration](./test-framework-integration.md)
- **Purpose**: Multi-framework testing support
- **Features**: Language-specific test integration, coverage tracking
- **Integration**: CI/CD pipelines, quality reporting
- **Status**: ✅ Production Ready

#### [Test Quality Gates](./test-quality-gates.md)
- **Purpose**: Quality gate enforcement for testing
- **Features**: Coverage thresholds, test quality metrics
- **Integration**: Deployment blocking, quality assurance
- **Status**: ✅ Production Ready

#### [Testing Patterns Library](./testing-patterns-library.md)
- **Purpose**: Comprehensive testing pattern repository
- **Features**: Best practices, anti-pattern prevention
- **Integration**: Framework templates, quality guidance
- **Status**: ✅ Production Ready

### 📦 Package Verification System (I16-I20)

#### I16 - [Package Whitelist System](./package-whitelist-system.md)
- **Purpose**: Verified package management across all programming languages
- **Features**: Real-time package verification, comprehensive whitelists, version validation
- **Coverage**: PyPI, npm, crates.io, Maven Central, and 8+ package ecosystems
- **Status**: ✅ Production Ready

#### I17 - [Hallucination Prevention](./hallucination-prevention.md)
- **Purpose**: Eliminate LLM package and API method hallucinations
- **Features**: Real-time validation, API method verification, proactive correction
- **Coverage**: Package existence, method validation, syntax checking
- **Status**: ✅ Production Ready

#### I18 - [Dependency Resolution Engine](./dependency-resolution-engine.md)
- **Purpose**: Advanced dependency management and conflict resolution
- **Features**: Circular dependency detection, version conflict resolution, compatibility checking
- **Coverage**: Multi-language dependency graphs, constraint satisfaction
- **Status**: ✅ Production Ready

#### I19 - [Package Security Validation](./package-security-validation.md)
- **Purpose**: Comprehensive package security assessment
- **Features**: Vulnerability scanning, license compliance, supply chain validation
- **Coverage**: CVE databases, SAST/DAST integration, security scoring
- **Status**: ✅ Production Ready

#### I20 - [Package Usage Patterns](./package-usage-patterns.md)
- **Purpose**: Language-specific package templates and best practices
- **Features**: Usage examples, anti-pattern detection, best practice templates
- **Coverage**: Common operations, error handling, security patterns
- **Status**: ✅ Production Ready

### 🚫 Anti-Pattern Prevention Framework (I26-I30)

#### I26 - [Anti-Pattern Detection Engine](./anti-pattern-detection-engine.md)
- **Purpose**: Comprehensive real-time detection of software anti-patterns
- **Features**: God object detection, testing theatre identification, hallucinated architecture detection, pattern smell analysis
- **Coverage**: Real-time IDE integration, parallel processing, intelligent pattern recognition
- **Status**: ✅ Production Ready

#### I27 - [Prevention Protocols Framework](./prevention-protocols-framework.md)
- **Purpose**: Proactive prevention of anti-patterns before they occur
- **Features**: Real-time triggers, automatic refactoring suggestions, education/guidance system, enforcement mechanisms
- **Coverage**: Git hook integration, IDE prevention, adaptive learning, quality gate enforcement
- **Status**: ✅ Production Ready

#### I28 - [Code Quality Monitoring](./code-quality-monitoring.md)
- **Purpose**: Continuous tracking and analysis of code quality metrics
- **Features**: Mutation score tracking, test effectiveness monitoring, architecture compliance checks, trend analysis
- **Coverage**: Advanced mutation testing, quality dashboards, performance benchmarking, predictive analytics
- **Status**: ✅ Production Ready

#### I29 - [Remediation Automation](./remediation-automation.md)
- **Purpose**: Automated fixing capabilities with comprehensive safety mechanisms
- **Features**: Automatic refactoring patterns, guided remediation workflows, incremental improvement, rollback safety
- **Coverage**: God object remediation, testing theatre fixes, safe automation, user experience adaptation
- **Status**: ✅ Production Ready

#### I30 - [Framework Integration Hub](./framework-integration-hub.md)
- **Purpose**: Complete system integration connecting all anti-pattern prevention systems
- **Features**: Unified reporting dashboard, cross-module coordination, comprehensive documentation, system health monitoring
- **Coverage**: Event-driven integration, workflow coordination, centralized configuration, performance monitoring
- **Status**: ✅ Production Ready

#### 📋 [Anti-Pattern Prevention Framework Overview](./anti-pattern-prevention-framework-overview.md)
- **Purpose**: Complete framework documentation and integration guide
- **Features**: End-to-end anti-pattern prevention, workflow integration, performance characteristics
- **Coverage**: Complete system architecture, usage examples, success metrics, future enhancements
- **Status**: ✅ Production Ready

## Key Features

### 🔒 Security-First Architecture

#### Defense in Depth
- **Input Validation**: Whitelist-based validation with schema enforcement
- **Authentication & Authorization**: Multi-factor auth with RBAC and audit logging
- **Data Protection**: AES-256-GCM encryption with PII handling and secrets management
- **Security Scanning**: SAST/DAST integration with vulnerability management
- **LLM Security**: Prompt injection prevention with output validation

#### OWASP 2025 Compliance
- **Traditional Web Security**: Complete coverage of OWASP Top 10 2025
- **LLM-Specific Security**: Full implementation of OWASP LLM Top 10
- **Zero Trust Architecture**: Never trust, always verify approach
- **Continuous Monitoring**: Real-time threat detection and incident response

### 🏗️ Architectural Excellence

#### Automated Constraint Enforcement
- **Real-time Monitoring**: Continuous monitoring during development with immediate alerts
- **Pre-commit Validation**: Comprehensive validation before code commits
- **Blocking Enforcement**: Hard limits that prevent constraint violations
- **Intelligent Remediation**: Automatic suggestions and fixes for violations

#### Size and Complexity Constraints
- **Files**: Maximum 500 lines (warning at 300, preferred <200)
- **Classes**: Maximum 15 methods, 200 lines (warning at 10 methods, 150 lines)
- **Methods**: Maximum 25 lines, 5 parameters, complexity 10 (warning at 15 lines)

#### Anti-Pattern Prevention
- **God Object Detection**: Scoring system with automatic refactoring triggers
- **Single Responsibility**: Interface contracts with dependency health monitoring
- **Naming Conventions**: Consistent standards with automated checking

### 📦 Package Verification Excellence

#### Real-Time Package Validation
- **Multi-Ecosystem Coverage**: PyPI, npm, crates.io, Maven Central, RubyGems, Packagist, NuGet
- **Existence Verification**: Real-time API validation against official package repositories
- **Version Validation**: Comprehensive version existence and compatibility checking
- **Fallback Systems**: Intelligent alternatives and typo correction for missing packages

#### LLM Hallucination Prevention
- **API Method Validation**: Comprehensive database of valid API methods for major packages
- **Import Statement Verification**: Syntax and package existence validation for all languages
- **Common Hallucination Detection**: Pattern matching for frequently fabricated APIs
- **Proactive Correction**: Automatic correction of common LLM fabrications

#### Advanced Dependency Management
- **Dependency Graph Analysis**: Complete transitive dependency mapping and validation
- **Circular Dependency Detection**: Advanced algorithms for detecting and resolving dependency cycles
- **Version Conflict Resolution**: Constraint satisfaction solver for complex version requirements
- **Cross-Language Compatibility**: Multi-language project dependency coordination

#### Comprehensive Security Assessment
- **Vulnerability Scanning**: Integration with OSV, Snyk, GitHub Advisory, and npm audit databases
- **License Compliance**: Automated license compatibility checking and policy enforcement
- **Supply Chain Validation**: Package reputation analysis, maintainer trust scoring, typosquatting detection
- **Security Scoring**: Weighted security assessment with risk level determination

#### Intelligent Usage Patterns
- **Language-Specific Templates**: Comprehensive usage examples for major packages in all languages
- **Best Practice Enforcement**: Automatic injection of security, error handling, and performance patterns
- **Anti-Pattern Detection**: Real-time detection and correction of common package usage mistakes
- **Context-Aware Suggestions**: Smart recommendations based on development context

### Integration Points

#### Command Integration
- **/task**: Size-aware single-file development with decomposition triggers, real-time package validation
- **/feature**: Multi-component architectural validation with constraint planning, dependency resolution
- **/swarm**: Distributed constraint enforcement across multiple agents, package security coordination
- **All Commands**: Universal constraint checking with adaptive guidance, comprehensive package verification

#### Quality Gates
1. **Design Validation**: Pre-implementation constraint feasibility checking, package security assessment
2. **Implementation Validation**: Real-time constraint adherence monitoring, package verification
3. **Integration Validation**: Cross-component constraint compliance verification, dependency resolution
4. **Security Validation**: Vulnerability scanning, license compliance checking, supply chain validation

#### Template System
- **Size-aware Templates**: Automatically selected based on estimated implementation size
- **Constraint-embedded Patterns**: Templates with built-in constraint guidance
- **Decomposition Templates**: Automatic splitting for large implementations

## Usage Examples

### Basic Constraint Checking
```markdown
# Automatically triggered during any implementation command
/task "implement user validation service"
# Framework automatically:
# 1. Estimates implementation size against constraints
# 2. Selects appropriate constraint-compliant template
# 3. Monitors implementation with real-time alerts
# 4. Validates final result against all constraints
```

### Package Verification in Action
```markdown
# Real-time package validation during code generation
/task "create REST API client using requests and pandas"
# Framework automatically:
# 1. Validates 'requests' exists in PyPI ✅
# 2. Validates 'pandas' exists in PyPI ✅
# 3. Checks for known vulnerabilities ✅
# 4. Applies secure usage patterns ✅
# 5. Injects proper error handling ✅
# 6. Validates import statements ✅
```

### Hallucination Prevention
```markdown
# LLM attempts to use non-existent method
response = requests.get(url).json_content  # ❌ BLOCKED
# Framework detects hallucination:
# - Method 'json_content' does not exist on Response object
# - Correct usage: response.json()
# - Auto-correction applied ✅
```

### Dependency Conflict Resolution
```markdown
# Complex dependency requirements detected
Package: tensorflow
- Project requires: >=2.8.0
- Another dependency requires: >=2.10.0,<2.12.0
- Framework resolves: tensorflow==2.11.0 ✅
# Circular dependency detected and resolved:
# package-a → package-b → package-c → package-a
# Resolution: Extract common interface pattern
```

### God Object Prevention
```markdown
# Framework detects god object risk automatically
# Scoring: Size(8) + Responsibility(10) + Coupling(7) = 25 (CRITICAL)
# Automatic remediation suggestions:
# - Extract UserValidator class (handles validation logic)
# - Extract UserRepository class (handles data access)
# - Apply Strategy pattern for different validation types
```

### Structure Constraint Enforcement
```markdown
# Single responsibility validation
Class: UserService
Issues detected:
- Mixed concerns: authentication + validation + persistence
- Interface bloat: 12 public methods (limit: 10)
- High coupling: 8 dependencies (limit: 5)

Automatic remediation:
- Extract AuthenticationService
- Extract ValidationService  
- Create UserRepository interface
- Apply dependency injection patterns
```

## Configuration

### Constraint Profiles

#### Strict Profile (Production Code)
- File limit: 200 lines
- Class limit: 8 methods, 150 lines
- Method limit: 20 lines, 4 parameters
- God object threshold: Score >15

#### Standard Profile (Regular Development)
- File limit: 300 lines  
- Class limit: 10 methods, 200 lines
- Method limit: 25 lines, 5 parameters
- God object threshold: Score >20

#### Development Profile (Prototyping)
- File limit: 500 lines (warnings only)
- Class limit: 15 methods, 300 lines
- Method limit: 30 lines, 6 parameters
- God object threshold: Score >25

### Customization Options
- Project-specific constraint adjustments
- Technology stack adaptations
- Domain-specific exemptions
- Emergency override procedures

## Implementation Status

### Completed Components ✅
- [x] Core architectural constraints definition
- [x] God object detection and prevention system
- [x] Module structure constraint framework
- [x] Comprehensive validation engine
- [x] Command integration architecture

### Integration Roadmap

#### Phase 1: Task Command Integration (Immediate)
- Size constraint enforcement for single-file implementations
- Real-time monitoring and decomposition triggers
- Constraint-aware template selection

#### Phase 2: Feature Command Integration (2 weeks)
- Multi-component architectural validation
- Interface contract enforcement
- Cross-component dependency validation

#### Phase 3: Swarm Command Integration (4 weeks)  
- Distributed constraint enforcement
- Agent coordination for consistent standards
- Aggregated validation and reporting

#### Phase 4: Framework-wide Integration (6 weeks)
- Universal constraint enforcement
- Advanced metrics and trend analysis
- Optimization based on usage patterns

## Success Metrics

### Quantitative Goals
- 95% constraint violation detection accuracy
- 90% compliance with size constraints
- 85% compliance with structure constraints
- 95% god object prevention rate
- 99% package hallucination prevention rate
- 100% dependency conflict resolution success
- 95% security vulnerability detection accuracy
- <10% development time overhead

### Qualitative Goals
- Improved code maintainability and readability
- Consistent architectural patterns across codebase
- Enhanced developer understanding of quality practices
- Reduced technical debt accumulation
- Elimination of LLM package hallucinations
- Secure and compliant package usage patterns
- Reliable dependency management across multi-language projects
- Proactive security vulnerability prevention

## Emergency Procedures

### Critical Fix Overrides
- Security vulnerability fixes: Immediate constraint override
- Production outages: Expedited review process
- Data loss prevention: Emergency bypass with documentation
- Post-emergency remediation: Mandatory constraint restoration

### Fallback Mechanisms
- Progressive constraint relaxation under time pressure
- Alternative architecture suggestions for constraint conflicts
- Phased implementation for complex requirements
- Graceful degradation with enhanced compensation (testing, documentation, monitoring)

## Getting Started

### Framework Fundamentals
1. **Review Constraint Definitions**: Start with [architectural-constraints.md](./architectural-constraints.md)
2. **Understand God Object Prevention**: Study [god-object-prevention.md](./god-object-prevention.md)  
3. **Learn Structure Requirements**: Read [module-structure-constraints.md](./module-structure-constraints.md)
4. **Explore Validation Engine**: Examine [constraint-validation-engine.md](./constraint-validation-engine.md)
5. **See Command Integration**: Review [command-constraint-integration.md](./command-constraint-integration.md)

### Package Verification System
6. **Package Management**: Learn [package-whitelist-system.md](./package-whitelist-system.md)
7. **Hallucination Prevention**: Study [hallucination-prevention.md](./hallucination-prevention.md)
8. **Dependency Resolution**: Explore [dependency-resolution-engine.md](./dependency-resolution-engine.md)
9. **Security Validation**: Review [package-security-validation.md](./package-security-validation.md)
10. **Usage Patterns**: Master [package-usage-patterns.md](./package-usage-patterns.md)

## Support and Documentation

- **Framework Documentation**: Complete specification in individual module files
- **Template Library**: Constraint-aware templates for common implementation patterns
- **Best Practices**: Examples and anti-patterns with remediation guidance
- **Troubleshooting**: Common constraint conflicts and resolution strategies

The Architectural Constraints Framework represents a significant advancement in LLM code generation quality, providing the structure and discipline needed for maintainable, scalable software development.