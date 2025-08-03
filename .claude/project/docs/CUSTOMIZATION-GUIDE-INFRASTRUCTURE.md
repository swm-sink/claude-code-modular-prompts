# Customization Guide: Infrastructure Commands

This guide provides detailed instructions for customizing infrastructure-focused commands including Database, DevOps, Monitoring, Security, Specialized, Testing, and Web-dev categories.

## Overview

Infrastructure commands handle the operational aspects of your application. They need heavy customization to match your specific deployment environments, security requirements, and operational practices.

## Command Categories

### Database Commands
- **`/db-backup`** - Database backup and disaster recovery
- **`/db-migrate`** - Schema migrations and versioning
- **`/db-restore`** - Database restoration procedures
- **`/db-seed`** - Test data and development seeding

### DevOps Commands  
- **`/ci-run`** - Continuous integration execution
- **`/ci-setup`** - CI/CD pipeline configuration
- **`/deploy`** - Application deployment workflows
- **`/cd-rollback`** - Deployment rollback procedures

### Monitoring Commands
- **`/monitor-setup`** - Monitoring infrastructure setup
- **`/monitor-alerts`** - Alert configuration and management

### Security Commands
- **`/secure-audit`** - Security auditing and compliance
- **`/secure-scan`** - Vulnerability scanning and assessment

### Specialized Commands
- **`/db-admin`** - Advanced database administration
- **`/secure-assess`** - Comprehensive security assessment
- **`/secure-manage`** - Security policy management

### Testing Commands
- **`/test-integration`** - Integration testing workflows
- **`/test-unit`** - Unit testing frameworks

### Web Development Commands
- **`/component-gen`** - Component generation and scaffolding

## Category-by-Category Customization

### 1. Database Commands Customization

#### Essential Database Placeholders

| Placeholder | Example Replacement | Usage Context |
|-------------|-------------------|---------------|
| `[INSERT_DATABASE_TYPE]` | `"PostgreSQL"` | Backup commands, connection strings |
| `[INSERT_DATABASE_URL]` | `"postgresql://user:pass@host:5432/db"` | Connection configuration |
| `[INSERT_BACKUP_STRATEGY]` | `"daily-incremental"` | Backup scheduling and retention |
| `[INSERT_MIGRATION_TOOL]` | `"Flyway"` or `"Prisma Migrate"` | Migration execution |

#### Database Type-Specific Customizations

**PostgreSQL Configuration**:
```markdown
# /db-backup - PostgreSQL Backup for EcommerceAPI

## Backup Strategy for PostgreSQL
- **Full Backup**: Daily at 2 AM UTC using pg_dump
- **Incremental**: WAL-E for continuous archiving
- **Retention**: 30 days local, 1 year in S3
- **Encryption**: AES-256 encryption for all backups

### Backup Commands
```bash
# Production backup
/db-backup production --full --encrypt --s3-upload

# Development backup  
/db-backup development --schema-only --local

# Point-in-time recovery preparation
/db-backup --wal-archive --streaming-replication
```

### PostgreSQL-Specific Features
- Connection pooling with PgBouncer
- Read replica management
- Vacuum and maintenance scheduling
- Performance monitoring with pg_stat_statements
```

**MongoDB Configuration**:
```markdown
# /db-backup - MongoDB Backup for ContentPlatform

## Backup Strategy for MongoDB
- **Full Backup**: mongodump with compression
- **Replica Set**: Backup from secondary to avoid performance impact
- **Sharding**: Coordinated backup across all shards
- **Retention**: 7 days local, 6 months in Atlas

### Backup Commands
```bash
# Replica set backup
/db-backup replica-set --secondary-preferred --compress

# Sharded cluster backup
/db-backup sharded --all-shards --consistent-snapshot

# Point-in-time backup
/db-backup --oplog --timestamp "2024-01-15T10:30:00Z"
```

### MongoDB-Specific Features
- Replica set configuration
- Sharding key management
- Index optimization
- Performance monitoring with MongoDB Compass
```

#### Migration Strategy Customizations

**Node.js/Prisma Migrations**:
```markdown
# /db-migrate - Prisma Migration for EcommerceAPI

## Migration Strategy
- **Development**: `prisma db push` for rapid iteration
- **Staging**: `prisma migrate deploy` with validation
- **Production**: Blue-green deployment with rollback plan

### Migration Workflow
```bash
# Create new migration
/db-migrate create "add-payment-methods-table" --prisma

# Deploy to staging
/db-migrate deploy staging --dry-run --validate

# Production deployment
/db-migrate deploy production --backup-first --rollback-plan
```

### Prisma-Specific Features
- Schema drift detection
- Seed data management
- Multi-database support
- Generated client updates
```

### 2. DevOps Commands Customization

#### Cloud Provider Customizations

**AWS Infrastructure**:
```markdown
# /deploy - AWS Deployment for EcommerceAPI

## AWS Deployment Architecture
- **Compute**: ECS Fargate for containers
- **Database**: RDS PostgreSQL with Multi-AZ
- **Storage**: S3 for static files, CloudFront CDN
- **Monitoring**: CloudWatch + DataDog integration

### Deployment Environments
```bash
# Development deployment
/deploy development --ecs-service ecommerce-dev --single-az

# Staging deployment  
/deploy staging --ecs-service ecommerce-staging --blue-green

# Production deployment
/deploy production --ecs-service ecommerce-prod --rolling-update --health-checks
```

### AWS-Specific Features
- Auto Scaling Groups configuration
- Application Load Balancer setup
- CloudFormation template management
- IAM role and policy management
- Cost optimization strategies
```

**Google Cloud Platform**:
```markdown
# /deploy - GCP Deployment for MLPipeline

## GCP Deployment Architecture
- **Compute**: Cloud Run for serverless containers
- **ML Platform**: Vertex AI for model training and serving
- **Database**: Cloud SQL PostgreSQL
- **Storage**: Cloud Storage for model artifacts

### Deployment Commands
```bash
# Cloud Run deployment
/deploy cloud-run --service ml-inference --region us-central1

# Vertex AI model deployment
/deploy vertex-ai --model customer-segmentation --endpoint production

# Cloud Function deployment
/deploy cloud-functions --trigger-http --runtime python39
```

### GCP-Specific Features
- Cloud Build CI/CD integration
- Identity and Access Management (IAM)
- Monitoring with Cloud Operations
- Cost management and budgeting
```

#### CI/CD Pipeline Customizations

**GitHub Actions Integration**:
```markdown
# /ci-setup - GitHub Actions for EcommerceAPI

## Pipeline Configuration
- **Triggers**: Push to main, pull requests
- **Environments**: Development, Staging, Production
- **Secrets**: AWS credentials, database URLs, API keys
- **Matrix Testing**: Node.js 16/18, PostgreSQL 13/14

### Workflow Templates
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18]
        postgres-version: [13, 14]
    
  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
```

### GitHub Actions Features
- Dependency caching for faster builds
- Parallel job execution
- Environment protection rules
- Deployment approval workflows
```

### 3. Monitoring Commands Customization

#### Monitoring Stack Customizations

**Prometheus + Grafana Stack**:
```markdown
# /monitor-setup - Prometheus Monitoring for EcommerceAPI

## Monitoring Architecture
- **Metrics**: Prometheus with Node Exporter
- **Visualization**: Grafana dashboards
- **Alerting**: AlertManager with Slack integration
- **Tracing**: Jaeger for distributed tracing

### Monitoring Setup
```bash
# Infrastructure monitoring
/monitor-setup prometheus --targets "api,database,redis"

# Application metrics
/monitor-setup custom-metrics --express-middleware --business-metrics

# Alert configuration
/monitor-setup alerts --critical-services --pager-duty-integration
```

### Key Metrics for E-commerce
- **Business**: Conversion rate, cart abandonment, revenue per session
- **Performance**: API response times, database query duration
- **Infrastructure**: CPU/memory usage, disk space, network I/O
- **Errors**: 4xx/5xx rates, exception tracking, payment failures
```

**DataDog Integration**:
```markdown
# /monitor-setup - DataDog Monitoring for MLPipeline

## DataDog Configuration
- **APM**: Application performance monitoring for Python services
- **Infrastructure**: Host and container monitoring
- **Logs**: Centralized logging with structured data
- **Synthetics**: API endpoint uptime monitoring

### DataDog Setup
```bash
# Agent installation
/monitor-setup datadog --agent-install --integrations "postgres,redis,kafka"

# Custom dashboards
/monitor-setup dashboards --ml-metrics --model-performance

# Log aggregation
/monitor-setup logs --python-logging --structured-json
```

### ML-Specific Monitoring
- **Model Performance**: Accuracy drift, prediction latency
- **Data Quality**: Schema validation, data drift detection
- **Pipeline Health**: ETL job success rates, data freshness
- **Resource Usage**: GPU utilization, memory consumption
```

#### Alert Configuration Customizations

**Critical Business Alerts**:
```markdown
## E-commerce Critical Alerts

### Revenue-Impacting Alerts
- **Payment Gateway Down**: Immediate PagerDuty notification
- **Checkout Flow Error Rate >1%**: Alert development team
- **Inventory Sync Failure**: Alert operations team
- **CDN Performance Degradation**: Alert DevOps team

### Alert Escalation
1. **Immediate** (< 1 min): Slack notification
2. **Critical** (< 5 min): PagerDuty to on-call engineer
3. **Business Critical** (< 1 min): Page CTO and VP Engineering
```

### 4. Security Commands Customization

#### Security Framework Customizations

**Enterprise Security (PCI DSS)**:
```markdown
# /secure-audit - PCI DSS Compliance for EcommerceAPI

## PCI DSS Requirements
- **Requirement 1**: Firewall configuration
- **Requirement 2**: System hardening (no default passwords)
- **Requirement 3**: Cardholder data protection
- **Requirement 4**: Encrypted transmission
- **Requirement 6**: Secure development practices

### Security Audit Checklist
```bash
# Network security audit
/secure-audit network --pci-compliance --firewall-rules

# Application security
/secure-audit application --owasp-top10 --payment-flows

# Data protection
/secure-audit data --encryption-at-rest --cardholder-data
```

### PCI DSS Specific Validations
- SSL/TLS configuration and certificate management
- Database encryption and key management
- Access logging and monitoring
- Vulnerability scanning and penetration testing
- Employee access controls and training
```

**GDPR Compliance (Data Science)**:
```markdown
# /secure-audit - GDPR Compliance for MLPipeline

## GDPR Requirements
- **Data Minimization**: Collect only necessary personal data
- **Consent Management**: Track and manage user consent
- **Right to be Forgotten**: Data deletion capabilities
- **Data Portability**: Export user data in standard formats
- **Privacy by Design**: Built-in privacy protection

### GDPR Audit Checklist
```bash
# Data inventory and mapping
/secure-audit gdpr --data-mapping --personal-data-inventory

# Consent management validation
/secure-audit consent --consent-tracking --withdrawal-mechanisms

# Data retention policies
/secure-audit retention --deletion-schedules --anonymization
```

### GDPR Specific Features
- Automated data subject request handling
- Consent management integration
- Data retention and deletion automation
- Privacy impact assessment workflows
```

### 5. Specialized Commands Customization

#### Advanced Database Administration

**High-Availability PostgreSQL**:
```markdown
# /db-admin - PostgreSQL HA for EcommerceAPI

## High Availability Configuration
- **Primary-Replica Setup**: Streaming replication with automatic failover
- **Connection Pooling**: PgBouncer with load balancing
- **Backup Strategy**: Point-in-time recovery with 5-minute RPO
- **Monitoring**: pg_stat_statements, pg_stat_activity monitoring

### Advanced Operations
```bash
# Failover management
/db-admin failover --promote-replica --update-dns --health-check

# Performance tuning
/db-admin optimize --analyze-queries --index-recommendations --vacuum-schedule

# Replication management
/db-admin replication --add-replica --region us-west-2 --sync-mode async
```

### Enterprise Features
- Multi-region replication
- Automated backup validation
- Query performance optimization
- Security hardening and compliance
```

### 6. Testing Commands Customization

#### Integration Testing Frameworks

**API Integration Testing**:
```markdown
# /test-integration - API Testing for EcommerceAPI

## Integration Test Strategy
- **API Contract Testing**: OpenAPI specification validation
- **Database Integration**: Test data setup and cleanup
- **Third-Party Services**: Mock payment gateways and shipping APIs
- **Performance Testing**: Load testing critical endpoints

### Test Environment Setup
```bash
# API integration tests
/test-integration api --contract-testing --postman-collection

# Database integration
/test-integration database --migrations --seed-data --cleanup

# Third-party mocks
/test-integration mocks --stripe --shopify --ups-shipping
```

### E-commerce Specific Tests
- Shopping cart operations
- Payment processing workflows
- Inventory management
- Order fulfillment processes
- Customer authentication flows
```

### 7. Web Development Commands Customization

#### Component Generation

**React Component Generation**:
```markdown
# /component-gen - React Components for EcommerceAPI

## Component Templates
- **Business Components**: ProductCard, ShoppingCart, CheckoutForm
- **UI Components**: Button, Modal, Form, DataTable
- **Layout Components**: Header, Footer, Sidebar, Grid
- **Functional Components**: ErrorBoundary, Loader, Toast

### Component Generation
```bash
# Business component with TypeScript
/component-gen ProductCard --typescript --styled-components --storybook

# Form component with validation
/component-gen CheckoutForm --react-hook-form --yup-validation --tests

# Layout component with responsive design
/component-gen ProductGrid --responsive --accessibility --performance
```

### React-Specific Features
- TypeScript integration
- Styled Components or CSS Modules
- Storybook documentation
- Unit test generation
- Accessibility compliance
```

## Domain-Specific Infrastructure Examples

### E-commerce Platform Complete Infrastructure

**Full Stack E-commerce Setup**:
```markdown
## Infrastructure Customization for ShopifyClone

### Database Layer
```bash
# PostgreSQL with read replicas
/db-backup production --hot-standby --s3-encryption
/db-migrate deploy --zero-downtime --rollback-plan

### Application Layer
```bash
# Node.js API with Redis caching
/deploy api --ecs-fargate --redis-cluster --auto-scaling

### Monitoring & Security
```bash
# Comprehensive monitoring
/monitor-setup --business-metrics --performance --security
/secure-audit --pci-compliance --penetration-testing

### CI/CD Pipeline
```bash
# Full deployment pipeline
/ci-setup --github-actions --multi-environment --security-scanning
```

### Key Performance Indicators
- **Availability**: 99.9% uptime SLA
- **Performance**: < 200ms API response time
- **Security**: Zero high-severity vulnerabilities
- **Business**: Real-time conversion tracking
```

### Machine Learning Platform Infrastructure

**ML Infrastructure Setup**:
```markdown
## Infrastructure Customization for MLPipeline

### Data Layer
```bash
# Data warehouse with ML feature store
/db-admin --data-warehouse --feature-store --lineage-tracking

### ML Operations
```bash
# Model training and serving infrastructure
/deploy ml-training --gpu-nodes --distributed-training
/deploy ml-serving --auto-scaling --a-b-testing

### Monitoring & Compliance
```bash
# ML-specific monitoring
/monitor-setup --model-drift --data-quality --bias-detection
/secure-audit --gdpr-compliance --data-privacy --ml-security

### MLOps Pipeline
```bash
# Automated ML pipeline
/ci-setup --ml-pipeline --experiment-tracking --model-registry
```

### ML-Specific Metrics
- **Model Performance**: Accuracy, precision, recall trends
- **Data Quality**: Schema compliance, drift detection
- **Infrastructure**: GPU utilization, training job success rate
- **Business**: Prediction accuracy impact on business metrics
```

## Validation Checklist for Infrastructure Commands

### Technical Infrastructure
- [ ] All cloud provider configurations match your actual setup
- [ ] Database connection strings and credentials are properly templated
- [ ] Monitoring and alerting match your operational requirements
- [ ] Security configurations align with compliance requirements

### Operational Procedures
- [ ] Deployment workflows match your release process
- [ ] Backup and disaster recovery plans are realistic and tested
- [ ] Alert escalation procedures match your team structure
- [ ] Security audit processes align with regulatory requirements

### Team Integration
- [ ] CI/CD pipelines match your development workflow
- [ ] Access controls and permissions reflect team structure
- [ ] Documentation standards support knowledge transfer
- [ ] Training materials are relevant for your technology stack

## Common Infrastructure Customization Issues

### "Deployment doesn't match our environment"
**Problem**: Commands reference different cloud providers or deployment methods
**Solution**:
1. Replace all cloud provider placeholders with your actual platform
2. Update deployment commands to match your container orchestration
3. Align security and networking configurations with your setup
4. Test deployment workflows in staging environment

### "Security requirements are generic"
**Problem**: Security commands don't address your specific compliance needs
**Solution**:
1. Identify your specific compliance requirements (PCI DSS, GDPR, SOX, etc.)
2. Customize security audit checklists for your industry
3. Add domain-specific security patterns and validations
4. Integrate with your existing security tools and processes

### "Monitoring doesn't capture what matters"
**Problem**: Monitoring commands focus on generic metrics instead of business-critical indicators
**Solution**:
1. Define business-specific metrics and KPIs
2. Add domain-specific alerting rules and thresholds
3. Customize dashboards for your team's operational needs
4. Integrate with your existing monitoring and incident response tools

---

*This completes the infrastructure customization guide. Next: See documentation for anti-patterns and best practices.*