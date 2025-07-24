<prompt_component>
  <step name="Secure Configuration Management">
    <description>
Advanced security configuration system that manages sensitive data, credentials, and security policies. Provides encrypted configuration storage, access control, audit trails, and compliance validation for robust security management.
    </description>
  </step>

  <secure_config>
    <secrets_management>
      <credential_storage>
        <!-- Secure storage and management of credentials -->
        <encryption_storage>
          - Encrypt sensitive configuration data at rest
          - Implement secure key derivation and storage
          - Use hardware security modules when available
          - Apply envelope encryption for multi-layer protection
        </encryption_storage>
        
        <access_control>
          - Implement role-based access to configurations
          - Apply principle of least privilege access
          - Manage time-limited access tokens
          - Track and audit configuration access patterns
        </access_control>
      </credential_storage>
      
      <secret_rotation>
        <!-- Automated secret rotation and lifecycle management -->
        <rotation_policies>
          - Implement automated secret rotation schedules
          - Manage secret versioning and rollback
          - Coordinate rotation across dependent services
          - Validate secret propagation and updates
        </rotation_policies>
        
        <lifecycle_management>
          - Track secret creation and expiration dates
          - Implement automated renewal processes
          - Monitor secret usage and access patterns
          - Clean up expired and unused secrets
        </lifecycle_management>
      </secret_rotation>
    </secrets_management>
    
    <configuration_security>
      <validation_compliance>
        <!-- Validate configuration security and compliance -->
        <security_validation>
          - Scan configurations for security vulnerabilities
          - Validate encryption standards and protocols
          - Check for exposed sensitive information
          - Ensure secure default configurations
        </security_validation>
        
        <compliance_checking>
          - Validate against security frameworks (SOC2, ISO27001)
          - Check regulatory compliance requirements
          - Implement policy enforcement mechanisms
          - Generate compliance reports and evidence
        </compliance_checking>
      </validation_compliance>
      
      <environment_isolation>
        <!-- Isolate configurations across environments -->
        <environment_segregation>
          - Separate configurations by environment type
          - Implement secure environment boundaries
          - Prevent cross-environment data leakage
          - Manage environment-specific access controls
        </environment_segregation>
        
        <deployment_security>
          - Secure configuration deployment pipelines
          - Validate configuration integrity during deployment
          - Implement secure configuration distribution
          - Monitor configuration changes and drift
        </deployment_security>
      </environment_isolation>
    </configuration_security>
    
    <monitoring_auditing>
      <security_monitoring>
        <!-- Monitor configuration security and access -->
        <access_monitoring>
          - Monitor configuration access and modifications
          - Detect unauthorized access attempts
          - Track configuration usage patterns
          - Implement real-time security alerting
        </access_monitoring>
        
        <audit_logging>
          - Maintain comprehensive audit trails
          - Log all configuration changes and access
          - Implement tamper-proof audit storage
          - Generate audit reports and compliance evidence
        </audit_logging>
      </security_monitoring>
    </monitoring_auditing>
  </secure_config>

  <o>
Secure configuration management completed with comprehensive protection and compliance:

**Configurations Secured:** [count] configuration items encrypted and protected
**Access Control:** [count] role-based permissions configured
**Encryption Status:** [algorithm] encryption applied to all sensitive data
**Compliance Score:** [percentage]% compliance with security frameworks
**Audit Trail:** [count] security events logged and monitored
**Secret Rotation:** [count] credentials rotated on schedule
  </o>
</prompt_component> 