# Placeholder Reference Guide

This document provides a comprehensive reference for all placeholder patterns used in the Claude Code Modular Prompts template library.

## Standard Placeholder Format

All placeholders follow the format: `[INSERT_PLACEHOLDER_NAME]`

- **Brackets**: Square brackets `[]` (not curly braces or angle brackets)
- **Prefix**: Always starts with `INSERT_`
- **Name**: Uppercase with underscores for separation
- **No spaces**: Use underscores instead of spaces or hyphens

## Core Placeholders (Used in 20+ Commands)

| Placeholder | Description | Examples | Usage Count |
|------------|-------------|----------|-------------|
| `[INSERT_PROJECT_NAME]` | Your project's name | "my-web-app", "DataAnalyzer" | 108 |
| `[INSERT_TECH_STACK]` | Primary technology stack | "React/Node.js", "Python/Django" | 58 |
| `[INSERT_DOMAIN]` | Project domain/category | "web-dev", "data-science", "devops" | 55 |
| `[INSERT_TEAM_SIZE]` | Team size category | "solo", "small (2-5)", "medium (6-15)" | 52 |
| `[INSERT_CI_CD_PLATFORM]` | CI/CD platform used | "GitHub Actions", "Jenkins", "GitLab CI" | 40 |
| `[INSERT_SECURITY_LEVEL]` | Security requirements | "basic", "enterprise", "high-security" | 38 |
| `[INSERT_DEPLOYMENT_TARGET]` | Deployment environment | "AWS", "Docker", "Heroku", "bare-metal" | 34 |
| `[INSERT_WORKFLOW_TYPE]` | Development workflow | "agile", "waterfall", "lean" | 33 |
| `[INSERT_DATABASE_TYPE]` | Database technology | "PostgreSQL", "MongoDB", "MySQL" | 31 |
| `[INSERT_TESTING_FRAMEWORK]` | Testing framework | "Jest", "pytest", "RSpec" | 29 |
| `[INSERT_PRIMARY_LANGUAGE]` | Main programming language | "JavaScript", "Python", "Java" | 26 |
| `[INSERT_USER_BASE]` | Target user base | "internal", "public", "B2B", "enterprise" | 25 |
| `[INSERT_API_STYLE]` | API architecture style | "REST", "GraphQL", "gRPC" | 23 |

## Infrastructure Placeholders (5-20 Commands)

| Placeholder | Description | Examples | Usage Count |
|------------|-------------|----------|-------------|
| `[INSERT_PERFORMANCE_PRIORITY]` | Performance focus | "speed", "memory", "throughput" | 16 |
| `[INSERT_COMPANY_NAME]` | Organization name | "Acme Corp", "TechStartup Inc" | 8 |
| `[INSERT_CLOUD_PROVIDER]` | Cloud service provider | "AWS", "Azure", "GCP" | 7 |
| `[INSERT_COMPLIANCE_REQUIREMENTS]` | Regulatory compliance | "GDPR", "HIPAA", "SOX" | 6 |
| `[INSERT_MONITORING_PLATFORM]` | Monitoring service | "DataDog", "New Relic", "Prometheus" | 4 |

## Specialized Placeholders (1-5 Commands)

| Placeholder | Description | Examples | Usage Count |
|------------|-------------|----------|-------------|
| `[INSERT_TEST_FRAMEWORK]` | Alternative testing framework | "Mocha", "PHPUnit", "NUnit" | 3 |
| `[INSERT_DEPLOYMENT_SCHEDULE]` | Deployment timing | "daily", "weekly", "on-demand" | 3 |
| `[INSERT_VERSION_CONTROL]` | Version control system | "Git", "SVN", "Mercurial" | 2 |
| `[INSERT_PREFERRED_TOOLS]` | Team's preferred tools | "VS Code, Slack", "IntelliJ, Teams" | 2 |
| `[INSERT_DOCUMENTATION_TOOL]` | Documentation platform | "GitBook", "Confluence", "Notion" | 2 |
| `[INSERT_CONTAINER_PLATFORM]` | Container orchestration | "Kubernetes", "Docker Swarm" | 2 |
| `[INSERT_STAGING_URL]` | Staging environment URL | "https://staging.example.com" | 1 |
| `[INSERT_PROD_URL]` | Production environment URL | "https://example.com" | 1 |
| `[INSERT_DEV_URL]` | Development environment URL | "http://localhost:3000" | 1 |
| `[INSERT_PROJECT_MANAGEMENT_TOOL]` | Project management platform | "Jira", "Trello", "Asana" | 1 |
| `[INSERT_PAYMENT_PROVIDER]` | Payment processing service | "Stripe", "PayPal", "Square" | 1 |
| `[INSERT_COMMUNICATION_PLATFORM]` | Team communication tool | "Slack", "Microsoft Teams", "Discord" | 1 |
| `[INSERT_CODE_REVIEW_TOOL]` | Code review platform | "GitHub", "GitLab", "Bitbucket" | 1 |
| `[INSERT_BLOCKED_TOOLS]` | Tools not to use | "eval(), exec(), system()" | 1 |

## Meta Placeholders (Used in Documentation)

| Placeholder | Description | Usage |
|------------|-------------|-------|
| `[INSERT_XXX]` | Generic placeholder example | Used in documentation to show format |

## Replacement Guidelines

### 1. Required Replacements
These placeholders **must** be replaced for commands to work properly:
- `[INSERT_PROJECT_NAME]`
- `[INSERT_TECH_STACK]` 
- `[INSERT_DOMAIN]`

### 2. Context-Specific Replacements
Replace these based on the commands you're using:
- Database commands: `[INSERT_DATABASE_TYPE]`
- Security commands: `[INSERT_SECURITY_LEVEL]`
- Deployment commands: `[INSERT_DEPLOYMENT_TARGET]`

### 3. Optional Replacements
These enhance command relevance but aren't strictly required:
- `[INSERT_TEAM_SIZE]`
- `[INSERT_WORKFLOW_TYPE]`
- `[INSERT_PERFORMANCE_PRIORITY]`

## Domain-Specific Values

### Common `[INSERT_DOMAIN]` Values:
- `web-dev` - Web development projects
- `data-science` - Data analysis and ML projects  
- `devops` - Infrastructure and operations
- `enterprise` - Enterprise software development
- `mobile` - Mobile app development
- `api` - API-focused projects

### Common `[INSERT_TECH_STACK]` Values:
- `React/Node.js` - JavaScript full-stack
- `Python/Django` - Python web development
- `Java/Spring` - Java enterprise
- `PHP/Laravel` - PHP web development
- `C#/.NET` - Microsoft stack
- `Ruby/Rails` - Ruby web development

### Common `[INSERT_SECURITY_LEVEL]` Values:
- `basic` - Standard security practices
- `enterprise` - Enhanced security for business
- `high-security` - Maximum security (finance, healthcare)
- `startup` - Minimal viable security
- `government` - Regulatory compliance required

## Validation Commands

Use these commands to check your placeholder replacements:

```bash
# Find all remaining placeholders
grep -r "\[INSERT_" .claude/

# Check specific command files
grep "\[INSERT_" .claude/commands/core/*.md

# Validate adaptation completeness
/validate-adaptation
```

## Best Practices

1. **Replace systematically**: Work through one placeholder type at a time
2. **Use consistent values**: Same placeholder should have the same replacement across all files
3. **Test incrementally**: Try commands after replacing major placeholders
4. **Keep a reference**: Document your replacements in `project-config.yaml`
5. **Validate thoroughly**: Use grep to ensure no placeholders were missed

## Common Mistakes to Avoid

1. **Partial replacements**: Don't replace just "INSERT" - replace the full `[INSERT_XXX]`
2. **Case sensitivity**: Placeholders are UPPERCASE - don't change the case
3. **Missing brackets**: Include the square brackets in your search/replace
4. **Nested placeholders**: Some placeholders may contain others - handle carefully
5. **Code examples**: Be careful not to replace placeholders in code examples that should remain as examples
6. **Documentation patterns**: Don't replace regex patterns like `\[INSERT_.*?\]` in documentation - these are instructional

---

*This reference covers 102 command templates with 31 unique placeholder types*
*Total placeholder instances: 674*
*Generated: 2025-07-29*