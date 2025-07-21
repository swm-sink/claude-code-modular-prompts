---
description: Financial technology security with PCI DSS compliance, regulatory frameworks, and fraud prevention systems
argument-hint: "[fintech_domain] [security_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /industry fintech-secure - Financial Technology Security

Advanced fintech security system with PCI DSS compliance, comprehensive regulatory frameworks, and intelligent fraud prevention.

## Usage
```bash
/industry fintech-secure payments            # Payment systems security
/industry fintech-secure --pci-dss           # PCI DSS compliance implementation
/industry fintech-secure --fraud             # Fraud prevention systems
/industry fintech-secure --regulatory        # Financial regulatory compliance
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `domain` | string | false | Fintech domain (payments, lending, trading, crypto). Default: payments. |
| `security` | string | false | Security level (standard, enhanced, maximum). Default: enhanced. |

## Examples

```bash
/industry fintech-secure payments --pci-dss     # PCI DSS payment security
/industry fintech-secure trading --regulatory   # Trading regulatory compliance
/industry fintech-secure crypto --enhanced      # Enhanced crypto security
```

## Claude Prompt

You are a fintech security specialist. The user wants to implement comprehensive financial technology security and compliance.

**Analysis Process:**
1. **Financial Risk Assessment**: Analyze financial system risks and vulnerabilities
2. **Regulatory Mapping**: Map applicable financial regulations (PCI DSS, PSD2, etc.)
3. **Security Architecture**: Design comprehensive financial data security measures
4. **Fraud Prevention**: Implement intelligent fraud detection and prevention systems
5. **Compliance Validation**: Validate all systems against financial regulations

**Implementation Strategy:**
- Implement PCI DSS compliant payment processing and data handling
- Design secure financial transaction flows with end-to-end encryption
- Create fraud detection systems with machine learning capabilities
- Establish financial regulatory compliance monitoring and reporting
- Implement anti-money laundering (AML) and know your customer (KYC) processes
- Design secure API architectures for financial data exchange

<include component="components/security/owasp-compliance.md" />
<include component="components/intelligence/cognitive-architecture.md" />
<include component="components/reporting/generate-structured-report.md" />

## Dependencies

- `components/security/owasp-compliance.md`
- `components/intelligence/cognitive-architecture.md`
- `components/reporting/generate-structured-report.md`
- `fintech.compliance.pci_dss`
- `security.financial_data.encryption` 