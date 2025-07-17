# Custom Modules Example

## Overview
This example demonstrates how to create custom modules for your specific project needs, extending the framework's capabilities with domain-specific functionality.

## Example Scenario
You're building a fintech application and need specialized modules for financial calculations, compliance validation, and audit logging that aren't covered by the standard framework.

## Custom Module Structure

### 1. Create Custom Module Directory
```bash
mkdir -p .claude/custom/fintech
```

### 2. Custom Module: Financial Calculations

**File: `.claude/custom/fintech/financial-calculations.md`**
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-15   | stable |

# Financial Calculations Module

```xml
<module purpose="Specialized financial calculations and validations for fintech applications">
  <thinking_pattern>
    <checkpoint>Validate all financial inputs for precision and compliance</checkpoint>
    <checkpoint>Apply domain-specific calculation rules (compound interest, present value, etc.)</checkpoint>
    <checkpoint>Ensure regulatory compliance (GAAP, IFRS standards)</checkpoint>
    <checkpoint>Generate audit trails for all calculations</checkpoint>
  </thinking_pattern>
  
  <core_capabilities>
    <capability>Compound interest calculations with precision handling</capability>
    <capability>Present value and future value calculations</capability>
    <capability>Amortization schedule generation</capability>
    <capability>Risk assessment calculations</capability>
    <capability>Currency conversion with rate validation</capability>
  </core_capabilities>
  
  <validation_rules>
    <rule>All monetary values must use decimal precision (not float)</rule>
    <rule>Interest rates must be validated against regulatory limits</rule>
    <rule>Currency codes must be ISO 4217 compliant</rule>
    <rule>All calculations must include audit timestamps</rule>
  </validation_rules>
  
  <implementation_patterns>
    <pattern name="decimal_precision">
      <code>
        from decimal import Decimal, getcontext
        
        # Set precision for financial calculations
        getcontext().prec = 28
        
        def calculate_compound_interest(principal, rate, time, frequency=1):
            """Calculate compound interest with precise decimal arithmetic"""
            principal = Decimal(str(principal))
            rate = Decimal(str(rate))
            time = Decimal(str(time))
            frequency = Decimal(str(frequency))
            
            amount = principal * (1 + rate/frequency) ** (frequency * time)
            return amount
      </code>
    </pattern>
    
    <pattern name="audit_trail">
      <code>
        import logging
        from datetime import datetime
        
        def create_audit_log(calculation_type, inputs, result, user_id):
            """Create audit trail for financial calculations"""
            audit_entry = {
                'timestamp': datetime.utcnow().isoformat(),
                'calculation_type': calculation_type,
                'inputs': inputs,
                'result': str(result),
                'user_id': user_id,
                'compliance_check': True
            }
            
            # Log to secure audit system
            logging.getLogger('financial_audit').info(audit_entry)
            return audit_entry
      </code>
    </pattern>
  </implementation_patterns>
  
  <quality_gates>
    <gate>All financial calculations must include unit tests with known values</gate>
    <gate>Regulatory compliance validation required for all functions</gate>
    <gate>Performance testing for high-volume calculations</gate>
    <gate>Security review for sensitive financial data handling</gate>
  </quality_gates>
</module>
```

### 3. Custom Module: Compliance Validation

**File: `.claude/custom/fintech/compliance-validation.md`**
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-15   | stable |

# Compliance Validation Module

```xml
<module purpose="Regulatory compliance validation for financial applications">
  <thinking_pattern>
    <checkpoint>Identify applicable regulations (PCI DSS, SOX, GDPR, etc.)</checkpoint>
    <checkpoint>Apply regulatory validation rules</checkpoint>
    <checkpoint>Generate compliance reports</checkpoint>
    <checkpoint>Flag potential compliance violations</checkpoint>
  </thinking_pattern>
  
  <compliance_frameworks>
    <framework name="PCI_DSS">
      <requirement>Credit card data encryption</requirement>
      <requirement>Secure transmission protocols</requirement>
      <requirement>Access control and monitoring</requirement>
    </framework>
    
    <framework name="SOX">
      <requirement>Financial reporting controls</requirement>
      <requirement>Audit trail maintenance</requirement>
      <requirement>Data integrity validation</requirement>
    </framework>
    
    <framework name="GDPR">
      <requirement>Data privacy protection</requirement>
      <requirement>Consent management</requirement>
      <requirement>Data retention policies</requirement>
    </framework>
  </compliance_frameworks>
  
  <validation_patterns>
    <pattern name="pci_validation">
      <code>
        import re
        
        def validate_credit_card_handling(code_snippet):
            """Validate credit card data handling for PCI compliance"""
            violations = []
            
            # Check for hardcoded credit card numbers
            cc_pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
            if re.search(cc_pattern, code_snippet):
                violations.append("Hardcoded credit card number detected")
            
            # Check for unencrypted storage
            if 'credit_card' in code_snippet.lower() and 'encrypt' not in code_snippet.lower():
                violations.append("Credit card data may not be encrypted")
            
            return violations
      </code>
    </pattern>
  </validation_patterns>
  
  <reporting_templates>
    <template name="compliance_report">
      <section>Executive Summary</section>
      <section>Compliance Status by Framework</section>
      <section>Identified Violations</section>
      <section>Remediation Recommendations</section>
    </template>
  </reporting_templates>
</module>
```

### 4. Custom Module: Audit Logging

**File: `.claude/custom/fintech/audit-logging.md`**
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-15   | stable |

# Audit Logging Module

```xml
<module purpose="Comprehensive audit logging for financial transactions and operations">
  <thinking_pattern>
    <checkpoint>Identify all actions requiring audit logs</checkpoint>
    <checkpoint>Structure audit data for compliance requirements</checkpoint>
    <checkpoint>Implement secure, tamper-proof logging</checkpoint>
    <checkpoint>Ensure audit log retention and retrieval</checkpoint>
  </thinking_pattern>
  
  <audit_categories>
    <category name="financial_transactions">
      <events>Payment processing, fund transfers, balance updates</events>
      <retention_period>7_years</retention_period>
      <encryption_required>true</encryption_required>
    </category>
    
    <category name="user_access">
      <events>Login, logout, permission changes, data access</events>
      <retention_period>2_years</retention_period>
      <encryption_required>true</encryption_required>
    </category>
    
    <category name="system_operations">
      <events>Configuration changes, deployments, maintenance</events>
      <retention_period>5_years</retention_period>
      <encryption_required>false</encryption_required>
    </category>
  </audit_categories>
  
  <logging_patterns>
    <pattern name="secure_audit_log">
      <code>
        import hashlib
        import json
        from datetime import datetime
        
        class SecureAuditLogger:
            def __init__(self, secret_key):
                self.secret_key = secret_key
            
            def log_event(self, event_type, user_id, details):
                """Create tamper-proof audit log entry"""
                timestamp = datetime.utcnow().isoformat()
                
                audit_entry = {
                    'timestamp': timestamp,
                    'event_type': event_type,
                    'user_id': user_id,
                    'details': details
                }
                
                # Create tamper-proof hash
                entry_string = json.dumps(audit_entry, sort_keys=True)
                signature = hashlib.sha256(
                    (entry_string + self.secret_key).encode()
                ).hexdigest()
                
                audit_entry['signature'] = signature
                
                # Store in secure audit database
                self._store_audit_entry(audit_entry)
                
                return audit_entry
      </code>
    </pattern>
  </logging_patterns>
</module>
```

## Integration with Framework

### 5. Update PROJECT_CONFIG.xml
```xml
<project_config>
  <!-- ... existing configuration ... -->
  
  <custom_modules>
    <module_paths>
      <path>.claude/custom/fintech/</path>
    </module_paths>
    
    <fintech_config>
      <regulatory_frameworks>
        <framework>PCI_DSS</framework>
        <framework>SOX</framework>
        <framework>GDPR</framework>
      </regulatory_frameworks>
      
      <audit_retention>
        <financial_transactions>7_years</financial_transactions>
        <user_access>2_years</user_access>
        <system_operations>5_years</system_operations>
      </audit_retention>
    </fintech_config>
  </custom_modules>
  
  <!-- ... rest of configuration ... -->
</project_config>
```

### 6. Create Custom Command Using Modules

**File: `.claude/commands/fintech-calculation.md`**
```markdown
| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-15   | stable |

# Fintech Calculation Command

```xml
<command purpose="Perform financial calculations with compliance validation and audit logging">
  <delegation target="custom/fintech/financial-calculations.md">
    Financial calculation → Compliance validation → Audit logging → Result
  </delegation>
  
  <module_orchestration>
    <core_modules>
      <module>custom/fintech/financial-calculations.md</module>
      <module>custom/fintech/compliance-validation.md</module>
      <module>custom/fintech/audit-logging.md</module>
    </core_modules>
    
    <support_modules>
      <module>system/quality/tdd.md</module>
      <module>system/security/threat-modeling.md</module>
    </support_modules>
  </module_orchestration>
</command>
```

## Usage Examples

### 7. Using Custom Fintech Command
```bash
# Calculate loan payment with compliance validation
/fintech-calculation "calculate monthly payment for $500,000 loan at 3.5% APR over 30 years"

# Perform risk assessment calculation
/fintech-calculation "calculate value at risk for portfolio with 95% confidence level"

# Currency conversion with audit trail
/fintech-calculation "convert $100,000 USD to EUR with current exchange rate"
```

### 8. Expected Framework Response
```
🔍 FINTECH CALCULATION ANALYSIS...
- Detected: Loan payment calculation request
- Regulatory frameworks: PCI DSS, SOX compliance required
- Audit category: Financial transactions (7-year retention)

📋 COMPLIANCE VALIDATION:
✅ Calculation follows GAAP standards
✅ No sensitive data exposure detected
✅ Audit trail configuration verified

💰 FINANCIAL CALCULATION:
Principal: $500,000.00
Interest Rate: 3.5% APR
Term: 30 years (360 payments)
Monthly Payment: $2,245.22

🔒 SECURITY MEASURES:
- Decimal precision arithmetic implemented
- Calculation inputs validated
- Audit log entry created
- Compliance report generated

📊 GENERATED IMPLEMENTATION:
```

## Key Benefits

### ✅ Domain Expertise
- **Specialized Logic**: Custom modules contain domain-specific knowledge
- **Regulatory Compliance**: Built-in compliance validation
- **Industry Standards**: Follows financial industry best practices
- **Audit Requirements**: Comprehensive audit logging

### ✅ Framework Integration
- **Seamless Integration**: Custom modules work with existing framework
- **Quality Gates**: Same quality standards applied to custom modules
- **Command Orchestration**: Custom commands can use multiple modules
- **Configuration**: Project-specific configuration support

### ✅ Maintainability
- **Modular Design**: Each module has single responsibility
- **Versioning**: Individual module versioning
- **Documentation**: Self-documenting module structure
- **Testing**: Module-specific test requirements

## Best Practices

### 1. Module Design
- Keep modules focused on single domain
- Use clear, descriptive module names
- Include comprehensive documentation
- Implement proper error handling

### 2. Quality Standards
- Write tests for custom modules
- Follow framework's XML structure
- Include thinking patterns for AI guidance
- Validate against quality gates

### 3. Integration
- Update PROJECT_CONFIG.xml with custom paths
- Create custom commands that orchestrate modules
- Maintain compatibility with framework updates
- Document integration points

## Advanced Usage

### Custom Module Testing
```bash
# Test custom modules independently
/query "validate the financial-calculations module for accuracy"

# Test compliance integration
/query "check if custom modules meet regulatory requirements"

# Test performance
/query "analyze performance of custom fintech calculations"
```

This example demonstrates how to extend the framework with domain-specific modules while maintaining all the benefits of the core framework's quality, testing, and integration capabilities.