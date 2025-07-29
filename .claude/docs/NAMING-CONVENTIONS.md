# Template Library Naming Conventions

## Overview
This document defines the consistent naming conventions used throughout the template library for commands, components, files, and directories.

## File Naming Conventions

### Command Files
**Pattern**: `command-name.md`
**Rules**:
- Use kebab-case (lowercase with hyphens)
- Descriptive and concise
- Action-oriented when applicable
- No abbreviations unless widely understood

**Examples**:
✅ Good:
- `task.md`
- `dev-setup.md`
- `secure-audit.md`
- `test-integration.md`

❌ Bad:
- `Task.md` (capital letters)
- `dev_setup.md` (underscores)
- `secaudit.md` (unclear abbreviation)
- `testint.md` (unclear abbreviation)

### Component Files
**Pattern**: `functional-name.md`
**Rules**:
- Use kebab-case (lowercase with hyphens)
- Function or capability focused
- Framework suffixes when applicable (`-framework.md`)
- Clear purpose indication

**Examples**:
✅ Good:
- `context-optimization.md`
- `input-validation-framework.md`
- `git-commit.md`
- `tree-of-thoughts.md`

❌ Bad:
- `contextOpt.md` (camelCase)
- `input_validation.md` (underscores)
- `gitcommit.md` (no separation)
- `tot.md` (unclear abbreviation)

### Documentation Files
**Pattern**: `DOCUMENT-TYPE.md` or `specific-topic.md`
**Rules**:
- UPPERCASE for major documentation files
- kebab-case for specific guides
- Clear content indication
- Use standard document types

**Examples**:
✅ Good:
- `README.md`
- `TEMPLATE-LIBRARY-ARCHITECTURE.md`
- `NAMING-CONVENTIONS.md`
- `template-workspace-separation.md`

## Directory Naming Conventions

### Command Categories
**Pattern**: `category-name/`
**Rules**:
- Use kebab-case for multi-word categories
- Functional grouping
- Logical hierarchy
- No deep nesting (max 3 levels)

**Current Categories**:
- `core/` - Essential commands
- `development/` - Development workflow
- `devops/` - DevOps and deployment
- `data-science/` - Data science specific
- `web-dev/` - Web development specific
- `quality/` - Quality assurance and testing
- `security/` - Security commands
- `database/` - Database operations
- `monitoring/` - System monitoring
- `testing/` - Testing specific
- `specialized/` - Domain-specific commands
- `deprecated/` - Archived commands

### Component Categories  
**Pattern**: `functional-area/`
**Rules**:
- Technical concern based
- Clear functional boundaries
- Reusability focused
- Cross-cutting when applicable

**Current Categories**:
- `actions/` - Concrete action execution
- `analysis/` - Code and system analysis
- `constitutional/` - AI safety and alignment
- `context/` - Context management
- `git/` - Git operations
- `intelligence/` - AI coordination
- `interaction/` - User interaction
- `learning/` - Adaptive learning
- `meta/` - System meta-components
- `optimization/` - Performance optimization
- `orchestration/` - Workflow coordination
- `performance/` - Performance monitoring
- `planning/` - Planning and strategy
- `quality/` - Quality assurance
- `reasoning/` - AI reasoning patterns
- `reliability/` - System reliability
- `reporting/` - Report generation
- `security/` - Security validation
- `testing/` - Testing frameworks
- `validation/` - Validation patterns
- `workflow/` - Workflow management

## Command Naming Patterns

### Slash Command Names
**Pattern**: `/command-name`
**Rules**:
- Use kebab-case after the slash
- Action-oriented verbs when applicable
- Hierarchical naming for related commands
- Consistent with file names (without .md)

**Examples**:
✅ Good:
- `/task`
- `/dev-setup`
- `/secure-audit`
- `/test-integration`

❌ Bad:
- `/Task` (capital letters)
- `/dev_setup` (underscores)
- `/secAudit` (camelCase)

### Command Categories in Names
**Pattern**: `category-action` or standalone names
**Rules**:
- Category prefix for grouped functionality
- Standalone names for core commands
- Consistent categorization
- Clear action indication

**Category Examples**:
- `secure-*`: `secure-audit`, `secure-scan`, `secure-config`
- `test-*`: `test-unit`, `test-integration`, `test-coverage`
- `db-*`: `db-backup`, `db-restore`, `db-migrate`
- `dev-*`: `dev-setup`, `dev-test`, `dev-build`

### Deprecated Command Handling
**Pattern**: Preserve original names in deprecated/
**Rules**:
- Keep original naming for historical reference
- Document migration path to new names
- Maintain naming consistency within deprecated archive
- Clear deprecation indicators

## Component Naming Patterns

### Framework Components
**Pattern**: `name-framework.md`
**Examples**:
- `constitutional-framework.md`
- `input-validation-framework.md`
- `testing-framework.md`
- `validation-framework.md`

### Action Components
**Pattern**: `action-verb-noun.md`
**Examples**:
- `apply-code-changes.md`
- `generate-structured-report.md`
- `create-step-by-step-plan.md`

### Capability Components
**Pattern**: `capability-name.md`
**Examples**:
- `context-optimization.md`
- `dependency-analysis.md`
- `progress-tracking.md`

## Placeholder Naming Conventions

### Standard Placeholders
**Pattern**: `[INSERT_CATEGORY_ITEM]`
**Rules**:
- ALL_CAPS with underscores
- Descriptive category and item
- Consistent across all templates
- Clear replacement indication

**Standard Set**:
- `[INSERT_PROJECT_NAME]`
- `[INSERT_DOMAIN]`
- `[INSERT_TECH_STACK]`
- `[INSERT_COMPANY_NAME]`
- `[INSERT_TEAM_SIZE]`
- `[INSERT_WORKFLOW_TYPE]`

### Context-Specific Placeholders
**Pattern**: `[INSERT_SPECIFIC_CONTEXT]`
**Examples**:
- `[INSERT_DATABASE_TYPE]`
- `[INSERT_CLOUD_PROVIDER]`
- `[INSERT_CI_PLATFORM]`
- `[INSERT_MONITORING_TOOL]`

## Configuration Naming

### YAML Files
**Pattern**: `config-type.yaml`
**Examples**:
- `project-config.yaml`
- `template-config.yaml`
- `validation-config.yaml`

### JSON Files  
**Pattern**: `data-type.json`
**Examples**:
- `command-metadata.json`
- `component-index.json`
- `validation-results.json`

## Variable and Identifier Naming

### Internal Variables (when applicable)
**Pattern**: `snake_case` for internal processing
**Examples**:
- `command_name`
- `template_path`
- `validation_result`

### Configuration Keys
**Pattern**: `kebab-case` in YAML, `snake_case` in JSON
**YAML Examples**:
```yaml
project-config:
  tech-stack: "..."
  team-size: "..."
```

**JSON Examples**:
```json
{
  "command_metadata": {
    "tech_stack": "...",
    "team_size": "..."
  }
}
```

## Naming Validation Rules

### Automated Checks
Commands and components should validate:
1. **File Extension**: Must be `.md` for templates
2. **Case Consistency**: kebab-case throughout
3. **Character Set**: Only lowercase letters, numbers, hyphens
4. **Length Limits**: 
   - Commands: 3-30 characters
   - Components: 5-40 characters
   - Directories: 3-20 characters

### Manual Review Checklist
Before adding new templates:
- [ ] Name follows kebab-case convention
- [ ] Name is descriptive and clear
- [ ] Name fits within category logic
- [ ] Name doesn't conflict with existing files
- [ ] Placeholders follow [INSERT_X] pattern
- [ ] Directory structure is logical

## Migration Guidelines

### Renaming Existing Files
When renaming for consistency:
1. **Document Changes** in git commit message
2. **Update References** in other files
3. **Preserve Functionality** ensure commands still work
4. **Test Thoroughly** after renaming
5. **Update Documentation** reflect new names

### Adding New Templates
When adding new templates:
1. **Follow Conventions** use established patterns
2. **Check Conflicts** ensure name uniqueness
3. **Logical Placement** put in appropriate category
4. **Update Indexes** add to relevant documentation
5. **Test Integration** ensure works with existing templates

## Convention Benefits

### User Experience
- **Predictable**: Users can guess command/component names
- **Discoverable**: Logical naming aids in finding functionality
- **Consistent**: Same patterns across all templates
- **Professional**: Clean, standardized appearance

### Maintenance Benefits
- **Organized**: Clear structure for developers
- **Searchable**: Easy to find specific functionality
- **Scalable**: Patterns support growth
- **Automated**: Enables automated processing and validation

### Integration Benefits
- **Compatible**: Works well with various editors and tools
- **Portable**: Consistent across different environments
- **Version Control**: Clean git history and diffs
- **Documentation**: Self-documenting through clear names

---
*Naming Convention Version: 1.0*
*Last Updated: 2025-07-29*
*Compliance: All 102 commands and 72 components follow these conventions*