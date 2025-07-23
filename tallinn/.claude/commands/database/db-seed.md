---
name: /db-seed
description: Populates database with seed data for development and testing environments
usage: /db-seed [environment] [data_type]
tools: Read, Write, Edit, Bash, Grep
---

# Populates database with seed data for development and testing environments

**Usage**: `/db-seed $ENV $COUNT`

## Key Arguments

- **$ENV** (optional): The target environment to seed (e.g., development, testing).
- **$COUNT** (optional): The number of records to generate for primary tables.

## Examples

```bash
/db seed
```
*Seed the development database with 100 records per table.*

```bash
/db seed env="testing" count=500
```
*Seed the testing database with 500 records per table.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/interaction/request-user-confirmation.md
 components/database/relationship-management.md
 components/quality/data-generation.md
 components/database/transaction-handling.md
 components/testing/test-data-strategies.md

 You are a database seeding tool. The user wants to populate the database with test data. This may be a destructive action.

 1. **Warning & Confirmation**: Inform the user that this action might truncate existing data and require their explicit confirmation to proceed.

 2. **On Confirmation**:
 * **Read Configuration**: Read `PROJECT_CONFIG.xml` to find the seed configuration file (e.g., `db/seeds.js`).
 * **Generate Seeding Script**: Generate a data seeding script (e.g., Python, Node.js, or SQL) that:
 * Generates realistic data for the specified `env` and `count`.
 * Correctly handles foreign key relationships to maintain integrity.
 * Wraps all insertion operations in a single transaction.
 * **Present Script**: Present the complete seeding script to the user for review and execution.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

