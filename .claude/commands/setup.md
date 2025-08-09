---
name: setup
description: Initialize Claude Code native project structure
usage: "/setup"
allowed-tools: [Write, Read, Glob, LS, Edit]
model: sonnet
---

# Setup Command - Pure Claude Code Native

<command_execution>
This command EXECUTES immediately using Claude's native tools.
No shell scripts. No external dependencies. Everything in conversation.
</command_execution>

## Immediate Actions

### 1. Create Project Structure
I'll create the essential Claude Code structure:

```
.claude/
├── commands/      # Your custom commands go here
├── context/       # Project understanding lives here
└── settings.json  # Claude configuration
```

Using Write tool to create:
- `.claude/settings.json` with minimal config
- `.claude/context/PROJECT.md` placeholder
- `CLAUDE.md` if it doesn't exist

### 2. Analyze Current Project
I'll use these tools to understand your project:
- **Glob**: Find all config files (`**/*.{json,yaml,toml,xml}`)
- **Read**: Examine package.json, requirements.txt, pom.xml
- **LS**: Map directory structure
- **Grep**: Identify testing patterns

### 3. Generate Initial Context
Create `.claude/context/initial-analysis.md` with:
- Detected technology stack
- Project structure overview
- Key patterns identified
- Suggested next steps

<semantic_configuration>
  <minimal_settings>
    {
      "tools": {
        "enabled": ["Read", "Write", "Edit", "Glob", "Grep", "LS", "Bash"],
        "dangerouslySkipConfirmation": false
      },
      "model": "sonnet",
      "context": {
        "maxTokens": 200000
      }
    }
  </minimal_settings>
  
  <project_detection>
    <pattern name="javascript">
      <indicator>package.json</indicator>
      <commands>test, build, dev, start</commands>
      <framework>React, Vue, Angular, Next.js</framework>
    </pattern>
    <pattern name="python">
      <indicator>requirements.txt, pyproject.toml</indicator>
      <commands>pytest, python -m unittest</commands>
      <framework>Django, Flask, FastAPI</framework>
    </pattern>
    <pattern name="java">
      <indicator>pom.xml, build.gradle</indicator>
      <commands>mvn test, gradle test</commands>
      <framework>Spring, Quarkus</framework>
    </pattern>
  </project_detection>
</semantic_configuration>

## What This Command Does

1. **Creates Structure** - Sets up `.claude/` directory with proper organization
2. **Analyzes Project** - Detects your tech stack and patterns automatically
3. **Generates Context** - Creates initial understanding for Claude
4. **Zero Dependencies** - Uses only Claude's native tools

## Next Steps After Setup

Run `/discover` to perform deep project analysis and create your PROJECT-DNA.md

<execution_guarantee>
This command executes immediately when run.
No manual steps. No external scripts. Pure Claude native.
</execution_guarantee>