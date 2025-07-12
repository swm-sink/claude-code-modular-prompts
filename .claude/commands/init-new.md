# /init-new - Interactive Setup for New Projects

Guides you through creating a perfectly configured framework for your new project.

## Usage
```
/init-new
```

## What It Does

This command provides an interactive setup wizard for new projects:

1. **Project Information Gathering**
   - Project name and description
   - Domain (web, mobile, data science, etc.)
   - Primary programming language
   - Framework and technology choices

2. **Configuration Customization**
   - Directory structure preferences
   - Quality standards and thresholds
   - Development workflow setup
   - Testing and deployment configuration

3. **Framework Optimization**
   - Domain-specific module selection
   - Custom persona configuration
   - Quality gate customization
   - Performance and security settings

## Interactive Questions

I'll ask you about:

**Project Basics**
- What type of project are you building?
- What domain/industry is this for?
- What's your primary programming language?
- What frameworks will you use?

**Quality Standards**
- What test coverage percentage do you target?
- How strict should quality enforcement be?
- What performance benchmarks matter?

**Development Workflow**
- What's your preferred directory structure?
- What build and test commands will you use?
- How do you manage deployments?

**Team Preferences**
- Coding style and conventions?
- Documentation standards?
- Git workflow preferences?

## Example Session

```
/init-new

> What type of project are you building?
"A React web application with TypeScript"

> What domain is this for?
"E-commerce platform"

> Target test coverage?
"90%"

[... more questions ...]

✅ Generated PROJECT_CONFIG.xml with your preferences!
```

## Benefits

- **Zero Manual Configuration** - Answer questions, get perfect setup
- **Best Practices Built-in** - Recommendations based on your domain
- **Customized Workflows** - Framework adapts to your preferences
- **Production Ready** - Quality gates and standards configured

## Related Commands

- `/init-custom` - For existing projects
- `/init-research` - Research-driven setup
- `/init-validate` - Validate configuration

$ARGUMENTS