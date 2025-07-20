# Context Templates Library

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-20   | production |

## Purpose

Comprehensive library of reusable context templates for domain-specific optimization, project type templates, team preference patterns, and context inheritance system for maximum development efficiency.

## Architecture Overview

```xml
<context_templates_library version="1.0.0" enforcement="CRITICAL">
  <purpose>Reusable context templates with intelligent inheritance and customization</purpose>
  
  <template_categories>
    <category name="domain_specific" count="12">
      <description>Templates optimized for specific technical domains</description>
      <examples>web_development, data_science, mobile_apps, devops, security</examples>
      <inheritance>Domain base → Technology stack → Project specifics</inheritance>
    </category>
    
    <category name="project_types" count="8">
      <description>Templates based on project structure and methodology</description>
      <examples>microservices, monolith, library, cli_tool, api, frontend</examples>
      <inheritance>Project type → Architecture patterns → Implementation details</inheritance>
    </category>
    
    <category name="team_preferences" count="6">
      <description>Templates based on team size, experience, and preferences</description>
      <examples>startup, enterprise, solo_dev, remote_team, junior_team</examples>
      <inheritance>Team context → Workflow preferences → Quality standards</inheritance>
    </category>
    
    <category name="workflow_patterns" count="10">
      <description>Templates for specific development workflows</description>
      <examples>tdd_strict, agile_sprints, continuous_deployment, research_heavy</examples>
      <inheritance>Workflow base → Process specifics → Tool configurations</inheritance>
    </category>
  </template_categories>
  
  <template_composition>
    <base_template>Core framework patterns and quality gates</base_template>
    <domain_layer>Domain-specific patterns and best practices</domain_layer>
    <project_layer>Project-specific configuration and preferences</project_layer>
    <team_layer>Team workflow and collaboration patterns</team_layer>
    <custom_layer>User-specific customizations and overrides</custom_layer>
  </template_composition>
  
  <inheritance_system>
    <pattern>child_template extends parent_template with override_capabilities</pattern>
    <resolution>Custom → Team → Project → Domain → Base (highest priority first)</resolution>
    <validation>Ensure all template layers are compatible and consistent</validation>
  </inheritance_system>
</context_templates_library>
```

## Domain-Specific Templates

### Web Development Template

```xml
<template name="web_development" extends="base_framework" version="1.0.0">
  <domain_context>
    <tech_stack>
      <frontend>React, Vue, Angular, Svelte, vanilla JS</frontend>
      <backend>Node.js, Python, Go, Java, PHP</backend>
      <database>PostgreSQL, MongoDB, Redis, SQLite</database>
      <deployment>Docker, Kubernetes, Vercel, Netlify, AWS</deployment>
    </tech_stack>
    
    <common_patterns>
      <pattern name="component_architecture">
        <description>Reusable UI components with proper separation</description>
        <files>components/, hooks/, utils/, styles/</files>
        <quality_gates>Component testing, accessibility, performance</quality_gates>
      </pattern>
      
      <pattern name="api_design">
        <description>RESTful or GraphQL API design patterns</description>
        <files>routes/, controllers/, middleware/, models/</files>
        <quality_gates>API testing, documentation, security validation</quality_gates>
      </pattern>
      
      <pattern name="state_management">
        <description>Client-side state management patterns</description>
        <files>store/, reducers/, actions/, selectors/</files>
        <quality_gates>State testing, immutability, performance</quality_gates>
      </pattern>
    </common_patterns>
    
    <quality_standards>
      <accessibility>WCAG 2.1 AA compliance required</accessibility>
      <performance>Core Web Vitals within acceptable ranges</performance>
      <security>OWASP Top 10 vulnerability prevention</security>
      <testing>Unit tests for components and functions, integration tests for user flows</testing>
    </quality_standards>
    
    <development_workflow>
      <commands>
        <dev_server>npm run dev / yarn dev</dev_server>
        <build>npm run build / yarn build</build>
        <test>npm test / yarn test</test>
        <lint>eslint src/ --fix</lint>
        <type_check>tsc --noEmit</type_check>
      </commands>
      
      <file_structure>
        <source>src/components/, src/pages/, src/utils/</source>
        <tests>__tests__/, *.test.js, *.spec.js</tests>
        <config>package.json, tsconfig.json, .eslintrc</config>
        <build>dist/, build/, .next/</build>
      </file_structure>
    </development_workflow>
  </domain_context>
  
  <command_optimizations>
    <task_command>
      <focus>Single component or utility function</focus>
      <context>Component file, test file, related utilities</context>
      <validation>Component rendering, props validation, accessibility</validation>
    </task_command>
    
    <feature_command>
      <focus>Complete user feature with UI and backend</focus>
      <context>User stories, API design, component hierarchy</context>
      <validation>End-to-end user flow, API integration, performance</validation>
    </feature_command>
    
    <query_command>
      <focus>Architecture understanding, performance analysis</focus>
      <context>Component relationships, data flow, bundle analysis</context>
      <analysis>Dependency analysis, performance bottlenecks, security review</analysis>
    </query_command>
  </command_optimizations>
</template>
```

### Data Science Template

```xml
<template name="data_science" extends="base_framework" version="1.0.0">
  <domain_context>
    <tech_stack>
      <languages>Python, R, Julia, SQL</languages>
      <frameworks>pandas, numpy, scikit-learn, tensorflow, pytorch</frameworks>
      <tools>Jupyter, conda, docker, git-lfs</tools>
      <visualization>matplotlib, seaborn, plotly, bokeh</visualization>
    </tech_stack>
    
    <common_patterns>
      <pattern name="data_pipeline">
        <description>ETL/ELT pipelines with data validation</description>
        <files>data/, pipelines/, transforms/, validators/</files>
        <quality_gates>Data quality tests, pipeline monitoring, lineage tracking</quality_gates>
      </pattern>
      
      <pattern name="model_development">
        <description>ML model development with experiment tracking</description>
        <files>models/, experiments/, features/, evaluation/</files>
        <quality_gates>Model validation, performance metrics, bias detection</quality_gates>
      </pattern>
      
      <pattern name="reproducible_research">
        <description>Reproducible analysis with environment management</description>
        <files>notebooks/, reports/, environment.yml, requirements.txt</files>
        <quality_gates>Reproducibility tests, documentation, version control</quality_gates>
      </pattern>
    </common_patterns>
    
    <quality_standards>
      <data_quality>Completeness, accuracy, consistency, timeliness validation</data_quality>
      <model_quality>Cross-validation, bias detection, interpretability</model_quality>
      <reproducibility>Environment specification, data versioning, experiment tracking</reproducibility>
      <documentation>Data dictionaries, model cards, analysis documentation</documentation>
    </quality_standards>
    
    <development_workflow>
      <commands>
        <environment>conda env create -f environment.yml</environment>
        <notebook>jupyter lab</notebook>
        <test>pytest tests/</test>
        <lint>flake8 src/ --max-line-length=88</lint>
        <format>black src/ && isort src/</format>
      </commands>
      
      <file_structure>
        <data>data/raw/, data/processed/, data/external/</data>
        <code>src/data/, src/features/, src/models/</code>
        <notebooks>notebooks/exploratory/, notebooks/reports/</notebooks>
        <outputs>models/, reports/, figures/</outputs>
      </file_structure>
    </development_workflow>
  </domain_context>
  
  <command_optimizations>
    <task_command>
      <focus>Single analysis function or data transformation</focus>
      <context>Data schema, transformation logic, validation tests</context>
      <validation>Data quality checks, unit tests, performance benchmarks</validation>
    </task_command>
    
    <feature_command>
      <focus>Complete analysis pipeline or model development</focus>
      <context>Research question, data sources, analysis plan</context>
      <validation>End-to-end pipeline test, model evaluation, documentation</validation>
    </feature_command>
    
    <query_command>
      <focus>Data exploration, model analysis, performance investigation</focus>
      <context>Data characteristics, model performance, system metrics</context>
      <analysis>Statistical analysis, model interpretability, bottleneck identification</analysis>
    </query_command>
  </command_optimizations>
</template>
```

### DevOps Template

```xml
<template name="devops" extends="base_framework" version="1.0.0">
  <domain_context>
    <tech_stack>
      <infrastructure>Docker, Kubernetes, Terraform, Ansible</infrastructure>
      <cloud_platforms>AWS, GCP, Azure, DigitalOcean</cloud_platforms>
      <monitoring>Prometheus, Grafana, ELK Stack, DataDog</monitoring>
      <ci_cd>GitHub Actions, GitLab CI, Jenkins, CircleCI</ci_cd>
    </tech_stack>
    
    <common_patterns>
      <pattern name="infrastructure_as_code">
        <description>Declarative infrastructure management</description>
        <files>terraform/, ansible/, k8s/, docker/</files>
        <quality_gates>Infrastructure testing, security scanning, cost optimization</quality_gates>
      </pattern>
      
      <pattern name="ci_cd_pipeline">
        <description>Automated build, test, and deployment pipelines</description>
        <files>.github/workflows/, .gitlab-ci.yml, Jenkinsfile</files>
        <quality_gates>Pipeline testing, security checks, deployment validation</quality_gates>
      </pattern>
      
      <pattern name="observability">
        <description>Comprehensive monitoring and alerting</description>
        <files>monitoring/, alerts/, dashboards/</files>
        <quality_gates>SLA monitoring, alert effectiveness, incident response</quality_gates>
      </pattern>
    </common_patterns>
    
    <quality_standards>
      <reliability>99.9% uptime SLA, automated failover, disaster recovery</reliability>
      <security>Security scanning, secrets management, access control</security>
      <scalability>Auto-scaling, load testing, performance monitoring</scalability>
      <compliance>SOC2, GDPR, audit trails, change management</compliance>
    </quality_standards>
    
    <development_workflow>
      <commands>
        <infrastructure>terraform plan && terraform apply</infrastructure>
        <containers>docker build . && docker run</containers>
        <kubernetes>kubectl apply -f k8s/</kubernetes>
        <test>ansible-playbook --check playbook.yml</test>
        <validate>terraform validate && ansible-lint</validate>
      </commands>
      
      <file_structure>
        <infrastructure>terraform/, ansible/, k8s/</infrastructure>
        <containers>Dockerfile, docker-compose.yml</containers>
        <ci_cd>.github/workflows/, scripts/</ci_cd>
        <monitoring>monitoring/, alerts/</monitoring>
      </file_structure>
    </development_workflow>
  </domain_context>
  
  <command_optimizations>
    <task_command>
      <focus>Single infrastructure component or pipeline step</focus>
      <context>Infrastructure state, dependencies, security requirements</context>
      <validation>Infrastructure tests, security scans, deployment verification</validation>
    </task_command>
    
    <feature_command>
      <focus>Complete infrastructure feature or deployment pipeline</focus>
      <context>Requirements, architecture, compliance needs</context>
      <validation>End-to-end deployment test, security validation, monitoring setup</validation>
    </feature_command>
    
    <protocol_command>
      <focus>Production deployments and incident response</focus>
      <context>Production environment, rollback plans, monitoring dashboards</context>
      <safety>Blue-green deployments, health checks, automated rollback</safety>
    </protocol_command>
  </command_optimizations>
</template>
```

## Project Type Templates

### Microservices Template

```python
class MicroservicesTemplate:
    """Template for microservices architecture projects"""
    
    def __init__(self):
        self.template_config = {
            'architecture_patterns': {
                'service_decomposition': 'Domain-driven design with bounded contexts',
                'communication': 'Event-driven with message queues and REST APIs',
                'data_management': 'Database per service pattern',
                'deployment': 'Containerized with orchestration'
            },
            
            'quality_standards': {
                'service_testing': 'Unit, integration, contract, and end-to-end tests',
                'monitoring': 'Distributed tracing and service mesh observability',
                'resilience': 'Circuit breakers, bulkheads, timeouts',
                'security': 'Service-to-service authentication and authorization'
            },
            
            'development_patterns': {
                'service_structure': {
                    'api': 'REST/GraphQL endpoints',
                    'business_logic': 'Domain services and entities',
                    'data_access': 'Repository pattern with ORM',
                    'infrastructure': 'External service integrations'
                },
                
                'cross_cutting_concerns': {
                    'logging': 'Structured logging with correlation IDs',
                    'configuration': 'Environment-based configuration',
                    'health_checks': 'Liveness and readiness probes',
                    'metrics': 'Application and business metrics'
                }
            }
        }
        
    def get_service_context(self, service_name: str) -> dict:
        """Get context template for specific service"""
        return {
            'service_identity': {
                'name': service_name,
                'bounded_context': self._determine_bounded_context(service_name),
                'responsibilities': self._get_service_responsibilities(service_name),
                'dependencies': self._analyze_service_dependencies(service_name)
            },
            
            'technical_context': {
                'technology_stack': self._get_tech_stack_for_service(service_name),
                'data_storage': self._get_storage_requirements(service_name),
                'communication_patterns': self._get_communication_patterns(service_name),
                'deployment_requirements': self._get_deployment_config(service_name)
            },
            
            'quality_context': {
                'testing_strategy': self._get_testing_strategy(service_name),
                'monitoring_requirements': self._get_monitoring_config(service_name),
                'security_requirements': self._get_security_requirements(service_name),
                'performance_targets': self._get_performance_targets(service_name)
            }
        }
        
    def optimize_commands_for_microservices(self) -> dict:
        """Optimize framework commands for microservices development"""
        return {
            'task': {
                'scope': 'Single service component or cross-cutting concern',
                'context': 'Service boundaries, API contracts, data schemas',
                'validation': 'Service tests, contract validation, integration checks'
            },
            
            'feature': {
                'scope': 'Complete business capability across services',
                'context': 'Domain model, service interactions, data flow',
                'validation': 'End-to-end scenarios, performance testing, security validation'
            },
            
            'swarm': {
                'scope': 'Coordinated changes across multiple services',
                'context': 'Service dependency graph, deployment order, rollback plans',
                'coordination': 'Service-specific agents with cross-service orchestration'
            },
            
            'protocol': {
                'scope': 'Production deployments with service coordination',
                'context': 'Service health, dependency readiness, traffic management',
                'safety': 'Rolling deployments, canary releases, circuit breaker monitoring'
            }
        }
```

### Library Template

```python
class LibraryTemplate:
    """Template for library/package development"""
    
    def __init__(self):
        self.template_config = {
            'architecture_patterns': {
                'api_design': 'Clear, consistent, and backward-compatible public APIs',
                'modularity': 'Logical module organization with minimal dependencies',
                'extensibility': 'Plugin architecture and customization points',
                'performance': 'Optimized for common use cases with lazy loading'
            },
            
            'quality_standards': {
                'api_stability': 'Semantic versioning with deprecation policies',
                'documentation': 'Comprehensive API docs with examples',
                'testing': '95%+ code coverage with integration examples',
                'compatibility': 'Multiple language/platform version support'
            },
            
            'development_patterns': {
                'public_api': {
                    'interface_design': 'Intuitive method names and parameter patterns',
                    'error_handling': 'Consistent exception hierarchy and error messages',
                    'configuration': 'Sensible defaults with override capabilities',
                    'extensibility': 'Hook points and customization interfaces'
                },
                
                'internal_structure': {
                    'core_functionality': 'Essential features with minimal dependencies',
                    'optional_features': 'Modular components with optional dependencies',
                    'utilities': 'Internal helpers and common functionality',
                    'testing_utilities': 'Test helpers and fixtures for users'
                }
            }
        }
        
    def get_library_context(self, library_type: str) -> dict:
        """Get context template for specific library type"""
        return {
            'library_identity': {
                'purpose': self._determine_library_purpose(library_type),
                'target_audience': self._identify_target_users(library_type),
                'use_cases': self._document_primary_use_cases(library_type),
                'ecosystem_position': self._analyze_ecosystem_fit(library_type)
            },
            
            'technical_context': {
                'api_surface': self._design_api_surface(library_type),
                'dependencies': self._manage_dependencies(library_type),
                'platform_support': self._define_platform_support(library_type),
                'performance_requirements': self._establish_performance_targets(library_type)
            },
            
            'user_experience': {
                'getting_started': self._create_onboarding_flow(library_type),
                'documentation_strategy': self._plan_documentation(library_type),
                'example_gallery': self._design_example_set(library_type),
                'migration_guides': self._prepare_migration_support(library_type)
            }
        }
```

## Team Preference Templates

### Startup Team Template

```xml
<template name="startup_team" extends="base_framework" version="1.0.0">
  <team_context>
    <characteristics>
      <size>2-10 developers</size>
      <experience>Mixed levels, learning-oriented</experience>
      <velocity>High iteration speed, MVP focus</velocity>
      <resources>Limited budget, time constraints</resources>
    </characteristics>
    
    <workflow_preferences>
      <methodology>Lean startup with rapid prototyping</methodology>
      <planning>Short sprints, flexible requirements</planning>
      <quality_balance>Functional over perfect, tech debt managed</quality_balance>
      <communication>Informal, high-bandwidth collaboration</communication>
    </workflow_preferences>
    
    <technology_choices>
      <criteria>Fast development, proven solutions, minimal complexity</criteria>
      <stack_preference>Popular, well-documented, community-supported</stack_preference>
      <tooling>Free/low-cost tools, SaaS solutions</tooling>
      <deployment>Simple, automated, cloud-native</deployment>
    </technology_choices>
  </team_context>
  
  <framework_optimizations>
    <command_defaults>
      <task>Focus on speed and functionality over perfection</task>
      <feature>MVP approach with iterative enhancement</feature>
      <query>Prioritize actionable insights over comprehensive analysis</query>
      <docs>Minimal viable documentation with user focus</docs>
    </command_defaults>
    
    <quality_adjustments>
      <test_coverage>70% minimum, focus on critical paths</test_coverage>
      <code_review>Lightweight, learning-focused</code_review>
      <documentation>Essential only, inline comments preferred</documentation>
      <performance>Good enough for current scale, optimize later</performance>
    </quality_adjustments>
    
    <workflow_patterns>
      <development_cycle>Feature → Test → Deploy → Learn → Iterate</development_cycle>
      <decision_making>Rapid experimentation over extensive planning</decision_making>
      <technical_debt>Tracked but balanced against feature velocity</technical_debt>
      <knowledge_sharing>Pair programming, informal documentation</knowledge_sharing>
    </workflow_patterns>
  </framework_optimizations>
</template>
```

### Enterprise Team Template

```xml
<template name="enterprise_team" extends="base_framework" version="1.0.0">
  <team_context>
    <characteristics>
      <size>20-100+ developers across multiple teams</size>
      <experience>Senior developers with specialized expertise</experience>
      <velocity>Measured progress with quality emphasis</velocity>
      <resources>Adequate budget, compliance requirements</resources>
    </characteristics>
    
    <workflow_preferences>
      <methodology>Scaled agile with governance frameworks</methodology>
      <planning>Quarterly planning with detailed requirements</planning>
      <quality_balance>High quality standards, comprehensive testing</quality_balance>
      <communication>Formal processes, documented decisions</communication>
    </workflow_preferences>
    
    <compliance_requirements>
      <security>Security reviews, threat modeling, compliance audits</security>
      <quality>Code reviews, architectural reviews, quality gates</quality>
      <documentation>Comprehensive documentation, change logs</documentation>
      <process>Standardized workflows, approval processes</process>
    </compliance_requirements>
  </team_context>
  
  <framework_optimizations>
    <command_defaults>
      <task>Comprehensive testing and documentation required</task>
      <feature>Full design review and implementation planning</feature>
      <protocol>Extensive safety checks and rollback procedures</protocol>
      <docs>Comprehensive documentation with stakeholder review</docs>
    </command_defaults>
    
    <quality_requirements>
      <test_coverage>90%+ coverage with multiple test types</test_coverage>
      <code_review>Mandatory peer review with security check</code_review>
      <documentation>Architecture docs, API docs, user guides</documentation>
      <performance>Performance testing and optimization required</performance>
    </quality_requirements>
    
    <governance_patterns>
      <architectural_decisions>ADR process with stakeholder approval</architectural_decisions>
      <change_management>Formal change requests and impact analysis</change_management>
      <risk_management>Risk assessment and mitigation planning</risk_management>
      <compliance_tracking>Audit trails and compliance verification</compliance_tracking>
    </governance_patterns>
  </framework_optimizations>
</template>
```

## Workflow Pattern Templates

### TDD Strict Template

```python
class TDDStrictTemplate:
    """Template for strict TDD workflow"""
    
    def __init__(self):
        self.workflow_rules = {
            'red_phase': {
                'requirement': 'Write failing test first, always',
                'validation': 'Test must fail for the right reason',
                'tools': 'Test frameworks with immediate feedback',
                'duration': 'Keep cycles short, 2-5 minutes max'
            },
            
            'green_phase': {
                'requirement': 'Minimal code to make test pass',
                'validation': 'All tests must pass',
                'approach': 'Simplest implementation first',
                'refactoring': 'Not allowed in green phase'
            },
            
            'refactor_phase': {
                'requirement': 'Improve code while keeping tests green',
                'validation': 'Tests must remain passing throughout',
                'focus': 'Code quality, design patterns, performance',
                'safety': 'Continuous test execution'
            }
        }
        
    def optimize_commands_for_tdd(self) -> dict:
        """Optimize framework commands for strict TDD"""
        return {
            'task': {
                'red_phase': 'Write failing test with clear assertions',
                'green_phase': 'Implement minimal solution to pass test',
                'refactor_phase': 'Improve implementation while maintaining tests',
                'validation': 'Each phase must be completed before proceeding'
            },
            
            'feature': {
                'acceptance_tests': 'Write high-level acceptance tests first',
                'unit_tests': 'TDD cycle for each component',
                'integration': 'Test component interactions',
                'system': 'End-to-end scenario validation'
            }
        }
        
    def create_tdd_context(self, task_description: str) -> dict:
        """Create TDD-optimized context for task"""
        return {
            'test_strategy': self._design_test_strategy(task_description),
            'implementation_order': self._plan_implementation_order(task_description),
            'refactoring_opportunities': self._identify_refactoring_points(task_description),
            'quality_gates': self._define_quality_checkpoints(task_description)
        }
```

## Context Inheritance System

```python
class ContextInheritanceSystem:
    """Manage context template inheritance and composition"""
    
    def __init__(self):
        self.template_registry = {}
        self.inheritance_graph = {}
        self.resolution_cache = {}
        
    def register_template(self, name: str, template: dict, extends: str = None):
        """Register a context template with optional inheritance"""
        self.template_registry[name] = template
        
        if extends:
            if extends not in self.inheritance_graph:
                self.inheritance_graph[extends] = []
            self.inheritance_graph[extends].append(name)
            
    def resolve_template(self, template_name: str, overrides: dict = None) -> dict:
        """Resolve template with inheritance and overrides"""
        if template_name in self.resolution_cache:
            base_context = self.resolution_cache[template_name]
        else:
            base_context = self._build_inherited_context(template_name)
            self.resolution_cache[template_name] = base_context
            
        # Apply overrides
        if overrides:
            resolved_context = self._apply_overrides(base_context, overrides)
        else:
            resolved_context = base_context
            
        return resolved_context
        
    def _build_inherited_context(self, template_name: str) -> dict:
        """Build context by traversing inheritance chain"""
        inheritance_chain = self._get_inheritance_chain(template_name)
        
        # Start with base template
        context = {}
        
        # Apply templates in inheritance order (parent to child)
        for template in inheritance_chain:
            template_config = self.template_registry[template]
            context = self._merge_contexts(context, template_config)
            
        return context
        
    def _get_inheritance_chain(self, template_name: str) -> list:
        """Get complete inheritance chain for template"""
        chain = []
        current = template_name
        
        while current:
            chain.insert(0, current)  # Insert at beginning for correct order
            current = self._get_parent_template(current)
            
        return chain
        
    def _merge_contexts(self, base: dict, overlay: dict) -> dict:
        """Intelligently merge two context dictionaries"""
        merged = base.copy()
        
        for key, value in overlay.items():
            if key in merged:
                if isinstance(value, dict) and isinstance(merged[key], dict):
                    merged[key] = self._merge_contexts(merged[key], value)
                elif isinstance(value, list) and isinstance(merged[key], list):
                    merged[key] = merged[key] + value  # Append lists
                else:
                    merged[key] = value  # Override value
            else:
                merged[key] = value
                
        return merged
        
    def create_custom_template(self, base_template: str, customizations: dict) -> dict:
        """Create custom template based on existing template"""
        base_context = self.resolve_template(base_template)
        custom_context = self._apply_overrides(base_context, customizations)
        
        return custom_context
        
    def validate_template_compatibility(self, template_name: str) -> dict:
        """Validate template compatibility and consistency"""
        try:
            resolved = self.resolve_template(template_name)
            
            validation_results = {
                'valid': True,
                'inheritance_chain': self._get_inheritance_chain(template_name),
                'conflicts': self._detect_conflicts(resolved),
                'missing_required': self._check_required_fields(resolved),
                'recommendations': self._generate_recommendations(resolved)
            }
            
        except Exception as e:
            validation_results = {
                'valid': False,
                'error': str(e),
                'recommendations': ['Fix inheritance chain or template structure']
            }
            
        return validation_results

# Usage examples
def setup_project_context():
    """Example: Set up project-specific context"""
    inheritance_system = ContextInheritanceSystem()
    
    # Register base and specialized templates
    inheritance_system.register_template('base_framework', BASE_FRAMEWORK_TEMPLATE)
    inheritance_system.register_template('web_development', WEB_DEV_TEMPLATE, extends='base_framework')
    inheritance_system.register_template('react_spa', REACT_SPA_TEMPLATE, extends='web_development')
    
    # Create project-specific context
    project_overrides = {
        'tech_stack': {'frontend': 'React 18', 'backend': 'Node.js'},
        'team_preferences': {'startup_team': True},
        'quality_standards': {'test_coverage': 80}
    }
    
    project_context = inheritance_system.resolve_template('react_spa', project_overrides)
    return project_context
```

## Template Optimization Engine

```python
class TemplateOptimizationEngine:
    """Optimize context templates based on usage patterns"""
    
    def __init__(self):
        self.usage_analytics = {}
        self.performance_metrics = {}
        self.optimization_rules = {}
        
    def analyze_template_usage(self, template_name: str, usage_data: dict):
        """Analyze how templates are used in practice"""
        if template_name not in self.usage_analytics:
            self.usage_analytics[template_name] = {
                'total_uses': 0,
                'common_overrides': {},
                'performance_impact': {},
                'user_satisfaction': {}
            }
            
        analytics = self.usage_analytics[template_name]
        analytics['total_uses'] += 1
        
        # Track common override patterns
        for override_key, override_value in usage_data.get('overrides', {}).items():
            if override_key not in analytics['common_overrides']:
                analytics['common_overrides'][override_key] = {}
            
            value_key = str(override_value)
            if value_key in analytics['common_overrides'][override_key]:
                analytics['common_overrides'][override_key][value_key] += 1
            else:
                analytics['common_overrides'][override_key][value_key] = 1
                
    def optimize_template(self, template_name: str) -> dict:
        """Generate optimized template based on usage patterns"""
        if template_name not in self.usage_analytics:
            return {'status': 'insufficient_data'}
            
        analytics = self.usage_analytics[template_name]
        current_template = self.template_registry[template_name]
        
        optimization_suggestions = {
            'common_defaults': self._suggest_default_improvements(analytics),
            'remove_unused': self._identify_unused_features(analytics),
            'add_shortcuts': self._suggest_shortcuts(analytics),
            'performance_improvements': self._suggest_performance_optimizations(analytics)
        }
        
        return optimization_suggestions
        
    def generate_usage_report(self) -> dict:
        """Generate comprehensive template usage report"""
        report = {
            'template_popularity': {},
            'override_patterns': {},
            'performance_analysis': {},
            'optimization_opportunities': {}
        }
        
        for template_name, analytics in self.usage_analytics.items():
            report['template_popularity'][template_name] = analytics['total_uses']
            report['override_patterns'][template_name] = analytics['common_overrides']
            
            # Identify optimization opportunities
            opportunities = self.optimize_template(template_name)
            if opportunities['status'] != 'insufficient_data':
                report['optimization_opportunities'][template_name] = opportunities
                
        return report
```

## Performance Targets

- **Template Resolution**: <500ms for complex inheritance chains
- **Context Building**: <2 seconds for comprehensive domain context
- **Override Application**: <100ms for standard customizations
- **Cache Hit Ratio**: >85% for frequently used templates
- **Memory Efficiency**: <1MB total template storage
- **Inheritance Depth**: Maximum 5 levels for maintainability

## Integration with Framework Commands

```xml
<command_integration>
  <automatic_template_selection>
    <trigger>Project initialization or context establishment</trigger>
    <mechanism>Analyze project structure and configuration to select optimal template</mechanism>
    <fallback>User selection from categorized template library</fallback>
  </automatic_template_selection>
  
  <dynamic_context_adaptation>
    <trigger>Command execution with insufficient context</trigger>
    <mechanism>Load appropriate template sections based on command requirements</mechanism>
    <optimization>Cache loaded template sections for session reuse</optimization>
  </dynamic_context_adaptation>
  
  <template_evolution>
    <trigger>Usage pattern analysis and optimization opportunities</trigger>
    <mechanism>Suggest template improvements based on real usage data</mechanism>
    <validation>A/B testing of template variations for effectiveness</validation>
  </template_evolution>
</command_integration>
```

This completes I24 - Context Templates Library with comprehensive domain-specific templates, project type templates, team preference patterns, and an intelligent inheritance system for maximum customization and efficiency.