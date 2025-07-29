# Comprehensive Placeholder Reference Guide

**Complete documentation of all 24 placeholder types across 102 Claude Code command templates**

## Overview

This reference guide documents all placeholder patterns used in the Claude Code modular prompts template library, providing comprehensive replacement guidelines, examples, and security considerations.

**Total Placeholder Statistics:**
- 24 unique placeholder types
- 597 total placeholder instances  
- 41 files requiring manual replacement
- 100% coverage across command categories

## Placeholder Inventory by Frequency

### High-Frequency Placeholders (50+ instances)

#### 1. [INSERT_PROJECT_NAME] - 137 instances
**Usage**: Primary project identifier used throughout commands
**Pattern**: `^[a-zA-Z][a-zA-Z0-9\-_]{1,49}$`
**Examples**:
```
✅ Valid: "MyApp", "web-dashboard", "data_pipeline", "ProjectAlpha"
❌ Invalid: "123app", "my app", "app-", "project!"
```
**Security**: Must start with letter, no spaces or special characters
**Files with most usage**: All core commands, project.md, query.md

#### 2. [INSERT_TECH_STACK] - 72 instances  
**Usage**: Technology stack description for customized commands
**Pattern**: `^[a-zA-Z0-9\s\+\-_\.]{3,80}$`
**Examples**:
```
✅ Valid: "React+Node.js", "Python+FastAPI", "Vue.js+Express", "Go+PostgreSQL"
❌ Invalid: "React & Node", "Python/FastAPI", "React | Vue", "Node.js only"
```
**Security**: Plus separators allowed, no other special characters
**Common in**: Development, API, and deployment commands

#### 3. [INSERT_DOMAIN] - 54 instances
**Usage**: Project domain/category for context-specific customization  
**Type**: Enumerated values only
**Allowed Values**:
```
"web-dev"      - Web development projects
"data-science" - Data analysis, ML, AI projects
"devops"       - Infrastructure, deployment, monitoring
"enterprise"   - Large-scale enterprise applications  
"mobile"       - Mobile app development
"ai-ml"        - AI/ML specific projects
"blockchain"   - Blockchain/crypto projects
"iot"          - Internet of things projects
```
**Security**: Must use exact values from list, case-sensitive
**Files with most usage**: Meta commands, domain-specific templates

### Medium-Frequency Placeholders (20-50 instances)

#### 4. [INSERT_CI_CD_PLATFORM] - 40 instances
**Usage**: Continuous integration/deployment platform specification
**Type**: Enumerated values
**Allowed Values**:
```
"GitHub Actions"     - GitHub's CI/CD platform
"Jenkins"           - Open source automation server
"GitLab CI"         - GitLab's integrated CI/CD
"Azure DevOps"      - Microsoft's DevOps platform
"CircleCI"          - Cloud-based CI/CD service
"Travis CI"         - Hosted CI service
"Bitbucket Pipelines" - Atlassian's CI/CD solution
```
**Security**: Must match exactly, spaces allowed in names
**Common in**: DevOps, deployment, and testing commands

#### 5. [INSERT_TEAM_SIZE] - 40 instances
**Usage**: Team size category for workflow customization
**Type**: Enumerated values
**Allowed Values**:
```
"solo"       - Individual developer
"small"      - 2-5 developers
"medium"     - 6-15 developers  
"large"      - 16-50 developers
"enterprise" - 50+ developers
```
**Security**: Predefined categories only, no custom values
**Common in**: Project setup, workflow, and management commands

#### 6. [INSERT_SECURITY_LEVEL] - 36 instances
**Usage**: Security requirements specification for project context
**Type**: Enumerated values
**Allowed Values**:
```
"basic"    - Standard security practices
"standard" - Enhanced security with monitoring
"high"     - Advanced security with compliance
```
**Security**: Determines security features enabled in commands
**Common in**: Security, deployment, and enterprise commands

#### 7. [INSERT_DEPLOYMENT_TARGET] - 33 instances
**Usage**: Deployment environment specification
**Type**: Enumerated values
**Allowed Values**:
```
"AWS"              - Amazon Web Services
"Azure"            - Microsoft Azure
"Google Cloud"     - Google Cloud Platform
"Kubernetes"       - Container orchestration
"Docker"           - Container deployment
"Heroku"           - Platform as a Service
"Vercel"           - Frontend deployment
"Netlify"          - JAMstack deployment
"DigitalOcean"     - Cloud infrastructure
```
**Security**: Must match supported deployment targets
**Common in**: DevOps, deployment, and infrastructure commands

#### 8. [INSERT_DATABASE_TYPE] - 33 instances
**Usage**: Database technology specification
**Type**: Enumerated values
**Allowed Values**:
```
"PostgreSQL"    - Open source relational database
"MySQL"         - Popular relational database
"MongoDB"       - NoSQL document database
"Redis"         - In-memory data structure store
"SQLite"        - Lightweight relational database
"DynamoDB"      - AWS NoSQL database
"Elasticsearch" - Search and analytics engine
"Cassandra"     - Distributed NoSQL database
```
**Security**: Must match supported database types
**Common in**: Database, backend, and data commands

#### 9. [INSERT_WORKFLOW_TYPE] - 28 instances
**Usage**: Development workflow methodology
**Type**: Enumerated values
**Allowed Values**:
```
"agile"     - Agile/Scrum methodology
"waterfall" - Traditional waterfall approach
"hybrid"    - Combined agile/waterfall approach
"kanban"    - Kanban workflow
"lean"      - Lean development principles
```
**Security**: Standard workflow methodologies only
**Common in**: Project management and development commands

### Low-Frequency Placeholders (1-25 instances)

#### 10. [INSERT_API_STYLE] - 22 instances
**Allowed Values**: `"REST"`, `"GraphQL"`, `"gRPC"`, `"WebSocket"`

#### 11. [INSERT_TESTING_FRAMEWORK] - 22 instances  
**Examples**: `"Jest"`, `"PyTest"`, `"RSpec"`, `"JUnit"`, `"Mocha"`

#### 12. [INSERT_USER_BASE] - 21 instances
**Allowed Values**: `"internal"`, `"b2b"`, `"b2c"`, `"enterprise"`

#### 13. [INSERT_PRIMARY_LANGUAGE] - 21 instances
**Examples**: `"JavaScript"`, `"Python"`, `"Go"`, `"Java"`, `"TypeScript"`

#### 14. [INSERT_PERFORMANCE_PRIORITY] - 13 instances
**Allowed Values**: `"balanced"`, `"optimized"`, `"minimal"`

#### 15. [INSERT_CLOUD_PROVIDER] - 5 instances
**Examples**: `"AWS"`, `"Azure"`, `"Google Cloud"`

#### 16. [INSERT_COMPLIANCE_REQUIREMENTS] - 5 instances
**Examples**: `"GDPR"`, `"HIPAA"`, `"SOC2"`, `"PCI-DSS"`

#### 17. [INSERT_COMPANY_NAME] - 5 instances
**Pattern**: `^[a-zA-Z][a-zA-Z0-9\s\-_.]{1,59}$`
**Examples**: `"Acme Corp"`, `"TechStart Inc"`, `"DataCorp"`

#### 18-24. Rare Placeholders (1-2 instances each)
- `[INSERT_MONITORING_PLATFORM]` - `"DataDog"`, `"New Relic"`
- `[INSERT_TEST_FRAMEWORK]` - Alternative testing framework reference
- `[INSERT_XXX]` - Generic placeholder for documentation
- `[INSERT_CODE_STYLE]` - `"Standard"`, `"Prettier"`, `"ESLint"`
- `[INSERT_PROJECT_TYPE]` - `"Library"`, `"Application"`, `"Service"`
- `[INSERT_DOMAIN_CONFIG]` - Domain-specific configuration
- `[INSERT_DEPLOYMENT_SCHEDULE]` - `"On-demand"`, `"Scheduled"`

## Files Requiring Replacement

### Commands with Most Placeholders
```
1. development/api-design.md        (25 placeholders)  
2. query.md                         (24 placeholders)
3. devops/deploy.md                 (24 placeholders)
4. meta/replace-placeholders.md     (23 placeholders)
5. development/env-setup.md         (22 placeholders)
6. database/db-seed.md              (21 placeholders)
7. development/dev-setup.md         (21 placeholders)
8. monitoring/monitor-setup.md      (21 placeholders)
9. project.md                       (19 placeholders)
10. devops/ci-setup.md              (19 placeholders)
```

### Commands by Category
**Core Commands (3 files)**:
- `core/help.md`, `core/task.md`, `core/project-task.md`

**Development Commands (4 files)**:
- `development/api-design.md`, `development/dev.md`, `development/dev-setup.md`, `development/env-setup.md`

**DevOps Commands (4 files)**:
- `devops/ci-run.md`, `devops/ci-setup.md`, `devops/deploy.md`, `devops/cd-rollback.md`

**Database Commands (4 files)**:
- `database/db-backup.md`, `database/db-migrate.md`, `database/db-restore.md`, `database/db-seed.md`

**Quality Commands (6 files)**:
- `quality/analyze-code.md`, `quality/analyze-system.md`, `quality/quality.md`, `quality/test.md`, `quality/validate-command.md`, `quality/validate-component.md`

**Meta Commands (4 files)**:
- `meta/adapt-to-project.md`, `meta/replace-placeholders.md`, `meta/share-adaptation.md`, `meta/undo-adaptation.md`, `meta/welcome.md`

## Replacement Strategy Guide

### 1. Planning Phase
```markdown
1. Choose your domain (web-dev, data-science, etc.)
2. Define your tech stack (React+Node.js, Python+FastAPI, etc.) 
3. Specify your team size (solo, small, medium, large, enterprise)
4. Select your deployment target (AWS, Azure, Kubernetes, etc.)
5. Choose your database type (PostgreSQL, MongoDB, etc.)
```

### 2. Value Preparation
```markdown
□ Validate all values against security guidelines
□ Ensure enumerated values match exactly from allowed lists
□ Check pattern compliance for free-form values  
□ Test values with validation script if available
□ Document all chosen values in secure location
```

### 3. Systematic Replacement
```markdown
□ Start with highest-frequency placeholders first
□ Replace one placeholder type completely before moving to next
□ Work through files in order of placeholder density
□ Save and test files incrementally
□ Search for remaining placeholders after each type
```

### 4. Validation and Testing
```markdown
□ Search entire .claude/ directory for "[INSERT_" patterns
□ Test sample commands to ensure they work correctly
□ Verify no syntax errors in modified files
□ Confirm context loading works properly
□ Run security scan on replaced content
```

## Common Replacement Patterns

### Web Development Project Example
```yaml
INSERT_PROJECT_NAME: "web-dashboard"
INSERT_DOMAIN: "web-dev"  
INSERT_TECH_STACK: "React+Node.js+TypeScript"
INSERT_PRIMARY_LANGUAGE: "TypeScript"
INSERT_TEAM_SIZE: "small"
INSERT_WORKFLOW_TYPE: "agile"
INSERT_API_STYLE: "REST"
INSERT_DATABASE_TYPE: "PostgreSQL"
INSERT_DEPLOYMENT_TARGET: "AWS"
INSERT_CI_CD_PLATFORM: "GitHub Actions"
INSERT_TESTING_FRAMEWORK: "Jest"
INSERT_SECURITY_LEVEL: "standard"
INSERT_PERFORMANCE_PRIORITY: "balanced"
INSERT_USER_BASE: "b2b"
INSERT_COMPANY_NAME: "WebCorp"
```

### Data Science Project Example  
```yaml
INSERT_PROJECT_NAME: "ml-pipeline"
INSERT_DOMAIN: "data-science"
INSERT_TECH_STACK: "Python+Jupyter+TensorFlow"
INSERT_PRIMARY_LANGUAGE: "Python"
INSERT_TEAM_SIZE: "medium"
INSERT_WORKFLOW_TYPE: "agile"
INSERT_DATABASE_TYPE: "PostgreSQL"
INSERT_DEPLOYMENT_TARGET: "AWS"
INSERT_CI_CD_PLATFORM: "GitLab CI"
INSERT_TESTING_FRAMEWORK: "PyTest"
INSERT_SECURITY_LEVEL: "high"
INSERT_PERFORMANCE_PRIORITY: "optimized"
INSERT_USER_BASE: "internal"
```

### Enterprise DevOps Example
```yaml
INSERT_PROJECT_NAME: "enterprise-platform"
INSERT_DOMAIN: "enterprise"
INSERT_TECH_STACK: "Java+Spring+Kubernetes"
INSERT_PRIMARY_LANGUAGE: "Java"
INSERT_TEAM_SIZE: "enterprise"
INSERT_WORKFLOW_TYPE: "hybrid"
INSERT_API_STYLE: "REST"
INSERT_DATABASE_TYPE: "PostgreSQL"
INSERT_DEPLOYMENT_TARGET: "Kubernetes"
INSERT_CI_CD_PLATFORM: "Jenkins"
INSERT_TESTING_FRAMEWORK: "JUnit"
INSERT_SECURITY_LEVEL: "high"
INSERT_PERFORMANCE_PRIORITY: "optimized"
INSERT_USER_BASE: "enterprise"
INSERT_COMPLIANCE_REQUIREMENTS: "SOC2"
```

## Nested Placeholder Handling

### Understanding Nested Patterns
Some placeholders contain other placeholders:
```
[INSERT_[INSERT_DOMAIN]_CONFIG] → [INSERT_web-dev_CONFIG]
[INSERT_[INSERT_TECH_STACK]_SETUP] → [INSERT_React+Node.js_SETUP]
```

### Replacement Strategy
1. **First Pass**: Replace inner placeholders
   - `[INSERT_DOMAIN]` → `web-dev`
   - Result: `[INSERT_web-dev_CONFIG]`

2. **Second Pass**: Replace resolved placeholders
   - `[INSERT_web-dev_CONFIG]` → appropriate configuration value
   - Final result: resolved configuration

### Security Considerations for Nested Placeholders
- ✅ Inner placeholders resolve safely
- ✅ No infinite recursion possible
- ✅ Validation applies to final resolved values
- ⚠️ Manual verification required for complex nested patterns

## Troubleshooting Guide

### Issue: "Cannot find placeholder in file"
**Cause**: Placeholder may have been modified or doesn't exist
**Solution**: 
1. Search for partial pattern: `[INSERT_`
2. Check for typos in placeholder name  
3. Verify file hasn't been previously modified

### Issue: "Replacement value rejected by validation"
**Cause**: Value doesn't meet security or format requirements
**Solution**:
1. Review input validation guidelines
2. Check allowed values for enumerated placeholders
3. Test pattern compliance for free-form values
4. Remove special characters or adjust format

### Issue: "Commands not working after replacement"
**Cause**: Syntax errors or invalid values introduced
**Solution**:
1. Revert to backup version
2. Replace placeholders one at a time
3. Test each file after modification
4. Check YAML front matter integrity

### Issue: "Still finding [INSERT_ patterns after replacement"
**Cause**: Missed placeholders or nested patterns
**Solution**:
1. Search entire directory: `grep -r "\[INSERT_" .claude/`
2. Check for nested placeholders requiring multiple passes
3. Verify enumerated values match exactly
4. Look for placeholder variants or typos

## Security Warnings

### ⚠️ Critical Security Reminders
1. **Never use values from untrusted sources**
2. **Always validate inputs before replacement**
3. **Test all replaced commands in safe environment**
4. **Monitor for security violations during replacement**
5. **Maintain backups throughout process**

### 🚨 Immediate Security Threats
```
❌ Command injection: "app; rm -rf /"
❌ Script injection: "<script>alert('xss')</script>"
❌ Path traversal: "../../etc/passwd"
❌ Quote escaping: "app\"evil"
❌ Variable expansion: "${malicious_var}"
```

---

## Quick Reference Tables

### Enumerated Placeholders
| Placeholder | Type | Count | Validation |
|-------------|------|-------|------------|
| INSERT_DOMAIN | enum | 54 | 8 predefined values |
| INSERT_TEAM_SIZE | enum | 40 | 5 size categories |
| INSERT_CI_CD_PLATFORM | enum | 40 | 7 platform options |
| INSERT_DEPLOYMENT_TARGET | enum | 33 | 9 target environments |
| INSERT_DATABASE_TYPE | enum | 33 | 8 database systems |

### Pattern-Validated Placeholders  
| Placeholder | Pattern | Max Length | Examples |
|-------------|---------|------------|----------|
| INSERT_PROJECT_NAME | `^[a-zA-Z][a-zA-Z0-9\-_]{1,49}$` | 50 | "MyApp", "web-dashboard" |
| INSERT_TECH_STACK | `^[a-zA-Z0-9\s\+\-_\.]{3,80}$` | 80 | "React+Node.js" |
| INSERT_COMPANY_NAME | `^[a-zA-Z][a-zA-Z0-9\s\-_.]{1,59}$` | 60 | "Acme Corp" |

---

**Last Updated**: 2025-07-29  
**Coverage**: 597 placeholder instances across 102 command templates  
**Security Level**: Production-ready with comprehensive validation