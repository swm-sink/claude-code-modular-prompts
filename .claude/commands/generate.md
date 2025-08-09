---
name: generate
description: Generate project-specific commands from PROJECT-DNA
usage: "/generate"
allowed-tools: [Read, Write]
model: sonnet
---

# Generate Command - Create Your Custom Commands

<command_execution>
This command reads your PROJECT-DNA.md and generates custom commands.
Pure execution through Claude's tools. Zero external dependencies.
</command_execution>

## Generation Process

### 1. Read PROJECT-DNA
I'll use Read tool to examine your PROJECT-DNA.md and extract:
- Technology stack specifics
- Testing frameworks
- Deployment targets
- Domain patterns
- Team conventions

### 2. Generate Custom Commands

Based on your DNA, I'll create commands like:

#### For React + TypeScript Project:
- `/test-react` - Runs jest with coverage
- `/build-prod` - Optimized production build
- `/analyze-bundle` - Webpack bundle analysis
- `/check-types` - TypeScript validation

#### For Python + FastAPI Project:
- `/test-pytest` - Runs pytest with fixtures
- `/serve-dev` - Uvicorn hot reload
- `/migrate-db` - Alembic migrations
- `/generate-openapi` - Schema generation

#### For Java + Spring Project:
- `/test-junit` - Maven test execution
- `/build-jar` - Package application
- `/run-local` - Spring Boot dev server
- `/check-security` - OWASP dependency check

### 3. Command Template Structure

Each generated command will follow this pattern:

```markdown
---
name: [command-name]
description: [specific to your project]
usage: "/[command-name] [args]"
allowed-tools: [only what's needed]
model: sonnet
---

# [Command Name] - [Your Project Specific]

<command_execution>
Direct execution for your [framework/tool].
No scripts. Pure Claude native.
</command_execution>

## What This Does
[Specific to your project's setup]

## Execution
[Direct tool usage for your stack]

<project_specific>
  <configuration>
    [Your project's specific config]
  </configuration>
  <patterns>
    [Your team's conventions]
  </patterns>
</project_specific>
```

<generation_engine>
  <template_patterns>
    <!-- Core patterns for all projects -->
    <pattern type="test">
      <detect>test_framework</detect>
      <generate>test_command</generate>
      <customize>coverage_options</customize>
    </pattern>
    <pattern type="build">
      <detect>build_tool</detect>
      <generate>build_command</generate>
      <customize>optimization_flags</customize>
    </pattern>
    <pattern type="serve">
      <detect>dev_server</detect>
      <generate>serve_command</generate>
      <customize>hot_reload_options</customize>
    </pattern>
  </template_patterns>
  
  <customization_rules>
    <rule>Match exact framework versions</rule>
    <rule>Use team's naming conventions</rule>
    <rule>Follow existing patterns</rule>
    <rule>Include team-specific tools</rule>
  </customization_rules>
</generation_engine>

## Output Location

Generated commands will be created in:
- `.claude/commands/[command-name].md`

Each command will be:
- **Executable** - Runs immediately when invoked
- **Project-specific** - Customized for your exact setup
- **Self-contained** - No external dependencies
- **Claude native** - Uses only Claude's tools

## Validation

After generation, I'll:
1. Show you each generated command
2. Explain what it does
3. Test it can execute properly
4. Ask for your confirmation

<quality_assurance>
  <principles>
    <principle>No generic templates</principle>
    <principle>Project-specific only</principle>
    <principle>Evidence-based generation</principle>
    <principle>Executable not instructional</principle>
  </principles>
</quality_assurance>

## Usage

After generation completes:
1. Review generated commands in `.claude/commands/`
2. Test each command with its name (e.g., `/test-react`)
3. Commands execute immediately using Claude's tools
4. Modify as needed for your workflow

<execution_guarantee>
This generates real, working commands for YOUR project.
Not templates. Not examples. Your actual commands.
</execution_guarantee>