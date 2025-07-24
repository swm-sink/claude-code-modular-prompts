---
description: Advanced enterprise examples with industry best practices, scalable architectures, and comprehensive implementation patterns
argument-hint: "[enterprise_domain] [example_complexity]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /enterprise examples - Advanced Enterprise Examples

Sophisticated enterprise examples system with industry best practices, scalable architectures, and comprehensive implementation patterns.

## Usage
```bash
/enterprise examples architecture            # Enterprise architecture examples
/enterprise examples --scalability           # Scalability pattern examples
/enterprise examples --security              # Security implementation examples
/enterprise examples --comprehensive         # Comprehensive enterprise patterns
```

<command_file>
  <metadata>
    <n>/enterprise-examples</n>
    <purpose>Generate comprehensive enterprise-grade examples, templates, and implementation patterns for the Claude Code Prompt Factory across various industries and use cases.</purpose>
    <usage>
      <![CDATA[
      /enterprise-examples "[use_case]" --industry=[healthcare|finance|manufacturing|government|tech] --complexity=[basic|advanced|enterprise]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="use_case" type="string" required="true">
      <description>Target use case or scenario (e.g., "onboarding", "compliance-audit", "global-deployment", "security-implementation").</description>
    </argument>
    <argument name="industry" type="string" required="false" default="tech">
      <description>Industry context: healthcare, finance, manufacturing, government, tech, retail, education.</description>
    </argument>
    <argument name="complexity" type="string" required="false" default="advanced">
      <description>Complexity level: basic (simple examples), advanced (comprehensive), enterprise (full-scale implementation).</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate healthcare compliance examples</description>
      <usage>/enterprise-examples "compliance-audit" --industry=healthcare --complexity=enterprise</usage>
    </example>
    <example>
      <description>Create financial services onboarding templates</description>
      <usage>/enterprise-examples "team-onboarding" --industry=finance --complexity=advanced</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <include component="components/context/adaptive-thinking.md" />
      <include component="components/learning/examples-library.md" />
      <include component="components/analytics/business-intelligence.md" />

      You are an expert enterprise solutions architect with extensive experience in creating comprehensive implementation examples, templates, and best practices across multiple industries. Generate practical, production-ready examples for the Claude Code Prompt Factory.

      **Enterprise Examples Intelligence Framework**:

      <examples_framework>
        <use_case_scenarios>
          **Comprehensive Use Case Scenarios**:
          - **Team Onboarding**: Complete team setup, training, and productivity acceleration
          - **Compliance Audit**: Regulatory compliance validation and audit preparation
          - **Global Deployment**: Multi-region deployment with localization and cultural adaptation
          - **Security Implementation**: Enterprise security hardening and threat mitigation
          - **Performance Optimization**: System performance analysis and optimization
          - **Quality Assurance**: Comprehensive quality management and testing
          - **Integration Projects**: Complex system integration and API management
          - **Innovation Initiatives**: Emerging technology adoption and implementation
          - **Crisis Response**: Incident response and business continuity
          - **Ecosystem Growth**: Platform expansion and marketplace development
        </use_case_scenarios>
        
        <industry_contexts>
          **Industry-Specific Implementation Contexts**:
          - **Healthcare**: HIPAA compliance, patient data protection, clinical workflows
          - **Finance**: PCI DSS compliance, fraud detection, trading systems, regulatory reporting
          - **Manufacturing**: Industrial IoT, supply chain optimization, quality control
          - **Government**: FedRAMP compliance, citizen services, interagency collaboration
          - **Technology**: DevOps automation, cloud-native architecture, API-first design
          - **Retail**: E-commerce optimization, omnichannel experience, customer analytics
          - **Education**: FERPA compliance, learning analytics, accessibility standards
        </industry_contexts>
        
        <complexity_levels>
          **Implementation Complexity Levels**:
          - **Basic**: Fundamental examples with essential patterns and practices
          - **Advanced**: Comprehensive implementations with sophisticated features
          - **Enterprise**: Full-scale, production-ready implementations with all enterprise features
        </complexity_levels>
      </examples_framework>

      **Enterprise Template Generation**:

      <template_generation>
        <workflow_templates>
          **End-to-End Workflow Templates**:
          - **Project Initialization**: Complete project setup with configuration and structure
          - **Development Workflows**: TDD, CI/CD, code review, and quality assurance processes
          - **Deployment Patterns**: Blue-green, canary, and rolling deployment strategies
          - **Monitoring Setup**: Comprehensive observability and alerting configuration
          - **Security Hardening**: Complete security implementation and compliance validation
          - **Performance Optimization**: Systematic performance analysis and improvement
        </workflow_templates>
        
        <configuration_templates>
          **Configuration and Setup Templates**:
          - **PROJECT_CONFIG.xml**: Industry-specific configuration templates
          - **Environment Setup**: Development, staging, and production environment configuration
          - **Security Configuration**: Security policies, access controls, and compliance settings
          - **Performance Configuration**: Performance optimization and monitoring settings
          - **Integration Configuration**: API integration, third-party service setup
          - **Compliance Configuration**: Regulatory compliance and audit trail setup
        </configuration_templates>
        
        <command_sequences>
          **Practical Command Sequence Examples**:
          - **Daily Development**: Common development task sequences and patterns
          - **Project Delivery**: Complete project delivery workflow from inception to deployment
          - **Maintenance Operations**: Ongoing maintenance, updates, and optimization tasks
          - **Crisis Management**: Incident response and recovery command sequences
          - **Compliance Activities**: Audit preparation and regulatory compliance workflows
          - **Innovation Projects**: Technology adoption and integration command patterns
        </command_sequences>
      </template_generation>

      **Industry-Specific Implementation Examples**:

      <industry_implementations>
        <healthcare_examples>
          **Healthcare Industry Implementation**:
          - **Patient Data Platform**: HIPAA-compliant patient data management system
          - **Clinical Decision Support**: AI-powered clinical decision assistance tools
          - **Telemedicine Platform**: Secure remote healthcare delivery system
          - **Medical Device Integration**: FDA-compliant medical device data integration
          - **Research Data Management**: Clinical research data processing and analysis
          - **Compliance Monitoring**: Continuous HIPAA compliance monitoring and reporting
        </healthcare_examples>
        
        <finance_examples>
          **Financial Services Implementation**:
          - **Trading Platform**: High-frequency trading system with risk management
          - **Payment Processing**: PCI DSS-compliant payment processing system
          - **Fraud Detection**: Real-time fraud detection and prevention system
          - **Regulatory Reporting**: Automated compliance reporting and audit trails
          - **Digital Banking**: Customer-facing digital banking platform
          - **Risk Management**: Comprehensive risk assessment and mitigation system
        </finance_examples>
        
        <manufacturing_examples>
          **Manufacturing Industry Implementation**:
          - **Industrial IoT Platform**: Connected manufacturing and predictive maintenance
          - **Supply Chain Optimization**: End-to-end supply chain visibility and optimization
          - **Quality Control System**: Automated quality assurance and defect detection
          - **Production Planning**: AI-powered production scheduling and resource optimization
          - **Safety Management**: Comprehensive workplace safety monitoring and compliance
          - **Digital Twin**: Virtual factory modeling and simulation platform
        </manufacturing_examples>
      </industry_implementations>

      **Enterprise Implementation Patterns**:

      <implementation_patterns>
        <scalability_patterns>
          **Enterprise Scalability Implementation**:
          - **Multi-Tenant Architecture**: Scalable multi-organization deployment patterns
          - **Global Distribution**: Multi-region deployment with data sovereignty
          - **Auto-Scaling**: Intelligent resource scaling and cost optimization
          - **Load Balancing**: Advanced load distribution and traffic management
          - **Performance Optimization**: Enterprise-grade performance tuning and monitoring
          - **Disaster Recovery**: Comprehensive business continuity and disaster recovery
        </scalability_patterns>
        
        <integration_patterns>
          **System Integration Implementation**:
          - **API Gateway**: Enterprise API management and security
          - **Event-Driven Architecture**: Scalable event processing and workflow automation
          - **Data Integration**: Enterprise data pipeline and analytics implementation
          - **Legacy System Integration**: Modern integration with legacy systems
          - **Third-Party Integration**: Secure integration with external services and partners
          - **Microservices Architecture**: Cloud-native microservices implementation
        </integration_patterns>
        
        <security_patterns>
          **Enterprise Security Implementation**:
          - **Zero Trust Architecture**: Comprehensive zero-trust security implementation
          - **Identity Management**: Enterprise identity and access management
          - **Data Protection**: Advanced data encryption and privacy protection
          - **Threat Detection**: Real-time threat detection and response
          - **Compliance Automation**: Automated compliance monitoring and reporting
          - **Security Operations**: Security operations center (SOC) implementation
        </security_patterns>
      </implementation_patterns>

      **Example Generation Workflow**:

      <generation_workflow>
        <requirements_analysis>
          **Use Case Requirements Analysis**:
          1. Analyze target use case and identify specific requirements and constraints
          2. Map industry-specific regulations, standards, and best practices
          3. Assess complexity requirements and implementation scope
          4. Identify integration points and system dependencies
          5. Plan example structure and implementation approach
        </requirements_analysis>
        
        <template_creation>
          **Template and Example Creation**:
          1. Generate comprehensive configuration templates and setup examples
          2. Create step-by-step implementation workflows and command sequences
          3. Develop industry-specific customizations and compliance patterns
          4. Build integration examples and system architecture patterns
          5. Create validation and testing examples for quality assurance
        </template_creation>
        
        <documentation_generation>
          **Comprehensive Documentation**:
          1. Generate detailed implementation guides and best practices
          2. Create troubleshooting guides and common issue resolution
          3. Develop training materials and onboarding documentation
          4. Build reference materials and quick-start guides
          5. Create maintenance and operational procedures
        </documentation_generation>
        
        <validation_testing>
          **Example Validation and Testing**:
          1. Validate all examples for correctness and completeness
          2. Test implementation patterns in various scenarios and environments
          3. Verify compliance with industry standards and regulations
          4. Assess performance and scalability characteristics
          5. Document known limitations and optimization opportunities
        </validation_testing>
      </generation_workflow>

      **Practical Implementation Examples**:

      <practical_examples>
        <onboarding_example>
          **Enterprise Team Onboarding Example**:
          ```
          # Day 1: Framework Setup and Configuration
          /existing --scan-deep --generate-config
          /industry-adapt "fintech" --compliance=strict
          /security-scan --level=enterprise
          
          # Day 2: Development Environment Setup
          /dev-setup --env=team --security=enterprise
          /cicd-setup --strategy=gitops --security=devsecops
          /monitoring-setup --level=enterprise
          
          # Week 1: Team Training and Best Practices
          /help --mode=training --role=developer
          /quality-enforce --standards=enterprise
          /performance-benchmark --baseline=true
          ```
        </onboarding_example>
        
        <compliance_example>
          **Healthcare Compliance Audit Example**:
          ```
          # Pre-Audit Preparation
          /industry-adapt "healthcare" --compliance=strict
          /security-audit --standard=hipaa --depth=comprehensive
          /docs-generate --type=compliance --standard=hipaa
          
          # Audit Execution
          /quality-report --compliance=hipaa --evidence=true
          /error-trace --audit-mode --retention=7years
          /backup-create --encryption=hipaa --verification=true
          
          # Post-Audit Optimization
          /secure-fix --findings=audit --priority=critical
          /monitor-setup --compliance=hipaa --alerting=required
          ```
        </compliance_example>
        
        <deployment_example>
          **Global Enterprise Deployment Example**:
          ```
          # Multi-Region Deployment Strategy
          /global-deploy "US,EU,APAC" --strategy=blue-green
          /industry-adapt "finance" --compliance=auto
          /performance-optimize --target=global --scale=enterprise
          
          # Regional Customization
          /global-deploy "EU" --localize=gdpr --compliance=strict
          /global-deploy "APAC" --localize=auto --performance=edge
          
          # Monitoring and Optimization
          /monitor-dashboard --global=true --sla=enterprise
          /cost-analyze --multi-region --optimization=auto
          ```
        </deployment_example>
      </practical_examples>

      Generate comprehensive, production-ready examples and templates using Claude's deep understanding of enterprise requirements, industry best practices, and implementation patterns. Focus on practical, actionable examples that teams can immediately implement and customize for their specific needs.

      **Remember**: Enterprise examples must be comprehensive, compliant, and immediately actionable. Include all necessary configuration, security considerations, and operational procedures to ensure successful implementation.
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/adaptive-thinking.md</component>
      <component>components/learning/examples-library.md</component>
      <component>components/analytics/business-intelligence.md</component>
    </includes_components>
    <uses_config_values>
      <config>industry_sector</config>
      <config>complexity_requirements</config>
      <config>compliance_standards</config>
      <config>deployment_scope</config>
    </uses_config_values>
  </dependencies>
</command_file> 