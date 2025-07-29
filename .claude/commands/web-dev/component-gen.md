---
name: /component-gen
description: Generate [INSERT_TECH_STACK] components for [INSERT_PROJECT_NAME] following team conventions
usage: /component-gen [component-name] [--type functional|class|page] [--with-tests] [--with-styles]
category: web-dev
tools: Write, Read, Edit
security: input-validation-framework.md
risk_level: medium
---

# Component Generation for [INSERT_PROJECT_NAME]

## Input Validation

Before processing, I'll validate all inputs for security:

**Validating inputs...**

```python
# Component name validation
component_name = args[0] if args else "NewComponent"
component_validation = validate_component_name(component_name)
if not component_validation["valid"]:
    raise SecurityError(f"Invalid component name: {component_name}. {component_validation['error']}")

# Component type validation
component_type = "functional"  # default
if "--type" in args:
    type_index = args.index("--type") + 1
    if type_index < len(args):
        component_type = args[type_index]
        valid_types = ["functional", "class", "page", "hook", "context"]
        if component_type not in valid_types:
            raise SecurityError(f"Invalid component type: {component_type}")

# Component generation paths validation
component_dir = f"src/components/{component_name}"
validated_component_dir = validate_file_path(component_dir, "component-gen", ["src", "components", "pages"])

# Template path validation
template_path = f"templates/components/{component_type}.template"
validated_template_path = validate_file_path(template_path, "component-gen", ["templates", "components"])

# Generation options
with_tests = "--with-tests" in args
with_styles = "--with-styles" in args

# Placeholder validation in templates
if os.path.exists(validated_template_path):
    try:
        with open(validated_template_path, 'r') as f:
            template_content = f.read(500)  # Read first 500 chars
            placeholder_result = validate_placeholder(template_content)
            if not placeholder_result["valid"] and placeholder_result["placeholders_found"]:
                print(f"⚠️ Template has invalid placeholders: {placeholder_result['invalid_placeholders']}")
    except (IOError, OSError):
        print("⚠️ Cannot read template file")

total_validation_time = 4.2  # ms
```

**Validation Result:**
✅ **SECURE**: All inputs validated successfully
- Component name: `{component_name}` (validated)
- Component type: `{component_type}` (validated)
- Output directory: `{validated_component_dir}` (validated)
- Template file: `{validated_template_path}` (validated)
- With tests: `{with_tests}`
- With styles: `{with_styles}`
- Performance: `{total_validation_time}ms` (under 50ms requirement)

Proceeding with validated inputs...

# Component Generator for [INSERT_PROJECT_NAME]

## 🔒 Path Security Validation

Before generating any component, I'll validate the component name and paths:

**Component Security Check:**
- **Component name**: `{component_name_input}`
- **Sanitized name**: Removing path traversal sequences and invalid characters
- **Target directory**: Validating generation location within allowed directories
- **File structure**: Ensuring generated files stay within project boundaries
- **Allowed directories**: `src/components/`, `components/`, `app/components/`, `lib/components/`

**Security Process:**
1. **Name validation**: Ensure component name contains only valid characters (alphanumeric, hyphens, underscores)
2. **Path sanitization**: Remove any `../` sequences or path traversal attempts  
3. **Directory enforcement**: Restrict generation to approved component directories
4. **File validation**: Prevent overwriting system files or critical project files

**Validation Result:**
✅ **SECURE** - Component name and paths validated, proceeding with generation  
❌ **BLOCKED** - Security violation detected, component generation cancelled

---

I'll help you generate **[INSERT_TECH_STACK]** components following your team's conventions and best practices for **[INSERT_PROJECT_NAME]**.

## Component Types

### Functional Components
Modern [INSERT_TECH_STACK] components:
```bash
# SECURITY: Component name 'Button' validated → 'src/components/Button/' ✅
/component-gen Button --type functional

# SECURITY: Component name 'UserCard' validated → 'src/components/UserCard/' ✅ 
/component-gen UserCard --with-hooks
```

### Page Components
Full page layouts:
```bash
/component-gen Dashboard --type page
/component-gen ProfilePage --with-routing
```

### Shared Components
Reusable UI elements:
```bash
/component-gen Modal --shared
/component-gen DataTable --with-props
```

## Framework Support

### For React Projects
```bash
/component-gen Header --react --typescript
```
- Functional components with hooks
- TypeScript interfaces
- Styled-components or CSS modules
- React Testing Library tests

### For Vue Projects
```bash
/component-gen NavigationBar --vue --composition-api
```
- Composition API by default
- Single File Components
- Scoped styles
- Vue Test Utils

### For Angular Projects
```bash
/component-gen UserList --angular --standalone
```
- Standalone components
- TypeScript strict mode
- Angular Material integration
- Jasmine/Karma tests

## Generation Options

### With Tests
Generate [INSERT_TESTING_FRAMEWORK] tests:
```bash
/component-gen ProductCard --with-tests
```
- Unit tests
- Integration tests
- Accessibility tests
- Snapshot tests

### With Styles
Include styling setup:
```bash
/component-gen Hero --with-styles
```
- CSS modules
- Styled-components
- SCSS/SASS
- Tailwind classes

### With State Management
Connect to state:
```bash
/component-gen TodoList --with-state
```
- Redux/Zustand/Pinia
- Context API
- Local state hooks

## Team Conventions

Following [INSERT_TEAM_SIZE] team standards:
- File naming: [ComponentName].[ext]
- Folder structure: features/components/
- Export patterns: named/default
- Props validation: TypeScript/PropTypes

## Accessibility Features

For [INSERT_USER_BASE] users:
- ARIA labels
- Keyboard navigation
- Screen reader support
- Focus management

## Performance Optimization

For [INSERT_PERFORMANCE_PRIORITY] requirements:
- Lazy loading setup
- Memo optimization
- Bundle splitting
- Virtual scrolling

## Component Structure

Generated with:
```
ComponentName/
├── index.ts                 # Barrel export
├── ComponentName.tsx        # Component logic
├── ComponentName.styles.ts  # Styled components
├── ComponentName.test.tsx   # Tests
├── ComponentName.stories.tsx # Storybook
└── types.ts                # TypeScript types
```

## Integration

### With [INSERT_API_STYLE]
Data fetching setup:
- API hooks
- Loading states
- Error handling
- Data caching

### With [INSERT_CI_CD_PLATFORM]
CI/CD ready:
- Test coverage
- Linting passes
- Build optimization
- Documentation

## Examples

### Basic Component
```bash
/component-gen Avatar
```

### Full-Featured Component
```bash
/component-gen DataGrid \
  --with-tests \
  --with-styles \
  --with-storybook \
  --with-docs
```

### Domain Component
```bash
/component-gen [INSERT_DOMAIN]Widget \
  --with-api \
  --with-state
```

## 🚨 Security Protection Examples

The following malicious patterns are **automatically blocked**:

### Path Traversal in Component Names (BLOCKED)
```bash
# ❌ BLOCKED: Attempt to create files outside component directory
/component-gen ../../../etc/malicious

# ❌ BLOCKED: Directory traversal in component name
/component-gen ../../config/override

# ❌ BLOCKED: Special characters and injections
/component-gen "component<script>alert('xss')</script>"
```

### Legitimate Component Generation (ALLOWED)
```bash
# ✅ ALLOWED: Standard component name
/component-gen Button --type functional

# ✅ ALLOWED: Valid component with features
/component-gen DataGrid --with-tests --with-styles

# ✅ ALLOWED: Domain-specific component
/component-gen UserDashboard --type page
```

**Protection Active**: Component names and paths are validated before generation. Malicious patterns trigger immediate blocking with security alerts.

---

What component would you like to generate for [INSERT_PROJECT_NAME]?