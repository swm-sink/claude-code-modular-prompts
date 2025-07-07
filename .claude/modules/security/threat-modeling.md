| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Threat Modeling Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="threat_modeling" category="security">
  
  <purpose>
    Systematic threat identification using STRIDE methodology with DREAD risk assessment and regulatory compliance integration.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Security architecture design, compliance requirements, vulnerability assessments</condition>
    <condition type="explicit">User requests threat analysis, security modeling, or compliance threat assessment</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="attack_surface_mapping" order="1">
      <requirements>
        System components and data flows identified comprehensively
        Trust boundaries defined with security implications
        Entry points cataloged with vulnerability assessment
      </requirements>
      <actions>
        Map entry points: APIs, web endpoints, file uploads, authentication mechanisms
        Define trust boundaries: internet-DMZ, DMZ-internal, service-to-service
        Catalog assets: user data, financial data, credentials, business logic
        Document data flows and identify security control points
      </actions>
      <validation>
        Attack surface completely mapped with all entry points identified
        Trust boundaries clearly defined with security implications
        Asset catalog complete with sensitivity classifications
      </validation>
    </phase>
    
    <phase name="stride_analysis" order="2">
      <requirements>
        STRIDE methodology applied systematically to all components
        Risk assessment completed using DREAD scoring framework
        Mitigations mapped to identified threats with implementation priorities
      </requirements>
      <actions>
        Apply STRIDE analysis: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
        Score threats using DREAD: Damage, Reproducibility, Exploitability, Affected Users, Discoverability
        Map threats to mitigations: preventive, detective, responsive controls
        Prioritize implementations based on risk scores and business impact
      </actions>
      <validation>
        All STRIDE categories analyzed for each system component
        DREAD scores calculated with documented rationale
        Mitigations selected and prioritized based on risk assessment
      </validation>
    </phase>
    
    <phase name="regulatory_integration" order="3">
      <requirements>
        Compliance frameworks mapped to threat categories
        Regulatory controls integrated with technical mitigations
        Audit requirements documented for compliance verification
      </requirements>
      <actions>
        Integrate PCI DSS requirements for payment data protection
        Apply SOX controls for financial reporting system threats
        Implement GDPR privacy protection threat mitigations
        Document compliance mappings for audit requirements
      </actions>
      <validation>
        Regulatory requirements fully integrated with threat model
        Compliance controls mapped to specific threats and mitigations
        Audit trail established for regulatory verification
      </validation>
    </phase>
    
  </implementation>
  
  <stride_framework>
    <spoofing>
      <threats>Identity impersonation, credential theft, session hijacking</threats>
      <mitigations>Multi-factor authentication, certificate-based auth, secure session management</mitigations>
    </spoofing>
    <tampering>
      <threats>Data modification, SQL injection, XSS, parameter tampering</threats>
      <mitigations>Input validation, parameterized queries, data integrity checks, code signing</mitigations>
    </tampering>
    <repudiation>
      <threats>Denying actions, transaction disputes, unauthorized access claims</threats>
      <mitigations>Non-repudiable audit trails, digital signatures, immutable logging</mitigations>
    </repudiation>
    <information_disclosure>
      <threats>Data exposure, memory dumps, error leakage, side-channel attacks</threats>
      <mitigations>Encryption at rest/transit, access controls, secure error handling</mitigations>
    </information_disclosure>
    <denial_of_service>
      <threats>Resource exhaustion, DDoS, logic bombs, resource locks</threats>
      <mitigations>Rate limiting, resource quotas, circuit breakers, load balancing</mitigations>
    </denial_of_service>
    <elevation_of_privilege>
      <threats>Privilege escalation, buffer overflows, configuration vulnerabilities</threats>
      <mitigations>Least privilege principle, RBAC, privilege reviews, secure coding</mitigations>
    </elevation_of_privilege>
  </stride_framework>
  
  <defense_in_depth>
    <perimeter_defense>Firewalls, IPS, DDoS protection, WAF</perimeter_defense>
    <network_security>Segmentation, zero trust, VPN, traffic monitoring</network_security>
    <endpoint_security>Antivirus, host IDS, device management, application whitelisting</endpoint_security>
    <application_security>Secure coding, code review, penetration testing, dependency scanning</application_security>
    <data_security>Encryption at rest/transit, DLP, backup security</data_security>
  </defense_in_depth>
  
  <regulatory_frameworks>
    <pci_dss>
      <scope>Payment card data processing systems</scope>
      <threats>Data exposure, unauthorized processing, weak authentication, insufficient monitoring</threats>
      <controls>Encryption, network segmentation, security testing, comprehensive logging</controls>
    </pci_dss>
    <sox>
      <scope>Financial reporting controls</scope>
      <threats>Data manipulation, unauthorized access, inadequate audit trails, segregation failures</threats>
      <controls>Access controls, change management, audit trails, internal assessments</controls>
    </sox>
    <gdpr>
      <scope>Personal data protection</scope>
      <threats>Unauthorized access, breach notifications, consent violations, transfer risks</threats>
      <controls>Data minimization, consent management, subject rights, privacy assessments</controls>
    </gdpr>
  </regulatory_frameworks>
  
  <session_integration>
    <mandatory_creation>
      Complex threat modeling requiring architectural analysis
      Multi-system security assessment with regulatory requirements
      Enterprise security implementations requiring audit trails
    </mandatory_creation>
    <session_documentation>
      Attack surface mapping with component and data flow analysis
      STRIDE analysis results with DREAD risk scoring
      Mitigation strategy with implementation priorities and timelines
      Regulatory compliance mapping with audit requirements
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      security/financial-compliance.md for regulatory threat frameworks
      quality/critical-thinking.md for rigorous threat analysis methodology
      patterns/session-management.md for complex security project tracking
    </depends_on>
    <provides_to>
      security/audit.md for threat-based security scanning priorities
      quality/production-standards.md for security control integration
      quality/production-standards.md for enterprise security requirements
    </provides_to>
  </integration_points>
  
</module>
```