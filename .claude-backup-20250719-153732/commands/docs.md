# Docs Command - Generate documentation and guides

**Description**: Generate documentation and guides

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 80%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/documentation-pattern.md</delegation_target>
  <orchestration_flow>
    1. Analyze documentation requirements and audience
    2. Delegate to documentation pattern module
    3. Generate comprehensive documentation with quality validation
    4. Organize content with proper structure and maintainability
  </orchestration_flow>
  <documentation_types>
    <api_docs>API documentation with examples and schemas</api_docs>
    <user_guides>User-friendly guides and tutorials</user_guides>
    <technical_specs>Technical specifications and architecture docs</technical_specs>
    <setup_guides>Installation and setup instructions</setup_guides>
  </documentation_types>
</command_orchestration>
```

## Usage

**Generate API documentation:**
```
/docs "Create API documentation for user endpoints"
```

**Create user guides:**
```
/docs "Write user guide for the admin dashboard"
```

**Technical documentation:**
```
/docs "Document system architecture and deployment"
```

## What This Command Does

- **Comprehensive**: Generates complete documentation with proper structure
- **Audience-focused**: Tailors content for specific audiences (users, developers, admins)
- **Quality validation**: Ensures documentation meets quality standards
- **Maintainable**: Creates documentation that's easy to update and maintain
- **Multi-format**: Supports various documentation formats and structures

## Examples

- `/docs "README file"` - Creates comprehensive project README with setup and usage
- `/docs "API reference"` - Generates complete API documentation with examples
- `/docs "User manual"` - Creates user-friendly guides and tutorials