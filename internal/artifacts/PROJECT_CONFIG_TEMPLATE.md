# Project Configuration Template

This template contains all customizable insertion points for adapting the Claude Code Modular Prompts Framework to your specific project. Replace all [INSERT ...] tags with your project-specific values.

```xml
<project_configuration version="1.0.0">
  <!-- Basic Project Information -->
  <project_info>
    <name>[INSERT PROJECT NAME]</name>
    <domain>[INSERT DOMAIN: web-development | mobile-engineering | platform-engineering | data-analytics | etc.]</domain>
    <description>[INSERT PROJECT DESCRIPTION]</description>
    <primary_language>[INSERT PRIMARY LANGUAGE: python | javascript | typescript | go | rust | etc.]</primary_language>
    <framework_stack>[INSERT FRAMEWORKS: react+express | django | rails | etc.]</framework_stack>
  </project_info>

  <!-- Project Structure - Customize paths to match your project -->
  <project_structure>
    <root_directory>[INSERT ROOT: . | /workspace | /app]</root_directory>
    <source_directory>[INSERT SOURCE DIR: src | app | lib]</source_directory>
    <test_directory>[INSERT TEST DIR: tests | test | spec]</test_directory>
    <docs_directory>[INSERT DOCS DIR: docs | documentation]</docs_directory>
    <scripts_directory>[INSERT SCRIPTS DIR: scripts | bin | tools]</scripts_directory>
    <config_directory>[INSERT CONFIG DIR: config | .config | etc]</config_directory>
    <build_directory>[INSERT BUILD DIR: build | dist | out]</build_directory>
  </project_structure>

  <!-- Quality Standards - Adjust thresholds for your project -->
  <quality_standards>
    <test_coverage>
      <threshold>[INSERT COVERAGE THRESHOLD: 90]</threshold>
      <enforcement>[INSERT ENFORCEMENT: BLOCKING | CONDITIONAL | ADVISORY]</enforcement>
      <tool>[INSERT COVERAGE TOOL: pytest-cov | jest | nyc | go-cover]</tool>
    </test_coverage>
    <performance>
      <response_time_p95>[INSERT P95 THRESHOLD: 200ms]</response_time_p95>
      <response_time_p99>[INSERT P99 THRESHOLD: 500ms]</response_time_p99>
      <memory_limit>[INSERT MEMORY LIMIT: 512MB]</memory_limit>
    </performance>
    <code_quality>
      <linter>[INSERT LINTER: eslint | pylint | rubocop | golint]</linter>
      <formatter>[INSERT FORMATTER: prettier | black | gofmt]</formatter>
      <type_checker>[INSERT TYPE CHECKER: typescript | mypy | flow]</type_checker>
    </code_quality>
  </quality_standards>

  <!-- Development Workflow - Customize commands and processes -->
  <development_workflow>
    <commands>
      <install>[INSERT INSTALL CMD: npm install | pip install -r requirements.txt | go mod download]</install>
      <test>[INSERT TEST CMD: npm test | pytest | go test ./...]</test>
      <lint>[INSERT LINT CMD: npm run lint | pylint src | golint ./...]</lint>
      <build>[INSERT BUILD CMD: npm run build | python setup.py build | go build]</build>
      <run>[INSERT RUN CMD: npm start | python main.py | go run .]</run>
      <format>[INSERT FORMAT CMD: npm run format | black . | gofmt -w .]</format>
    </commands>
    <git_workflow>
      <branch_pattern>[INSERT BRANCH PATTERN: feature/* | feat/* | feature-*]</branch_pattern>
      <commit_style>[INSERT COMMIT STYLE: conventional | descriptive | ticket-based]</commit_style>
      <pr_template>[INSERT PR TEMPLATE: enabled | disabled]</pr_template>
    </git_workflow>
  </development_workflow>

  <!-- Token and Context Management -->
  <context_management>
    <max_file_tokens>[INSERT MAX FILE TOKENS: 4000]</max_file_tokens>
    <max_context_tokens>[INSERT MAX CONTEXT TOKENS: 120000]</max_context_tokens>
    <reserved_work_tokens>[INSERT RESERVED TOKENS: 50000]</reserved_work_tokens>
  </context_management>

  <!-- Domain-Specific Rules -->
  <domain_specific_rules>
    [INSERT DOMAIN RULES:
    <!-- Example for web development -->
    <rule>Use semantic HTML and ARIA attributes</rule>
    <rule>Implement responsive design with mobile-first approach</rule>
    <rule>Follow REST API conventions</rule>
    
    <!-- Example for mobile development -->
    <rule>Support iOS 14+ and Android 8+</rule>
    <rule>Implement proper lifecycle management</rule>
    <rule>Use platform-specific UI guidelines</rule>
    ]
  </domain_specific_rules>

  <!-- Custom Personas - Add project-specific expertise -->
  <custom_personas>
    [INSERT CUSTOM PERSONAS:
    <persona>
      <name>domain-expert</name>
      <expertise>Specific domain knowledge for this project</expertise>
      <tools>Domain-specific tools and frameworks</tools>
    </persona>
    ]
  </custom_personas>

  <!-- Security Requirements -->
  <security_requirements>
    <authentication>[INSERT AUTH METHOD: jwt | oauth2 | session | api-key]</authentication>
    <data_encryption>[INSERT ENCRYPTION: at-rest | in-transit | both]</data_encryption>
    <compliance>[INSERT COMPLIANCE: GDPR | HIPAA | SOC2 | PCI-DSS | none]</compliance>
    <vulnerability_scanning>[INSERT SCANNING: enabled | disabled]</vulnerability_scanning>
  </security_requirements>

  <!-- Deployment Configuration -->
  <deployment>
    <environment>[INSERT ENVIRONMENT: kubernetes | docker | serverless | vm]</environment>
    <ci_cd_tool>[INSERT CI/CD: github-actions | gitlab-ci | jenkins | circleci]</ci_cd_tool>
    <cloud_provider>[INSERT PROVIDER: aws | gcp | azure | on-premise]</cloud_provider>
    <monitoring>[INSERT MONITORING: datadog | prometheus | newrelic | custom]</monitoring>
  </deployment>

  <!-- Framework Behavior Customization -->
  <framework_behavior>
    <file_creation_policy>[INSERT POLICY: conservative | moderate | liberal]</file_creation_policy>
    <documentation_generation>[INSERT DOC GEN: automatic | on-request | disabled]</documentation_generation>
    <test_first_enforcement>[INSERT TDD: strict | flexible | advisory]</test_first_enforcement>
    <ai_temperature>
      <factual>[INSERT FACTUAL TEMP: 0.2]</factual>
      <analysis>[INSERT ANALYSIS TEMP: 0.3]</analysis>
      <creative>[INSERT CREATIVE TEMP: 0.7]</creative>
    </ai_temperature>
  </framework_behavior>

  <!-- Integration Points -->
  <integrations>
    <external_apis>
      [INSERT EXTERNAL APIS:
      <api>
        <name>Payment Gateway</name>
        <type>REST</type>
        <authentication>API Key</authentication>
      </api>
      ]
    </external_apis>
    <databases>
      [INSERT DATABASES:
      <database>
        <type>PostgreSQL</type>
        <orm>SQLAlchemy | Sequelize | GORM</orm>
      </database>
      ]
    </databases>
  </integrations>
</project_configuration>
```

## Instructions for Use

1. **Copy this template** to your project root as `PROJECT_CONFIG.xml`
2. **Replace all [INSERT ...] tags** with your project-specific values
3. **Remove unused sections** that don't apply to your project
4. **Run the initialization command**: `/init --config PROJECT_CONFIG.xml`
5. **The framework will adapt** all its components based on your configuration

## Examples

### Web Development Project
```xml
<project_info>
  <name>E-Commerce Platform</name>
  <domain>web-development</domain>
  <primary_language>typescript</primary_language>
  <framework_stack>react+nextjs+express</framework_stack>
</project_info>
```

### Mobile Engineering Project
```xml
<project_info>
  <name>Health Tracking App</name>
  <domain>mobile-engineering</domain>
  <primary_language>swift</primary_language>
  <framework_stack>swiftui+combine</framework_stack>
</project_info>
```

### Data Analytics Project
```xml
<project_info>
  <name>Customer Analytics Pipeline</name>
  <domain>data-analytics</domain>
  <primary_language>python</primary_language>
  <framework_stack>pandas+dask+airflow</framework_stack>
</project_info>
```