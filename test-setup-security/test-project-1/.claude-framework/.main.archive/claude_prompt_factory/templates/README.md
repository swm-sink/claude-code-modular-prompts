# Claude Code Prompt Factory Templates

This directory contains standardized templates and validation tools to ensure consistency and DRY principles across the entire Claude Code Prompt Factory.

## 📋 Available Templates

### 🤖 Command Template (`command-template.md`)
Standardized template for creating new commands with:
- **YAML Frontmatter**: Required metadata for Claude Code discovery
- **XML Structure**: Proper command structure with metadata, arguments, examples
- **Component Integration**: Standard patterns for including shared components
- **Dependencies Section**: Automatic dependency tracking and validation

**Key Features:**
- 5-phase execution pattern
- Built-in DRY component integration
- Standardized error handling and reporting
- Consistent argument handling and validation

### 🧩 Component Template (`component-template.md`)
Standardized template for creating reusable components with:
- **XML Structure**: `<prompt_component>` with `<step>` elements
- **Process Sections**: Structured approach to component functionality
- **Output Standardization**: Consistent output formats and behaviors
- **Integration Guidelines**: Clear patterns for component usage

**Key Features:**
- 4-phase process structure
- Standardized output formatting
- Behavioral consistency guidelines
- Parameter handling patterns

### ⚙️ Core Template (`core-template.md`)
Specialized template for foundational system components with:
- **System Integration**: Deep integration with Claude Code infrastructure
- **High Priority**: Core system functionality designation
- **Enhanced Validation**: Additional system integrity checks
- **Foundation Capabilities**: System-wide behavior and routing

**Key Features:**
- Core system responsibility patterns
- System validation and integrity checks
- Foundational operation structure
- Enhanced error handling for system-critical functions

## 🔍 Validation System

### Template Validator (`template-validator.py`)
Comprehensive validation system that ensures all commands and components follow standardized patterns:

**Command Validation:**
- ✅ YAML frontmatter completeness (description, argument-hint, allowed-tools)
- ✅ XML structure validity and proper formatting
- ✅ Component includes existence and formatting
- ✅ Dependencies section accuracy

**Component Validation:**
- ✅ XML structure with required elements (step, description, output)
- ✅ Proper component structure and formatting
- ✅ Output format consistency and completeness

**Usage:**
```bash
cd claude_prompt_factory/templates
python3 template-validator.py
```

**Output:**
- Detailed validation report with scores and recommendations
- Error identification and resolution guidance
- Template compliance metrics and trending

## 📚 Best Practices

### Command Creation
1. **Start with Template**: Always begin with `command-template.md`
2. **Follow DRY Principles**: Include relevant shared components
3. **Validate Early**: Run template validator during development
4. **Test Integration**: Ensure component includes work correctly

### Component Creation
1. **Single Responsibility**: Each component should have one clear purpose
2. **Standardized Output**: Follow consistent formatting patterns
3. **Clear Documentation**: Include comprehensive description and usage
4. **Integration Friendly**: Design for reuse across multiple commands

### Validation Workflow
1. **Pre-Commit**: Run template validator before committing changes
2. **Continuous Integration**: Include validation in CI/CD pipeline
3. **Quality Gates**: Maintain minimum template compliance scores
4. **Regular Audits**: Periodic comprehensive validation runs

## 🎯 Template Usage Examples

### Creating a New Command
```bash
# 1. Copy template
cp templates/command-template.md commands/new-category/my-command.md

# 2. Replace placeholders
# [COMMAND_NAME] → my-command
# [TITLE] → My Command Title
# [DESCRIPTION] → Command description

# 3. Add relevant components
# Include appropriate shared components for your use case

# 4. Validate
python3 templates/template-validator.py
```

### Creating a New Component
```bash
# 1. Copy template
cp templates/component-template.md components/category/my-component.md

# 2. Replace placeholders
# [COMPONENT_NAME] → My Component Name
# [PROCESS_SECTION_NAME] → process_flow
# [ADDITIONAL_SECTION_NAME] → standards

# 3. Validate
python3 templates/template-validator.py
```

## 📊 Quality Standards

### Scoring System
- **Commands**: 100 point scale
  - YAML Frontmatter: 24 points
  - XML Structure: 25 points
  - Component Includes: 25 points
  - Dependencies Section: 25 points

- **Components**: 100 point scale
  - XML Structure: 50 points
  - Component Structure: 25 points
  - Output Format: 25 points

### Quality Gates
- **Minimum Score**: 80/100 for production deployment
- **Target Score**: 95/100 for exemplary templates
- **Critical Issues**: 0 errors for production readiness

## 🔄 Template Evolution

### Version Control
- Templates are versioned alongside the main codebase
- Breaking changes require migration guidelines
- Backward compatibility maintained where possible

### Enhancement Process
1. **Proposal**: Document template improvements
2. **Validation**: Test with existing commands/components
3. **Migration**: Update existing files to new standard
4. **Documentation**: Update best practices and examples

## 🛡️ Quality Assurance

### Automated Validation
- Pre-commit hooks for template compliance
- CI/CD integration for continuous validation
- Automated quality reporting and trending

### Manual Review
- Peer review for template changes
- Architecture review for new template patterns
- Regular audits of template effectiveness

---

## Getting Started

1. **Review Templates**: Familiarize yourself with the standard patterns
2. **Run Validator**: Test current state of your commands/components
3. **Follow Examples**: Use the patterns in `feature.md` and `debug.md`
4. **Validate Changes**: Always run validation before committing

For questions or improvements, refer to the main project documentation or submit issues through the standard process.