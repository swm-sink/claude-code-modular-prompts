<command name="security" purpose="Financial-grade security implementation with compliance frameworks and threat modeling">
  
  <delegation target="modules/security/audit.md">
    This command delegates ALL implementation to the security audit module which provides comprehensive enterprise security patterns including PCI DSS, SOX, GDPR compliance, threat modeling, and financial-grade security controls.
  </delegation>
  
  <module_integration>
    <primary_module>modules/security/audit.md</primary_module>
    <supporting_modules>
      <module>modules/security/threat-modeling.md</module>
      <module>modules/security/financial-compliance.md</module>
      <module>modules/patterns/session-management.md</module>
      <module>modules/quality/production-standards.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="payment">/security "Implement PCI-compliant payment system"</example>
    <example type="auth">/security "Add OAuth2 with MFA"</example>
    <example type="gdpr">/security "Implement GDPR-compliant data handling"</example>
    <example type="audit">/security --audit "Review application security"</example>
    <example type="sox">/security "Implement SOX compliance for financial reports"</example>
  </usage_examples>
  
  <strict_enforcement target="compliance_requirements">
    <primary_rule>MUST satisfy ALL applicable compliance frameworks (PCI DSS, SOX, GDPR)</primary_rule>
    <verification>Threat model + security controls + audit trails + compliance checklist complete</verification>
    <consequence>Security implementation blocked until all compliance requirements satisfied</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/security/audit.md for complete implementation details including compliance frameworks, threat modeling patterns, and financial-grade security controls.
  </reference>
  
</command>
