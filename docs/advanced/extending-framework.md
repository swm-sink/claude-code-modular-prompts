# Extending Framework - Custom Development

> **Prerequisites**: Understanding of [Framework Architecture](framework-architecture.md) and experience with advanced configuration.

This guide covers developing custom modules, commands, and extensions for the Claude Code Framework.

## 🧩 Module Development

### Creating Custom Modules

**Module Template Structure**:
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-12   | stable |

# Custom Module Name - Purpose Statement

> **Purpose**: Clear description of what this module does and when to use it.

## Interface Contract

**Input Requirements**:
- Parameter 1: Description and validation rules
- Parameter 2: Expected format and constraints
- Context: Required environmental context

**Output Guarantees**:
- Primary Output: What this module produces
- Side Effects: Any secondary effects or modifications
- Error Conditions: Failure modes and handling

**Dependencies**:
- Required Modules: Other modules this depends on
- External Tools: Required external dependencies
- Quality Gates: Validation requirements

## Module Implementation

### Core Logic
<!-- Primary module functionality -->

### Error Handling
<!-- How this module handles and recovers from errors -->

### Quality Validation
<!-- Built-in quality checks and validation -->

### Integration Points
<!-- How this module connects with others -->

## Usage Examples

### Basic Usage
<!-- Simple examples of using this module -->

### Advanced Patterns
<!-- Complex scenarios and edge cases -->

### Common Integrations
<!-- How this module works with other framework components -->

## Testing and Validation

### Unit Tests
<!-- Module-specific testing requirements -->

### Integration Tests
<!-- Testing with other modules and framework components -->

### Performance Tests
<!-- Performance characteristics and benchmarks -->

## Documentation and Maintenance

### API Documentation
<!-- Complete interface documentation -->

### Maintenance Notes
<!-- Known issues, limitations, and future improvements -->

### Version History
<!-- Change log and migration notes -->
```

### Domain-Specific Module Example

**Example: Custom Payment Processing Module**
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 1.2.0   | 2025-07-12   | stable |

# Payment Processing Module - Secure Financial Transactions

> **Purpose**: Implement PCI-compliant payment processing with multiple gateway support and comprehensive security validation.

## Interface Contract

**Input Requirements**:
- Payment Method: credit_card, paypal, stripe, square
- Transaction Type: charge, refund, subscription, preauth
- Security Level: standard, high_security, pci_compliant
- Integration Pattern: direct, hosted, tokenized

**Output Guarantees**:
- Secure implementation with encryption and tokenization
- PCI DSS compliance validation
- Comprehensive error handling and recovery
- Audit logging and transaction tracking
- Test coverage >95% with security test scenarios

**Dependencies**:
- security/threat-modeling.md (threat analysis)
- quality/tdd.md (test-driven development)
- patterns/error-handling.md (robust error recovery)
- compliance/pci-dss.md (PCI compliance validation)

## Module Implementation

### Core Payment Logic
```typescript
// Example implementation patterns for payment processing
interface PaymentConfig {
  gateway: 'stripe' | 'paypal' | 'square';
  environment: 'sandbox' | 'production';
  security_level: 'standard' | 'high_security' | 'pci_compliant';
}

interface PaymentResult {
  transaction_id: string;
  status: 'success' | 'failed' | 'pending';
  security_audit: SecurityAuditResult;
  compliance_check: ComplianceResult;
}
```

### Security Implementation
- **Tokenization**: Never store raw payment data
- **Encryption**: AES-256 for data at rest, TLS 1.3 for transit
- **Validation**: CVV, address verification, fraud detection
- **Audit Logging**: Complete transaction audit trail

### Error Handling
- **Gateway Failures**: Automatic retry with exponential backoff
- **Validation Errors**: Clear user feedback with security considerations
- **Security Violations**: Immediate alert and transaction blocking
- **Compliance Issues**: Automatic remediation or escalation

### Quality Validation
- **Security Testing**: Penetration testing and vulnerability scanning
- **Compliance Validation**: Automated PCI DSS compliance checking
- **Performance Testing**: Load testing under financial transaction volumes
- **Integration Testing**: Multi-gateway testing and failover scenarios

## Usage Examples

### Basic Credit Card Processing
```bash
/task "implement credit card payment with Stripe integration"
# → Uses this module to create PCI-compliant implementation
# → Includes tokenization, validation, and error handling
# → Generates comprehensive test suite
```

### Multi-Gateway Implementation
```bash
/feature "payment system with multiple gateway support"
# → Uses this module for architecture and security patterns
# → Implements failover and routing logic
# → Ensures consistent security across all gateways
```

### High-Security Financial Application
```bash
/protocol "implement payment processing for banking application"
# → Uses maximum security patterns from this module
# → Includes additional compliance frameworks
# → Implements advanced fraud detection
```

## Testing and Validation

### Security Test Requirements
- Penetration testing for common payment vulnerabilities
- OWASP Top 10 validation for financial applications
- PCI DSS compliance automated testing
- Encryption and tokenization validation

### Performance Requirements
- <100ms response time for payment validation
- >99.9% uptime for payment processing
- Horizontal scaling support for high transaction volumes
- Graceful degradation during peak loads

### Compliance Validation
- Automated PCI DSS compliance checking
- SOX compliance for financial reporting
- GDPR compliance for European customers
- Industry-specific regulatory compliance

## Integration with Framework Commands

### Command Integration Patterns
```xml
<!-- How commands use this module -->
<command name="/task">
  <payment_patterns>
    <simple>basic credit card processing</simple>
    <intermediate>multi-gateway with validation</intermediate>
    <advanced>enterprise payment architecture</advanced>
  </payment_patterns>
</command>

<command name="/feature">
  <payment_features>
    <subscription>recurring payment management</subscription>
    <marketplace>multi-vendor payment splitting</marketplace>
    <international>multi-currency and localization</international>
  </payment_features>
</command>

<command name="/protocol">
  <security_levels>
    <banking>maximum security with comprehensive auditing</banking>
    <fintech>PCI compliance with fraud detection</fintech>
    <ecommerce>standard security with performance optimization</ecommerce>
  </security_levels>
</command>
```

## Module Configuration

### PROJECT_CONFIG.xml Integration
```xml
<domain_extensions>
  <payment_processing>
    <primary_gateway>stripe</primary_gateway>
    <backup_gateways>paypal,square</backup_gateways>
    <security_level>pci_compliant</security_level>
    <compliance_frameworks>PCI-DSS,SOX</compliance_frameworks>
    <fraud_detection>enabled</fraud_detection>
    <audit_logging>comprehensive</audit_logging>
  </payment_processing>
</domain_extensions>
```

### Dynamic Configuration
```xml
<payment_rules>
  <rule condition="transaction_amount>$1000">
    <additional_verification>required</additional_verification>
    <security_level>high_security</security_level>
  </rule>
  <rule condition="international_transaction=true">
    <compliance_check>enhanced</compliance_check>
    <fraud_monitoring>increased</fraud_monitoring>
  </rule>
</payment_rules>
```
```

## 🎯 Command Development

### Custom Command Creation

**Command Structure Template**:
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-12   | stable |

# Custom Command - /custom-command

> **Purpose**: Specific workflow orchestration for [domain/use case]

## Command Interface

**Syntax**: `/custom-command "description of task"`

**Parameters**:
- Required: task description
- Optional: scope, complexity level, quality requirements

**Scope**: [single-file|multi-component|system-wide]
**Quality Level**: [standard|enhanced|maximum]

## Thinking Pattern

### Checkpoint 1: Analysis and Understanding
```xml
<thinking_checkpoint name="analysis">
  <purpose>Understand the request and current context</purpose>
  <validation>
    <check>Request clarity and feasibility</check>
    <check>Current codebase context</check>
    <check>Dependencies and constraints</check>
  </validation>
  <next_step>Planning and approach selection</next_step>
</thinking_checkpoint>
```

### Checkpoint 2: Planning and Strategy
```xml
<thinking_checkpoint name="planning">
  <purpose>Develop implementation strategy</purpose>
  <validation>
    <check>Approach alignment with requirements</check>
    <check>Resource and time estimates</check>
    <check>Risk assessment and mitigation</check>
  </validation>
  <next_step>Module selection and orchestration</next_step>
</thinking_checkpoint>
```

### Checkpoint 3: Execution and Validation
```xml
<thinking_checkpoint name="execution">
  <purpose>Execute plan with quality validation</purpose>
  <validation>
    <check>Implementation quality and correctness</check>
    <check>Test coverage and validation</check>
    <check>Integration and compatibility</check>
  </validation>
  <next_step>Documentation and completion</next_step>
</thinking_checkpoint>
```

## Module Orchestration

### Core Modules (Always Required)
- **Critical Thinking**: patterns/critical-thinking.md
- **Quality Gates**: quality/universal-quality-gates.md
- **TDD Enforcement**: quality/tdd.md

### Contextual Modules (Based on Request)
- **Domain Specific**: domain/[detected-domain]/*.md
- **Technology Stack**: patterns/[tech-stack]-patterns.md
- **Security**: security/threat-modeling.md (if security relevant)

### Support Modules (As Needed)
- **Error Handling**: patterns/error-recovery.md
- **Performance**: patterns/performance-optimization.md
- **Documentation**: development/documentation/*.md

## Implementation Workflow

### Phase 1: Request Analysis
1. Parse and validate command parameters
2. Analyze current project context and constraints
3. Determine complexity and scope requirements
4. Select appropriate quality gate level

### Phase 2: Module Selection and Loading
1. Load core modules (critical thinking, quality gates, TDD)
2. Determine and load contextual modules based on request
3. Load support modules based on complexity and requirements
4. Validate module dependencies and compatibility

### Phase 3: Execution Orchestration
1. Execute thinking pattern checkpoints in sequence
2. Coordinate module interactions and data flow
3. Apply quality gates at each execution boundary
4. Handle errors and edge cases with appropriate recovery

### Phase 4: Validation and Completion
1. Validate outputs against quality requirements
2. Generate documentation and update project context
3. Provide completion summary and next steps
4. Update framework learning and optimization data

## Quality Gate Integration

### Standard Quality Gates
- **TDD Compliance**: RED→GREEN→REFACTOR mandatory
- **Test Coverage**: Minimum threshold from PROJECT_CONFIG.xml
- **Security Validation**: Threat modeling for security-relevant changes
- **Performance Standards**: Response time and resource usage validation

### Custom Quality Gates
<!-- Domain-specific quality requirements -->

### Error Recovery Procedures
<!-- How this command handles and recovers from failures -->

## Example Usage

### Basic Usage
```bash
/custom-command "implement user authentication with OAuth"
```

### Advanced Usage with Parameters
```bash
/custom-command "complex multi-service integration" --scope=system-wide --quality=maximum
```

### Integration with Other Commands
```bash
# Research phase
/query "analyze current authentication patterns"
# Implementation phase
/custom-command "modernize authentication system"
# Documentation phase
/docs "update authentication documentation"
```

## Performance and Optimization

### Execution Time Targets
- Simple requests: <30 seconds
- Medium complexity: <2 minutes
- Complex requests: <5 minutes

### Resource Utilization
- Context window: Efficient module loading and composition
- Memory usage: Optimal for concurrent execution
- Parallel execution: Where possible for performance

### Caching and Optimization
- Module caching for repeated operations
- Context preservation for related requests
- Pattern learning for improved future performance
```

### Integration with Framework Architecture

**Command Registration**:
```xml
<!-- Add to .claude/commands/ directory structure -->
<commands location=".claude/commands/" delegate_only="true">
  <cmd name="/custom-command" module="custom/custom-workflow.md"/>
</commands>
```

**Module Runtime Integration**:
```xml
<!-- Integration with module runtime engine -->
<module_runtime_integration>
  <loading_priority>high</loading_priority>
  <dependency_resolution>automatic</dependency_resolution>
  <quality_gate_enforcement>standard</quality_gate_enforcement>
</module_runtime_integration>
```

## 🔧 Framework Extension Patterns

### Plugin Architecture

**Plugin Interface**:
```typescript
interface FrameworkPlugin {
  name: string;
  version: string;
  description: string;
  
  // Lifecycle hooks
  initialize(context: FrameworkContext): Promise<void>;
  beforeCommand(command: Command, context: Context): Promise<void>;
  afterCommand(result: CommandResult, context: Context): Promise<void>;
  cleanup(): Promise<void>;
  
  // Extension points
  customCommands?: CustomCommand[];
  customModules?: CustomModule[];
  qualityGates?: QualityGate[];
  integrations?: ExternalIntegration[];
}
```

**Plugin Registration**:
```xml
<plugins>
  <plugin name="company-standards">
    <location>plugins/company-standards/</location>
    <version>1.0.0</version>
    <enabled>true</enabled>
    <config>
      <company_style_guide>enabled</company_style_guide>
      <proprietary_tools>enabled</proprietary_tools>
    </config>
  </plugin>
</plugins>
```

### Custom Quality Gates

**Quality Gate Development**:
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-12   | stable |

# Custom Quality Gate - Accessibility Compliance

> **Purpose**: Ensure WCAG 2.1 AA compliance for all UI components

## Gate Interface

**Trigger Conditions**:
- UI component creation or modification
- Frontend code changes in /src/components/
- Style or CSS modifications

**Validation Criteria**:
- WCAG 2.1 AA compliance score >90%
- Color contrast ratio >4.5:1
- Keyboard navigation support
- Screen reader compatibility
- Focus management implementation

**Tools Integration**:
- axe-core for automated accessibility testing
- Lighthouse accessibility audit
- Manual testing checklist for complex interactions

## Implementation

### Automated Testing
```typescript
// Example accessibility testing integration
interface AccessibilityResult {
  wcag_score: number;
  contrast_issues: ContrastIssue[];
  keyboard_issues: KeyboardIssue[];
  screen_reader_issues: ScreenReaderIssue[];
  compliance_level: 'A' | 'AA' | 'AAA' | 'fail';
}
```

### Manual Validation Checklist
- [ ] Keyboard navigation works without mouse
- [ ] Focus indicators are visible and logical
- [ ] Screen reader announces content correctly
- [ ] Color is not the only way to convey information
- [ ] Text alternatives provided for images
- [ ] Form labels are properly associated

### Integration with Commands
```xml
<quality_gate name="accessibility_compliance">
  <triggers>
    <file_pattern>src/components/**/*.{tsx,jsx,vue}</file_pattern>
    <file_pattern>src/styles/**/*.{css,scss,less}</file_pattern>
  </triggers>
  <enforcement>BLOCKING</enforcement>
  <tools>
    <tool name="axe-core" required="true" />
    <tool name="lighthouse" required="true" />
  </tools>
</quality_gate>
```
```

### External Tool Integration

**Integration Pattern**:
```typescript
interface ExternalToolIntegration {
  name: string;
  version: string;
  
  // Connection management
  connect(config: ToolConfig): Promise<Connection>;
  disconnect(): Promise<void>;
  healthCheck(): Promise<HealthStatus>;
  
  // Data synchronization
  syncData(data: FrameworkData): Promise<SyncResult>;
  fetchUpdates(): Promise<Update[]>;
  
  // Event handling
  onFrameworkEvent(event: FrameworkEvent): Promise<void>;
  onToolEvent(event: ToolEvent): Promise<FrameworkEvent[]>;
}
```

**Example: JIRA Integration**:
```xml
<external_integration name="jira">
  <connection>
    <url>https://company.atlassian.net</url>
    <authentication>oauth2</authentication>
    <project_key>PROJ</project_key>
  </connection>
  
  <sync_rules>
    <framework_to_jira>
      <swarm_command>creates_epic</swarm_command>
      <session_command>creates_story</session_command>
      <task_command>creates_task</task_command>
    </framework_to_jira>
    
    <jira_to_framework>
      <epic_update>updates_session_context</epic_update>
      <story_completion>triggers_documentation_update</story_completion>
    </jira_to_framework>
  </sync_rules>
</external_integration>
```

## 🚀 Advanced Extension Examples

### AI-Enhanced Code Review Module

```markdown
# AI Code Review Enhancement Module

> **Purpose**: Provide intelligent code review suggestions using multiple AI models

## AI Integration Architecture

### Multi-Model Analysis
- **Code Quality**: GPT-4 for comprehensive code analysis
- **Security**: Specialized security-focused models
- **Performance**: Performance optimization models
- **Architecture**: System design and pattern analysis

### Learning and Adaptation
- Learn from accepted/rejected suggestions
- Adapt to team coding standards and preferences
- Improve accuracy based on project-specific patterns

### Integration Points
```xml
<ai_code_review>
  <triggers>
    <git_commit>enabled</git_commit>
    <pull_request>enabled</pull_request>
    <framework_command>task,feature</framework_command>
  </triggers>
  
  <analysis_types>
    <code_quality>enabled</code_quality>
    <security_analysis>enabled</security_analysis>
    <performance_review>enabled</performance_review>
    <architecture_feedback>enabled</architecture_feedback>
  </analysis_types>
  
  <learning_features>
    <suggestion_tracking>enabled</suggestion_tracking>
    <team_preference_learning>enabled</team_preference_learning>
    <pattern_recognition>enabled</pattern_recognition>
  </learning_features>
</ai_code_review>
```

### Predictive Development Assistant

```markdown
# Predictive Development Assistant Module

> **Purpose**: Anticipate development needs and proactively suggest optimizations

## Predictive Capabilities

### Pattern Recognition
- Analyze development patterns and predict next likely actions
- Suggest relevant modules and tools before explicitly requested
- Identify potential issues before they become problems

### Proactive Suggestions
- Recommend refactoring opportunities based on code evolution
- Suggest testing strategies based on code complexity
- Predict performance issues based on architectural patterns

### Integration Example
```bash
# User starts working on authentication
/task "update user login form"

# Assistant proactively suggests:
# "Based on your recent authentication work, consider:"
# 1. Adding 2FA support (detected missing security feature)
# 2. Implementing session management improvements (detected pattern)
# 3. Updating related test cases (detected testing gaps)
```

## 🧪 Testing Framework Extensions

### Extension Testing Strategy

**Module Testing**:
```bash
# Test individual modules
python scripts/testing/test_module.py --module custom/payment-processing.md

# Test module integration
python scripts/testing/test_integration.py --modules security,payment,quality

# Performance testing
python scripts/testing/performance_test.py --module custom/payment-processing.md
```

**Command Testing**:
```bash
# Test custom commands
python scripts/testing/test_command.py --command custom-command

# Test command orchestration
python scripts/testing/test_orchestration.py --workflow custom_workflow

# Load testing
python scripts/testing/load_test.py --command custom-command --iterations 100
```

### Validation Framework

**Extension Validation Checklist**:
- [ ] **Interface Compliance**: Follows framework interface standards
- [ ] **Quality Gate Integration**: Proper quality gate implementation
- [ ] **Error Handling**: Robust error handling and recovery
- [ ] **Performance**: Meets performance requirements
- [ ] **Documentation**: Complete documentation and examples
- [ ] **Testing**: Comprehensive test coverage
- [ ] **Security**: Security review and validation
- [ ] **Compatibility**: Works with existing framework components

## 📚 Extension Documentation

### Documentation Requirements

**API Documentation**:
- Complete interface specification
- Usage examples and patterns
- Integration guidelines
- Performance characteristics

**User Documentation**:
- Getting started guide
- Configuration options
- Troubleshooting guide
- Best practices

**Developer Documentation**:
- Architecture overview
- Extension points
- Testing strategies
- Contribution guidelines

### Documentation Templates

Available templates for extension documentation:
- `templates/module-documentation.md`
- `templates/command-documentation.md`
- `templates/plugin-documentation.md`
- `templates/integration-documentation.md`

## ✅ Extension Development Checklist

### Planning Phase
- [ ] **Requirements Analysis**: Clear understanding of extension purpose
- [ ] **Architecture Design**: Integration points and dependencies identified
- [ ] **Interface Design**: Clean, consistent interface specification
- [ ] **Quality Requirements**: Performance and reliability standards defined

### Development Phase
- [ ] **Core Implementation**: Main functionality implemented and tested
- [ ] **Quality Gates**: Appropriate validation and error handling
- [ ] **Integration**: Proper framework integration and orchestration
- [ ] **Testing**: Comprehensive test coverage and validation

### Release Phase
- [ ] **Documentation**: Complete user and developer documentation
- [ ] **Performance Validation**: Performance requirements met
- [ ] **Security Review**: Security implications assessed and addressed
- [ ] **Compatibility Testing**: Works with framework versions and configurations

### Maintenance Phase
- [ ] **Monitoring**: Performance and usage monitoring implemented
- [ ] **Feedback Integration**: User feedback collection and response
- [ ] **Continuous Improvement**: Regular updates and optimizations
- [ ] **Version Management**: Proper versioning and migration support

---

**Ready to build?** Start with [Contributing Guide](contributing.md) for development environment setup.

**Need inspiration?** Check existing modules in `.claude/modules/` for implementation patterns.