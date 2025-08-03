<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/security/owasp-compliance.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>owasp-compliance</component_id>
  <component_count>91</component_count>
  <category>security</category>
  <subcategory>compliance</subcategory>
  
  <complexity_metrics>
    <usage_complexity>high</usage_complexity>
    <implementation_effort>days_1</implementation_effort>
    <prerequisite_knowledge>expert</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="input-validation-framework" strength="strong"/>
      <component ref="credential-protection" strength="strong"/>
      <component ref="prompt-injection-prevention" strength="strong"/>
      <component ref="path-validation" strength="strong"/>
      <component ref="error-handler" strength="medium"/>
      <component ref="response-validator" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="quick-command" reason="security_complexity_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>enterprise_security</common_workflow>
    <typical_position>security_foundation</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>enterprise_security</primary_discovery_path>
    <alternative_paths>
      <path>compliance_framework</path>
      <path>owasp_standards</path>
      <path>security_governance</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="standard" ref="OWASP_Top_10_2025" relation="compliance_standard"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="input-validation-framework" relation="security_implementation"/>
      <file type="component" ref="credential-protection" relation="security_implementation"/>
      <file type="component" ref="prompt-injection-prevention" relation="security_implementation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="security-audit" similarity="0.75"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Enterprise applications requiring security compliance</scenario>
      <scenario>Applications handling sensitive or regulated data</scenario>
      <scenario>Security-first development methodologies</scenario>
      <scenario>Compliance audit and certification requirements</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple prototype or proof-of-concept applications</scenario>
      <scenario>Internal tools with no external access or sensitive data</scenario>
      <scenario>Learning or educational projects without compliance requirements</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>owasp compliance security standards enterprise governance top 10 2025 security framework</keywords>
    <semantic_tags>security_compliance enterprise_standards owasp_framework</semantic_tags>
    <functionality_vectors>compliance_checking security_governance standards_implementation</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>10</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../context/llm-antipatterns.md" importance="critical"/>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../security/credential-protection.md" importance="high"/>
      <context_file ref="../security/input-validation-framework.md" importance="high"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>security_foundation</workflow_stage>
    <integration_patterns>
      <pattern>enterprise_compliance</pattern>
      <pattern>security_governance</pattern>
      <pattern>standards_implementation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>enterprise_security_compliance</concept_introduction>
    <skill_progression>expert</skill_progression>
    <mastery_indicators>
      <indicator>Comprehensive OWASP Top 10 2025 compliance framework</indicator>
      <indicator>Enterprise-grade security standards implementation</indicator>
      <indicator>Automated security validation and compliance reporting</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

<prompt_component>
  <step name="OWASP Security Compliance Framework">
    <description>
Comprehensive OWASP Top 10 2025 compliance system that ensures secure code generation and validation. Provides automated security analysis, vulnerability prevention, and compliance verification for enterprise-grade security standards.
    </description>
  </step>

  <owasp_compliance>
    <security_framework>
      <!-- Implement OWASP Top 10 2025 compliance for all generated code -->
      <top_10_2025_compliance>
        <a01_broken_access_control>
          <prevention_patterns>
            - Implement principle of least privilege in all access controls
            - Use role-based access control (RBAC) with proper permission validation
            - Validate access permissions at the business logic layer, not just UI
            - Implement proper session management with secure session tokens
            - Use secure direct object references with authorization checks
          </prevention_patterns>
          
          <code_generation_rules>
            When generating authentication/authorization code:
            - Always validate user permissions before data access
            - Implement proper role checking mechanisms
            - Use parameterized access control patterns
            - Include audit logging for access control decisions
            - Validate ownership of resources before modification
          </code_generation_rules>
        </a01_broken_access_control>
        
        <a02_cryptographic_failures>
          <prevention_patterns>
            - Use strong, up-to-date cryptographic algorithms (AES-256, RSA-4096+)
            - Implement proper key management and rotation
            - Use secure random number generation for tokens and keys
            - Apply encryption for data at rest and in transit
            - Implement proper certificate validation for TLS
          </prevention_patterns>
          
          <code_generation_rules>
            When generating cryptographic code:
            - Use established crypto libraries, never custom implementations
            - Generate secure random salts for password hashing
            - Use bcrypt, scrypt, or Argon2 for password hashing
            - Implement proper IV generation for encryption
            - Validate all cryptographic parameters and keys
          </code_generation_rules>
        </a02_cryptographic_failures>
        
        <a03_injection>
          <prevention_patterns>
            - Use parameterized queries for all database interactions
            - Implement input validation and sanitization at all entry points
            - Use safe APIs and avoid shell command execution
            - Apply output encoding based on context (HTML, SQL, LDAP, etc.)
            - Implement Content Security Policy (CSP) for web applications
          </prevention_patterns>
          
          <code_generation_rules>
            When generating data access code:
            - Always use prepared statements or ORM query builders
            - Validate and sanitize all user inputs before processing
            - Use allowlist validation for user inputs where possible
            - Implement proper output encoding for dynamic content
            - Never concatenate user input directly into queries or commands
          </code_generation_rules>
        </a03_injection>
        
        <a04_insecure_design>
          <prevention_patterns>
            - Implement secure design patterns from the start
            - Use threat modeling to identify security requirements
            - Apply defense-in-depth principles throughout the architecture
            - Implement proper error handling that doesn't leak information
            - Use secure defaults for all configuration options
          </prevention_patterns>
          
          <code_generation_rules>
            When generating application architecture:
            - Design with security controls integrated, not bolted on
            - Implement proper separation of concerns for security
            - Use established security patterns and frameworks
            - Include security validations in business logic
            - Design for graceful failure and proper error handling
          </code_generation_rules>
        </a04_insecure_design>
        
        <a05_security_misconfiguration>
          <prevention_patterns>
            - Implement secure configuration management
            - Use infrastructure as code for consistent deployments
            - Apply security hardening to all system components
            - Implement regular security configuration reviews
            - Use automated security scanning in CI/CD pipelines
          </prevention_patterns>
          
          <code_generation_rules>
            When generating configuration code:
            - Use secure defaults for all configuration options
            - Implement configuration validation and security checks
            - Generate configuration with proper access controls
            - Include security headers and protective settings
            - Validate third-party component configurations
          </code_generation_rules>
        </a05_security_misconfiguration>
        
        <a06_vulnerable_components>
          <prevention_patterns>
            - Implement automated dependency vulnerability scanning
            - Use software composition analysis (SCA) tools
            - Maintain inventory of all components and dependencies
            - Apply security patches promptly and systematically
            - Use only necessary components with minimal attack surface
          </prevention_patterns>
          
          <code_generation_rules>
            When generating dependency usage:
            - Verify all dependencies against project requirements
            - Use specific versions rather than wildcards
            - Implement dependency validation and checking
            - Generate code that gracefully handles component failures
            - Include security update procedures in documentation
          </code_generation_rules>
        </a06_vulnerable_components>
        
        <a07_identification_authentication_failures>
          <prevention_patterns>
            - Implement multi-factor authentication where appropriate
            - Use strong session management with secure session tokens
            - Apply account lockout and rate limiting for failed attempts
            - Implement secure password recovery mechanisms
            - Use secure authentication protocols and standards
          </prevention_patterns>
          
          <code_generation_rules>
            When generating authentication code:
            - Implement proper password strength requirements
            - Use secure session token generation and validation
            - Include account lockout mechanisms for brute force protection
            - Generate secure password reset functionality
            - Implement proper logout and session invalidation
          </code_generation_rules>
        </a07_identification_authentication_failures>
        
        <a08_software_data_integrity_failures>
          <prevention_patterns>
            - Implement digital signatures for critical software updates
            - Use secure CI/CD pipelines with integrity validation
            - Apply input validation and deserialization safeguards
            - Implement data integrity checks and validation
            - Use secure backup and recovery procedures
          </prevention_patterns>
          
          <code_generation_rules>
            When generating data handling code:
            - Validate data integrity through checksums or signatures
            - Implement secure deserialization with allowlist validation
            - Generate code with proper data validation and sanitization
            - Include data backup and recovery mechanisms
            - Implement audit trails for data modifications
          </code_generation_rules>
        </a08_software_data_integrity_failures>
        
        <a09_security_logging_monitoring_failures>
          <prevention_patterns>
            - Implement comprehensive security event logging
            - Use centralized logging with proper access controls
            - Apply real-time monitoring and alerting for security events
            - Implement log integrity protection and retention policies
            - Use SIEM integration for security event correlation
          </prevention_patterns>
          
          <code_generation_rules>
            When generating logging code:
            - Log all security-relevant events (authentication, authorization, failures)
            - Implement structured logging with proper context information
            - Generate monitoring and alerting for suspicious activities
            - Include proper error handling without information disclosure
            - Implement log rotation and secure storage procedures
          </code_generation_rules>
        </a09_security_logging_monitoring_failures>
        
        <a10_server_side_request_forgery>
          <prevention_patterns>
            - Implement URL validation and allowlist filtering
            - Use network segmentation to limit server-side requests
            - Apply input validation for all URL parameters
            - Implement proper timeout and resource limits
            - Use DNS validation and IP address filtering
          </prevention_patterns>
          
          <code_generation_rules>
            When generating HTTP client code:
            - Validate all URLs against allowlist patterns
            - Implement proper timeout and connection limits
            - Use network policies to restrict outbound connections
            - Generate code with SSRF protection mechanisms
            - Include request validation and sanitization
          </code_generation_rules>
        </a10_server_side_request_forgery>
      </top_10_2025_compliance>
      
      <security_validation>
        <!-- Automated security validation during code generation -->
        <pre_generation_security_check>
          <threat_assessment>
            Before generating code, assess security implications:
            - Identify data flow and trust boundaries
            - Evaluate authentication and authorization requirements
            - Assess encryption and data protection needs
            - Consider input validation and output encoding requirements
          </threat_assessment>
          
          <security_pattern_selection>
            Select appropriate security patterns based on:
            - Application architecture and technology stack
            - Data sensitivity and protection requirements
            - Threat model and risk assessment results
            - Compliance and regulatory requirements
          </security_pattern_selection>
        </pre_generation_security_check>
        
        <real_time_security_validation>
          <code_analysis>
            During code generation, continuously validate:
            - Input validation and sanitization implementation
            - Authentication and authorization logic correctness
            - Cryptographic implementation and key management
            - Error handling and information disclosure prevention
          </code_analysis>
          
          <security_pattern_enforcement>
            Enforce security patterns throughout generation:
            - Use established security libraries and frameworks
            - Apply secure coding practices consistently
            - Implement defense-in-depth principles
            - Include proper security documentation and comments
          </security_pattern_enforcement>
        </real_time_security_validation>
        
        <post_generation_security_audit>
          <automated_security_scanning>
            After code generation, perform automated checks:
            - Static code analysis for security vulnerabilities
            - Dependency vulnerability scanning
            - Configuration security validation
            - Compliance verification against OWASP standards
          </automated_security_scanning>
          
          <security_testing_integration>
            Generate security testing alongside functional code:
            - Security unit tests for authentication and authorization
            - Integration tests for security controls
            - Penetration testing scripts for critical functionality
            - Security regression tests for ongoing validation
          </security_testing_integration>
        </post_generation_security_audit>
      </security_validation>
    </security_framework>
    
    <compliance_reporting>
      <!-- Generate compliance reports and documentation -->
      <owasp_compliance_matrix>
        <compliance_tracking>
          Track compliance status for each OWASP category:
          - Implementation status and coverage percentage
          - Security controls and their effectiveness
          - Remaining gaps and remediation plans
          - Regular compliance assessment and updates
        </compliance_tracking>
        
        <documentation_generation>
          Generate security documentation including:
          - Security architecture and design decisions
          - Threat model and risk assessment results
          - Security control implementation details
          - Compliance validation and testing results
        </documentation_generation>
      </owasp_compliance_matrix>
      
      <continuous_improvement>
        <security_learning>
          Learn from security implementations and outcomes:
          - Track security vulnerability patterns and prevention
          - Analyze security testing results and improvements
          - Incorporate new security threats and mitigations
          - Update security patterns based on industry best practices
        </security_learning>
        
        <compliance_evolution>
          Evolve compliance implementation based on:
          - OWASP standard updates and new recommendations
          - Industry security threat landscape changes
          - Project-specific security requirements and lessons learned
          - Regulatory and compliance requirement changes
        </compliance_evolution>
      </continuous_improvement>
    </compliance_reporting>
  </owasp_compliance>

  <o>
OWASP security compliance completed with comprehensive protection framework:

**Compliance Status:** [percentage]% OWASP Top 10 2025 compliance achieved
**Security Vulnerabilities:** [count] vulnerabilities prevented and mitigated
**Security Controls:** [count] security controls implemented and validated
**Risk Assessment:** [low/medium/high] overall security risk level
**Compliance Score:** [0-100] OWASP compliance effectiveness rating
**Security Certification:** [passed/failed] enterprise security standards validation
  </o>
</prompt_component> 