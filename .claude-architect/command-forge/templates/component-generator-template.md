---
name: create-[COMPONENT_TYPE]
description: Generate a new [COMPONENT_TYPE] following project conventions
usage: "create-[COMPONENT_TYPE] <name> [options]"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob]
category: component-generation
---

# Create [COMPONENT_TYPE] Command

## Purpose
This command generates a new [COMPONENT_TYPE] following the project's established patterns and conventions discovered during the deep discovery consultation.

## Discovery-Based Configuration

### Detected Patterns
- **Naming Convention**: [NAMING_CONVENTION]
- **Directory Structure**: [DIRECTORY_STRUCTURE]
- **Test Pattern**: [TEST_PATTERN]
- **Framework**: [FRAMEWORK_DETECTED]
- **Style Guide**: [STYLE_GUIDE]

## Command Workflow

### Step 1: Validate Component Name
```yaml
validation:
  - Check naming convention compliance
  - Verify no conflicts with existing components
  - Ensure valid characters and format
```

### Step 2: Generate Component Structure

The command will create the following structure based on discovered patterns:

```
[COMPONENT_ROOT]/
├── [COMPONENT_NAME].[EXTENSION]
├── [COMPONENT_NAME].test.[EXTENSION]
├── [COMPONENT_NAME].types.[EXTENSION] (if TypeScript)
├── [COMPONENT_NAME].styles.[STYLE_EXTENSION] (if applicable)
└── index.[EXTENSION] (if barrel pattern detected)
```

### Step 3: Apply Project-Specific Templates

#### Component Template
```[LANGUAGE]
[IMPORT_PATTERN]

[COMPONENT_DECLARATION_PATTERN]

[IMPLEMENTATION_PATTERN]

[EXPORT_PATTERN]
```

#### Test Template
```[LANGUAGE]
[TEST_IMPORT_PATTERN]

[TEST_SUITE_PATTERN]

[TEST_CASES_PATTERN]
```

### Step 4: Integration Tasks

1. **Update barrel exports** (if pattern detected)
2. **Register in module system** (if applicable)
3. **Update dependency injection** (if applicable)
4. **Add to component index** (if maintained)

### Step 5: Generate Documentation

Automatically create documentation following project standards:
- Component API documentation
- Usage examples
- Props/Parameters documentation
- Integration guide

## Options

- `--type <type>`: Specify component type (default: [DEFAULT_TYPE])
- `--skip-tests`: Skip test generation
- `--with-story`: Include Storybook story (if Storybook detected)
- `--with-docs`: Generate extended documentation
- `--dry-run`: Preview what will be generated

## Success Criteria

- [ ] Component follows naming conventions
- [ ] Proper directory placement
- [ ] Tests generated and passing
- [ ] Documentation created
- [ ] No linting errors
- [ ] Type checking passes (if applicable)

## Error Handling

- **Name conflicts**: Suggest alternative names
- **Invalid patterns**: Fall back to safe defaults
- **Missing dependencies**: Prompt for installation
- **Permission issues**: Request appropriate access

## Examples

```bash
# Basic component creation
/create-[COMPONENT_TYPE] UserProfile

# With options
/create-[COMPONENT_TYPE] UserProfile --type container --with-story

# Dry run to preview
/create-[COMPONENT_TYPE] UserProfile --dry-run
```

## Post-Generation Checklist

1. ✅ Component file created in correct location
2. ✅ Test file generated with basic test cases
3. ✅ Component registered/exported appropriately
4. ✅ Documentation updated
5. ✅ Linting and type checking pass
6. ✅ Git status shows expected changes

## Discovered Project Context

This command is customized based on discoveries from:
- **Technical Architecture Analysis**: [ANALYSIS_DATE]
- **Code Pattern Detection**: [DETECTION_DATE]
- **Framework Analysis**: [FRAMEWORK_VERSION]
- **Testing Strategy**: [TEST_FRAMEWORK]

## Related Commands

- `/test-[COMPONENT_TYPE]`: Run tests for components
- `/document-[COMPONENT_TYPE]`: Generate documentation
- `/refactor-[COMPONENT_TYPE]`: Refactor existing components
- `/analyze-[COMPONENT_TYPE]`: Analyze component usage

---

*This command template is generated based on deep discovery consultation completed on [CONSULTATION_DATE]*