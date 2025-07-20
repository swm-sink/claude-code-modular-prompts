# /env setup - Environment Setup Command

**Purpose**: Configure and validate development environment settings, including environment files, secrets, and tool configurations.

## Usage
```bash
/env setup [environment] [--validate]
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