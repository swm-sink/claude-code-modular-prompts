| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Persona Customization Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="persona_customization" category="routing">
  
  <purpose>
    Enable project-specific customization of personas through configuration, allowing teams to adapt personas to their specific needs, add custom personas, and override default behaviors.
  </purpose>
  
  <customization_mechanisms>
    <override_existing_personas>
      <description>Modify specific attributes of existing personas</description>
      <capabilities>
        <capability>Override quality standards and success metrics</capability>
        <capability>Customize tool preferences for project stack</capability>
        <capability>Adjust experience level and expertise domain</capability>
        <capability>Modify decision priorities and trade-offs</capability>
      </capabilities>
      <implementation>
        <step>Load base persona from framework</step>
        <step>Apply PROJECT_CONFIG overrides</step>
        <step>Merge configurations with override precedence</step>
        <step>Validate resulting persona configuration</step>
      </implementation>
    </override_existing_personas>
    
    <add_custom_personas>
      <description>Define entirely new personas for project-specific roles</description>
      <capabilities>
        <capability>Create domain-specific expert personas</capability>
        <capability>Define custom quality gates and metrics</capability>
        <capability>Specify unique tool preferences and workflows</capability>
        <capability>Establish project-specific collaboration patterns</capability>
      </capabilities>
      <implementation>
        <step>Parse custom persona definition from PROJECT_CONFIG</step>
        <step>Validate persona structure and required fields</step>
        <step>Register persona in available persona pool</step>
        <step>Enable persona selection in routing decisions</step>
      </implementation>
    </add_custom_personas>
    
    <dynamic_attribute_injection>
      <description>Inject project-specific attributes into all personas</description>
      <capabilities>
        <capability>Add project-specific quality gates to all personas</capability>
        <capability>Inject custom tool configurations</capability>
        <capability>Apply global success metrics across personas</capability>
        <capability>Set project-wide risk tolerance levels</capability>
      </capabilities>
    </dynamic_attribute_injection>
  </customization_mechanisms>
  
  <configuration_schema>
    <persona_overrides>
      <format>
        [PROJECT_CONFIG: persona_overrides.backend_engineer | DEFAULT: none]
        <!-- Example override structure:
        <backend_engineer>
          <quality_standards>
            <success_metrics>
              <metric>API response time < 100ms for 99% of requests</metric>
              <metric>Custom project-specific metric</metric>
            </success_metrics>
          </quality_standards>
          <tool_preferences>
            <primary_tools>
              <tool>Rust/Actix-web for high-performance APIs</tool>
              <tool>ScyllaDB for distributed database</tool>
            </primary_tools>
          </tool_preferences>
        </backend_engineer>
        -->
      </format>
    </persona_overrides>
    
    <custom_personas>
      <format>
        [PROJECT_CONFIG: custom_personas | DEFAULT: none]
        <!-- Example custom persona:
        <blockchain_engineer>
          <persona_identity>
            <name>Blockchain Engineer</name>
            <expertise_domain>Distributed Ledger & Smart Contract Development</expertise_domain>
            <experience_level>Expert</experience_level>
          </persona_identity>
          <quality_standards>
            <mandatory_gates>
              <gate>Smart contract security audit</gate>
              <gate>Gas optimization verification</gate>
            </mandatory_gates>
          </quality_standards>
        </blockchain_engineer>
        -->
      </format>
    </custom_personas>
    
    <global_injections>
      <format>
        [PROJECT_CONFIG: persona_global_injections | DEFAULT: none]
        <!-- Applied to all personas:
        <all_personas>
          <additional_quality_gates>
            <gate>Compliance with project security standards</gate>
            <gate>Performance within project SLA requirements</gate>
          </additional_quality_gates>
          <required_tools>
            <tool>Company-specific CI/CD pipeline</tool>
            <tool>Internal code analysis tools</tool>
          </required_tools>
        </all_personas>
        -->
      </format>
    </global_injections>
  </configuration_schema>
  
  <integration_with_routing>
    <persona_selection>
      <description>Enhanced persona selection with custom personas</description>
      <process>
        <step>Include custom personas in available persona pool</step>
        <step>Apply overrides during persona activation</step>
        <step>Consider project-specific expertise in routing decisions</step>
        <step>Prioritize custom personas for domain-specific tasks</step>
      </process>
    </persona_selection>
    
    <auto_detection_enhancement>
      <description>Improve auto-detection with project context</description>
      <rules>
        <rule>Custom personas take precedence for matching domains</rule>
        <rule>Override attributes influence auto-detection scoring</rule>
        <rule>Project-specific patterns guide persona selection</rule>
      </rules>
    </auto_detection_enhancement>
  </integration_with_routing>
  
  <validation_and_safety>
    <structure_validation>
      <check>All required persona fields present</check>
      <check>Quality gates properly formatted</check>
      <check>Tool preferences valid and available</check>
      <check>No conflicts with framework safety rules</check>
    </structure_validation>
    
    <override_safety>
      <rule>Cannot override core safety requirements</rule>
      <rule>Cannot reduce minimum quality thresholds</rule>
      <rule>Cannot disable mandatory TDD enforcement</rule>
      <rule>Must maintain framework integrity</rule>
    </override_safety>
    
    <custom_persona_requirements>
      <requirement>Must define all mandatory fields</requirement>
      <requirement>Must specify quality standards</requirement>
      <requirement>Must include collaboration patterns</requirement>
      <requirement>Must be compatible with framework commands</requirement>
    </custom_persona_requirements>
  </validation_and_safety>
  
  <examples>
    <override_example>
      <scenario>Project using Rust instead of typical backend languages</scenario>
      <configuration>
</module>
</examples>
</override_example>
</configuration>
        ```xml
        <persona_overrides>
          <backend_engineer>
            <tool_preferences>
              <primary_tools>
                <tool>Rust/Actix-web for backend services</tool>
                <tool>Diesel ORM for database interactions</tool>
                <tool>cargo for dependency management</tool>
              </primary_tools>
            </tool_preferences>
            <quality_standards>
              <success_metrics>
                <metric>Memory safety verified by Rust compiler</metric>
                <metric>Zero unsafe blocks without justification</metric>
              </success_metrics>
            </quality_standards>
          </backend_engineer>
        </persona_overrides>
        ```
      </configuration>
    </override_example>
    
    <custom_persona_example>
      <scenario>Project needs ML operations engineer</scenario>
      <configuration>
        ```xml
        <custom_personas>
          <mlops_engineer>
            <persona_identity>
              <name>MLOps Engineer</name>
              <expertise_domain>Machine Learning Operations & Model Deployment</expertise_domain>
              <experience_level>Senior</experience_level>
            </persona_identity>
            <quality_standards>
              <mandatory_gates>
                <gate>Model performance validation</gate>
                <gate>Data pipeline integrity checks</gate>
                <gate>Model versioning and reproducibility</gate>
              </mandatory_gates>
              <success_metrics>
                <metric>Model inference latency < 50ms</metric>
                <metric>Pipeline data quality score > 95%</metric>
                <metric>Model drift detection in place</metric>
              </success_metrics>
            </quality_standards>
            <tool_preferences>
              <primary_tools>
                <tool>MLflow for model tracking</tool>
                <tool>Kubeflow for ML pipelines</tool>
                <tool>TensorFlow Serving for deployment</tool>
              </primary_tools>
            </tool_preferences>
          </mlops_engineer>
        </custom_personas>
        ```
      </configuration>
    </custom_persona_example>
  </examples>
  
  <performance_considerations>
    <caching>Cache merged persona configurations per session</caching>
    <lazy_loading>Only load and merge personas when activated</lazy_loading>
    <validation_timing>Validate custom personas during initialization only</validation_timing>
  </performance_considerations>
</module>
```