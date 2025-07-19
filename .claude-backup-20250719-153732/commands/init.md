# Init Command - Framework Initialization

**Description**: Initialize the framework in your project

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-19   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>domain/wizard/README.md</delegation_target>
  <orchestration_flow>
    1. Analyze project structure and requirements
    2. Delegate to domain wizard for guided setup
    3. Configure framework for project-specific needs
    4. Validate installation and configuration
  </orchestration_flow>
  <setup_process>
    <project_analysis>Understand existing project structure</project_analysis>
    <framework_installation>Install .claude framework components</framework_installation>
    <configuration>Set up project-specific configuration</configuration>
    <validation>Verify framework is working correctly</validation>
  </setup_process>
</command_orchestration>
```

## Usage

**Set up framework in new project:**
```
/init "Set up framework for React TypeScript project"
```

**Add framework to existing project:**
```
/init "Add framework to existing Python Django project"
```

## What This Command Does

- **Project analysis**: Understands your existing project structure
- **Framework installation**: Installs .claude framework components
- **Configuration**: Sets up project-specific configuration
- **Validation**: Ensures framework is working correctly
- **Guided setup**: Walks through setup process step by step

## Related Commands

For specific initialization scenarios, use:
- `/init-new` - New project with full scaffolding
- `/init-custom` - Custom configuration for complex projects
- `/init-research` - Research-focused framework setup
- `/init-validate` - Validate existing framework installation

## Examples

- `/init "JavaScript project"` - Sets up framework for JS development
- `/init "Python API project"` - Configures framework for Python API development