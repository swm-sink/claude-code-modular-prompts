---
name: discover-project
description: Analyze current project and create PROJECT-DNA.md with discovered patterns
usage: "discover-project"
allowed-tools: [Read, Write, Glob, Grep, LS, Bash]
category: core
version: "2.0"
---

# Discover Project DNA - Functional Version

## Purpose
Analyze the current project directory and create PROJECT-DNA.md with discovered patterns. This version provides specific, executable instructions for consistent results.

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

## How It Works (INTEGRATED WITH BACKEND)

This command now integrates with the `.claude-architect/research/` backend components to perform deep analysis:

1. **Loads Analysis Framework**: Uses `.claude-architect/research/analysis-framework.md` methodology
2. **Applies Pattern Extraction**: Executes `.claude-architect/research/pattern-extraction-engine.md` logic
3. **Validates with CRAAP**: Applies `.claude-architect/research/validation/craap-test-framework.yaml` 
4. **Stores in Research Database**: Populates `.claude-architect/research/research-database.yaml` structure
5. **Generates PROJECT-DNA.md**: Creates comprehensive analysis using backend templates

### Backend Integration Details

The command reads and executes the following backend components:

#### From `analysis-framework.md`:
- Repository viability assessment
- Systematic pattern extraction phases
- Evidence collection methodology
- Quality validation steps

#### From `pattern-extraction-engine.md`:
- Repository analysis setup
- Pattern identification workflows
- Cross-reference identification
- Confidence scoring system

#### From `research-database.yaml`:
- Pattern categorization structure
- Evidence requirements
- Confidence scoring weights
- Quality gate criteria

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

## Execution Logic (Backend Integration)

When this command runs, Claude performs the following integrated workflow:

### Step 1: Load Backend Configuration
```yaml
# Read backend components
1. Load: .claude-architect/research/analysis-framework.md
2. Load: .claude-architect/research/pattern-extraction-engine.md  
3. Load: .claude-architect/research/research-database.yaml
4. Load: .claude-architect/research/validation/craap-test-framework.yaml
```

### Step 2: Execute Analysis Framework
Following the `analysis-framework.md` methodology:

#### Phase 1: Repository Preparation
- Assess project viability (active, documented, working code)
- Map directory structure and key files
- Create analysis workspace in memory

#### Phase 2: Pattern Extraction
Using `pattern-extraction-engine.md` logic:
- **Commands**: Analyze `.claude/commands/` if present
- **Architecture**: Detect frameworks, languages, tools
- **Patterns**: Extract coding conventions, test strategies
- **Workflows**: Identify development, testing, deployment patterns

#### Phase 3: Evidence Collection
For each discovered pattern:
- Document file locations and line numbers
- Extract code snippets with context
- Note configuration examples
- Record usage patterns

#### Phase 4: CRAAP Validation
Apply `craap-test-framework.yaml` scoring:
- **Currency**: How recent are the patterns?
- **Relevance**: How applicable to this project?
- **Authority**: Source credibility and maintenance
- **Accuracy**: Working examples and tests
- **Purpose**: Production readiness

#### Phase 5: Confidence Scoring
Using `research-database.yaml` weights:
- Evidence strength (source count, diversity)
- Validation confidence (CRAAP scores)
- Implementation confidence (working examples)
- Calculate overall confidence (0-1 scale)

### Step 3: Generate PROJECT-DNA.md
Create comprehensive output following backend templates:

```markdown
# Project DNA Analysis
<!-- Generated using .claude-architect/research/ backend -->

## Extraction Metadata
- Analysis Framework Version: 1.0
- Extraction Date: [timestamp]
- Confidence Score: [0-1 score]
- Evidence Sources: [count]

## Technical Architecture
[Detected patterns with confidence scores]

## Project Patterns  
[Extracted patterns with evidence references]

## Conventions Discovered
[Team conventions with validation scores]

## Anti-Patterns Identified
[Issues found with mitigation recommendations]

## Cross-References
[Related patterns and dependencies]

## Generation Recommendations
[Specific commands to generate based on DNA]
```

### Backend Files Referenced
This command integrates with:
- `.claude-architect/research/analysis-framework.md` - Core methodology
- `.claude-architect/research/pattern-extraction-engine.md` - Extraction logic
- `.claude-architect/research/research-database.yaml` - Storage schema
- `.claude-architect/research/validation/craap-test-framework.yaml` - Validation
- `.claude-architect/research/templates/` - Output templates

The integration ensures systematic, evidence-based discovery rather than guesswork.