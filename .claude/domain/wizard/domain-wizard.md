# Domain Wizard - R&D Engineering Framework

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Selection Guide

This wizard helps you select the optimal domain configuration for your R&D engineering project. The Claude Code Framework provides specialized domain templates optimized for different engineering disciplines.

## Available R&D Engineering Domains

### Mobile Engineering
**Domain:** `mobile-engineering-rd.md`
**Best For:** iOS, Android, and cross-platform mobile development
**Key Technologies:** Swift, Kotlin, React Native, Flutter, ARKit, ARCore
**Specialized Features:** App store optimization, device testing, performance profiling

### Platform Engineering & Infrastructure
**Domain:** `platform-engineering-infrastructure.md`
**Best For:** Developer platforms, infrastructure automation, self-service tools
**Key Technologies:** Kubernetes, Docker, CI/CD, Infrastructure as Code
**Specialized Features:** Developer experience, platform automation, service mesh

### Site Reliability Engineering
**Domain:** `site-reliability-engineering.md`
**Best For:** System reliability, SLO management, incident response
**Key Technologies:** Monitoring, alerting, error budgets, chaos engineering
**Specialized Features:** SLO tracking, incident management, reliability patterns

### Cloud Infrastructure Engineering
**Domain:** `cloud-infrastructure-engineering.md`
**Best For:** Cloud architecture, multi-cloud strategies, cost optimization
**Key Technologies:** AWS, GCP, Azure, Terraform, CloudFormation
**Specialized Features:** Cloud security, cost optimization, multi-cloud patterns

### Data & Analytics Engineering
**Domain:** `data-analytics-engineering-rd.md`
**Best For:** Data pipelines, analytics platforms, data quality
**Key Technologies:** Apache Spark, Kafka, dbt, Airflow, Snowflake
**Specialized Features:** Data quality, pipeline reliability, analytics governance

### AI/ML Engineering & Research
**Domain:** `ai-ml-engineering-research.md`
**Best For:** Machine learning operations, model development, responsible AI
**Key Technologies:** PyTorch, TensorFlow, MLflow, Kubeflow, ONNX
**Specialized Features:** Model validation, bias assessment, production monitoring

### Backend Engineering & Architecture
**Domain:** `backend-engineering-architecture.md`
**Best For:** Server-side development, API architecture, microservices
**Key Technologies:** Node.js, Python, Java, Go, PostgreSQL, Redis
**Specialized Features:** API design, performance optimization, scalability

### Frontend Engineering & UX
**Domain:** `frontend-engineering-ux.md`
**Best For:** User interface development, web performance, accessibility
**Key Technologies:** React, Vue, Angular, TypeScript, Webpack, Vite
**Specialized Features:** Performance optimization, accessibility, user experience

### Security Engineering & Research
**Domain:** `security-engineering-research.md`
**Best For:** Application security, threat modeling, vulnerability research
**Key Technologies:** SAST, DAST, penetration testing, cryptography
**Specialized Features:** Threat modeling, compliance, security architecture

### Test Engineering & Quality Assurance
**Domain:** `test-engineering-qa.md`
**Best For:** Test automation, quality engineering, performance testing
**Key Technologies:** Selenium, Cypress, Jest, JMeter, TestRail
**Specialized Features:** Test automation, coverage analysis, quality metrics

### API Engineering & Microservices
**Domain:** `api-engineering-microservices.md`
**Best For:** API design, microservices architecture, distributed systems
**Key Technologies:** GraphQL, REST, gRPC, API gateways, service mesh
**Specialized Features:** API contracts, developer experience, integration

### Research Engineering & Innovation
**Domain:** `research-engineering-innovation.md`
**Best For:** Technology research, prototype development, innovation
**Key Technologies:** Experimental frameworks, research methodologies
**Specialized Features:** Research validation, prototype testing, innovation assessment

## Domain Selection Logic

### Single Domain Projects
Choose the primary domain that best matches your project's main focus:

```bash
# Mobile app development
claude-code --domain=mobile-engineering-rd

# Data pipeline development
claude-code --domain=data-analytics-engineering-rd

# Infrastructure automation
claude-code --domain=platform-engineering-infrastructure
```

### Multi-Domain Projects
For projects spanning multiple domains, select the primary domain and use personas for cross-cutting concerns:

```bash
# Full-stack web application
claude-code --domain=backend-engineering-architecture --persona=technical-architect

# Mobile app with ML features
claude-code --domain=mobile-engineering-rd --persona=ml-engineer

# Cloud platform with security focus
claude-code --domain=cloud-infrastructure-engineering --persona=security-engineer
```

### Research and Innovation Projects
For experimental and research projects:

```bash
# Breakthrough technology research
claude-code --domain=research-engineering-innovation

# AI/ML research
claude-code --domain=ai-ml-engineering-research --persona=research-engineer
```

## Domain Configuration

### Automatic Domain Detection
The framework automatically detects domain based on project characteristics:

- **Mobile:** iOS/Android projects, mobile frameworks
- **Platform:** Kubernetes, Docker, CI/CD configurations
- **Data:** Data pipelines, analytics tools, ML models
- **Security:** Security libraries, authentication systems
- **Frontend:** Web frameworks, UI components

### Manual Domain Selection
Override automatic detection:

```bash
# Force specific domain
claude-code --domain=security-engineering-research

# Multiple domain support
claude-code --domains=backend-engineering-architecture,security-engineering-research
```

### Domain-Specific Quality Gates
Each domain includes specialized quality gates:

- **Mobile:** App store guidelines, device compatibility
- **Security:** Threat modeling, vulnerability scanning
- **Platform:** SLO compliance, developer experience
- **Data:** Data quality, pipeline reliability

## Integration with Personas

Domains work seamlessly with R&D engineering personas:

| Domain | Compatible Personas |
|--------|-------------------|
| Mobile Engineering | ios-engineer, android-engineer, cross-platform-mobile-engineer |
| Platform Engineering | platform-engineer, devops-engineer, site-reliability-engineer |
| Data Engineering | data-engineer, analytics-engineer, ml-engineer |
| Security Engineering | security-engineer |
| Frontend Engineering | frontend-engineer |
| Backend Engineering | backend-engineer, api-engineer |
| Test Engineering | test-engineer |
| Research Engineering | research-engineer |
| Architecture | technical-architect, engineering-manager |

## Usage Examples

### Mobile App Development
```bash
# iOS app development
claude-code --domain=mobile-engineering-rd --persona=ios-engineer

# Cross-platform app with security
claude-code --domain=mobile-engineering-rd --persona=cross-platform-mobile-engineer --advisory=security-engineer
```

### Platform Engineering
```bash
# Developer platform
claude-code --domain=platform-engineering-infrastructure --persona=platform-engineer

# SRE for reliability
claude-code --domain=site-reliability-engineering --persona=site-reliability-engineer
```

### Data & Analytics
```bash
# Data pipeline
claude-code --domain=data-analytics-engineering-rd --persona=data-engineer

# ML model development
claude-code --domain=ai-ml-engineering-research --persona=ml-engineer
```

### Full-Stack Development
```bash
# Backend API
claude-code --domain=backend-engineering-architecture --persona=api-engineer

# Frontend application
claude-code --domain=frontend-engineering-ux --persona=frontend-engineer
```

## Domain Optimization

### Performance Optimization
- Token usage optimized for domain-specific patterns
- Domain-specific module loading
- Specialized quality gates reduce unnecessary validation

### Context Management
- Domain-specific context compression
- Optimized memory usage for domain patterns
- Efficient module composition

### Quality Assurance
- Domain-specific TDD patterns
- Specialized testing frameworks
- Quality metrics tailored to domain requirements

## Getting Started

1. **Analyze Your Project:**
   - Identify primary technology stack
   - Determine main engineering discipline
   - Consider cross-cutting concerns

2. **Select Domain:**
   - Choose primary domain from list above
   - Consider multi-domain for complex projects
   - Use domain wizard for guidance

3. **Configure Personas:**
   - Select primary persona for main work
   - Add advisory personas for cross-cutting concerns
   - Use technical-architect for complex coordination

4. **Validate Configuration:**
   - Test domain-specific quality gates
   - Verify persona integration
   - Optimize for your workflow

## Support

For domain-specific questions or customization needs:
- Use `/docs` command for domain documentation
- Use `/query` command for domain-specific research
- Use `/adapt` command for domain customization
- Use `/validate` command for domain verification

---

**Note:** This wizard is designed specifically for R&D engineering contexts. For other domains or custom configurations, use the `/adapt` command to create domain-specific templates.