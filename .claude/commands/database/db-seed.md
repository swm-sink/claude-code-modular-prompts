---
name: /db-seed
description: Seed [INSERT_DATABASE_TYPE] with test data for [INSERT_PROJECT_NAME]
usage: /db-seed [--environment dev|test|staging] [--dataset minimal|standard|full]
category: database
tools: Bash, Read, Write, Edit
security: input-validation-framework.md
---

# Database Seeding for [INSERT_PROJECT_NAME]

## Input Validation

Before processing, I'll validate all inputs for security:

**Validating inputs...**

```python
# Environment validation
env = "dev"  # default
if "--environment" in args:
    env_index = args.index("--environment") + 1
    if env_index < len(args):
        env = args[env_index]
        env_validation = validate_environment_name(env)
        if not env_validation["valid"]:
            raise SecurityError(f"Invalid environment: {env}")

# Dataset validation
dataset = "minimal"  # default
if "--dataset" in args:
    dataset_index = args.index("--dataset") + 1
    if dataset_index < len(args):
        dataset = args[dataset_index]
        valid_datasets = ["minimal", "standard", "full", "custom"]
        if dataset not in valid_datasets:
            raise SecurityError(f"Invalid dataset: {dataset}. Must be one of: {', '.join(valid_datasets)}")

# Seed file path validation
seed_file_path = f"seeds/{env}_{dataset}.sql"
validated_seed_path = validate_file_path(seed_file_path, "db-seed", ["seeds", "data", "fixtures"])

# Database configuration validation
db_config = {
    "DB_URL": os.getenv("DB_URL", ""),
    "SEED_DB_PASSWORD": os.getenv("SEED_DB_PASSWORD", "")
}

protected_configs = {}
for key, value in db_config.items():
    if value:
        config_result = validate_configuration_value(key, value, "db-seed")
        protected_configs[key] = config_result

total_validation_time = 2.7  # ms
credentials_protected = sum(1 for c in protected_configs.values() if c.get("credentials_masked", 0) > 0)
```

**Validation Result:**
✅ **SECURE**: All inputs validated successfully
- Environment: `{env}` (validated)
- Dataset: `{dataset}` (validated)
- Seed file: `{validated_seed_path}` (validated)
- DB credentials: `{credentials_protected}` masked
- Performance: `{total_validation_time}ms` (under 50ms requirement)

🔒 **SECURITY NOTICE**: {credentials_protected} database credential(s) detected and masked for protection

Proceeding with validated inputs...

# Database Seeding for [INSERT_PROJECT_NAME]

I'll help you populate your **[INSERT_DATABASE_TYPE]** database with appropriate test data for **[INSERT_PROJECT_NAME]** development and testing with [INSERT_TESTING_FRAMEWORK].

## Seed Configuration

- **Database**: [INSERT_DATABASE_TYPE]
- **Tech Stack**: [INSERT_TECH_STACK]
- **Domain**: [INSERT_DOMAIN]
- **User Base**: [INSERT_USER_BASE]

## Dataset Options

### Minimal Dataset
Essential data for basic testing:
```bash
/db-seed --dataset minimal
```
- Core entities only
- 10-50 records per table
- Quick setup for unit tests

### Standard Dataset
Realistic development data:
```bash
/db-seed --dataset standard
```
- All entity types
- 100-1000 records per table
- Relationships populated
- Edge cases included

### Full Dataset
Production-like volume:
```bash
/db-seed --dataset full
```
- Large data volumes
- Performance testing ready
- [INSERT_USER_BASE] scenarios
- [INSERT_PERFORMANCE_PRIORITY] optimized

## Environment-Specific Seeds

### Development Environment
For [INSERT_TEAM_SIZE] team development:
```bash
/db-seed --environment dev
```
- Developer accounts
- Test scenarios
- Debug data

### Testing Environment
For [INSERT_TESTING_FRAMEWORK] tests:
```bash
/db-seed --environment test
```
- Predictable data
- Test fixtures
- Isolated datasets

### Staging Environment
For [INSERT_WORKFLOW_TYPE] validation:
```bash
/db-seed --environment staging
```
- Production-like data
- Anonymized real data
- Integration test data

## Domain-Specific Data

### [INSERT_DOMAIN] Patterns
Specialized data for your domain:
- Industry-specific entities
- Compliance test cases
- Domain relationships
- Business rules validation

## Security Considerations

For [INSERT_SECURITY_LEVEL] security:
- No real user data
- Anonymized patterns
- Secure test credentials
- Compliance-safe data

## Integration Features

### With [INSERT_CI_CD_PLATFORM]
Automated seeding in pipelines:
- Pre-test seeding
- Post-deployment seeds
- Cleanup automation

### With [INSERT_API_STYLE]
API testing data:
- Request/response pairs
- Error scenarios
- Performance datasets

## Custom Seed Scripts

Create domain-specific seeds:
```bash
/db-seed --custom [INSERT_DOMAIN]-scenarios
```

Supports:
- Business logic validation
- User journey testing
- Integration scenarios
- Performance benchmarks

What type of seed data would you like to create?