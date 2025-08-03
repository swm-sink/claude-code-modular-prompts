---
name: /generate-command
description: Meta-prompt system to automatically generate new Claude Code slash commands (v1.0)
version: "1.0"
usage: '/generate-command <task-description> [--framework=<framework>]'
category: meta
allowed-tools:
- Read
- Write
- Edit
- MultiEdit
- Glob
- LS
- Bash
dependencies:
- /quick-command
- /build-command
- /assemble-command
validation:
  pre-execution: Validate task description clarity and framework compatibility
  during-execution: Monitor command generation quality and completeness
  post-execution: Verify generated command follows v1.0 standards
progressive-disclosure:
  layer-integration: Meta-generation across all Progressive Disclosure layers
  escalation-path: Simple generation → framework-specific → custom templates
  de-escalation: Use pre-built templates for common patterns
safety-measures:
  - Validate generated YAML syntax
  - Check for command name conflicts
  - Ensure proper tool permissions
  - Test generated commands
error-recovery:
  generation-failure: Provide partial result with completion guidance
  syntax-error: Show YAML validation errors with fixes
  conflict-error: Suggest alternative command names
---

# Automated Command Generation System

**Generate new Claude Code slash commands using meta-prompting and framework detection.**

## How This Works (TRUE AUTOMATION)

I will:
1. **Analyze your request** and detect the optimal command pattern
2. **Scan your project** to understand context and frameworks
3. **Generate a complete command** with proper YAML frontmatter
4. **Test the command** against your project structure
5. **Save it** to your `.claude/commands/` directory

## Usage Examples

### Generate Framework-Specific Commands
```
/generate-command "create React component with tests"
/generate-command "deploy Python Flask app to production" 
/generate-command "run database migrations for Django"
/generate-command "optimize build performance for Next.js"
```

### Generate Project-Specific Commands
```
/generate-command "run our custom test suite and generate coverage report"
/generate-command "deploy to our staging environment with health checks"
/generate-command "generate API documentation from our OpenAPI spec"
```

## Command Generation Process

### Step 1: Request Analysis
I'll analyze your request to determine:
- **Primary task**: What the command should accomplish
- **Target framework**: Which technology stack to optimize for
- **Complexity level**: Simple task vs multi-step workflow
- **Required tools**: Which Claude Code tools are needed

### Step 2: Project Context Detection
Using the framework detection system, I'll automatically determine:
- **Project type**: Web app, API, CLI tool, library
- **Tech stack**: Languages, frameworks, databases
- **File structure**: Where relevant files are located
- **Existing patterns**: How your project is organized

### Step 3: Template Generation
I'll create a complete command template including:
- **YAML frontmatter** with proper metadata
- **Clear instructions** tailored to your tech stack
- **Specific examples** using your project structure
- **Error handling** for common failure modes
- **Tool specifications** for required Claude Code tools

### Step 4: Validation & Testing
Before saving, I'll:
- **Validate YAML syntax** and required fields
- **Test command logic** against your project
- **Check for conflicts** with existing commands
- **Ensure path references** are correct for your structure

## Generated Command Structure

### Example Output for React Component Generation
```markdown
---
name: /create-component
description: "Create React component with TypeScript and tests"
usage: /create-component <ComponentName> [--type=functional|class]
category: development
allowed-tools: Write, Edit, MultiEdit, LS
---

# React Component Generator

Create a new React component with TypeScript definitions and test files.

## Usage
\`\`\`
/create-component UserProfile
/create-component Button --type=functional
\`\`\`

## Implementation

I'll create the following files:
- \`src/components/{ComponentName}/{ComponentName}.tsx\` - Main component
- \`src/components/{ComponentName}/{ComponentName}.test.tsx\` - Test file  
- \`src/components/{ComponentName}/index.ts\` - Export file

The component will follow your project's existing patterns:
- TypeScript interfaces for props
- CSS modules for styling (if detected)
- Jest/React Testing Library for tests
- Proper error boundaries and accessibility

## Example Generated Component
[Component code example tailored to your project structure]
```

## Meta-Prompting Templates

### For API Development
```
Generate a command that creates RESTful API endpoints for [detected framework]:
- Route definition with proper HTTP methods
- Input validation and sanitization  
- Database operations using [detected ORM]
- Error handling with consistent response format
- API documentation generation
- Unit and integration tests
```

### For Frontend Development
```
Generate a command that creates [detected framework] components:
- Component file with TypeScript definitions
- Styling files in [detected CSS approach]
- Unit tests with [detected testing framework]
- Storybook stories (if Storybook detected)
- Proper imports and exports
```

### For DevOps Tasks
```
Generate a command for deployment to [detected infrastructure]:
- Build optimization for [detected bundler]
- Environment configuration management
- Health checks and monitoring setup
- Rollback procedures
- CI/CD pipeline integration
```

## Command Categories

Based on project analysis, I'll categorize new commands:

**Core Development**: File creation, code generation, refactoring
**Testing**: Test generation, test running, coverage analysis
**DevOps**: Deployment, monitoring, CI/CD, infrastructure
**Database**: Migrations, queries, schema management
**API**: Endpoint creation, documentation, testing
**Frontend**: Components, pages, styling, optimization

## Quality Assurance

Every generated command includes:
- **Working examples** tested against your project
- **Error handling** for common failure scenarios  
- **Documentation** with clear usage instructions
- **Framework compliance** with your tech stack conventions
- **Performance optimization** for your specific setup

## Integration with Existing Commands

Generated commands will:
- **Avoid conflicts** with existing command names
- **Follow naming conventions** from your current commands
- **Use consistent patterns** with your team's style
- **Reference existing utilities** and helper functions

---

## Ready to Generate?

Just describe what you want the command to do, and I'll create a complete, working Claude Code slash command tailored to your project.

**Example**: `/generate-command "create a new API endpoint with validation, database operations, and tests"`