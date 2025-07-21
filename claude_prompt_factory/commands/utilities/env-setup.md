---
description: Intelligent environment setup with automated configuration, dependency resolution, and platform optimization
argument-hint: "[environment_type] [platform]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /env setup - Intelligent Environment Setup

Advanced environment setup system with automated configuration, intelligent dependency resolution, and platform optimization.

## Usage
```bash
/env setup development                       # Development environment setup
/env setup --docker                         # Containerized environment
/env setup --cloud                          # Cloud environment configuration
/env setup --auto                           # Fully automated setup
```

## Workflow

The `/env setup` command follows a systematic process to set up a development environment.

```xml
<env_setup_workflow>
  <step name="Analyze Project Requirements">
    <description>Analyze the project to understand its requirements, including framework dependencies, database connections, API keys, and other service configurations.</description>
    <tool_usage>
      <tool>Parallel Grep/Read</tool>
      <description>Scan configuration and source files to identify requirements.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Environment Files">
    <description>Generate or update the necessary environment files (e.g., `.env`, `.env.example`, environment-specific configs) with the required variables.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create or modify environment files.</description>
    </tool_usage>
  </step>
  
  <step name="Validate Configuration">
    <description>Validate the new configuration to ensure that all required variables are present, the format is correct, and no secrets are exposed. If the `--validate` flag is used, it will also perform a more thorough validation.</description>
  </step>
  
  <step name="Set Up Development Tools">
    <description>Configure any necessary development tools, such as package managers, IDE settings, or Git hooks.</description>
  </step>
</env_setup_workflow>
```

## Environment Types
- **development**: Local development with debug features.
- **staging**: Pre-production testing environment.
- **production**: Live environment with security hardening.
- **testing**: Isolated testing configuration.