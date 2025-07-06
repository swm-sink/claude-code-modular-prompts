<module name="financial_compliance" category="security">
  
  <purpose>
    Implement financial-grade security controls for PCI DSS, SOX, GDPR, and banking compliance with comprehensive audit documentation.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Payment processing, financial data handling, regulatory compliance requirements</condition>
    <condition type="explicit">User requests financial compliance implementation or regulatory security standards</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="compliance_framework_selection" order="1">
      <requirements>
        Applicable regulations identified based on business operations
        Compliance requirements mapped to technical controls
        Session created for mandatory audit trail tracking
      </requirements>
      <actions>
        Identify applicable frameworks: PCI DSS, SOX, GDPR, HIPAA, banking regulations
        Map regulatory requirements to technical implementation controls
        Create compliance tracking session with audit capabilities
        Establish baseline compliance posture assessment
      </actions>
      <validation>
        All applicable regulatory frameworks identified and documented
        Compliance requirements mapped to specific technical controls
        Session tracking established for complete audit trail
      </validation>
    </phase>
    
    <phase name="security_controls_implementation" order="2">
      <requirements>
        Multi-layer encryption implemented for financial data protection
        Access controls enforced with role-based authentication
        Audit trails established with immutable logging
      </requirements>
      <actions>
        Implement AES-256 encryption at rest and TLS 1.3+ in transit
        Deploy HSM-based key management with 90-day rotation cycles
        Establish role-based access control with principle of least privilege
        Create immutable audit trails with blockchain-based logging
      </actions>
      <validation>
        Encryption verified for all financial data storage and transmission
        Access controls tested and documented with compliance evidence
        Audit trails operational with tamper-evident storage
      </validation>
    </phase>
    
    <phase name="compliance_validation" order="3">
      <requirements>
        Compliance scanning completed with zero critical violations
        External auditor verification for regulatory requirements
        Comprehensive documentation package prepared for regulatory review
      </requirements>
      <actions>
        Execute automated compliance scanning for all applicable frameworks
        Coordinate external auditor validation of implemented controls
        Generate comprehensive compliance documentation with evidence
        Prepare regulatory reporting automation and monitoring systems
      </actions>
      <validation>
        Compliance scans show zero critical violations across all frameworks
        External auditor attestation confirms regulatory compliance
        Documentation package complete with audit evidence and controls
      </validation>
    </phase>
    
  </implementation>
  
  <regulatory_frameworks>
    <pci_dss level="1">
      <scope>Payment card data processing and storage systems</scope>
      <requirements>Network security, data protection, vulnerability management, access controls</requirements>
      <controls>Firewall configuration, encryption, tokenization, access monitoring</controls>
    </pci_dss>
    <sox compliance="section_404">
      <scope>Financial reporting controls and internal assessments</scope>
      <requirements>Internal controls, external auditor attestation, material weakness remediation</requirements>
      <controls>Automated testing, audit trails, change management, access reviews</controls>
    </sox>
    <gdpr data_protection="article_32">
      <scope>Personal data processing and privacy protection</scope>
      <requirements>Lawful basis, data subject rights, privacy by design, breach notification</requirements>
      <controls>Consent management, data minimization, subject rights portal, impact assessments</controls>
    </gdpr>
    <hipaa safeguards="physical_administrative_technical">
      <scope>Healthcare information protection and privacy</scope>
      <requirements>PHI protection, minimum necessary access, business associate controls</requirements>
      <controls>Audit controls, integrity verification, transmission security, access management</controls>
    </hipaa>
  </regulatory_frameworks>
  
  <encryption_standards grade="financial">
    <at_rest>AES-256-GCM with HSM key management and 90-day rotation</at_rest>
    <in_transit>TLS 1.3+ with certificate pinning and perfect forward secrecy</in_transit>
    <field_level>Sensitive data fields encrypted with separate keys and access logging</field_level>
    <key_management>FIPS 140-2 Level 3 HSM with non-extractable keys and audit trails</key_management>
  </encryption_standards>
  
  <audit_requirements>
    <immutable_logging>Blockchain-based audit trails with cryptographic verification</immutable_logging>
    <real_time_monitoring>Continuous compliance monitoring with automated alerting</real_time_monitoring>
    <regulatory_reporting>Automated report generation with approval workflows</regulatory_reporting>
    <retention_policies>7-year minimum retention with secure archival and retrieval</retention_policies>
  </audit_requirements>
  
  <session_integration>
    <mandatory_creation>
      All financial compliance implementations require session tracking
      Regulatory audit requirements mandate comprehensive documentation
      External auditor coordination requires centralized progress tracking
    </mandatory_creation>
    <session_documentation>
      Compliance framework selection and regulatory mapping
      Security controls implementation with testing evidence
      External auditor coordination and attestation results
      Regulatory reporting automation and monitoring configuration
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      security/threat-modeling.md for regulatory threat analysis
      quality/production-standards.md for enterprise quality gates
      patterns/session-management.md for compliance audit trail tracking
    </depends_on>
    <provides_to>
      security/audit.md for compliance-focused security scanning
      development/protocol-enforcement.md for regulatory quality gates
      quality/production-standards.md for financial-grade requirements
    </provides_to>
  </integration_points>
  
</module>