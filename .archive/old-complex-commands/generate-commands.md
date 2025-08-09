---
name: /generate-commands
description: Generate custom Claude Code commands based on discovered Project DNA
usage: "/generate-commands"
allowed-tools: [Read, Write, Edit]
category: generation
version: "1.0"
---

# Generate Custom Commands - Create Project-Specific Claude Code Commands

## Purpose (INTEGRATED WITH BACKEND)
This command reads your PROJECT-DNA.md file (created by `/discover-project`) and generates custom Claude Code commands using the `.claude-architect/command-forge/` backend generation engine. It applies sophisticated pattern matching, template processing, and validation to create commands specifically tailored to YOUR project's patterns, conventions, and workflows.

## Backend Integration
This command now uses:
- `.claude-architect/command-forge/generation-engine.yaml` - Pattern-based generation logic
- `.claude-architect/command-forge/pattern-library.yaml` - Template patterns
- `.claude-architect/command-forge/command-categories.yaml` - Command organization
- `.claude-architect/command-forge/templates/` - Command templates

## What Gets Generated

### Based on Your Project DNA:

#### For React Projects
- `/create-component` - Using YOUR component patterns
- `/create-hook` - Following YOUR hook conventions
- `/add-route` - Matching YOUR routing setup
- `/create-context` - Using YOUR state patterns

#### For Python/Django Projects
- `/create-model` - Following YOUR model patterns
- `/create-view` - Matching YOUR view structure
- `/add-endpoint` - Using YOUR API patterns
- `/create-migration` - Following YOUR database conventions

#### For Any Project
- `/add-test` - Following YOUR testing patterns
- `/fix-lint` - Using YOUR linting rules
- `/add-feature` - Following YOUR feature structure
- `/debug-issue` - Using YOUR debugging patterns

## Generation Process

### Step 1: Read Project DNA
Reads the PROJECT-DNA.md file to understand:
- Your technical stack
- Your patterns and conventions
- Your project structure
- Your team preferences

### Step 2: Select Appropriate Templates
Based on your DNA, selects which commands to generate:
- React project → React-specific commands
- Python project → Python-specific commands
- API project → API-specific commands
- Full-stack → Combined command set

### Step 3: Customize Templates
Each command is customized with:
- YOUR file naming conventions
- YOUR import patterns
- YOUR testing approach
- YOUR error handling
- YOUR documentation style

### Step 4: Generate Command Files
Creates .md files in `.claude/commands/generated/`:
```
.claude/commands/generated/
├── create-component.md    # YOUR component pattern
├── add-test.md           # YOUR testing pattern
├── create-endpoint.md     # YOUR API pattern
└── debug-issue.md        # YOUR debugging pattern
```

## Example Generation

### Input: React + TypeScript + Jest Project DNA

#### Generated: `/create-component` Command
```markdown
---
name: /create-component
description: Create a new React component following project patterns
usage: "/create-component ComponentName [atoms|molecules|organisms]"
allowed-tools: [Write, Read]
---

# Create Component - Project Pattern

Creates a new React component following YOUR discovered patterns:
- TypeScript with interfaces
- CSS Modules for styling  
- Test file in __tests__ folder
- Barrel export in index.ts
- Storybook story file

## Usage
/create-component Button atoms
/create-component UserCard molecules
/create-component Dashboard organisms
```

### Input: Python + FastAPI Project DNA

#### Generated: `/create-endpoint` Command
```markdown
---
name: /create-endpoint
description: Create a new API endpoint following project patterns
usage: "/create-endpoint /path method"
allowed-tools: [Write, Edit, Read]
---

# Create API Endpoint - Project Pattern

Creates a new FastAPI endpoint following YOUR patterns:
- Pydantic models for validation
- Dependency injection pattern
- Async/await syntax
- OpenAPI documentation
- Pytest test file

## Usage
/create-endpoint /users GET
/create-endpoint /users/{id} PUT
/create-endpoint /auth/login POST
```

## Customization Examples

### YOUR Naming Convention
```javascript
// If DNA shows kebab-case files:
create-user-service.ts
create-user-service.test.ts

// If DNA shows PascalCase files:
CreateUserService.ts
CreateUserService.test.ts
```

### YOUR Test Pattern
```javascript
// If DNA shows Jest with Testing Library:
test('should create user', async () => {
  render(<CreateUser />);
  // YOUR testing pattern
});

// If DNA shows Vitest:
describe('CreateUser', () => {
  it('creates user', () => {
    // YOUR testing pattern
  });
});
```

### YOUR Import Pattern
```javascript
// If DNA shows barrel exports:
import { Button, Input } from '@/components';

// If DNA shows direct imports:
import Button from '@/components/atoms/Button';
import Input from '@/components/atoms/Input';
```

## How It Works

1. **Reads PROJECT-DNA.md**: Understands your project
2. **Selects Templates**: Chooses relevant command types
3. **Customizes Content**: Applies your patterns
4. **Generates Files**: Creates command files
5. **Validates Output**: Ensures commands are valid

## Benefits

- **Perfect Fit**: Commands match YOUR exact patterns
- **No Adaptation Needed**: Works immediately with your project
- **Team Consistency**: Everyone uses same patterns
- **Reduced Errors**: Follows established conventions
- **Faster Development**: No thinking about patterns

## Post-Generation

After generation:
1. **Review**: Check generated commands in `.claude/commands/generated/`
2. **Test**: Try commands on your project
3. **Adjust**: Edit any commands if needed
4. **Use**: Start being more productive!

## Advanced Features

### Pattern Learning
The generator learns from:
- Your existing code patterns
- Your test examples
- Your documentation style
- Your error handling

### Smart Defaults
Provides intelligent defaults based on:
- Common patterns in your tech stack
- Best practices for your framework
- Your team's apparent preferences

### Conflict Resolution
Handles pattern conflicts by:
- Preferring most common pattern
- Noting alternatives in comments
- Allowing easy customization

## Example Workflow

```bash
# 1. First discover your project
/discover-project

# 2. Generate custom commands
/generate-commands

# 3. Review what was generated
ls .claude/commands/generated/

# 4. Try your new commands
/create-component Header molecules
/add-test Header
/create-endpoint /api/users GET
```

Your commands now work exactly like YOUR team writes code!

## Execution Logic (Backend Integration)

When this command runs, Claude executes the following integrated workflow:

### Step 1: Load Backend Generation Engine
```yaml
# Read backend components
1. Load: .claude-architect/command-forge/generation-engine.yaml
2. Load: .claude-architect/command-forge/pattern-library.yaml
3. Load: .claude-architect/command-forge/command-categories.yaml
4. Load: .claude-architect/command-forge/templates/*.md
```

### Step 2: Execute Generation Pipeline
Following the `generation-engine.yaml` pipeline:

#### Stage 1: Discovery Analysis (2-3 minutes)
- Load PROJECT-DNA.md created by /discover-project
- Extract framework patterns, naming conventions, structures
- Calculate confidence scores for each pattern

#### Stage 2: Template Selection (1-2 minutes)
Using `pattern-library.yaml` and `command-categories.yaml`:
- Identify needed commands based on project type
- Select matching templates from backend
- Prioritize by usage frequency and productivity impact

#### Stage 3: Variable Resolution (2-3 minutes)
Map PROJECT-DNA patterns to template variables:
- `FRAMEWORK` → detected framework (React, Vue, Django, etc.)
- `TEST_RUNNER` → testing framework (Jest, Pytest, etc.)
- `NAMING_CONVENTION` → component naming (PascalCase, kebab-case, etc.)
- `DIRECTORY_STRUCTURE` → project organization pattern

#### Stage 4: Command Generation (3-5 minutes)
Process templates with variable substitution:
- Replace all placeholders with project-specific values
- Evaluate conditional sections based on patterns
- Generate YAML frontmatter with proper tool permissions
- Create documentation and usage examples

#### Stage 5: Validation & Optimization (1-2 minutes)
Apply quality gates from `generation-engine.yaml`:
- Validate YAML syntax and structure
- Check convention adherence (>90% target)
- Verify no conflicts with existing commands
- Optimize for performance

### Step 3: Output Generated Commands

Commands are created in `.claude/commands/generated/`:
```
.claude/commands/generated/
├── create-component.md      # Component generator
├── add-test.md              # Test creator
├── create-endpoint.md       # API endpoint builder
├── fix-lint.md              # Linting automation
└── [8-12 more commands]     # Based on your project
```

### Quality Metrics (from backend)
The generation engine targets:
- **Commands generated**: 10+ project-specific commands
- **Generation time**: <10 minutes total
- **Convention adherence**: >90% match to your patterns
- **Documentation coverage**: 100% with examples
- **Success rate**: >85% working on first try

### Backend Files Referenced
This command fully integrates with:
- `.claude-architect/command-forge/generation-engine.yaml` - Core pipeline
- `.claude-architect/command-forge/pattern-library.yaml` - Pattern matching
- `.claude-architect/command-forge/command-categories.yaml` - Organization
- `.claude-architect/command-forge/templates/` - Template library
- `.claude-architect/research/research-database.yaml` - Pattern validation

The integration ensures commands are generated based on evidence-based patterns, not generic templates.