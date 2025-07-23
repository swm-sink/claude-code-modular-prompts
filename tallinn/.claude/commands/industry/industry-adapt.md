---
name: /industry-adapt
description: Advanced industry adaptation with sector-specific optimization, compliance frameworks, and market alignment
usage: /industry-adapt [industry_sector] [adaptation_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced industry adaptation with sector-specific optimization, compliance frameworks, and market alignment

**Usage**: `/industry-adapt $INDUSTRY $DOMAIN $COMPLIANCE`

## Key Arguments

- **$INDUSTRY** (required): Target industry sector (e.g., "healthcare", "fintech", "e-commerce", "manufactur...
- **$DOMAIN** (optional): Industry domain focus for specialized expertise application.
- **$COMPLIANCE** (optional): Compliance handling: auto (Claude-recommended) or strict (maximum compliance).

## Examples

```bash
/industry-adapt "healthcare" --domain=medical-devices --compliance=strict
```
*Adapt code for healthcare industry with HIPAA compliance*

```bash
/industry-adapt "fintech" --domain=payments --compliance=auto
```
*Generate fintech solutions with regulatory awareness*

## Core Logic

You are an expert industry solutions architect with deep knowledge across multiple domains. Use Claude's comprehensive understanding of industry-specific requirements, regulations, and best practices to generate tailored solutions.

 **Industry Intelligence Matrix**:

**industry_domains**:

**healthcare**:

 **Healthcare & Life Sciences**:
 - **Regulatory Framework**: HIPAA, FDA 21 CFR Part 11, GDPR, SOX compliance
 - **Data Requirements**: PHI protection, audit trails, data integrity, patient consent
 - **Security Patterns**: Zero-trust architecture, end-to-end encryption, role-based access
 - **Integration Needs**: HL7 FHIR, EHR systems, medical devices, laboratory systems
 - **Performance Criteria**: Real-time patient monitoring, high availability, disaster recovery
 - **Industry Patterns**: Clinical workflows, patient journey optimization, care coordination

**fintech**:

 **Financial Technology**:
 - **Regulatory Framework**: PCI DSS, SOX, KYC/AML, Open Banking, PSD2, GDPR
 - **Data Requirements**: Financial data encryption, transaction integrity, audit logging
 - **Security Patterns**: Multi-factor authentication, fraud detection, secure payments
 - **Integration Needs**: Banking APIs, payment processors, credit bureaus, blockchain
 - **Performance Criteria**: Low-latency trading, high transaction throughput, 99.99% uptime
 - **Industry Patterns**: Risk management, algorithmic trading, digital wallets, robo-advisors

**ecommerce**:

 **E-Commerce & Retail**:
 - **Regulatory Framework**: GDPR, CCPA, PCI compliance, consumer protection laws

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

