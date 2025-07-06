<command purpose="Production-ready development with mandatory quality gates and compliance standards">
  
  <delegation target="modules/development/protocol-enforcement.md">
    This command delegates ALL implementation to the protocol enforcement module which provides comprehensive production standards including mandatory TDD, security reviews, performance validation, and regulatory compliance for enterprise systems.
  </delegation>
  
  <module_integration>
    <primary_module>modules/development/protocol-enforcement.md</primary_module>
    <supporting_modules>
      <module>modules/quality/tdd.md</module>
      <module>modules/security/audit.md</module>
      <module>modules/quality/production-standards.md</module>
      <module>modules/patterns/session-management.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="financial">/protocol "Implement wire transfer processing"</example>
    <example type="healthcare">/protocol "Add patient record system"</example>
    <example type="compliance">/protocol "Make payment processing SOX compliant"</example>
    <example type="critical">/protocol "Build real-time trading platform"</example>
  </usage_examples>
  
  <strict_enforcement target="production_standards">
    <primary_rule>MUST satisfy ALL quality gates before production deployment</primary_rule>
    <verification>95% coverage + security scan + performance baseline + documentation complete</verification>
    <consequence>Production deployment blocked until all compliance requirements satisfied</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/development/protocol-enforcement.md for complete implementation details including quality gate enforcement, compliance frameworks, and audit trail requirements.
  </reference>
  
</command>
