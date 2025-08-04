# Customization Guide: Development Commands

This guide provides detailed instructions for customizing development-focused commands that support your core coding workflows, environment setup, and API design processes.

## Overview

Development commands are workflow-centric and need heavy customization to match your specific technology stack, coding standards, and development processes. They include:

- **`/dev`** - Unified development workflow (format, lint, refactor, debug, feature, init, analyze, deps)
- **`/api-design`** - API design and documentation 
- **`/env-setup`** - Development environment configuration
- **`/dev-setup`** - Initial development setup and onboarding

## Command-by-Command Customization

### 1. `/dev` Command - Unified Development Workflow

**File**: `.claude/commands/development/dev.md`

**Purpose**: Single entry point for all development operations

#### Essential Placeholders to Replace

| Placeholder | Example Replacement | Usage Context |
|-------------|-------------------|---------------|
| `[INSERT_PROJECT_NAME]` | `"EcommerceAPI"` | All mode descriptions and examples |
| `[INSERT_TECH_STACK]` | `"Node.js, Express, PostgreSQL"` | Tool and workflow selection |
| `[INSERT_TEAM_SIZE]` | `"6 developers"` | Collaboration and review processes |
| `[INSERT_PRIMARY_LANGUAGE]` | `"JavaScript"` | Formatting and linting configuration |
| `[INSERT_CODE_STYLE]` | `"Airbnb"` | Code formatting standards |
| `[INSERT_DOMAIN]` | `"e-commerce"` | Domain-specific debugging and features |
| `[INSERT_PROJECT_TYPE]` | `"web-application"` | Initialization and setup patterns |

#### Mode-Specific Customizations

**Format Mode Customization**:
```markdown
# Before (Generic)
/dev format [INSERT_PRIMARY_LANGUAGE] --style [INSERT_CODE_STYLE]

# After (JavaScript/React Project)
/dev format javascript --style airbnb
/dev format jsx --style airbnb --react-version 18
/dev format scss --style bem
```

**Lint Mode Customization**:
```markdown
# Before (Generic)
/dev lint --[INSERT_PRIMARY_LANGUAGE] --fix

# After (Node.js Project)
/dev lint --javascript --fix --eslint-config airbnb-base
/dev lint --typescript --fix --strict
/dev lint --styles --stylelint
```

**Debug Mode Customization**:
```markdown
# Before (Generic)
/dev debug "[INSERT_DOMAIN] error" --interactive

# After (E-commerce Project)
/dev debug "payment processing error" --interactive
/dev debug "user authentication failure" --logs
/dev debug "database connection timeout" --trace
```

#### Domain-Specific Workflow Examples

**Web Development (React/Node.js)**:
```markdown
## Common Workflows for EcommerceAPI

### Frontend Development
/dev format --react && /dev lint --jsx --fix
/dev feature "shopping cart component" --responsive --accessible
/dev debug "rendering performance issue" --react-devtools

### Backend Development  
/dev format --node && /dev lint --javascript --fix
/dev feature "payment processing API" --secure --tested
/dev debug "database query optimization" --profiler

### Full-Stack Development
/dev --quality-check  # Format, lint, and basic quality checks
/dev analyze . --optimization --performance
/dev deps compatibility --security-audit
```

**Data Science (Python)**:
```markdown
## Common Workflows for MLPipeline

### Data Analysis
/dev format python --style black --line-length 88
/dev lint --python --flake8 --mypy
/dev feature "customer segmentation model" --reproducible

### Model Development
/dev debug "model convergence issue" --tensorboard
/dev analyze . --performance --memory-usage
/dev deps compatibility --security --data-privacy
```

**DevOps (Go/Kubernetes)**:
```markdown
## Common Workflows for K8sCluster  

### Infrastructure Code
/dev format go --style gofmt
/dev lint --go --golangci-lint --strict
/dev feature "auto-scaling policy" --tested --monitored

### Deployment Scripts
/dev debug "pod startup failure" --kubectl --logs
/dev analyze . --security --compliance
/dev deps compatibility --cve-scanning
```

### 2. `/api-design` Command

**File**: `.claude/commands/development/api-design.md`

**Purpose**: Design and document APIs following domain standards

#### Essential Placeholders to Replace

| Placeholder | Example Replacement | Impact |
|-------------|-------------------|---------|
| `[INSERT_API_STYLE]` | `"REST"` or `"GraphQL"` | Determines design patterns and examples |
| `[INSERT_[INSERT_DOMAIN]_STANDARDS]` | `"PCI DSS compliance"` | Security and compliance requirements |
| `[INSERT_DATABASE_TYPE]` | `"PostgreSQL"` | Query patterns and optimization |
| `[INSERT_SECURITY_LEVEL]` | `"enterprise"` | Authentication and authorization patterns |
| `[INSERT_DEPLOYMENT_TARGET]` | `"AWS EKS"` | Scaling and infrastructure considerations |

#### API Style Customizations

**REST API (E-commerce)**:
```markdown
## REST Best Practices for EcommerceAPI

### For e-commerce Domain
Applying PCI DSS compliance which includes:
- Secure payment data handling
- Customer data protection requirements  
- Audit logging for financial transactions
- Rate limiting for fraud prevention

### REST Patterns
Based on your choice of REST:
- Resource-based URL structure (/users, /products, /orders)
- HTTP status codes for proper error handling
- JSON:API specification for consistent responses
- OpenAPI 3.0 documentation format
```

**GraphQL API (Social Platform)**:
```markdown
## GraphQL Best Practices for SocialApp

### For social-media Domain
Applying GDPR compliance which includes:
- User consent management
- Data portability requirements
- Right to be forgotten implementation
- Privacy-by-design principles

### GraphQL Patterns  
Based on your choice of GraphQL:
- Schema-first design approach
- Field-level authorization
- Query complexity analysis
- Apollo Federation for microservices
```

#### Security Level Customizations

**Enterprise Security**:
```markdown
## Security Level: enterprise

Your enterprise security requirements mandate:
- OAuth 2.0 + OIDC authentication
- Role-based access control (RBAC)
- End-to-end encryption (TLS 1.3)
- Comprehensive audit logging
- Rate limiting with IP whitelisting
- API versioning for security updates
```

**Standard Security**:
```markdown
## Security Level: standard

Your standard security requirements mandate:
- JWT-based authentication
- Basic role validation
- HTTPS enforcement
- Request logging
- Rate limiting
- Input validation and sanitization
```

### 3. `/env-setup` Command

**File**: `.claude/commands/development/env-setup.md`

**Purpose**: Configure development environments consistently

#### Key Customization Areas

**Tool Stack Setup**: Replace generic tools with your specific stack:

**Web Development Stack**:
```markdown
## Development Environment for EcommerceAPI

### Required Tools
- Node.js 18+ with npm/yarn
- PostgreSQL 14+
- Redis for session storage
- VS Code with extensions:
  - ESLint, Prettier
  - Thunder Client for API testing
  - GitLens for git integration

### Environment Variables
```bash
# Database Configuration
DATABASE_URL=postgresql://localhost:5432/ecommerce_dev
REDIS_URL=redis://localhost:6379

# API Configuration  
API_PORT=3000
JWT_SECRET=your-dev-secret
STRIPE_TEST_KEY=sk_test_...

# Feature Flags
ENABLE_CART_PERSISTENCE=true
ENABLE_PAYMENT_GATEWAY=false
```

**Data Science Stack**:
```markdown
## Development Environment for MLPipeline

### Required Tools
- Python 3.9+ with pip/conda
- Jupyter Lab or VS Code
- PostgreSQL for data storage
- Docker for containerized services

### Python Environment
```bash
# Create conda environment
conda create -n mlpipeline python=3.9
conda activate mlpipeline

# Install requirements
pip install -r requirements.txt
pip install -e .  # Install package in development mode
```

### 4. `/dev-setup` Command

**File**: `.claude/commands/development/dev-setup.md`

**Purpose**: Initial onboarding and setup for new team members

#### Onboarding Customizations

**Team-Specific Onboarding**:
```markdown
## Developer Onboarding for [YOUR_COMPANY_NAME]

### Week 1: Environment & Codebase
1. **Day 1-2**: Environment setup using `/env-setup`
2. **Day 3-4**: Codebase tour and architecture overview
3. **Day 5**: First small contribution (documentation/tests)

### Week 2: Domain Knowledge  
1. **Understanding [YOUR_DOMAIN]**: Business logic and requirements
2. **Code Review Process**: Using our PR templates and standards
3. **Testing Practices**: Unit tests with [YOUR_TEST_FRAMEWORK]

### Team Integration
- Slack channels: #dev-team, #[project-name]-alerts
- Daily standups at 9:30 AM
- Code review assignments in GitHub
- Pair programming sessions with senior developers
```

## Advanced Customization Patterns

### 1. Multi-Language Support

For polyglot projects, customize tool support:

**Full-Stack JavaScript + Python**:
```markdown
## Multi-Language Development Workflow

### JavaScript (Frontend/API)
/dev format --javascript --typescript --jsx
/dev lint --eslint --typescript-eslint --react
/dev test --jest --cypress

### Python (Data Processing)  
/dev format --python --black --isort
/dev lint --flake8 --mypy --bandit
/dev test --pytest --coverage

### Combined Operations
/dev --quality-check  # Runs appropriate tools for each language
```

### 2. CI/CD Integration

Connect development commands to your pipeline:

**GitHub Actions Integration**:
```markdown
## CI/CD Integration

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: dev-format
        name: Format code
        entry: /dev format --all
        language: system
      - id: dev-lint  
        name: Lint code
        entry: /dev lint --all --fix
        language: system
```

### 3. Performance Optimization

Add performance considerations:

**High-Performance Requirements**:
```markdown
## Performance-Optimized Development

### Format Mode with Performance
/dev format --optimize-imports --tree-shaking
/dev analyze . --performance --bundle-size --memory-leaks

### Debug Mode with Profiling
/dev debug "slow query performance" --query-profiler --explain-analyze
/dev debug "memory usage spike" --heap-profiler --gc-analysis
```

## Domain-Specific Customization Examples

### E-commerce Platform

**Complete `/dev` customization**:
```markdown
# /dev - Unified Development Workflow for ShopifyClone

Comprehensive development workflow solution for ShopifyClone combining code formatting, linting, refactoring, debugging, feature development, project initialization, analysis, and dependency management tailored for React, Node.js, PostgreSQL and 8-person teams.

## Usage
```bash
# Code Quality & Maintenance  
/dev format javascript --style airbnb  # Format JavaScript code
/dev lint --javascript --react --fix   # Lint and fix React/JS issues
/dev refactor "src/cart-utils.js" --strategy extract-service

# E-commerce Development
/dev debug "payment processing error" --stripe-logs
/dev feature "wishlist functionality" --responsive --tested
/dev init react-component --typescript --storybook
/dev analyze . --performance --seo --accessibility
/dev deps compatibility --security --pci-compliance

# Combined E-commerce Operations
/dev format --all && /dev lint --all --accessibility
/dev --quality-check --performance --security
```

### Machine Learning Pipeline

**Complete `/api-design` customization**:
```markdown
# API Design for MLModelService

I'll help you design **REST** APIs following **GDPR compliance and ML model governance** best practices.

## Project API Configuration
- **API Style**: REST with ML-specific endpoints
- **Primary Language**: Python with FastAPI
- **Database**: PostgreSQL for metadata, S3 for model artifacts  
- **Authentication**: Based on enterprise security with API keys
- **Domain Standards**: MLOps governance and data privacy

## ML API Best Practices

### For machine-learning Domain
Applying ML model governance which includes:
- Model versioning and lineage tracking
- Data drift monitoring endpoints
- Model performance metrics exposure
- A/B testing infrastructure APIs

### REST Patterns for ML
Based on your choice of REST:
- Model serving endpoints (/predict, /batch-predict)
- Model management (/models/{version}/metadata)
- Monitoring endpoints (/health, /metrics, /drift)
- Async processing with job status tracking
```

## Validation Checklist

After customizing development commands:

### Technical Validation
- [ ] All tool references match your actual development stack
- [ ] Code style and linting rules align with team standards
- [ ] Environment setup reflects your actual infrastructure
- [ ] API design patterns match your architecture choices

### Workflow Validation
- [ ] Command examples reflect real development tasks
- [ ] Debug scenarios match common issues in your domain
- [ ] Feature development examples align with your product
- [ ] Integration points work with your existing tools

### Team Validation
- [ ] Onboarding steps match your actual process
- [ ] Tool permissions align with team access levels
- [ ] Documentation standards reflect team practices
- [ ] Code review processes are accurately represented

## Common Issues and Solutions

### "Commands are too generic"
**Problem**: Development commands don't reflect specific technology choices
**Solution**: 
1. Complete all technology placeholders first
2. Add domain-specific examples and workflows
3. Include actual tool configurations and settings
4. Test with real scenarios from your project

### "Tool integrations don't work"
**Problem**: Referenced tools or configurations don't match reality
**Solution**:
1. Audit all tool references in commands
2. Update to match actual versions and configurations
3. Add installation and setup instructions
4. Include troubleshooting for common tool issues

### "Workflow doesn't match team process"
**Problem**: Commands suggest workflows that don't fit team practices
**Solution**:
1. Map command steps to actual team workflow
2. Add team-specific validation and review steps
3. Include collaboration patterns (pair programming, code review)
4. Align with existing CI/CD and deployment processes

---

*Next: See `CUSTOMIZATION-GUIDE-QUALITY.md` for quality and testing command customization patterns.*