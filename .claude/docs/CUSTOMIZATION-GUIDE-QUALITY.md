# Customization Guide: Quality Commands

This guide provides detailed instructions for customizing quality-focused commands that support testing, code analysis, validation, and monitoring workflows in your development process.

## Overview

Quality commands ensure code reliability, performance, and maintainability. They need customization to match your specific tech stack, quality standards, and domain requirements. Key commands include:

- **`/test`** - Unified intelligent testing framework
- **`/analyze-code`** - Comprehensive code analysis and quality assessment
- **`/validate-command`** - Command and template validation
- **`/quality`** - Overall quality orchestration and reporting

## Command-by-Command Customization

### 1. `/test` Command - Unified Testing Framework

**File**: `.claude/commands/quality/test.md`

**Purpose**: Central testing hub for all testing activities

#### Essential Placeholders to Replace

| Placeholder | Example Replacement | Usage Context |
|-------------|-------------------|---------------|
| `[INSERT_PROJECT_NAME]` | `"EcommerceAPI"` | Test context and reporting |
| `[INSERT_TECH_STACK]` | `"Node.js, Express, PostgreSQL"` | Testing framework selection |
| `[INSERT_DOMAIN]` | `"e-commerce"` | Domain-specific test patterns |
| `[INSERT_TEST_FRAMEWORK]` | `"Jest"` | Actual testing tool configuration |
| `[INSERT_TEAM_SIZE]` | `"8 developers"` | Parallel testing and reporting |
| `[INSERT_CI_CD_PLATFORM]` | `"GitHub Actions"` | CI integration patterns |
| `[INSERT_CLOUD_PROVIDER]` | `"AWS"` | Environment and performance config |

#### Testing Framework Customizations

**JavaScript/Node.js Stack**:
```markdown
# /test - Unified Intelligent Testing Framework for EcommerceAPI
Comprehensive testing solution for Node.js, Express, PostgreSQL applications, combining unit, integration, and coverage analysis with automated test generation, environment management, and advanced reporting capabilities tailored for e-commerce projects.

### Usage Examples
```bash
# Unit Testing with Jest
/test unit "src/payment-service.js" --coverage high
/test unit "src/" --generate --jest-config jest.config.js

# Integration Testing with Supertest
/test integration "api_tests" --env "docker-compose.test.yml"
/test integration --all --setup-db --postgres

# E-commerce Specific Testing
/test --pattern "*payment*" --security-audit
/test integration "checkout-flow" --load-testing
```

**Python/Data Science Stack**:
```markdown
# /test - Unified Intelligent Testing Framework for MLPipeline
Comprehensive testing solution for Python, TensorFlow, PostgreSQL applications, combining unit, integration, and coverage analysis with automated test generation, environment management, and advanced reporting capabilities tailored for machine-learning projects.

### Usage Examples
```bash
# Unit Testing with pytest
/test unit "src/model_training.py" --coverage high --pytest-cov
/test unit "src/" --generate --hypothesis-testing

# Model Validation Testing
/test integration "model_validation" --env "ml-test-env.yml"
/test integration --all --setup-data --model-artifacts

# ML-Specific Testing
/test --pattern "*model*" --data-validation
/test performance "inference" --latency-requirements
```

#### Domain-Specific Test Patterns

**E-commerce Domain**:
```markdown
**Implementation Requirements:**
- Detect and use Jest with Supertest for API testing
- Support Node.js, Express, PostgreSQL integration testing
- Integrate with GitHub Actions CI/CD pipelines
- Provide clear, actionable feedback for 8-person team
- Optimize for performance with caching and parallelization on AWS

**E-commerce Test Categories:**
1. **Payment Processing**: Stripe integration, refund flows, security validation
2. **Inventory Management**: Stock updates, reservation logic, concurrency testing
3. **User Authentication**: Login flows, session management, security testing
4. **Order Workflows**: Cart operations, checkout process, order fulfillment
5. **Performance**: Load testing for high-traffic scenarios, database optimization
```

**Data Science Domain**:
```markdown
**Implementation Requirements:**
- Detect and use pytest with hypothesis for property testing
- Support Python, TensorFlow, PostgreSQL model testing
- Integrate with MLflow and model registry pipelines
- Provide clear, actionable feedback for 5-person data team
- Optimize for performance with GPU testing and model parallelization on AWS

**ML Test Categories:**
1. **Data Validation**: Schema validation, data drift detection, quality checks
2. **Model Testing**: Unit tests for model components, integration with training pipeline
3. **Performance Testing**: Inference latency, throughput, memory usage
4. **A/B Testing**: Model comparison, statistical significance, bias detection
5. **Production Monitoring**: Model degradation, data pipeline health
```

### 2. `/analyze-code` Command - Code Analysis Framework

**File**: `.claude/commands/quality/analyze-code.md`

**Purpose**: Comprehensive code quality and architectural analysis

#### Essential Placeholders to Replace

| Placeholder | Example Replacement | Impact |
|-------------|-------------------|---------|
| `[INSERT_PROJECT_NAME]` | `"ShopifyClone"` | Context for analysis reporting |
| `[INSERT_TECH_STACK]` | `"React, Node.js, MongoDB"` | Analysis patterns and tools |
| `[INSERT_DOMAIN]` | `"e-commerce"` | Domain-specific quality patterns |

#### Focus Mode Customizations

**Web Development Focus**:
```markdown
### Focus Mode Handling for ShopifyClone:
- **comprehensive**: Execute all analysis dimensions with React/Node.js insights
- **code**: Focus on component structure, React patterns, API organization
- **quality**: Emphasize maintainability, Redux patterns, async handling
- **patterns**: Concentrate on React patterns, Express middleware, database models
- **security**: Prioritize authentication, authorization, data validation, XSS prevention
- **performance**: Focus on bundle size, rendering performance, API response times
- **architectural**: Analyze component hierarchy, API design, data flow patterns

### Web Development Analysis Process:
1. **Code Discovery**: Scan React components, Express routes, database models
2. **Context Analysis**: Understand ShopifyClone structure, React/Node.js architecture, e-commerce patterns
3. **Focused Analysis**: Apply web development best practices and performance metrics
4. **Pattern Detection**: Identify React anti-patterns, API design issues, database bottlenecks
5. **Quality Assessment**: Evaluate component complexity, test coverage, bundle analysis
6. **Issue Identification**: Detect performance issues, security vulnerabilities, accessibility problems
7. **Report Generation**: Create structured reports with React/Node.js specific recommendations
```

**Data Science Focus**:
```markdown
### Focus Mode Handling for MLPipeline:
- **comprehensive**: Execute all analysis dimensions with Python/ML insights
- **code**: Focus on function organization, module structure, notebook quality
- **quality**: Emphasize reproducibility, documentation, error handling
- **patterns**: Concentrate on ML patterns, data processing pipelines, model architectures
- **security**: Prioritize data privacy, model security, credential management
- **performance**: Focus on training efficiency, inference latency, memory optimization
- **architectural**: Analyze data flow, model pipelines, service architecture

### Data Science Analysis Process:
1. **Code Discovery**: Scan Python modules, Jupyter notebooks, model definitions
2. **Context Analysis**: Understand MLPipeline structure, TensorFlow architecture, ML patterns
3. **Focused Analysis**: Apply ML engineering best practices and performance metrics
4. **Pattern Detection**: Identify data leakage, model bias, pipeline bottlenecks
5. **Quality Assessment**: Evaluate reproducibility, test coverage, documentation quality
6. **Issue Identification**: Detect performance issues, data privacy concerns, model drift
7. **Report Generation**: Create structured reports with ML-specific recommendations
```

### 3. `/validate-command` Command

**File**: `.claude/commands/quality/validate-command.md`

**Purpose**: Validate command templates and framework consistency

#### Command-Specific Customizations

**Framework Validation Rules**:
```markdown
## Validation Rules for EcommerceAPI Framework

### Required Command Structure
- All commands must have YAML front matter with name, description, usage
- E-commerce commands must include security considerations
- API-related commands must include authentication patterns
- Database commands must include transaction handling

### Domain-Specific Validation
- Payment processing commands must include PCI DSS compliance checks
- User authentication commands must include security best practices
- Inventory commands must include concurrency considerations
- Order processing must include audit trail requirements

### Tech Stack Validation
- Node.js commands must use ES6+ syntax examples
- React commands must follow current hook patterns
- Database commands must be PostgreSQL-compatible
- API commands must follow REST best practices
```

### 4. `/quality` Command - Quality Orchestration

**File**: `.claude/commands/quality/quality.md`

**Purpose**: Orchestrate overall quality processes and reporting

#### Quality Standards Customization

**E-commerce Quality Standards**:
```markdown
## Quality Standards for EcommerceAPI

### Code Quality Metrics
- **Test Coverage**: Minimum 85% for payment-related code, 80% for other features
- **Code Complexity**: Cyclomatic complexity < 10 for business logic
- **Performance**: API response times < 200ms for product queries
- **Security**: Zero high-severity vulnerabilities, regular security audits

### Domain-Specific Quality Gates
1. **Payment Security**: PCI DSS compliance validation
2. **Data Privacy**: GDPR compliance for user data
3. **Performance**: Load testing for Black Friday scenarios
4. **Accessibility**: WCAG 2.1 AA compliance for frontend
5. **SEO**: Core Web Vitals optimization for product pages

### Quality Process Integration
- **Pre-commit**: Format, lint, security scan, unit tests
- **PR Review**: Integration tests, security review, performance check
- **Staging**: Full regression suite, load testing, security audit
- **Production**: Monitoring, alerting, performance tracking
```

**Data Science Quality Standards**:
```markdown
## Quality Standards for MLPipeline

### Model Quality Metrics
- **Data Quality**: 95% data completeness, schema validation
- **Model Performance**: Accuracy > baseline, bias detection
- **Reproducibility**: All experiments trackable and reproducible
- **Documentation**: Model cards for all production models

### ML-Specific Quality Gates
1. **Data Validation**: Schema consistency, drift detection
2. **Model Testing**: Unit tests for preprocessing, model validation
3. **Performance**: Inference latency < 100ms, throughput requirements
4. **Bias Detection**: Fairness metrics across demographic groups
5. **Security**: Model security, data privacy, access controls

### MLOps Quality Process
- **Data Pipeline**: Validation, monitoring, error handling
- **Model Training**: Experiment tracking, reproducibility, validation
- **Model Deployment**: A/B testing, gradual rollout, monitoring
- **Production**: Model performance monitoring, drift detection, retraining triggers
```

## Advanced Customization Patterns

### 1. Multi-Stack Testing Configuration

For projects using multiple technologies:

```markdown
## Multi-Stack Testing for FullStackApp

### Frontend Testing (React/TypeScript)
```bash
/test unit "src/components/" --jest --typescript --coverage 90
/test integration "src/e2e/" --cypress --browser-matrix
/test performance "src/" --lighthouse --web-vitals
```

### Backend Testing (Node.js/Express)
```bash
/test unit "server/routes/" --jest --supertest --coverage 85
/test integration "server/tests/" --docker-compose --db-setup
/test security "server/" --snyk --owasp
```

### Mobile Testing (React Native)
```bash
/test unit "mobile/src/" --jest --react-native --coverage 80
/test integration "mobile/e2e/" --detox --device-matrix
/test performance "mobile/" --flipper --memory-profiling
```
```

### 2. Industry-Specific Quality Gates

**Financial Services**:
```markdown
## Financial Services Quality Requirements

### Regulatory Compliance
- **SOX Compliance**: All financial calculations must have 100% test coverage
- **PCI DSS**: Payment processing code requires security review
- **GDPR**: Data handling must include privacy impact assessment

### Risk Management
- **Security**: Penetration testing every quarter
- **Performance**: 99.9% uptime SLA requirements
- **Audit**: Complete audit trail for all transactions
```

**Healthcare**:
```markdown
## Healthcare Quality Requirements

### HIPAA Compliance
- **Data Security**: Encryption at rest and in transit
- **Access Control**: Role-based access with audit logging
- **Privacy**: Data minimization and anonymization

### Safety Standards
- **Testing**: 95% test coverage for patient data handling
- **Validation**: FDA guidelines for medical device software
- **Documentation**: Complete traceability from requirements to code
```

### 3. Performance Optimization Patterns

**High-Traffic Web Applications**:
```markdown
## Performance Quality Gates for HighTrafficApp

### Response Time Requirements
- **API Endpoints**: < 100ms for data queries, < 500ms for complex operations
- **Database**: Query optimization for < 50ms average response
- **Frontend**: First Contentful Paint < 1.5s, Largest Contentful Paint < 2.5s

### Load Testing Scenarios
```bash
/test performance "api/products" --concurrent-users 1000 --duration 10m
/test performance "checkout-flow" --peak-traffic --black-friday-scenario
/test performance "database" --connection-pool --query-optimization
```

### Scalability Validation
- **Horizontal Scaling**: Auto-scaling based on CPU/memory metrics
- **Database**: Read replicas, connection pooling, query optimization  
- **Caching**: Redis integration, CDN configuration, cache invalidation
```

## Domain-Specific Examples

### E-commerce Platform Quality Suite

**Complete Quality Workflow**:
```markdown
## Quality Workflow for ShopifyClone

### Daily Quality Checks
```bash
# Morning quality review
/analyze-code comprehensive --focus security,performance
/test unit --coverage 85 --parallel --pattern "*critical*"
/quality --metrics --team-dashboard

# Before deployment
/test integration --full-suite --load-testing
/analyze-code security --pci-compliance --data-privacy
/quality --deployment-ready --checklist
```

### Quality Metrics Dashboard
- **Code Quality**: Maintainability index, technical debt ratio
- **Test Coverage**: Unit (85%), Integration (70%), E2E (60%)
- **Security**: Vulnerability count, compliance score
- **Performance**: API latency (p95), Core Web Vitals
- **Business**: Conversion rate impact, error rates
```

### Machine Learning Platform Quality Suite

**ML Quality Workflow**:
```markdown
## Quality Workflow for MLPipeline

### Model Development Quality
```bash
# Data validation
/test data --schema-validation --drift-detection
/analyze-code quality --reproducibility --documentation

# Model validation  
/test model --cross-validation --bias-detection --performance
/quality --model-card --experiment-tracking

# Production readiness
/test performance --inference-latency --throughput --memory
/analyze-code security --data-privacy --model-security
/quality --production-ready --monitoring-setup
```

### ML Quality Metrics
- **Data Quality**: Completeness (95%), consistency, drift detection
- **Model Performance**: Accuracy vs baseline, precision/recall balance
- **Reproducibility**: Experiment tracking, version control, environment management
- **Production**: Inference latency (<100ms), model degradation monitoring
```

## Validation Checklist

After customizing quality commands:

### Technical Validation
- [ ] All testing frameworks match your actual stack
- [ ] Code analysis patterns align with your languages and frameworks
- [ ] Quality metrics reflect your team's actual standards
- [ ] Performance thresholds match your application requirements

### Process Validation
- [ ] Quality gates align with your CI/CD pipeline
- [ ] Test categories match your application architecture  
- [ ] Analysis focus modes address your specific concerns
- [ ] Reporting formats work with your team's tools

### Domain Validation
- [ ] Compliance requirements accurately represented
- [ ] Security standards match your regulatory needs
- [ ] Performance metrics align with user expectations
- [ ] Quality processes support your business objectives

## Common Customization Issues

### "Tests don't match our stack"
**Problem**: Testing commands reference wrong frameworks or tools
**Solution**:
1. Replace all testing framework placeholders with actual tools
2. Update command examples to use your specific test syntax
3. Add your actual configuration files and setup steps
4. Test with real scenarios from your codebase

### "Quality standards are too generic"
**Problem**: Quality metrics don't reflect your domain requirements
**Solution**:
1. Define domain-specific quality gates and metrics
2. Add industry compliance requirements
3. Set performance thresholds based on user needs  
4. Include security standards for your data sensitivity level

### "Analysis doesn't find relevant issues"  
**Problem**: Code analysis doesn't focus on your specific concerns
**Solution**:
1. Customize analysis focus modes for your tech stack
2. Add domain-specific pattern detection
3. Configure security analysis for your threat model
4. Set complexity and maintainability standards

---

*Next: See `CUSTOMIZATION-GUIDE-META.md` for meta command customization patterns.*