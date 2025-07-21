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