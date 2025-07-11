# Financial Technology Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Financial Technology domain template provides specialized framework configuration for fintech applications, payment processing systems, and financial services platforms. This template optimizes the Claude Code Framework for high-security, compliance-focused, and performance-critical financial workflows.

## Domain Configuration

```xml
<financial_technology_domain>
  <purpose>Specialized framework configuration for financial technology and services applications</purpose>
  
  <financial_services>
    <payment_processing>Payment gateways, transaction processing, settlement systems</payment_processing>
    <banking_systems>Core banking, digital banking, mobile banking applications</banking_systems>
    <investment_platforms>Trading platforms, robo-advisors, portfolio management</investment_platforms>
    <compliance_systems>KYC/AML, regulatory reporting, audit trail systems</compliance_systems>
  </financial_services>
  
  <development_characteristics>
    <security_first>Security-by-design with encryption and threat modeling</security_first>
    <compliance_mandatory>Regulatory compliance and audit requirements</compliance_mandatory>
    <performance_critical>High-performance transaction processing</performance_critical>
    <data_integrity>Data consistency and transaction integrity</data_integrity>
    <scalability_required>Horizontal scaling for transaction volume</scalability_required>
  </development_characteristics>
</financial_technology_domain>
```

## Template Variables

```xml
<template_variables>
  <financial_configuration>
    <service_type>{{SERVICE_TYPE:payment_processing|banking|investment|compliance|insurance}}</service_type>
    <regulatory_framework>{{REGULATORY_FRAMEWORK:pci_dss|gdpr|sox|psd2|mifid|basel}}</regulatory_framework>
    <security_level>{{SECURITY_LEVEL:standard|high|critical|government}}</security_level>
    <transaction_volume>{{TRANSACTION_VOLUME:low|medium|high|enterprise}}</transaction_volume>
  </financial_configuration>
  
  <project_configuration>
    <project_name>{{PROJECT_NAME:string}}</project_name>
    <financial_domain>{{FINANCIAL_DOMAIN:payments|banking|trading|insurance|lending|crypto}}</financial_domain>
    <deployment_environment>{{DEPLOYMENT_ENVIRONMENT:cloud|on_premise|hybrid|multi_cloud}}</deployment_environment>
    <compliance_requirements>{{COMPLIANCE_REQUIREMENTS:array}}</compliance_requirements>
  </project_configuration>
  
  <technical_settings>
    <primary_language>{{PRIMARY_LANGUAGE:java|csharp|python|go|rust|scala}}</primary_language>
    <database_system>{{DATABASE_SYSTEM:postgresql|oracle|sql_server|mongodb|cassandra}}</database_system>
    <message_queue>{{MESSAGE_QUEUE:kafka|rabbitmq|azure_service_bus|aws_sqs}}</message_queue>
    <security_framework>{{SECURITY_FRAMEWORK:oauth2|jwt|saml|mfa|hsm}}</security_framework>
  </technical_settings>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <fintech_specific_thinking>
      <security_assessment>Evaluate security implications and threat vectors</security_assessment>
      <compliance_validation>Ensure compliance with relevant financial regulations</compliance_validation>
      <data_protection>Validate data privacy and protection mechanisms</data_protection>
      <transaction_integrity>Ensure transaction consistency and reliability</transaction_integrity>
    </fintech_specific_thinking>
    
    <quality_gates>
      <security_testing>Comprehensive security testing including penetration testing</security_testing>
      <compliance_validation>Regulatory compliance validation and audit readiness</compliance_validation>
      <performance_testing>High-load transaction processing validation</performance_testing>
      <data_integrity_testing>Data consistency and transaction integrity validation</data_integrity_testing>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <fintech_feature_planning>
      <regulatory_impact>Assess regulatory impact and compliance requirements</regulatory_impact>
      <security_design>Design security architecture and threat mitigation</security_design>
      <transaction_flow>Design transaction processing and data flow</transaction_flow>
      <audit_requirements>Plan audit trail and compliance reporting</audit_requirements>
    </fintech_feature_planning>
    
    <development_workflow>
      <security_review>Mandatory security review for all features</security_review>
      <compliance_check>Compliance validation at each development stage</compliance_check>
      <performance_validation>Performance benchmarking for transaction processing</performance_validation>
      <audit_preparation>Audit trail implementation and documentation</audit_preparation>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <fintech_validation>
      <security_validation>Comprehensive security assessment and penetration testing</security_validation>
      <compliance_validation>Regulatory compliance verification and audit preparation</compliance_validation>
      <performance_validation>High-load performance testing and optimization</performance_validation>
      <data_integrity_validation>Transaction integrity and data consistency validation</data_integrity_validation>
    </fintech_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates Configuration

```xml
<quality_gates_configuration>
  <security_quality>
    <encryption_validation>
      <rule>All sensitive data encrypted at rest and in transit</rule>
      <validation>Automated encryption verification and key management validation</validation>
      <threshold>100% sensitive data encryption coverage</threshold>
    </encryption_validation>
    
    <authentication_validation>
      <rule>Multi-factor authentication for all privileged access</rule>
      <validation>Authentication mechanism testing and MFA validation</validation>
      <threshold>100% privileged access MFA coverage</threshold>
    </authentication_validation>
    
    <vulnerability_assessment>
      <rule>Zero high-severity security vulnerabilities</rule>
      <validation>Automated vulnerability scanning and penetration testing</validation>
      <threshold>Zero critical/high vulnerabilities in production</threshold>
    </vulnerability_assessment>
  </security_quality>
  
  <compliance_quality>
    <regulatory_compliance>
      <rule>Full compliance with applicable financial regulations</rule>
      <validation>Automated compliance checking and manual audit preparation</validation>
      <threshold>100% compliance with regulatory requirements</threshold>
    </regulatory_compliance>
    
    <audit_trail_completeness>
      <rule>Complete audit trail for all financial transactions</rule>
      <validation>Audit trail validation and compliance reporting</validation>
      <threshold>100% transaction audit trail coverage</threshold>
    </audit_trail_completeness>
    
    <data_governance>
      <rule>Data governance policies fully implemented</rule>
      <validation>Data governance validation and privacy compliance</validation>
      <threshold>100% data governance policy compliance</threshold>
    </data_governance>
  </compliance_quality>
  
  <performance_quality>
    <transaction_processing>
      <rule>Transaction processing meets performance benchmarks</rule>
      <validation>High-load transaction processing testing</validation>
      <threshold>99.9% transaction processing success rate</threshold>
    </transaction_processing>
    
    <response_time>
      <rule>API response times within acceptable limits</rule>
      <validation>Performance testing under various load conditions</validation>
      <threshold>Sub-second response times for 95% of requests</threshold>
    </response_time>
    
    <system_availability>
      <rule>High availability and disaster recovery capability</rule>
      <validation>Availability testing and disaster recovery validation</validation>
      <threshold>99.9% system uptime with <5 minute recovery time</threshold>
    </system_availability>
  </performance_quality>
</quality_gates_configuration>
```

## Module Selection

```xml
<module_selection>
  <core_modules>
    <financial_technology>
      <transaction_processing>High-performance transaction processing patterns</transaction_processing>
      <security_framework>Comprehensive security implementation patterns</security_framework>
      <compliance_automation>Automated compliance validation and reporting</compliance_automation>
      <audit_system>Complete audit trail and reporting system</audit_system>
    </financial_technology>
    
    <domain_specific>
      <payment_processing condition="{{SERVICE_TYPE:payment_processing}}">
        <payment_gateways>Payment gateway integration and management</payment_gateways>
        <settlement_systems>Transaction settlement and reconciliation</settlement_systems>
        <fraud_detection>Real-time fraud detection and prevention</fraud_detection>
      </payment_processing>
      
      <banking_systems condition="{{SERVICE_TYPE:banking}}">
        <core_banking>Core banking system integration patterns</core_banking>
        <account_management>Account lifecycle and management systems</account_management>
        <regulatory_reporting>Automated regulatory reporting systems</regulatory_reporting>
      </banking_systems>
      
      <investment_platforms condition="{{SERVICE_TYPE:investment}}">
        <trading_engine>High-performance trading system patterns</trading_engine>
        <portfolio_management>Portfolio optimization and management</portfolio_management>
        <market_data>Real-time market data processing</market_data>
      </investment_platforms>
    </domain_specific>
  </core_modules>
  
  <security_modules>
    <encryption_management>
      <data_encryption>Advanced encryption for sensitive data</data_encryption>
      <key_management>Secure key management and rotation</key_management>
      <hsm_integration>Hardware security module integration</hsm_integration>
      <tokenization>Payment card tokenization systems</tokenization>
    </encryption_management>
    
    <authentication_authorization>
      <multi_factor_auth>Multi-factor authentication implementation</multi_factor_auth>
      <oauth_integration>OAuth 2.0 and OpenID Connect integration</oauth_integration>
      <rbac_system>Role-based access control systems</rbac_system>
      <session_management>Secure session management and timeout</session_management>
    </authentication_authorization>
  </security_modules>
  
  <compliance_modules>
    <regulatory_compliance>
      <kyc_aml>KYC/AML compliance automation</kyc_aml>
      <pci_compliance>PCI DSS compliance validation</pci_compliance>
      <gdpr_compliance>GDPR privacy compliance automation</gdpr_compliance>
      <sox_compliance>SOX compliance and internal controls</sox_compliance>
    </regulatory_compliance>
    
    <audit_reporting>
      <audit_trail>Comprehensive audit trail implementation</audit_trail>
      <compliance_reporting>Automated compliance reporting</compliance_reporting>
      <risk_assessment>Risk assessment and management systems</risk_assessment>
      <incident_response>Security incident response procedures</incident_response>
    </audit_reporting>
  </compliance_modules>
</module_selection>
```

## Framework Integration

```xml
<framework_integration>
  <optimal_frameworks>
    <primary_framework>CARE - Context-aware development with rigorous evaluation</primary_framework>
    <secondary_framework>TRACE - Thorough requirements analysis with comprehensive evaluation</secondary_framework>
    <specialized_framework>SECURE - Security-focused development with compliance validation</specialized_framework>
  </optimal_frameworks>
  
  <framework_customization>
    <care_fintech_optimization>
      <context>Financial regulatory environment, security requirements, and compliance mandates</context>
      <action>Security-first development with compliance-driven feature implementation</action>
      <result>Secure, compliant financial systems with audit-ready documentation</result>
      <evaluation>Security assessment, compliance validation, and performance benchmarking</evaluation>
    </care_fintech_optimization>
    
    <trace_fintech_optimization>
      <task>Financial system requirements with security and compliance focus</task>
      <reasoning>Security architecture and compliance rationale documentation</reasoning>
      <action>Implementation with security controls and compliance validation</action>
      <conclusion>Secure system delivery with comprehensive audit documentation</conclusion>
      <evaluation>Security testing, compliance verification, and performance validation</evaluation>
    </trace_fintech_optimization>
  </framework_customization>
</framework_integration>
```

## Development Workflows

```xml
<development_workflows>
  <fintech_development_cycle>
    <requirements_analysis>
      <step>Define functional requirements with security and compliance constraints</step>
      <step>Identify applicable regulatory requirements and compliance standards</step>
      <step>Design security architecture and threat mitigation strategies</step>
      <step>Plan audit trail and compliance reporting requirements</step>
    </requirements_analysis>
    
    <secure_development>
      <step>Implement security controls and encryption mechanisms</step>
      <step>Develop with secure coding practices and code review</step>
      <step>Integrate compliance validation and audit trail logging</step>
      <step>Implement performance optimization for transaction processing</step>
    </secure_development>
    
    <security_testing>
      <step>Conduct comprehensive security testing and vulnerability assessment</step>
      <step>Perform penetration testing and security code review</step>
      <step>Validate compliance with regulatory requirements</step>
      <step>Test performance under high transaction loads</step>
    </security_testing>
    
    <compliance_validation>
      <step>Validate regulatory compliance and audit readiness</step>
      <step>Conduct internal audit and compliance review</step>
      <step>Prepare compliance documentation and reporting</step>
      <step>Implement continuous monitoring and compliance tracking</step>
    </compliance_validation>
  </fintech_development_cycle>
  
  <specialized_workflows>
    <payment_processing_workflow>
      <pci_compliance>Implement PCI DSS compliance requirements</pci_compliance>
      <fraud_prevention>Integrate fraud detection and prevention systems</fraud_prevention>
      <transaction_security>Implement secure transaction processing</transaction_security>
      <settlement_reconciliation>Develop settlement and reconciliation processes</settlement_reconciliation>
    </payment_processing_workflow>
    
    <banking_system_workflow>
      <core_banking_integration>Integrate with core banking systems</core_banking_integration>
      <regulatory_reporting>Implement automated regulatory reporting</regulatory_reporting>
      <customer_verification>Develop KYC/AML compliance systems</customer_verification>
      <account_security>Implement account security and access controls</account_security>
    </banking_system_workflow>
  </specialized_workflows>
</development_workflows>
```

## Security Architecture

```xml
<security_architecture>
  <defense_in_depth>
    <network_security>
      <firewall_protection>Multi-layer firewall protection with intrusion detection</firewall_protection>
      <network_segmentation>Network segmentation and micro-segmentation</network_segmentation>
      <vpn_access>Secure VPN access for remote connectivity</vpn_access>
      <ddos_protection>DDoS protection and traffic filtering</ddos_protection>
    </network_security>
    
    <application_security>
      <secure_coding>Security-focused coding practices and frameworks</secure_coding>
      <input_validation>Comprehensive input validation and sanitization</input_validation>
      <output_encoding>Secure output encoding and XSS prevention</output_encoding>
      <session_security>Secure session management and timeout controls</session_security>
    </application_security>
    
    <data_security>
      <encryption_at_rest>Strong encryption for data at rest</encryption_at_rest>
      <encryption_in_transit>TLS encryption for data in transit</encryption_in_transit>
      <key_management>Secure key management and rotation</key_management>
      <data_masking>Data masking and tokenization for sensitive data</data_masking>
    </data_security>
  </defense_in_depth>
  
  <identity_access_management>
    <authentication>
      <multi_factor_auth>Multi-factor authentication for all access</multi_factor_auth>
      <biometric_auth>Biometric authentication for high-security access</biometric_auth>
      <certificate_auth>Certificate-based authentication for systems</certificate_auth>
      <password_policy>Strong password policies and management</password_policy>
    </authentication>
    
    <authorization>
      <rbac_implementation>Role-based access control with least privilege</rbac_implementation>
      <dynamic_authorization>Dynamic authorization based on context</dynamic_authorization>
      <api_security>API security with OAuth 2.0 and rate limiting</api_security>
      <privilege_escalation>Secure privilege escalation procedures</privilege_escalation>
    </authorization>
  </identity_access_management>
</security_architecture>
```

## Performance Optimization

```xml
<performance_optimization>
  <transaction_processing_optimization>
    <high_throughput_processing>
      <parallel_processing>Parallel transaction processing for high throughput</parallel_processing>
      <queue_management>Efficient message queue management and processing</queue_management>
      <batch_processing>Optimized batch processing for bulk transactions</batch_processing>
      <caching_strategies>Intelligent caching for frequently accessed data</caching_strategies>
    </high_throughput_processing>
    
    <low_latency_optimization>
      <memory_optimization>Memory-efficient data structures and algorithms</memory_optimization>
      <database_optimization>Database query optimization and indexing</database_optimization>
      <network_optimization>Network latency reduction and connection pooling</network_optimization>
      <algorithm_optimization>Algorithm optimization for critical paths</algorithm_optimization>
    </low_latency_optimization>
  </transaction_processing_optimization>
  
  <scalability_architecture>
    <horizontal_scaling>
      <microservices_architecture>Microservices for independent scaling</microservices_architecture>
      <container_orchestration>Container orchestration for dynamic scaling</container_orchestration>
      <load_balancing>Advanced load balancing and traffic distribution</load_balancing>
      <auto_scaling>Automatic scaling based on transaction volume</auto_scaling>
    </horizontal_scaling>
    
    <database_scaling>
      <sharding_strategies>Database sharding for horizontal scaling</sharding_strategies>
      <replication_optimization>Database replication and read scaling</replication_optimization>
      <caching_layers>Multi-layer caching for database performance</caching_layers>
      <connection_pooling>Efficient database connection management</connection_pooling>
    </database_scaling>
  </scalability_architecture>
</performance_optimization>
```

## Testing Strategy

```xml
<testing_strategy>
  <security_testing_framework>
    <penetration_testing>
      <external_penetration>External penetration testing by certified professionals</external_penetration>
      <internal_penetration>Internal penetration testing and lateral movement assessment</internal_penetration>
      <web_application_testing>Web application security testing and vulnerability assessment</web_application_testing>
      <api_security_testing>API security testing and authorization validation</api_security_testing>
    </penetration_testing>
    
    <automated_security_testing>
      <sast_scanning>Static application security testing integration</sast_scanning>
      <dast_scanning>Dynamic application security testing automation</dast_scanning>
      <dependency_scanning>Dependency vulnerability scanning and management</dependency_scanning>
      <configuration_testing>Security configuration testing and validation</configuration_testing>
    </automated_security_testing>
  </security_testing_framework>
  
  <compliance_testing_framework>
    <regulatory_testing>
      <pci_compliance_testing>PCI DSS compliance validation and testing</pci_compliance_testing>
      <sox_compliance_testing>SOX compliance and internal controls testing</sox_compliance_testing>
      <gdpr_compliance_testing>GDPR privacy compliance and data protection testing</gdpr_compliance_testing>
      <industry_specific_testing>Industry-specific regulatory compliance testing</industry_specific_testing>
    </regulatory_testing>
    
    <audit_preparation>
      <audit_trail_testing>Audit trail completeness and integrity testing</audit_trail_testing>
      <compliance_reporting_testing>Compliance reporting accuracy and completeness testing</compliance_reporting_testing>
      <data_governance_testing>Data governance policy implementation testing</data_governance_testing>
      <risk_assessment_testing>Risk assessment and mitigation testing</risk_assessment_testing>
    </audit_preparation>
  </compliance_testing_framework>
  
  <performance_testing_framework>
    <load_testing>
      <transaction_load_testing>High-volume transaction processing testing</transaction_load_testing>
      <concurrent_user_testing>Concurrent user load testing and capacity planning</concurrent_user_testing>
      <stress_testing>System stress testing and breaking point analysis</stress_testing>
      <endurance_testing>Long-running system endurance and stability testing</endurance_testing>
    </load_testing>
    
    <latency_testing>
      <response_time_testing>API response time testing and optimization</response_time_testing>
      <database_performance_testing>Database performance and query optimization testing</database_performance_testing>
      <network_latency_testing>Network latency and throughput testing</network_latency_testing>
      <real_time_processing_testing>Real-time transaction processing performance testing</real_time_processing_testing>
    </latency_testing>
  </performance_testing_framework>
</testing_strategy>
```

## Deployment Configuration

```xml
<deployment_configuration>
  <secure_deployment>
    <infrastructure_security>
      <secure_infrastructure>Secure cloud infrastructure with defense-in-depth</secure_infrastructure>
      <network_isolation>Network isolation and micro-segmentation</network_isolation>
      <encryption_everywhere>End-to-end encryption for all data flows</encryption_everywhere>
      <security_monitoring>Real-time security monitoring and incident response</security_monitoring>
    </infrastructure_security>
    
    <deployment_automation>
      <secure_cicd>Secure CI/CD pipelines with security gates</secure_cicd>
      <infrastructure_as_code>Infrastructure as code with security validation</infrastructure_as_code>
      <automated_testing>Automated security and compliance testing</automated_testing>
      <deployment_validation>Deployment validation and rollback procedures</deployment_validation>
    </deployment_automation>
  </secure_deployment>
  
  <high_availability>
    <redundancy_architecture>
      <multi_region_deployment>Multi-region deployment for disaster recovery</multi_region_deployment>
      <load_balancing>Advanced load balancing and failover</load_balancing>
      <database_replication>Database replication and backup strategies</database_replication>
      <service_mesh>Service mesh for microservices communication</service_mesh>
    </redundancy_architecture>
    
    <monitoring_alerting>
      <real_time_monitoring>Real-time system monitoring and alerting</real_time_monitoring>
      <performance_monitoring>Performance monitoring and optimization</performance_monitoring>
      <security_monitoring>Security monitoring and incident detection</security_monitoring>
      <compliance_monitoring>Compliance monitoring and reporting</compliance_monitoring>
    </monitoring_alerting>
  </high_availability>
</deployment_configuration>
```

## Documentation Templates

```xml
<documentation_templates>
  <security_documentation>
    <security_architecture>
      <threat_model>Comprehensive threat modeling and risk assessment</threat_model>
      <security_controls>Security controls documentation and implementation</security_controls>
      <incident_response>Security incident response procedures</incident_response>
      <security_monitoring>Security monitoring and alerting procedures</security_monitoring>
    </security_architecture>
    
    <compliance_documentation>
      <regulatory_compliance>Regulatory compliance procedures and evidence</regulatory_compliance>
      <audit_procedures>Audit procedures and compliance validation</audit_procedures>
      <policy_documentation>Security and compliance policy documentation</policy_documentation>
      <training_materials>Security awareness and compliance training materials</training_materials>
    </compliance_documentation>
  </security_documentation>
  
  <technical_documentation>
    <system_architecture>
      <architecture_overview>System architecture and component interaction</architecture_overview>
      <api_documentation>Comprehensive API documentation and security</api_documentation>
      <database_design>Database design and security implementation</database_design>
      <integration_guide>Third-party integration and security considerations</integration_guide>
    </system_architecture>
    
    <operational_documentation>
      <deployment_guide>Secure deployment procedures and configuration</deployment_guide>
      <monitoring_guide>System monitoring and alerting configuration</monitoring_guide>
      <troubleshooting_guide>System troubleshooting and incident response</troubleshooting_guide>
      <maintenance_procedures>System maintenance and security updates</maintenance_procedures>
    </operational_documentation>
  </technical_documentation>
</documentation_templates>
```

## Success Metrics

```xml
<success_metrics>
  <security_metrics>
    <security_posture>Security vulnerability count and severity assessment</security_posture>
    <incident_response>Security incident response time and effectiveness</incident_response>
    <compliance_score>Regulatory compliance score and audit results</compliance_score>
    <threat_detection>Threat detection and prevention effectiveness</threat_detection>
  </security_metrics>
  
  <performance_metrics>
    <transaction_throughput>Transaction processing throughput and capacity</transaction_throughput>
    <system_availability>System uptime and availability metrics</system_availability>
    <response_time>API response time and user experience metrics</response_time>
    <scalability_metrics>System scalability and performance under load</scalability_metrics>
  </performance_metrics>
  
  <compliance_metrics>
    <regulatory_compliance>Regulatory compliance percentage and audit results</regulatory_compliance>
    <audit_readiness>Audit readiness and compliance documentation completeness</audit_readiness>
    <risk_management>Risk assessment and mitigation effectiveness</risk_management>
    <data_governance>Data governance policy compliance and effectiveness</data_governance>
  </compliance_metrics>
</success_metrics>
```

---

**Reference**: This template provides comprehensive financial technology domain configuration, enabling specialized framework adaptation for fintech applications with security-first design, regulatory compliance, and high-performance transaction processing capabilities.