| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Financial Compliance Module

────────────────────────────────────────────────────────────────────────────────

<purpose>Ensure financial software meets regulatory and security requirements</purpose>

## Core Components

```xml
<financial_compliance>
  <regulations>
    <rule>PCI DSS compliance for payment processing</rule>
    <rule>GDPR for personal financial data</rule>
    <rule>SOX compliance for financial reporting</rule>
    <rule>AML/KYC requirements for identity verification</rule>
  </regulations>
  
  <security_requirements>
    <encryption>AES-256 for data at rest, TLS 1.3 for transit</encryption>
    <authentication>Multi-factor authentication required</authentication>
    <audit_logging>Complete transaction and access logs</audit_logging>
    <data_retention>Follow regulatory requirements</data_retention>
  </security_requirements>
</financial_compliance>
```

## Implementation Patterns

```xml
<patterns>
  <payment_processing>
    <rule>Never store raw credit card numbers</rule>
    <rule>Use tokenization for sensitive data</rule>
    <rule>Implement fraud detection mechanisms</rule>
    <rule>Maintain PCI DSS compliance</rule>
  </payment_processing>
  
  <audit_trail>
    <rule>Log all financial transactions</rule>
    <rule>Immutable audit logs with timestamps</rule>
    <rule>User attribution for all actions</rule>
    <rule>Secure log storage and retention</rule>
  </audit_trail>
  
  <data_protection>
    <rule>Encrypt all financial data</rule>
    <rule>Implement access controls</rule>
    <rule>Regular security audits</rule>
    <rule>Incident response procedures</rule>
  </data_protection>
</patterns>
```

## Compliance Checklist

```xml
<checklist>
  <item>Encryption implemented for all sensitive data</item>
  <item>Authentication and authorization in place</item>
  <item>Audit logging configured and tested</item>
  <item>Data retention policies defined</item>
  <item>Security testing completed</item>
  <item>Compliance documentation maintained</item>
  <item>Incident response plan ready</item>
  <item>Regular security training conducted</item>
</checklist>
```

## Integration Points

```xml
<integration>
  <with module="quality/production-standards.md">
    <rule>Financial systems require production quality gates</rule>
    <rule>Extra security validation before deployment</rule>
  </with>
  <with module="security/threat-modeling.md">
    <rule>Financial systems need comprehensive threat models</rule>
    <rule>Regular security assessments required</rule>
  </with>
</integration>
```

## Thinking Pattern

```xml
<thinking_pattern>
  <step>1. Identify financial data and transactions</step>
  <step>2. Apply regulatory requirements</step>
  <step>3. Implement security controls</step>
  <step>4. Add audit logging</step>
  <step>5. Test compliance measures</step>
  <step>6. Document compliance status</step>
</thinking_pattern>
```