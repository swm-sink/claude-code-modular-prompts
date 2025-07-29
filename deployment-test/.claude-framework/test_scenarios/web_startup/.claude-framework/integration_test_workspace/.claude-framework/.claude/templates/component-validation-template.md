# Component Validation Template

## Component Information
- **Component Name**: `component-name.md`
- **Category**: [category]
- **Purpose**: [Brief description of what this component does]
- **Dependencies**: [List of other components this depends on]
- **Used By**: [List of commands that use this component]

## Validation Checklist

### ✅ Structure Validation
- [ ] Component file exists at correct path: `.claude/components/[category]/[name].md`
- [ ] Component has proper XML structure with `<prompt_component>` root
- [ ] Component has clear `<description>` section
- [ ] Component follows naming conventions (`*-framework.md`, `*-architecture.md`)

### ✅ Content Validation  
- [ ] Description clearly explains component purpose and functionality
- [ ] Component is reusable across multiple commands
- [ ] Component implements a specific framework/pattern, not ad-hoc logic
- [ ] Component content is focused and cohesive (single responsibility)

### ✅ Integration Validation
- [ ] Component can be included via `<include>components/[category]/[name].md</include>`
- [ ] Component doesn't conflict with other commonly used components
- [ ] Component variables/placeholders are clearly documented
- [ ] Component works when combined with validation-framework.md

### ✅ Dependency Validation
- [ ] All component dependencies are documented
- [ ] Circular dependencies are avoided
- [ ] Dependent components actually exist
- [ ] Dependency chain is reasonable (< 5 levels deep)

### ✅ Usage Validation
- [ ] At least one command successfully uses this component
- [ ] Component inclusion doesn't break command functionality
- [ ] Component adds clear value when included
- [ ] Component can be excluded without breaking core functionality

### ✅ Quality Standards
- [ ] Component follows prompt engineering best practices
- [ ] Component content is concise but comprehensive
- [ ] Component is documented in modular-components.md context file
- [ ] Component has clear use cases and examples

## Functional Testing

### Test 1: Component Inclusion
```bash
# Test that component can be included in a minimal command
echo "Testing component inclusion..."
# Create test command with component include
# Verify no syntax errors
```

### Test 2: Integration Testing  
```bash
# Test component with validation-framework.md
# Test component with common components (error-handling, progress-reporting)
# Verify no conflicts or duplicate functionality
```

### Test 3: Performance Testing
```bash
# Measure component load time
# Verify component doesn't significantly increase prompt size
# Test component with various input sizes
```

## Security Review
- [ ] Component doesn't expose sensitive information
- [ ] Component follows secure prompt engineering practices
- [ ] Component doesn't introduce prompt injection vulnerabilities
- [ ] Component input validation is appropriate

## Documentation Review
- [ ] Component is listed in components/README.md
- [ ] Component category is properly documented
- [ ] Component usage examples are clear and accurate
- [ ] Component architecture principles are followed

## Validation Results

### Issues Found
1. [List any issues found during validation]
2. [Include severity: Critical, High, Medium, Low]
3. [Include proposed fixes]

### Performance Metrics
- **Load Time**: [measured time]
- **Prompt Size Impact**: [token increase]
- **Memory Usage**: [if applicable]

### Compatibility Matrix
| Component | Compatible | Issues | Notes |
|-----------|------------|--------|-------|
| validation-framework.md | ✅/❌ | [issues] | [notes] |
| error-handling.md | ✅/❌ | [issues] | [notes] |
| progress-reporting.md | ✅/❌ | [issues] | [notes] |

### Final Status
- [ ] **APPROVED** - Component is ready for production use
- [ ] **CONDITIONAL** - Component needs minor fixes before approval  
- [ ] **REJECTED** - Component needs major rework or should be deprecated

### Validation Date
**Date**: [YYYY-MM-DD]  
**Validator**: [Name]  
**Next Review**: [YYYY-MM-DD]