# 🏗️ Project Templates - Quick Start Configurations

Ready-to-use PROJECT_CONFIG.xml templates for common tech stacks. Copy, customize, and start using the framework immediately.

## 🚀 Available Templates

### Web Applications
**Directory**: [web-applications/](web-applications/)

**Templates**:
- [react-project-config.xml](web-applications/react-project-config.xml) - **React/Next.js** projects with TypeScript, Jest, ESLint
- [python-django-config.xml](web-applications/python-django-config.xml) - **Django** projects with pytest, black, mypy
- [go-api-config.xml](web-applications/go-api-config.xml) - **Go API** projects with testing and linting standards

## 🎯 How to Use Templates

### 1. Choose Your Template
Pick the template that matches your tech stack:
```bash
# For React projects
cp examples/project-templates/web-applications/react-project-config.xml PROJECT_CONFIG.xml

# For Django projects  
cp examples/project-templates/web-applications/python-django-config.xml PROJECT_CONFIG.xml

# For Go API projects
cp examples/project-templates/web-applications/go-api-config.xml PROJECT_CONFIG.xml
```

### 2. Customize for Your Project
Edit the copied PROJECT_CONFIG.xml:
- Update project name and description
- Adjust directory structure to match your project
- Modify quality thresholds and standards
- Add project-specific tools and frameworks

### 3. Test Framework Integration
```bash
/auto "analyze my project structure"
# Should respond with project-specific suggestions
```

## 📋 Template Features

Each template includes:
- ✅ **Tech stack configuration** - Language, framework, database
- ✅ **Directory structure** - Source, tests, docs paths
- ✅ **Quality standards** - Test coverage, lint rules, security
- ✅ **Development commands** - Test, build, lint, deploy commands
- ✅ **Framework optimization** - Context management, performance tuning

## 🔧 Customization Guide

### Common Customizations
```xml
<!-- Update for your project -->
<project_info>
  <name>your-project-name</name>
  <domain>your-business-domain</domain>
</project_info>

<!-- Adjust quality thresholds -->
<quality_standards>
  <test_coverage>
    <threshold>95</threshold>  <!-- Increase for critical projects -->
  </test_coverage>
</quality_standards>

<!-- Add your tools -->
<development_workflow>
  <commands>
    <test>your-test-command</test>
    <lint>your-lint-command</lint>
  </commands>
</development_workflow>
```

## ✅ Validation

After setting up your template:
- [ ] Framework responds to `/auto` command
- [ ] Commands understand your tech stack
- [ ] Quality gates enforce your standards
- [ ] Project-specific suggestions work

## 🎓 Next Steps

1. **Start with examples** - Use [beginner examples](../01-beginner/) to test your setup
2. **Learn commands** - Master the core commands with your actual project
3. **Customize further** - Adjust configuration as you learn more about the framework

---

**Quick tip**: Start with the closest template and customize gradually. The framework adapts to your specific needs over time!