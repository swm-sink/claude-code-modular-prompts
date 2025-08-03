<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/security/secure-config.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>secure-config</component_id>
  <component_count>91</component_count>
  <category>security</category>
  <subcategory>configuration</subcategory>
  
  <complexity_metrics>
    <usage_complexity>high</usage_complexity>
    <implementation_effort>days_1</implementation_effort>
    <prerequisite_knowledge>expert</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="credential-protection" strength="strong"/>
      <component ref="owasp-compliance" strength="strong"/>
      <component ref="input-validation-framework" strength="medium"/>
      <component ref="path-validation" strength="medium"/>
      <component ref="error-handler" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="quick-command" reason="complexity_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>enterprise_configuration</common_workflow>
    <typical_position>infrastructure_foundation</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>security_configuration</primary_discovery_path>
    <alternative_paths>
      <path>secrets_management</path>
      <path>configuration_security</path>
      <path>compliance_management</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="standard" ref="security_frameworks_soc2_iso27001" relation="compliance_requirements"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="credential-protection" relation="secure_storage"/>
      <file type="component" ref="owasp-compliance" relation="security_configuration"/>
      <file type="command" ref="deploy" relation="configuration_security"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="harm-prevention-framework" similarity="0.65"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Enterprise applications requiring secure configuration management</scenario>
      <scenario>Applications handling sensitive credentials and secrets</scenario>
      <scenario>Compliance requirements for configuration security (SOC2, ISO27001)</scenario>
      <scenario>Multi-environment deployments with security isolation needs</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple applications without sensitive configuration needs</scenario>
      <scenario>Development-only environments without compliance requirements</scenario>
      <scenario>Static documentation or analysis tools</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>secure configuration management secrets encryption access control compliance audit configuration security</keywords>
    <semantic_tags>secure_configuration secrets_management compliance_security</semantic_tags>
    <functionality_vectors>configuration_security secrets_management compliance_validation</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../security/owasp-compliance.md" importance="critical"/>
      <context_file ref="../context/llm-antipatterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../security/credential-protection.md" importance="high"/>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>infrastructure_security</workflow_stage>
    <integration_patterns>
      <pattern>secure_configuration</pattern>
      <pattern>secrets_management</pattern>
      <pattern>compliance_enforcement</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>enterprise_configuration_security</concept_introduction>
    <skill_progression>expert</skill_progression>
    <mastery_indicators>
      <indicator>Advanced secrets management with encryption and rotation</indicator>
      <indicator>Comprehensive configuration security and compliance validation</indicator>
      <indicator>Enterprise-grade monitoring and audit trail systems</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

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