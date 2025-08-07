---
name: /discover-project
description: Analyze project and extract Project DNA for custom command generation
usage: "/discover-project [path]"
allowed-tools: [Read, Glob, Grep, LS, Write]
category: generation
version: "1.0"
---

# Discover Project DNA - Deep Analysis for Custom Generation

## Purpose
This command performs deep discovery of your project's unique characteristics (Project DNA) to enable generation of custom Claude Code commands tailored specifically to YOUR codebase.

## What Gets Discovered

### 1. Technical Architecture
- **Framework Detection**: React, Vue, Angular, Django, Rails, Express, etc.
- **Language Patterns**: JavaScript, TypeScript, Python, Ruby, Java, etc.
- **Package Manager**: npm, yarn, pip, bundler, maven, etc.
- **Build Tools**: webpack, vite, rollup, gradle, make, etc.

### 2. Project Structure
- **Directory Organization**: src/, lib/, app/, features/, components/
- **File Naming Conventions**: kebab-case, camelCase, PascalCase
- **Module Organization**: barrel exports, index patterns, explicit imports
- **Test Organization**: __tests__, spec/, test/, alongside files

### 3. Development Patterns
- **Testing Framework**: Jest, Mocha, Pytest, RSpec, JUnit
- **State Management**: Redux, MobX, Vuex, Context API
- **API Patterns**: REST, GraphQL, gRPC, WebSocket
- **Database**: PostgreSQL, MongoDB, MySQL, SQLite

### 4. Team Conventions
- **Code Style**: ESLint, Prettier, Black, RuboCop configs
- **Git Patterns**: Branch naming, commit message format
- **Documentation**: README structure, inline comments, API docs
- **CI/CD**: GitHub Actions, CircleCI, Jenkins, GitLab CI

## Discovery Process

### Step 1: Framework & Language Detection
```javascript
// Check package.json for JavaScript/TypeScript projects
{
  "dependencies": {
    "react": "^18.0.0",      // → React project
    "vue": "^3.0.0",         // → Vue project
    "@angular/core": "^15.0.0" // → Angular project
  }
}
```

```python
# Check requirements.txt for Python projects
django==4.2.0    # → Django project
flask==2.3.0     # → Flask project
fastapi==0.100.0 # → FastAPI project
```

### Step 2: Pattern Recognition
The command analyzes:
- Common import patterns
- File organization structure
- Testing patterns and coverage
- Error handling approaches
- State management patterns

### Step 3: Convention Extraction
Identifies your team's specific conventions:
- How you name things
- How you organize code
- How you handle errors
- How you write tests
- How you document code

### Step 4: Anti-Pattern Detection
Discovers project-specific issues:
- Technical debt patterns
- Common error sources
- Performance bottlenecks
- Security concerns
- Maintenance challenges

## Output: PROJECT-DNA.md

The discovery creates a comprehensive PROJECT-DNA.md file:

```markdown
# Project DNA Analysis

## Technical Architecture
- **Primary Language**: TypeScript
- **Framework**: React 18.2
- **Build Tool**: Vite
- **Package Manager**: pnpm
- **Testing**: Jest + React Testing Library

## Project Patterns
- **Component Structure**: Atomic design (atoms/molecules/organisms)
- **State Management**: Redux Toolkit with RTK Query
- **API Integration**: REST with Axios
- **Styling**: CSS Modules with Tailwind

## Conventions Discovered
- **File Naming**: kebab-case for files, PascalCase for components
- **Test Location**: __tests__ folders alongside components
- **Import Style**: Barrel exports from feature folders
- **Error Handling**: Custom error boundary components

## Generation Recommendations
Based on this DNA, generate commands for:
- Component scaffolding with your patterns
- Test generation matching your style
- API integration following your conventions
- State management using your patterns
```

## Usage

### Basic Discovery
```
/discover-project
```
Analyzes the current project

### Specific Path
```
/discover-project /path/to/project
```
Analyzes a specific project

### After Discovery
Once PROJECT-DNA.md is created, run:
```
/generate-commands
```
To create custom commands based on the discovered DNA

## How It Works

1. **Reads key files**: package.json, requirements.txt, Gemfile, etc.
2. **Scans project structure**: Identifies organization patterns
3. **Analyzes code samples**: Extracts coding patterns
4. **Detects frameworks**: Identifies all major dependencies
5. **Outputs PROJECT-DNA.md**: Comprehensive analysis for generation

## Benefits

- **No Generic Templates**: Everything based on YOUR project
- **Captures Nuance**: Understands YOUR specific patterns
- **Enables Generation**: Provides data for custom command creation
- **Documents Patterns**: Creates reference for team conventions

## Example Workflow

```bash
# 1. Discover your project
/discover-project

# 2. Review the PROJECT-DNA.md file
# (Make any corrections if needed)

# 3. Generate custom commands
/generate-commands

# 4. Start using your custom commands
/your-create-component MyComponent
/your-test-generator user-service
/your-api-scaffold /users endpoint
```

Your commands will follow YOUR patterns, not generic templates!