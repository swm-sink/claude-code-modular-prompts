# Security Engineering & Research R&D Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Security Engineering & Research R&D domain template provides specialized framework configuration for building secure systems, conducting security research, and implementing defense-in-depth strategies. This template optimizes the Claude Code Framework for security engineering workflows, threat modeling, and vulnerability research.

## Domain Configuration

```xml
<security_engineering_research_domain>
  <purpose>Advanced security engineering and research for resilient, secure systems</purpose>
  
  <core_capabilities>
    <security_architecture>Zero-trust architecture, defense-in-depth, secure by design</security_architecture>
    <threat_modeling>Systematic threat identification, risk assessment, mitigation strategies</threat_modeling>
    <vulnerability_research>Security research, defensive exploit analysis, vulnerability assessment</vulnerability_research>
    <security_automation>Automated security testing, continuous compliance, DevSecOps</security_automation>
    <incident_response>Security incident handling, forensics, threat hunting</incident_response>
    <ethical_framework>CRITICAL: All security research conducted for DEFENSIVE and EDUCATIONAL purposes only - protecting systems, not attacking them</ethical_framework>
  </core_capabilities>
  
  <security_domains>
    <application_security>SAST, DAST, code review, secure coding practices</application_security>
    <infrastructure_security>Network security, cloud security, container security</infrastructure_security>
    <data_security>Encryption, key management, data loss prevention, privacy</data_security>
    <identity_security>Authentication, authorization, identity management, SSO</identity_security>
  </security_domains>
  
  <rd_characteristics>
    <proactive_security>Threat hunting, vulnerability research, security innovation</proactive_security>
    <defensive_engineering>Secure coding, security testing, hardening practices</defensive_engineering>
    <compliance_automation>Automated compliance monitoring, audit trails, reporting</compliance_automation>
    <threat_intelligence>Threat intelligence integration, IOC analysis, attribution</threat_intelligence>
  </rd_characteristics>
</security_engineering_research_domain>
```

## Quality Gates

```xml
<quality_gates>
  <security_standards>
    <vulnerability_management>Zero high-severity vulnerabilities in production</vulnerability_management>
    <penetration_testing>Regular penetration testing and vulnerability assessments</penetration_testing>
    <code_security>Static and dynamic security testing with < 0.1% false positives</code_security>
    <compliance_validation>100% compliance with applicable security standards</compliance_validation>
    <incident_response>Mean time to detection < 5 minutes, containment < 1 hour</incident_response>
  </security_standards>
  
  <secure_development>
    <threat_modeling>Comprehensive threat modeling for all new features</threat_modeling>
    <security_testing>Automated security testing in CI/CD pipeline</security_testing>
    <secure_coding>Secure coding standards and peer review</secure_coding>
    <dependency_scanning>Automated dependency vulnerability scanning</dependency_scanning>
    <secrets_management>No hardcoded secrets, proper secret rotation</secrets_management>
  </secure_development>
</quality_gates>
```

**Usage**: Apply this template for security engineering projects focused on building secure systems, conducting security research, and implementing comprehensive security programs. Optimized for security engineers working on threat modeling, vulnerability assessment, and defensive security measures.