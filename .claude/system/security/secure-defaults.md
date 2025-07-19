| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-19   | stable |

# Secure Defaults Configuration Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="secure_defaults" category="security">
  
  <purpose>
    Enforce secure default configurations across all framework components with immutable security boundaries and defense-in-depth principles.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>component_type, configuration_request, security_context</required>
      <optional>user_overrides, compliance_requirements, risk_tolerance</optional>
    </inputs>
    <outputs>
      <success>secure_configuration, security_policy, compliance_status</success>
      <failure>configuration_violation, security_policy_breach, compliance_failure</failure>
    </outputs>
  </interface_contract>
  
  <immutable_security_defaults enforcement="BLOCKING">
    <core_security_settings>
      <security_validation>
        <enabled>true</enabled>
        <enforcement_level>BLOCKING</enforcement_level>
        <user_override>false</user_override>
        <description>Security validation cannot be disabled by users</description>
      </security_validation>
      <input_sanitization>
        <enabled>true</enabled>
        <strict_mode>true</strict_mode>
        <user_override>false</user_override>
        <description>Input sanitization always active with strict validation</description>
      </input_sanitization>
      <threat_monitoring>
        <enabled>true</enabled>
        <real_time>true</real_time>
        <user_override>false</user_override>
        <description>Continuous threat monitoring required for all operations</description>
      </threat_monitoring>
      <audit_logging>
        <enabled>true</enabled>
        <detailed_mode>true</detailed_mode>
        <user_override>false</user_override>
        <description>Comprehensive audit logging cannot be disabled</description>
      </audit_logging>
    </core_security_settings>
    
    <access_control_defaults>
      <file_system_access>
        <principle>least_privilege</principle>
        <default_permissions>read_only</default_permissions>
        <restricted_paths>/etc|/sys|/proc|~/.ssh|~/.aws</restricted_paths>
        <allowed_paths>./|.claude/|scripts/|docs/|examples/</allowed_paths>
      </file_system_access>
      <network_access>
        <default_policy>deny_all</default_policy>
        <whitelist_domains>docs.anthropic.com|github.com|api.github.com</whitelist_domains>
        <blacklist_domains>malware-domains.list|phishing-domains.list</blacklist_domains>
        <require_tls>true</require_tls>
      </network_access>
      <command_execution>
        <whitelist_commands>git|python|node|npm|pytest|eslint|test</whitelist_commands>
        <blacklist_commands>curl|wget|nc|telnet|ssh|sudo|rm -rf|dd</blacklist_commands>
        <execution_timeout>120_seconds</execution_timeout>
        <resource_limits>memory:512MB cpu:80% disk:1GB</resource_limits>
      </command_execution>
    </access_control_defaults>
  </immutable_security_defaults>
  
  <configurable_security_defaults enforcement="CONDITIONAL">
    <user_customizable_settings>
      <coverage_thresholds>
        <default>90%</default>
        <minimum>70%</minimum>
        <maximum>100%</maximum>
        <description>Test coverage thresholds can be adjusted within security bounds</description>
      </coverage_thresholds>
      <performance_targets>
        <response_time_p95>
          <default>200ms</default>
          <minimum>100ms</minimum>
          <maximum>2000ms</maximum>
        </response_time_p95>
        <description>Performance targets adjustable within operational bounds</description>
      </performance_targets>
      <development_tools>
        <allowed_tools>git,python,node,npm,pytest,eslint,typescript,go,rust</allowed_tools>
        <custom_tool_approval>security_team_required</custom_tool_approval>
        <description>Development tools can be customized with security approval</description>
      </development_tools>
    </user_customizable_settings>
    
    <security_policy_enforcement>
      <validation_rules>
        <rule name="no_security_reduction">
          <description>User configurations cannot reduce security below baseline</description>
          <enforcement>BLOCKING</enforcement>
          <validation>security_level >= baseline_security_level</validation>
        </rule>
        <rule name="compliance_maintenance">
          <description>All configurations must maintain compliance requirements</description>
          <enforcement>BLOCKING</enforcement>
          <validation>compliance_check(proposed_config) == PASS</validation>
        </rule>
        <rule name="threat_model_alignment">
          <description>Configurations must align with established threat models</description>
          <enforcement>CONDITIONAL</enforcement>
          <validation>threat_model_compatibility(config) >= ACCEPTABLE</validation>
        </rule>
      </validation_rules>
    </security_policy_enforcement>
  </configurable_security_defaults>
  
  <project_config_security enforcement="MANDATORY">
    <schema_validation>
      <xml_schema_enforcement>
        <enabled>true</enabled>
        <strict_validation>true</strict_validation>
        <user_schema_override>false</user_schema_override>
        <description>PROJECT_CONFIG.xml must conform to security-validated schema</description>
      </xml_schema_enforcement>
      <required_security_sections>
        <section name="security_standards" required="true">
          <minimum_fields>security_validation,threat_modeling,audit_logging</minimum_fields>
        </section>
        <section name="quality_standards" required="true">
          <minimum_fields>test_coverage,tdd_enforcement</minimum_fields>
        </section>
      </required_security_sections>
    </schema_validation>
    
    <configuration_integrity>
      <checksum_validation>
        <enabled>true</enabled>
        <algorithm>SHA-256</algorithm>
        <tamper_detection>true</tamper_detection>
        <action_on_tampering>BLOCK_EXECUTION_AND_ALERT</action_on_tampering>
      </checksum_validation>
      <digital_signatures>
        <required_for>production_configs</required_for>
        <certificate_validation>true</certificate_validation>
        <revocation_checking>true</revocation_checking>
      </digital_signatures>
    </configuration_integrity>
  </project_config_security>
  
  <external_tool_security_defaults enforcement="BLOCKING">
    <webfetch_defaults>
      <allowed_schemes>https</allowed_schemes>
      <timeout>30_seconds</timeout>
      <max_response_size>10MB</max_response_size>
      <domain_validation>required</domain_validation>
      <content_filtering>malware_detection_enabled</content_filtering>
      <user_agent>Claude-Framework-WebFetch/1.0 (Security-Enabled)</user_agent>
    </webfetch_defaults>
    
    <websearch_defaults>
      <query_sanitization>strict</query_sanitization>
      <result_filtering>safe_content_only</result_filtering>
      <domain_restrictions>reputable_sources_only</domain_restrictions>
      <rate_limiting>60_requests_per_hour</rate_limiting>
      <content_validation>required</content_validation>
    </websearch_defaults>
    
    <bash_execution_defaults>
      <execution_timeout>120_seconds</execution_timeout>
      <resource_limits>memory:512MB cpu:80%</resource_limits>
      <command_validation>whitelist_only</command_validation>
      <output_sanitization>enabled</output_sanitization>
      <environment_isolation>true</environment_isolation>
    </bash_execution_defaults>
  </external_tool_security_defaults>
  
  <security_monitoring_defaults enforcement="MANDATORY">
    <logging_configuration>
      <security_events>
        <level>INFO</level>
        <format>JSON_STRUCTURED</format>
        <retention>90_days</retention>
        <encryption>AES-256</encryption>
      </security_events>
      <audit_trail>
        <level>DEBUG</level>
        <format>JSON_STRUCTURED</format>
        <retention>365_days</retention>
        <integrity_protection>SHA-256_CHAIN</integrity_protection>
      </audit_trail>
    </logging_configuration>
    
    <alerting_configuration>
      <critical_alerts>
        <delivery>immediate</delivery>
        <channels>email,slack,sms</channels>
        <escalation>security_team</escalation>
      </critical_alerts>
      <warning_alerts>
        <delivery>within_15_minutes</delivery>
        <channels>email,slack</channels>
        <escalation>development_team</escalation>
      </warning_alerts>
    </alerting_configuration>
  </security_monitoring_defaults>
  
  <compliance_enforcement enforcement="BLOCKING">
    <regulatory_standards>
      <gdpr_compliance>
        <data_minimization>enabled</data_minimization>
        <consent_management>not_applicable</consent_management>
        <right_to_deletion>manual_process</right_to_deletion>
        <data_protection_officer>security_team</data_protection_officer>
      </gdpr_compliance>
      <sox_compliance>
        <audit_trail>comprehensive</audit_trail>
        <change_management>documented_approval</change_management>
        <access_controls>role_based</access_controls>
        <internal_controls>automated_testing</internal_controls>
      </sox_compliance>
      <iso27001_compliance>
        <information_security_policy>documented</information_security_policy>
        <risk_management>threat_modeling</risk_management>
        <access_control>principle_of_least_privilege</access_control>
        <incident_management>documented_procedures</incident_management>
      </iso27001_compliance>
    </regulatory_standards>
    
    <framework_specific_compliance>
      <claude_code_standards>
        <security_validation>mandatory</security_validation>
        <tdd_enforcement>strict</tdd_enforcement>
        <quality_gates>blocking</quality_gates>
        <atomic_operations>guaranteed</atomic_operations>
      </claude_code_standards>
      <ai_safety_standards>
        <output_filtering>enabled</output_filtering>
        <content_validation>strict</content_validation>
        <bias_detection>monitoring</bias_detection>
        <harmful_content_prevention>blocking</harmful_content_prevention>
      </ai_safety_standards>
    </framework_specific_compliance>
  </compliance_enforcement>
  
  <integration_points>
    <depends_on>
      system/security/command-security-integration.md for security pipeline integration
      system/security/threat-modeling.md for threat analysis alignment
      system/quality/universal-quality-gates.md for quality-security integration
    </depends_on>
    <provides_to>
      ALL framework components for secure default configuration
      PROJECT_CONFIG.xml for baseline security requirements
      commands/ for secure execution defaults
      modules/ for security-first implementation patterns
    </provides_to>
  </integration_points>
  
  <emergency_security_procedures enforcement="CRITICAL">
    <security_lockdown>
      <trigger_conditions>
        <multiple_security_violations>3_violations_in_5_minutes</multiple_security_violations>
        <critical_threat_detected>threat_level_HIGH_or_CRITICAL</critical_threat_detected>
        <compliance_breach>regulatory_violation_detected</compliance_breach>
      </trigger_conditions>
      <lockdown_actions>
        <immediate>Stop all command execution</immediate>
        <isolate>Disconnect external network access</isolate>
        <preserve>Capture full system state</preserve>
        <notify>Alert security team with highest priority</notify>
      </lockdown_actions>
      <recovery_requirements>
        <security_clearance>Manual security team approval required</security_clearance>
        <system_validation>Complete security audit before resumption</system_validation>
        <configuration_review>All configurations must be re-validated</configuration_review>
      </recovery_requirements>
    </security_lockdown>
  </emergency_security_procedures>
  
</module>
```