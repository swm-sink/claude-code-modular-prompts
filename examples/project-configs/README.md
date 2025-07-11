# Example Project Configurations

This directory contains example PROJECT_CONFIG.xml files for different types of projects. Use these as starting points for your own project configuration.

## Available Examples

### 1. web-react-typescript.xml
**For:** Modern web applications using React and TypeScript
- Frontend: React with TypeScript
- Backend: Node.js with Express
- Testing: Jest with 85% coverage requirement
- Quality: ESLint, Prettier, strict TypeScript
- Special focus: Accessibility, performance, responsive design

### 2. data-science-python.xml
**For:** Data science and machine learning projects
- Language: Python with scientific libraries
- Stack: pandas, scikit-learn, TensorFlow, Jupyter
- Testing: pytest with 80% coverage (conditional)
- Quality: pylint, black, mypy
- Special focus: Reproducibility, experiment tracking, fairness

### 3. mobile-react-native.xml
**For:** Cross-platform mobile applications
- Framework: React Native with TypeScript
- Platform: iOS and Android via Expo
- Testing: Jest with 75% coverage requirement
- Quality: Platform-specific guidelines
- Special focus: Performance, offline support, platform compliance

### 4. api-microservices.xml
**For:** Distributed microservices and API platforms
- Language: Go for high performance
- Architecture: Microservices with Kubernetes
- Testing: 90% coverage requirement (strict)
- Quality: API versioning, OpenAPI docs
- Special focus: Distributed tracing, rate limiting, resilience

## How to Use

1. **Choose an example** that matches your project type
2. **Copy to your project root**:
   ```bash
   cp examples/project-configs/web-react-typescript.xml ./PROJECT_CONFIG.xml
   ```
3. **Customize the values** for your specific needs
4. **Initialize the framework**:
   ```bash
   /init --config PROJECT_CONFIG.xml
   ```

## Customization Tips

### Adjusting Quality Standards
- **Strict projects**: Increase coverage to 95-100%, use BLOCKING enforcement
- **Prototypes**: Reduce coverage to 60-70%, use ADVISORY enforcement
- **Performance-critical**: Tighten response time thresholds

### Adding Custom Personas
Each example includes domain-appropriate personas. Add your own:
```xml
<custom_personas>
  <persona>
    <name>your-specialist</name>
    <expertise>Your domain expertise</expertise>
    <tools>Your specific tools</tools>
  </persona>
</custom_personas>
```

### Domain-Specific Rules
Each example includes rules specific to that domain. Modify based on your needs:
- Remove rules that don't apply
- Add project-specific requirements
- Adjust thresholds and limits

## Creating Your Own

If none of these examples fit:
1. Start with `PROJECT_CONFIG_TEMPLATE.md` in the root
2. Fill in all [INSERT HERE] placeholders
3. Use these examples as reference for values
4. Test with `/init --validate` before applying

## Common Modifications

### Different Package Managers
```xml
<!-- npm (default) -->
<install>npm install</install>

<!-- yarn -->
<install>yarn install</install>

<!-- pnpm -->
<install>pnpm install</install>

<!-- pip -->
<install>pip install -r requirements.txt</install>
```

### Different Test Runners
```xml
<!-- Jest (JavaScript) -->
<test>npm test</test>
<tool>jest</tool>

<!-- pytest (Python) -->
<test>pytest</test>
<tool>pytest-cov</tool>

<!-- Go test -->
<test>go test ./...</test>
<tool>go-cover</tool>
```

### Different Linters
```xml
<!-- JavaScript/TypeScript -->
<linter>eslint</linter>

<!-- Python -->
<linter>pylint</linter>

<!-- Go -->
<linter>golangci-lint</linter>

<!-- Rust -->
<linter>clippy</linter>
```

## Questions?

- See `docs/CUSTOMIZATION_GUIDE.md` for detailed documentation
- Run `/init --help` for command options
- These are starting points - customize freely!