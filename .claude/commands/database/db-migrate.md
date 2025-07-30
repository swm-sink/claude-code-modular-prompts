---
name: /db-migrate
description: "Safe database migration for your project's database system"
usage: /db-migrate [up|down|status|create] [migration-name]
category: database
allowed-tools: Read, Write, Edit, Bash, Grep
---

# Database Migration for [INSERT_PROJECT_NAME]

<!-- SECURITY: Include credential protection for database operations -->
<include>components/security/credential-protection.md</include>
<include>components/security/protection-feedback.md</include>

**🔒 CREDENTIAL PROTECTION ACTIVE**: All database connection strings, passwords, and credentials are automatically detected and masked in outputs and error messages.

I'll help you manage database migrations for **[INSERT_PROJECT_NAME]** using **[INSERT_DATABASE_TYPE]** with your configured migration framework.

## Project Database Configuration
- **Database**: [INSERT_DATABASE_TYPE]
- **Migration Tool**: Auto-detected based on [INSERT_TECH_STACK]
- **Environment**: Configured for [INSERT_DEPLOYMENT_TARGET]

## Migration Commands

### Apply Migrations (up)
```bash
/db-migrate up
```
Applies all pending migrations to your [INSERT_DATABASE_TYPE] database.

### Rollback Migration (down)
```bash
/db-migrate down
```
Rolls back the last applied migration with safety checks.

### Check Status
```bash
/db-migrate status
```
Shows current migration status for all environments.

### Create New Migration
```bash
/db-migrate create add-[INSERT_DOMAIN]-feature
```
Creates a new migration file following [INSERT_PROJECT_NAME] conventions.

## Safety Features with Credential Protection

Based on your **[INSERT_SECURITY_LEVEL]** security requirements:
- **CREDENTIAL MASKING**: Database URLs, passwords, and connection strings automatically masked in all outputs
- **ERROR SANITIZATION**: Connection failures and error messages sanitized to prevent credential exposure
- **PROTECTED LOGGING**: Migration logs automatically scan for credentials using 13 detection patterns
- Pre-migration backup (if configured)
- Dry-run capability with protected output
- Rollback plan generation with sanitized database details
- Change verification with credential-safe reporting

**Database Credential Protection:**
- MySQL/PostgreSQL/MongoDB connection strings automatically detected and masked
- Database passwords in environment variables protected
- Migration error messages sanitized to prevent credential leakage
- Real-time feedback when credentials are detected: "🔒 SECURITY: Database credentials masked"

## Integration with [INSERT_CI_CD_PLATFORM]

Migrations can be integrated into your [INSERT_CI_CD_PLATFORM] pipeline:
- Automated migration on deployment
- Migration testing in CI
- Rollback automation
- Change tracking

## Framework Detection

I'll automatically detect your migration framework based on [INSERT_TECH_STACK]:
- Django → Django migrations
- Rails → ActiveRecord migrations
- Node.js → Knex/Sequelize/TypeORM
- Python → Alembic/SQLAlchemy
- Java → Flyway/Liquibase
- Go → golang-migrate

## Best Practices for [INSERT_TEAM_SIZE] Teams

Your [INSERT_TEAM_SIZE] team should follow these practices:
- Migration review process
- Testing migrations locally first
- Backward compatibility consideration
- Documentation of schema changes

What migration operation would you like to perform?