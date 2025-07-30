# Claude Code Template Library - Real Examples

This document shows **real before/after examples** of how to manually customize the Claude Code templates for your specific project. Each example demonstrates the manual Find & Replace process you'll need to perform.

## 📋 Table of Contents
1. [Quick Reference: Standard Placeholders](#quick-reference-standard-placeholders)
2. [Example 1: Web Application Project](#example-1-web-application-project)
3. [Example 2: Data Science Project](#example-2-data-science-project)
4. [Example 3: Enterprise Java Project](#example-3-enterprise-java-project)
5. [Example 4: Mobile App Backend](#example-4-mobile-app-backend)
6. [Example 5: DevOps Platform](#example-5-devops-platform)

## Quick Reference: Standard Placeholders

These are the 15 standard placeholders you'll need to replace manually:

| Placeholder | Description | Example Value |
|-------------|-------------|---------------|
| `[INSERT_PROJECT_NAME]` | Your project's name | "EcommerceAPI" |
| `[INSERT_DOMAIN]` | Your application domain | "e-commerce" |
| `[INSERT_TECH_STACK]` | Primary technology stack | "Node.js/Express/PostgreSQL" |
| `[INSERT_TEAM_SIZE]` | Your team size | "5-person" |
| `[INSERT_COMPANY_NAME]` | Your organization | "TechStartup Inc" |
| `[INSERT_CLOUD_PROVIDER]` | Your cloud platform | "AWS" |
| `[INSERT_CI_CD_PLATFORM]` | Your CI/CD tool | "GitHub Actions" |
| `[INSERT_TEST_FRAMEWORK]` | Your testing framework | "Jest" |
| `[INSERT_DATABASE_TYPE]` | Your database system | "PostgreSQL" |
| `[INSERT_MONITORING_PLATFORM]` | Your monitoring tool | "DataDog" |
| `[INSERT_DEPLOYMENT_SCHEDULE]` | Your deployment cycle | "weekly" |
| `[INSERT_COMPLIANCE_REQUIREMENTS]` | Compliance needs | "PCI-DSS" |
| `[INSERT_VERSION_CONTROL]` | VCS system | "GitHub" |
| `[INSERT_DOCUMENTATION_TOOL]` | Docs platform | "Docusaurus" |
| `[INSERT_CONTAINER_PLATFORM]` | Container system | "Docker/Kubernetes" |

---

## Example 1: Web Application Project

**Project**: E-commerce REST API  
**Stack**: Node.js, Express, PostgreSQL, React frontend  
**Team**: 5 developers  
**Domain**: Online retail

### Before (Template with Placeholders)

#### `/task.md` command:
```markdown
---
name: /task
description: Break down complex [INSERT_DOMAIN] tasks for [INSERT_PROJECT_NAME]
---

You are an expert [INSERT_TECH_STACK] developer working on [INSERT_PROJECT_NAME]. 
Help the user break down their [INSERT_DOMAIN] task into manageable subtasks...
```

#### `/db-migrate.md` command:
```markdown
---
name: /db-migrate
description: Database migration for [INSERT_DATABASE_TYPE]
---

Execute database migrations for the [INSERT_PROJECT_NAME] [INSERT_DATABASE_TYPE] database.
Ensure compatibility with [INSERT_TECH_STACK] migration tools...
```

### After (Manually Customized)

#### `/task.md` command:
```markdown
---
name: /task
description: Break down complex e-commerce tasks for EcommerceAPI
---

You are an expert Node.js/Express/PostgreSQL developer working on EcommerceAPI. 
Help the user break down their e-commerce task into manageable subtasks...
```

#### `/db-migrate.md` command:
```markdown
---
name: /db-migrate  
description: Database migration for PostgreSQL
---

Execute database migrations for the EcommerceAPI PostgreSQL database.
Ensure compatibility with Node.js/Express/PostgreSQL migration tools...
```

### Manual Replacement Process
1. Open each file in your editor
2. Use Find & Replace (Ctrl+F / Cmd+F)
3. Replace each placeholder:
   - Find: `[INSERT_PROJECT_NAME]` → Replace: `EcommerceAPI`
   - Find: `[INSERT_DOMAIN]` → Replace: `e-commerce`
   - Find: `[INSERT_TECH_STACK]` → Replace: `Node.js/Express/PostgreSQL`
   - Find: `[INSERT_DATABASE_TYPE]` → Replace: `PostgreSQL`
   - And so on...

---

## Example 2: Data Science Project

**Project**: Customer Analytics Platform  
**Stack**: Python, Pandas, Scikit-learn, Jupyter  
**Team**: 3 data scientists  
**Domain**: Business intelligence

### Before (Template with Placeholders)

#### `/notebook-run.md` command:
```markdown
---
name: /notebook-run
description: Execute [INSERT_DOMAIN] notebooks in [INSERT_PROJECT_NAME]
---

Run Jupyter notebooks for [INSERT_PROJECT_NAME] using [INSERT_TECH_STACK].
Process [INSERT_DOMAIN] data and generate insights for [INSERT_TEAM_SIZE] team...
```

#### `project-config.yaml`:
```yaml
project_config:
  metadata:
    name: "[INSERT_PROJECT_NAME]"
    domain: "[INSERT_DOMAIN]"
  placeholders:
    TECH_STACK: "[INSERT_TECH_STACK]"
    TEAM_SIZE: "[INSERT_TEAM_SIZE]"
```

### After (Manually Customized)

#### `/notebook-run.md` command:
```markdown
---
name: /notebook-run
description: Execute business intelligence notebooks in Customer Analytics Platform
---

Run Jupyter notebooks for Customer Analytics Platform using Python/Pandas/Scikit-learn.
Process business intelligence data and generate insights for 3-person team...
```

#### `project-config.yaml`:
```yaml
project_config:
  metadata:
    name: "Customer Analytics Platform"
    domain: "business intelligence"
  placeholders:
    TECH_STACK: "Python/Pandas/Scikit-learn"
    TEAM_SIZE: "3-person"
```

---

## Example 3: Enterprise Java Project

**Project**: FinanceCore  
**Stack**: Java Spring Boot, Oracle DB, Kubernetes  
**Team**: 20 developers  
**Domain**: Financial services

### Before (Template with Placeholders)

#### `/secure-assess.md` command:
```markdown
---
name: /secure-assess
description: Security assessment for [INSERT_PROJECT_NAME]
---

Perform comprehensive security assessment for [INSERT_DOMAIN] applications 
built with [INSERT_TECH_STACK], ensuring [INSERT_COMPLIANCE_REQUIREMENTS] compliance...
```

### After (Manually Customized)

#### `/secure-assess.md` command:
```markdown
---
name: /secure-assess
description: Security assessment for FinanceCore
---

Perform comprehensive security assessment for financial services applications 
built with Java Spring Boot, ensuring SOC2 and PCI-DSS compliance...
```

---

## Example 4: Mobile App Backend

**Project**: FoodDeliveryAPI  
**Stack**: Ruby on Rails, Redis, PostgreSQL  
**Team**: 8 developers  
**Domain**: Food delivery

### Before (Template with Placeholders)

#### `/deploy.md` command:
```markdown
---
name: /deploy
description: Deploy [INSERT_PROJECT_NAME] to [INSERT_CLOUD_PROVIDER]
---

Deploy [INSERT_PROJECT_NAME] using [INSERT_CI_CD_PLATFORM] to [INSERT_CLOUD_PROVIDER].
Follow [INSERT_DEPLOYMENT_SCHEDULE] deployment schedule for [INSERT_DOMAIN] services...
```

### After (Manually Customized)

#### `/deploy.md` command:
```markdown
---
name: /deploy
description: Deploy FoodDeliveryAPI to AWS
---

Deploy FoodDeliveryAPI using CircleCI to AWS.
Follow daily deployment schedule for food delivery services...
```

---

## Example 5: DevOps Platform

**Project**: InfraManager  
**Stack**: Go, Terraform, Prometheus  
**Team**: 12 engineers  
**Domain**: Infrastructure automation

### Before (Template with Placeholders)

#### `/monitor-setup.md` command:
```markdown
---
name: /monitor-setup
description: Setup monitoring for [INSERT_PROJECT_NAME]
---

Configure [INSERT_MONITORING_PLATFORM] monitoring for [INSERT_TECH_STACK] applications.
Track [INSERT_DOMAIN] metrics for [INSERT_TEAM_SIZE] engineering team...
```

### After (Manually Customized)

#### `/monitor-setup.md` command:
```markdown
---
name: /monitor-setup
description: Setup monitoring for InfraManager
---

Configure Prometheus monitoring for Go/Terraform applications.
Track infrastructure automation metrics for 12-person engineering team...
```

---

## 🎯 Tips for Manual Customization

### 1. Use Your Editor's Find & Replace
Most editors support project-wide Find & Replace:
- **VS Code**: Ctrl+Shift+H (Cmd+Shift+H on Mac)
- **IntelliJ**: Ctrl+Shift+R (Cmd+Shift+R on Mac)
- **Sublime**: Ctrl+Shift+F (Cmd+Shift+F on Mac)

### 2. Order of Replacement Matters
Replace in this order to avoid partial replacements:
1. Longer, more specific placeholders first
2. Shorter, general placeholders last

### 3. Validate After Replacement
Use the validation command to check:
```bash
/validate-adaptation
```

### 4. Keep Reference Copy
The `.claude-framework/` directory maintains clean templates for reference.

### 5. Document Your Choices
Create a `ADAPTATION-NOTES.md` file documenting:
- Which placeholders you replaced
- What values you used
- Any commands you removed or modified
- Custom configurations you added

---

## 📚 Advanced Customization Patterns

### Pattern 1: Domain-Specific Language
For specialized domains, you might need additional replacements:
```
[INSERT_DOMAIN_ENTITY] → "Order" (for e-commerce)
[INSERT_DOMAIN_ACTION] → "Process Payment" (for fintech)
```

### Pattern 2: Multi-Environment Setup
For projects with multiple environments:
```
[INSERT_DEV_ENVIRONMENT] → "development.myapp.local"
[INSERT_STAGING_ENVIRONMENT] → "staging.myapp.com"
[INSERT_PROD_ENVIRONMENT] → "api.myapp.com"
```

### Pattern 3: Team-Specific Workflows
For specific team processes:
```
[INSERT_CODE_REVIEW_TOOL] → "GitHub PRs"
[INSERT_COMMUNICATION_PLATFORM] → "Slack"
[INSERT_PROJECT_MANAGEMENT_TOOL] → "Jira"
```

---

## 🔄 Keeping Templates Updated

When new versions of the template library are released:

1. **Check for Updates**:
   ```bash
   cd .claude-framework
   git pull origin main
   ```

2. **Review Changes**:
   ```bash
   git diff HEAD~1
   ```

3. **Manually Apply Updates**:
   - Compare your customized files with new templates
   - Manually merge beneficial changes
   - Re-apply your placeholder replacements

4. **Use Sync Guide**:
   ```bash
   /sync-from-reference
   ```

---

## 🤝 Share Your Examples

Have a great customization example? Share it with the community:

1. Document your adaptation pattern
2. Use `/share-adaptation` to generate a shareable format
3. Submit via GitHub Issues with tag `adaptation-example`

---

*Remember: This is a manual process. Take your time, be thorough, and validate your work!*