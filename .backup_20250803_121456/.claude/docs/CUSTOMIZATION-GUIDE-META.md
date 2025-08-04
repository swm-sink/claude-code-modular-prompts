# Customization Guide: Meta Commands

This guide provides detailed instructions for customizing meta commands that help users adapt, validate, and maintain the template framework itself.

## Overview

Meta commands are the framework's self-management system. They provide guided workflows for customization, validation, and maintenance. These commands include:

- **`/adapt-to-project`** - Primary customization guide
- **`/validate-adaptation`** - Verification and scoring system
- **`/replace-placeholders`** - Placeholder management guide
- **`/sync-from-reference`** - Update and maintenance guide
- **`/undo-adaptation`** - Recovery and rollback guide
- **`/share-adaptation`** - Team standardization helper
- **`/import-pattern`** - Pattern application guide
- **`/welcome`** - Onboarding and introduction

## Command-by-Command Customization

### 1. `/adapt-to-project` - Primary Customization Guide

**File**: `.claude/commands/meta/adapt-to-project.md`

**Purpose**: Main entry point for framework customization

#### Domain-Specific Question Sets

The current command has 50 generic questions. Customize these for your domain:

**Web Development Question Set**:
```markdown
## Express Mode Questions for Web Development

**Frontend Technology (10 questions)**:
1. Are you building a React application?
2. Do you use TypeScript for type safety?
3. Is responsive design a requirement?
4. Do you need accessibility (WCAG) compliance?
5. Are you building a single-page application (SPA)?
6. Do you use state management (Redux/Zustand)?
7. Is SEO optimization important?
8. Do you need Progressive Web App features?
9. Are you targeting mobile-first design?
10. Do you use component libraries (Material-UI/Ant Design)?

**Backend Architecture (10 questions)**:
11. Are you building REST APIs?
12. Do you prefer microservices architecture?
13. Is GraphQL part of your stack?
14. Do you need real-time features (WebSockets)?
15. Are you using Node.js with Express?
16. Do you need database migrations?  
17. Is caching strategy important (Redis)?
18. Do you need file upload capabilities?
19. Are you building multi-tenant applications?
20. Do you need API rate limiting?
```

**Data Science Question Set**:
```markdown
## Express Mode Questions for Data Science

**Data Processing (10 questions)**:
1. Are you working with large datasets (>1GB)?
2. Do you need real-time data processing?
3. Is data privacy/GDPR compliance required?
4. Are you building ETL/ELT pipelines?
5. Do you work with streaming data?
6. Is data quality validation critical?
7. Do you need distributed computing (Spark)?
8. Are you working with time-series data?
9. Do you need data versioning/lineage?
10. Is multi-source data integration required?

**Machine Learning (10 questions)**:
11. Are you building supervised learning models?
12. Do you need deep learning capabilities?
13. Is model interpretability important?
14. Do you require A/B testing for models?
15. Is automated model retraining needed?
16. Do you need model versioning/registry?
17. Is bias detection/fairness important?
18. Do you require GPU acceleration?
19. Is edge deployment a requirement?
20. Do you need model monitoring in production?
```

#### Customized Output Templates

**Web Development Output**:
```markdown
### Copy-Paste project-config.yaml for Web Development
```yaml
project_config:
  metadata:
    name: "ShopifyClone"
    domain: "e-commerce"
    type: "full-stack-web-app"
  
  technology:
    frontend: "React 18, TypeScript, Tailwind CSS"
    backend: "Node.js, Express, PostgreSQL"
    testing: "Jest, Cypress, Testing Library"
    deployment: "Vercel, Railway, AWS RDS"
  
  features:
    authentication: true
    payments: "Stripe integration"
    responsive_design: true
    accessibility: "WCAG 2.1 AA"
    seo_optimization: true
    
  team:
    size: 6
    experience_level: "intermediate"
    workflow: "feature-branch-workflow"
```

**Data Science Output**:
```markdown
### Copy-Paste project-config.yaml for Data Science
```yaml
project_config:
  metadata:
    name: "CustomerAnalytics"
    domain: "machine-learning"
    type: "ml-pipeline"
  
  technology:
    languages: "Python 3.9, SQL"
    ml_frameworks: "TensorFlow, scikit-learn, pandas"
    data_storage: "PostgreSQL, S3, Snowflake"
    orchestration: "Apache Airflow"
    deployment: "AWS SageMaker, Docker"
  
  data:
    privacy_compliance: "GDPR, CCPA"
    data_size: "large (>100GB)"
    real_time_processing: true
    data_quality_requirements: "high"
    
  ml_requirements:
    model_interpretability: true
    bias_detection: true
    automated_retraining: true
    a_b_testing: true
```

### 2. `/validate-adaptation` - Verification System

**File**: `.claude/commands/meta/validate-adaptation.md`

#### Domain-Specific Validation Rules

**Web Development Validation**:
```markdown
### Web Development Validation Checklist

#### Frontend Validation
```bash
# Check React-specific placeholders
grep -r "INSERT_COMPONENT_LIBRARY" .claude/commands/web-dev/
grep -r "INSERT_STATE_MANAGEMENT" .claude/commands/core/

# Validate accessibility requirements
grep -r "WCAG" .claude/commands/ || echo "Missing accessibility standards"
```

**Checklist:**
□ All React/TypeScript placeholders replaced
□ Component library specified (Material-UI, Ant Design, etc.)
□ State management solution configured
□ Accessibility standards defined
□ SEO optimization patterns included
□ Responsive design approach specified

#### Backend Validation
```bash
# Check API design placeholders  
grep -r "INSERT_API_STYLE" .claude/commands/development/
grep -r "INSERT_DATABASE_ORM" .claude/commands/database/

# Validate security configurations
grep -r "INSERT_AUTH_STRATEGY" .claude/commands/security/
```

**Checklist:**
□ API style (REST/GraphQL) specified
□ Database ORM/query builder configured
□ Authentication strategy defined
□ Security patterns implemented
□ Performance optimization settings configured
```

**Data Science Validation**:
```markdown
### Data Science Validation Checklist

#### Data Pipeline Validation
```bash
# Check data processing placeholders
grep -r "INSERT_DATA_SOURCE" .claude/commands/data-science/
grep -r "INSERT_ETL_FRAMEWORK" .claude/commands/development/

# Validate ML workflow placeholders
grep -r "INSERT_ML_FRAMEWORK" .claude/commands/quality/
grep -r "INSERT_MODEL_REGISTRY" .claude/commands/specialized/
```

**Checklist:**
□ Data sources and connections specified
□ ETL/ELT framework configured
□ ML frameworks and versions defined
□ Model registry and versioning set up
□ Data privacy compliance configured
□ Monitoring and alerting patterns included
```

### 3. `/replace-placeholders` - Placeholder Management

**File**: `.claude/commands/meta/replace-placeholders.md`

#### Smart Placeholder Detection

Add intelligent placeholder suggestions:

```markdown
## Smart Placeholder Replacement for [DETECTED_DOMAIN]

### Technology Stack Detection
Based on your project files, I've detected:
- **package.json found**: Suggests Node.js/JavaScript project
- **requirements.txt found**: Suggests Python project
- **Dockerfile present**: Containerized deployment
- **tsconfig.json found**: TypeScript usage

### Recommended Replacements
```bash
# Detected: Node.js + React project
[INSERT_PRIMARY_LANGUAGE] → "JavaScript/TypeScript"
[INSERT_FRONTEND_FRAMEWORK] → "React 18"
[INSERT_BACKEND_FRAMEWORK] → "Express.js"
[INSERT_TESTING_FRAMEWORK] → "Jest + Testing Library"
[INSERT_BUILD_TOOL] → "Vite" or "Webpack"
```

### Context-Aware Suggestions
Based on common patterns in your domain:
- **E-commerce projects** typically need payment processing, inventory management
- **SaaS applications** typically need authentication, subscription management
- **Content platforms** typically need CMS integration, SEO optimization
```

### 4. `/sync-from-reference` - Update Management

**File**: `.claude/commands/meta/sync-from-reference.md`

#### Update Strategy Customization

**Conservative Update Strategy** (for production systems):
```markdown
## Conservative Update Process

### Pre-Update Backup
```bash
# Create backup of current customizations
cp -r .claude .claude-backup-$(date +%Y%m%d)
git add .claude && git commit -m "Backup before framework update"

# Document current customizations
/share-adaptation --format=yaml > current-customizations.yaml
```

### Selective Update Process
1. **Review changelog** for breaking changes
2. **Update reference framework** only
3. **Compare changes** with diff tools
4. **Manually merge** critical updates only
5. **Test thoroughly** before committing
```

**Aggressive Update Strategy** (for development):
```markdown
## Aggressive Update Process

### Automated Update
```bash
# Pull latest framework
git submodule update --remote .claude-framework

# Auto-merge non-conflicting changes
/sync-from-reference --auto-merge --preserve-custom

# Re-run adaptation with new questions
/adapt-to-project --refresh --preserve-answers
```

### Rapid Validation
1. **Automated validation** with `/validate-adaptation --auto-run`
2. **Quick smoke tests** of core commands
3. **Commit and iterate** on remaining issues
```

## Advanced Meta Command Patterns

### 1. Team Standardization Workflows

**Enterprise Team Pattern**:
```markdown
## Enterprise Team Standardization

### Lead Developer Workflow
1. **Complete detailed adaptation**: `/adapt-to-project --guided --enterprise`
2. **Document team standards**: `/share-adaptation --format=enterprise-template`
3. **Create team onboarding**: Custom welcome command with company specifics
4. **Set up validation rules**: Custom validation for compliance requirements

### Team Member Workflow  
1. **Import team standards**: `/import-pattern company-standard-template.yaml`
2. **Validate compliance**: `/validate-adaptation --enterprise-rules`
3. **Customize personal workflow**: Minimal adaptation for individual preferences
4. **Stay synchronized**: Regular `/sync-from-reference --team-standard`
```

### 2. Continuous Customization

**Living Framework Pattern**:
```markdown
## Continuous Framework Evolution

### Monthly Framework Review
```bash
# Check for new framework features
/sync-from-reference --preview --changelog

# Review team usage patterns
/analyze-usage --team-metrics --command-popularity

# Update customizations based on learnings
/adapt-to-project --incremental --based-on-usage
```

### Feedback-Driven Improvement
- **Track command usage** to identify gaps
- **Gather team feedback** on pain points  
- **Iterate on customizations** based on real usage
- **Share improvements** back to reference framework
```

### 3. Domain-Specific Meta Commands

**Create specialized meta commands for your domain**:

**E-commerce Meta Command**:
```markdown
---
name: /adapt-to-ecommerce
description: "Specialized e-commerce adaptation with PCI compliance and conversion optimization"
---

# E-commerce Specific Adaptation

## Compliance Requirements
- **PCI DSS**: Payment card data security
- **GDPR**: European customer data privacy
- **ADA**: Accessibility compliance for public sites

## Performance Requirements  
- **Core Web Vitals**: < 2.5s LCP, < 100ms FID, < 0.1 CLS
- **Conversion Optimization**: A/B testing framework integration
- **Peak Traffic**: Black Friday/Cyber Monday scaling

## E-commerce Specific Validation
- Shopping cart abandonment tracking
- Payment gateway integration testing
- Inventory management validation
- Order fulfillment workflow testing
```

## Validation Checklist for Meta Commands

### Customization Validation
- [ ] Question sets match your domain and technology choices
- [ ] Output templates reflect your actual project structure
- [ ] Validation rules check for domain-specific requirements
- [ ] Update strategies align with your risk tolerance

### User Experience Validation
- [ ] Onboarding flow is clear for your team's skill level
- [ ] Customization time estimates are realistic
- [ ] Error recovery procedures are well-documented
- [ ] Team collaboration patterns are supported

### Maintenance Validation
- [ ] Update procedures preserve your customizations
- [ ] Rollback mechanisms work reliably
- [ ] Documentation stays current with changes
- [ ] Team knowledge transfer is facilitated

---

*Next: See `CUSTOMIZATION-GUIDE-INFRASTRUCTURE.md` for Database, DevOps, Monitoring, and Security command customization patterns.*