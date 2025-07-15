# Advanced Usage Guide

## Overview
This guide covers advanced techniques for power users who want to extend and customize the Claude Code Modular Prompts Framework. These techniques are for users who have mastered the [Foundation](../user-guide/README.md#foundation-level) and [Intermediate](../user-guide/README.md#intermediate-level) levels.

## Table of Contents
1. [Custom Modules](#custom-modules)
2. [Meta-Prompting](#meta-prompting)
3. [Framework Customization](#framework-customization)
4. [Performance Optimization](#performance-optimization)
5. [Team Integration](#team-integration)
6. [Advanced Workflows](#advanced-workflows)

## Custom Modules

### Creating Custom Modules
While the framework has a fixed command set, you can create custom modules to extend functionality:

```xml
<!-- PROJECT_CONFIG.xml -->
<custom_modules>
  <module name="security-scanner">
    <description>Custom security scanning module</description>
    <trigger>security scan</trigger>
    <implementation>custom_security_scan.py</implementation>
  </module>
  <module name="performance-profiler">
    <description>Custom performance profiling</description>
    <trigger>performance profile</trigger>
    <implementation>custom_profiler.py</implementation>
  </module>
</custom_modules>
```

### Module Structure
```python
# custom_security_scan.py
class SecurityScanModule:
    def __init__(self, config):
        self.config = config
        self.tools = ['bandit', 'safety', 'semgrep']
    
    def analyze(self, codebase):
        """Analyze codebase for security vulnerabilities"""
        results = {
            'vulnerabilities': [],
            'severity_counts': {},
            'recommendations': []
        }
        
        # Run security tools
        for tool in self.tools:
            tool_results = self.run_tool(tool, codebase)
            results['vulnerabilities'].extend(tool_results)
        
        return results
    
    def run_tool(self, tool, codebase):
        """Run specific security tool"""
        # Implementation depends on tool
        pass
    
    def generate_report(self, results):
        """Generate security report"""
        report = f"""
        # Security Analysis Report
        
        ## Summary
        - Total vulnerabilities: {len(results['vulnerabilities'])}
        - High severity: {results['severity_counts'].get('high', 0)}
        - Medium severity: {results['severity_counts'].get('medium', 0)}
        - Low severity: {results['severity_counts'].get('low', 0)}
        
        ## Recommendations
        """
        
        for recommendation in results['recommendations']:
            report += f"- {recommendation}\n"
        
        return report
```

### Integration with Framework
```bash
# Use custom module through /auto
/auto "run security scan on user authentication module"

# Framework will detect custom module and use it
```

## Meta-Prompting

### Understanding Meta-Prompting
Meta-prompting allows the framework to improve itself based on usage patterns:

```bash
# Analyze and improve framework performance
/meta-review "analyze framework effectiveness over last month"

# Adapt framework to specific patterns
/meta-evolve "optimize for microservices architecture patterns"

# Continuous optimization
/meta-optimize "improve response time and accuracy"
```

### Custom Meta-Prompting Patterns
```xml
<!-- PROJECT_CONFIG.xml -->
<meta_prompting>
  <learning_patterns>
    <pattern name="domain-specific">
      <description>Learn domain-specific patterns</description>
      <trigger>domain expertise</trigger>
      <focus>business logic, data models, workflows</focus>
    </pattern>
    <pattern name="team-workflow">
      <description>Adapt to team coding patterns</description>
      <trigger>team adaptation</trigger>
      <focus>code style, review process, deployment</focus>
    </pattern>
  </learning_patterns>
  
  <optimization_targets>
    <target name="response-time">
      <metric>average_response_time</metric>
      <threshold>30</threshold>
      <unit>seconds</unit>
    </target>
    <target name="accuracy">
      <metric>implementation_accuracy</metric>
      <threshold>95</threshold>
      <unit>percentage</unit>
    </target>
  </optimization_targets>
</meta_prompting>
```

### Advanced Meta-Command Usage
```bash
# Analyze specific aspects
/meta-review "analyze code quality improvements over time"
/meta-review "evaluate TDD compliance and effectiveness"
/meta-review "assess framework adaptation to our domain"

# Targeted optimization
/meta-optimize "improve accuracy of database query optimization"
/meta-optimize "enhance understanding of React component patterns"

# Specialized evolution
/meta-evolve "adapt to our microservices testing patterns"
/meta-evolve "learn from our deployment automation preferences"
```

## Framework Customization

### Domain-Specific Customization
```xml
<!-- PROJECT_CONFIG.xml for E-commerce -->
<domain_expertise>
  <type>e-commerce</type>
  <industry>retail</industry>
  <specialization>backend</specialization>
  
  <domain_patterns>
    <pattern name="product-catalog">
      <description>Product catalog management patterns</description>
      <components>Product, Category, Inventory, Pricing</components>
    </pattern>
    <pattern name="order-processing">
      <description>Order processing workflow patterns</description>
      <components>Cart, Order, Payment, Fulfillment</components>
    </pattern>
    <pattern name="user-management">
      <description>Customer management patterns</description>
      <components>User, Profile, Authentication, Authorization</components>
    </pattern>
  </domain_patterns>
  
  <business_rules>
    <rule name="inventory-validation">
      <description>Always validate inventory before order processing</description>
      <enforcement>blocking</enforcement>
    </rule>
    <rule name="price-calculation">
      <description>Include tax and shipping in price calculations</description>
      <enforcement>warning</enforcement>
    </rule>
  </business_rules>
</domain_expertise>
```

### Architecture-Specific Customization
```xml
<!-- PROJECT_CONFIG.xml for Microservices -->
<architecture>
  <type>microservices</type>
  <communication>rest-api</communication>
  <data_consistency>eventual</data_consistency>
  
  <service_patterns>
    <pattern name="api-gateway">
      <description>API Gateway pattern for service coordination</description>
      <implementation>Kong, Zuul, or custom</implementation>
    </pattern>
    <pattern name="circuit-breaker">
      <description>Circuit breaker for fault tolerance</description>
      <implementation>Hystrix, Resilience4j</implementation>
    </pattern>
    <pattern name="saga-pattern">
      <description>Saga pattern for distributed transactions</description>
      <implementation>Choreography or Orchestration</implementation>
    </pattern>
  </service_patterns>
  
  <monitoring>
    <distributed_tracing>Jaeger</distributed_tracing>
    <metrics>Prometheus</metrics>
    <logging>ELK Stack</logging>
  </monitoring>
</architecture>
```

### Quality Standards Customization
```xml
<!-- PROJECT_CONFIG.xml -->
<quality_standards>
  <test_coverage>
    <threshold>95</threshold>
    <enforcement>blocking</enforcement>
    <exclusions>
      <exclude>migrations/</exclude>
      <exclude>settings/</exclude>
    </exclusions>
  </test_coverage>
  
  <code_quality>
    <complexity_threshold>10</complexity_complexity>
    <line_length>120</line_length>
    <function_length>50</function_length>
  </code_quality>
  
  <security>
    <vulnerability_scan>enabled</vulnerability_scan>
    <dependency_check>enabled</dependency_check>
    <secrets_detection>enabled</secrets_detection>
  </security>
  
  <performance>
    <response_time_p95>200</response_time_p95>
    <memory_usage_threshold>512</memory_usage_threshold>
    <database_query_limit>100</database_query_limit>
  </performance>
</quality_standards>
```

## Performance Optimization

### Context Optimization
```xml
<!-- PROJECT_CONFIG.xml -->
<context_optimization>
  <max_file_tokens>4000</max_file_tokens>
  <max_context_tokens>150000</max_context_tokens>
  <reserved_work_tokens>60000</reserved_work_tokens>
  
  <hierarchical_loading>
    <enabled>true</enabled>
    <priority_files>
      <file>src/models/</file>
      <file>src/services/</file>
      <file>tests/</file>
    </priority_files>
  </hierarchical_loading>
  
  <compression>
    <enabled>true</enabled>
    <threshold>50000</threshold>
    <strategy>semantic</strategy>
  </compression>
</context_optimization>
```

### Parallel Processing
```xml
<!-- PROJECT_CONFIG.xml -->
<parallel_processing>
  <enabled>true</enabled>
  <max_concurrent_tasks>4</max_concurrent_tasks>
  
  <task_coordination>
    <strategy>dependency-aware</strategy>
    <conflict_resolution>sequential</conflict_resolution>
  </task_coordination>
  
  <resource_allocation>
    <cpu_limit>80</cpu_limit>
    <memory_limit>4096</memory_limit>
  </resource_allocation>
</parallel_processing>
```

### Caching Strategy
```xml
<!-- PROJECT_CONFIG.xml -->
<caching>
  <enabled>true</enabled>
  <ttl>3600</ttl>
  
  <cache_types>
    <type name="analysis">
      <enabled>true</enabled>
      <ttl>7200</ttl>
    </type>
    <type name="dependencies">
      <enabled>true</enabled>
      <ttl>1800</ttl>
    </type>
    <type name="test-results">
      <enabled>true</enabled>
      <ttl>600</ttl>
    </type>
  </cache_types>
</caching>
```

## Team Integration

### Multi-Developer Workflows
```xml
<!-- PROJECT_CONFIG.xml -->
<team_workflow>
  <developers>
    <developer name="backend-team">
      <specialization>backend</specialization>
      <preferences>
        <testing_framework>pytest</testing_framework>
        <code_style>black</code_style>
      </preferences>
    </developer>
    <developer name="frontend-team">
      <specialization>frontend</specialization>
      <preferences>
        <testing_framework>jest</testing_framework>
        <code_style>prettier</code_style>
      </preferences>
    </developer>
  </developers>
  
  <collaboration>
    <code_review>
      <required>true</required>
      <reviewers>2</reviewers>
      <approval_required>true</approval_required>
    </code_review>
    
    <pair_programming>
      <enabled>true</enabled>
      <session_length>2</session_length>
      <rotation_schedule>daily</rotation_schedule>
    </pair_programming>
  </collaboration>
</team_workflow>
```

### Shared Configuration Management
```bash
# Team configuration sharing
git add PROJECT_CONFIG.xml
git commit -m "Update team configuration for new quality standards"

# Environment-specific overrides
cp PROJECT_CONFIG.xml PROJECT_CONFIG.development.xml
cp PROJECT_CONFIG.xml PROJECT_CONFIG.production.xml
```

### Knowledge Sharing
```xml
<!-- PROJECT_CONFIG.xml -->
<knowledge_sharing>
  <documentation>
    <auto_generate>true</auto_generate>
    <formats>markdown, wiki, confluence</formats>
    <update_frequency>weekly</update_frequency>
  </documentation>
  
  <best_practices>
    <capture_patterns>true</capture_patterns>
    <share_learnings>true</share_learnings>
    <create_examples>true</create_examples>
  </best_practices>
</knowledge_sharing>
```

## Advanced Workflows

### Complex Feature Development
```bash
# Multi-phase feature development
/session "implement advanced search functionality"

# Phase 1: Research and architecture
/query "analyze existing search implementation"
/query "research elasticsearch integration patterns"

# Phase 2: Foundation
/task "implement search indexing service"
/task "create search result ranking algorithm"

# Phase 3: Integration
/feature "advanced search with filters and facets"

# Phase 4: Optimization
/meta-optimize "improve search performance"
/task "add search result caching"

# Phase 5: Production
/protocol "deploy advanced search to production"
```

### Microservices Development
```bash
# Service decomposition
/query "analyze monolith for microservices boundaries"
/feature "extract user service from monolith"
/feature "extract order service from monolith"

# Service coordination
/swarm "implement service mesh for microservices"
/task "add distributed tracing"
/task "implement circuit breaker pattern"

# Testing strategy
/task "create contract tests for services"
/task "implement end-to-end testing"
```

### Performance Optimization Workflow
```bash
# Performance analysis
/query "identify performance bottlenecks in application"
/meta-review "analyze performance metrics over time"

# Optimization implementation
/task "optimize database queries with indexes"
/task "implement Redis caching for frequently accessed data"
/task "add connection pooling for database"

# Validation
/task "create performance regression tests"
/protocol "deploy optimizations with monitoring"
```

## Advanced Configuration Examples

### Machine Learning Project
```xml
<project_config>
  <tech_stack>
    <primary_language>python</primary_language>
    <framework>pytorch</framework>
    <database>postgresql</database>
  </tech_stack>
  
  <ml_specific>
    <model_framework>pytorch</model_framework>
    <data_processing>pandas</data_processing>
    <experiment_tracking>mlflow</experiment_tracking>
    <model_serving>fastapi</model_serving>
  </ml_specific>
  
  <quality_standards>
    <test_coverage>
      <threshold>85</threshold>
      <enforcement>blocking</enforcement>
    </test_coverage>
    <model_validation>
      <accuracy_threshold>0.95</accuracy_threshold>
      <performance_threshold>100</performance_threshold>
    </model_validation>
  </quality_standards>
</project_config>
```

### DevOps Infrastructure
```xml
<project_config>
  <tech_stack>
    <primary_language>python</primary_language>
    <framework>terraform</framework>
    <database>none</database>
  </tech_stack>
  
  <infrastructure>
    <cloud_provider>aws</cloud_provider>
    <orchestration>kubernetes</orchestration>
    <monitoring>prometheus</monitoring>
    <logging>elasticsearch</logging>
  </infrastructure>
  
  <deployment>
    <strategy>blue-green</strategy>
    <rollback_strategy>automatic</rollback_strategy>
    <health_checks>enabled</health_checks>
  </deployment>
</project_config>
```

### Mobile Development
```xml
<project_config>
  <tech_stack>
    <primary_language>swift</primary_language>
    <framework>swiftui</framework>
    <database>coredata</database>
  </tech_stack>
  
  <mobile_specific>
    <target_platforms>ios</target_platforms>
    <minimum_version>14.0</minimum_version>
    <architecture>mvvm</architecture>
  </mobile_specific>
  
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>blocking</enforcement>
    </test_coverage>
    <performance>
      <app_launch_time>2</app_launch_time>
      <memory_usage>256</memory_usage>
    </performance>
  </quality_standards>
</project_config>
```

## Best Practices for Advanced Usage

### Configuration Management
1. **Version control PROJECT_CONFIG.xml** with your code
2. **Use environment-specific configurations** for different deployment stages
3. **Document custom configurations** for team members
4. **Regular reviews** of configuration effectiveness

### Performance Monitoring
1. **Regular performance reviews** using `/meta-review`
2. **Set up monitoring** for key metrics
3. **Optimize based on usage patterns** identified by framework
4. **Benchmark performance** before and after changes

### Team Collaboration
1. **Shared configuration standards** across team
2. **Regular framework optimization** sessions
3. **Knowledge sharing** of advanced techniques
4. **Continuous improvement** based on team feedback

### Security Considerations
1. **Regular security reviews** of generated code
2. **Custom security modules** for domain-specific checks
3. **Automated security scanning** integration
4. **Threat modeling** for new features

---

## Related Documentation
- [User Guide](../user-guide/README.md) - Foundation and intermediate usage
- [API Reference](../api-reference.md) - Complete API documentation
- [Examples](../../examples/advanced/) - Advanced usage examples
- [Contributing](../../CONTRIBUTING.md) - Contributing to the framework

## Next Steps
1. **Experiment with custom modules** for your specific needs
2. **Implement meta-prompting** for continuous improvement
3. **Optimize configuration** for your team and domain
4. **Share learnings** with the community