---
name: /protocol
description: Advanced protocol-driven development with AI safety frameworks and automated compliance (v1.0)
version: "1.0"
usage: '/protocol [task] [--safety-level low|medium|high|critical] [--compliance standards]'
category: development
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
- WebSearch
dependencies:
- /security
- /test
- /quality
validation:
  pre-execution: "Safety assessment and risk evaluation"
  during-execution: "Continuous compliance monitoring and quality gates"
  post-execution: "Comprehensive audit trail and approval verification"
interactive-consultation:
  layer-integration: "Phase 1: Basic safety checks, Phase 2: Full compliance frameworks, Phase 3: Enterprise governance"
  options:
    - name: standard
      description: "Standard safety protocols for general development"
    - name: regulated
      description: "Compliance frameworks for regulated industries"
    - name: critical
      description: "Mission-critical systems with full governance"
safety-checks:
  - "Constitutional AI alignment verification"
  - "Ethical impact assessment"
  - "Security vulnerability scanning"
  - "Compliance requirement validation"
error-recovery:
  - "Automatic rollback on safety violations"
  - "Incident response procedures"
  - "Root cause analysis documentation"
performance:
  - "Parallel safety validation"
  - "Incremental compliance checking"
  - "Cached approval workflows"
ai-safety:
  - "Harm prevention protocols"
  - "Bias detection and mitigation"
  - "Transparency requirements"
  - "Human oversight integration"
---

# Protocol-Driven Development (v1.0)

Advanced protocol-driven development with AI safety frameworks, automated compliance validation, and enterprise governance integration.

## 🚀 Interactive Consultation Phases

### Phase 1: Standard Safety Protocols (2 minutes)
```bash
/protocol "implement user feature"              # Auto-detect safety requirements
/protocol "database migration" --safety medium  # Specify safety level
```

### Phase 2: Compliance Frameworks (10 minutes)
```bash
/protocol "payment processing" --compliance PCI-DSS
/protocol "health records" --compliance HIPAA --safety high
```

### Phase 3: Enterprise Governance (30+ minutes)
```bash
/protocol "financial system" --governance SOX --approval-chain
/protocol "ai model deployment" --safety critical --ethics-review
```

## 🛡️ Safety-First Development

### Constitutional AI Principles
Every protocol implementation follows core safety principles:

1. **Harmlessness**: Prevent harmful outputs or behaviors
2. **Helpfulness**: Maximize beneficial outcomes
3. **Honesty**: Transparent about capabilities and limitations
4. **Humility**: Acknowledge uncertainty and seek clarification

### Safety Assessment Matrix
```yaml
safety_levels:
  low:
    - Basic input validation
    - Standard error handling
    - Activity logging
    
  medium:
    - Comprehensive validation
    - Rollback capabilities
    - Audit trails
    - Peer review required
    
  high:
    - Formal verification
    - Security scanning
    - Compliance validation
    - Multi-stage approval
    
  critical:
    - Full governance board review
    - External audit required
    - Disaster recovery plans
    - Legal compliance verification
```

## 🔍 Protocol Selection Framework

### Automatic Protocol Detection
The system analyzes your task to recommend appropriate protocols:

```python
protocol_analysis = {
    "task": "payment processing system",
    "detected_requirements": [
        "Financial data handling → PCI-DSS",
        "Personal information → GDPR",
        "High availability → SLA protocols",
        "Audit requirements → SOX compliance"
    ],
    "recommended_safety": "high",
    "required_approvals": ["security_team", "compliance_officer"]
}
```

### Available Protocol Frameworks

#### Security Protocols
- **OWASP**: Web application security
- **NIST**: Cybersecurity framework
- **ISO 27001**: Information security
- **Zero Trust**: Network security

#### Compliance Protocols
- **GDPR**: Data protection
- **HIPAA**: Healthcare privacy
- **PCI-DSS**: Payment card security
- **SOX**: Financial reporting

#### Development Protocols
- **TDD**: Test-driven development
- **DDD**: Domain-driven design
- **Clean Architecture**: Separation of concerns
- **SOLID**: Object-oriented principles

## 📋 Validation Pipeline

### Multi-Stage Validation
```bash
/protocol "critical feature" --validation-stages
```

**Stage 1: Pre-Development**
- Risk assessment
- Compliance requirements gathering
- Architecture review
- Security threat modeling

**Stage 2: During Development**
- Continuous integration checks
- Security scanning (SAST/DAST)
- Code quality gates
- Peer review checkpoints

**Stage 3: Pre-Deployment**
- Penetration testing
- Load testing
- Compliance audit
- Approval workflow

**Stage 4: Post-Deployment**
- Monitoring setup
- Incident response plan
- Performance baselines
- Continuous compliance

## 🚦 Quality Gates

### Automated Quality Checkpoints
```yaml
quality_gates:
  code_quality:
    - Coverage: ≥ 80%
    - Complexity: < 10
    - Duplication: < 3%
    - Security: A rating
    
  performance:
    - Response time: < 200ms
    - Error rate: < 0.1%
    - Availability: ≥ 99.9%
    
  compliance:
    - All tests passing
    - Security scan clean
    - Documentation complete
    - Approvals obtained
```

### Manual Review Gates
- Architecture review board
- Security team approval
- Compliance officer sign-off
- Business stakeholder acceptance

## 🔒 Risk Mitigation Strategies

### Automated Risk Detection
```bash
/protocol analyze-risks "new feature implementation"
```

**Risk Categories:**
- **Technical**: Performance, scalability, reliability
- **Security**: Vulnerabilities, access control, data protection
- **Compliance**: Regulatory requirements, audit trails
- **Business**: User impact, financial exposure, reputation

### Mitigation Playbooks
```python
mitigation_strategies = {
    "high_security_risk": [
        "Implement additional authentication layers",
        "Add encryption at rest and in transit",
        "Enable comprehensive audit logging",
        "Schedule penetration testing"
    ],
    "compliance_gap": [
        "Document data flows",
        "Implement retention policies",
        "Add consent management",
        "Create audit reports"
    ]
}
```

## 📊 Audit & Documentation

### Comprehensive Audit Trails
Every protocol execution maintains:
- Decision history with rationale
- Configuration changes
- Approval chains
- Test results
- Compliance evidence

### Auto-Generated Documentation
```bash
/protocol generate-docs "project-name"
```
Produces:
- Architecture decision records (ADRs)
- Security assessment reports
- Compliance matrices
- Risk registers
- Runbooks

## 🎯 Quick Start Examples

### Basic Development
```bash
/protocol "add user profile feature"
# → Standard safety, basic validation
```

### Regulated Industry
```bash
/protocol "medical records system" --compliance HIPAA --safety high
# → Full HIPAA compliance, audit trails, encryption
```

### Financial Services
```bash
/protocol "trading platform" --governance SOX --safety critical
# → SOX compliance, disaster recovery, legal review
```

### AI/ML Systems
```bash
/protocol "recommendation engine" --ethics-review --bias-testing
# → Fairness testing, explainability, human oversight
```

## 🔄 Integration with Development Workflow

### CI/CD Pipeline Integration
```yaml
# .protocol-ci.yml
stages:
  - safety-check
  - compliance-scan
  - quality-gates
  - approval-workflow
  - deployment-validation
```

### IDE Integration
- Real-time safety hints
- Compliance checklist
- Automated documentation
- Approval status tracking

---

Ready to implement protocol-driven development? Start with:
- 🛡️ **Safety First**: Let the system detect requirements
- 📋 **Compliance Ready**: Add industry standards
- 🏢 **Enterprise**: Full governance integration