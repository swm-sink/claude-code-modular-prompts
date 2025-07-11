# Framework Customization Guide

This guide explains how to customize the Claude Code Modular Prompts Framework for your specific project needs using the PROJECT_CONFIG.xml system.

## Quick Start

1. **Copy the template**: Copy `PROJECT_CONFIG_TEMPLATE.md` to your project root
2. **Create your config**: Save it as `PROJECT_CONFIG.xml` 
3. **Replace placeholders**: Fill in all [INSERT ...] tags with your values
4. **Initialize**: Run `/init --wizard` to validate and apply configuration

## Understanding Customization

The framework is now **configuration-driven** rather than hardcoded. This means:
- ✅ No need to modify framework files
- ✅ Project-specific values override defaults
- ✅ Easy to update and maintain
- ✅ Share configurations across team

## Configuration Sections

### 1. Basic Project Information
```xml
<project_info>
  <name>My Awesome Project</name>
  <domain>web-development</domain>
  <primary_language>typescript</primary_language>
  <framework_stack>react+nextjs+express</framework_stack>
</project_info>
```

**What it affects:**
- Domain-specific persona selection
- Default tool choices
- Quality gate priorities
- Command behaviors

### 2. Project Structure
```xml
<project_structure>
  <source_directory>app</source_directory>  <!-- Instead of default 'src' -->
  <test_directory>__tests__</test_directory> <!-- Instead of 'tests' -->
  <docs_directory>documentation</docs_directory>
</project_structure>
```

**What it affects:**
- Where framework looks for files
- Where new files are created
- Test discovery patterns
- Documentation generation location

### 3. Quality Standards
```xml
<quality_standards>
  <test_coverage>
    <threshold>95</threshold>  <!-- Higher than default 90% -->
    <enforcement>BLOCKING</enforcement>
  </test_coverage>
  <performance>
    <response_time_p95>100ms</response_time_p95>  <!-- Stricter than 200ms -->
  </performance>
</quality_standards>
```

**Enforcement Levels:**
- `BLOCKING`: Prevents any progress until satisfied
- `CONDITIONAL`: Warns but allows override with justification
- `ADVISORY`: Suggestions only

### 4. Development Commands
```xml
<commands>
  <test>pnpm test</test>  <!-- Instead of npm test -->
  <lint>pnpm run lint:fix</lint>
  <build>pnpm build && pnpm postbuild</build>
</commands>
```

**Auto-detection:** Use `auto_detect` to let framework figure it out

### 5. Domain-Specific Rules
```xml
<domain_specific_rules>
  <!-- Web Development Example -->
  <rule>All components must have accessibility tests</rule>
  <rule>Lighthouse score must be > 90 for all metrics</rule>
  <rule>Support latest 2 versions of major browsers</rule>
  
  <!-- Mobile Development Example -->
  <rule>Memory usage must stay under 100MB</rule>
  <rule>Cold start time < 2 seconds</rule>
  <rule>Support iOS 14+ and Android 10+</rule>
</domain_specific_rules>
```

### 6. Custom Personas
```xml
<custom_personas>
  <persona>
    <name>accessibility-specialist</name>
    <expertise>WCAG compliance and screen reader optimization</expertise>
    <tools>axe-core, NVDA, JAWS, VoiceOver</tools>
    <quality_gates>
      <gate>All interactive elements keyboard accessible</gate>
      <gate>ARIA labels on all meaningful elements</gate>
      <gate>Color contrast ratio > 4.5:1</gate>
    </quality_gates>
  </persona>
</custom_personas>
```

### 7. Framework Behavior
```xml
<framework_behavior>
  <file_creation_policy>conservative</file_creation_policy>  <!-- or moderate, liberal -->
  <test_first_enforcement>strict</test_first_enforcement>    <!-- or flexible, advisory -->
  <ai_temperature>
    <factual>0.1</factual>      <!-- Lower = more deterministic -->
    <analysis>0.2</analysis>
    <creative>0.8</creative>     <!-- Higher = more creative -->
  </ai_temperature>
</framework_behavior>
```

## Advanced Customization

### Overriding Existing Personas
```xml
<persona_overrides>
  <backend_engineer>
    <tool_preferences>
      <primary_tools>
        <tool>Deno instead of Node.js</tool>
        <tool>PostgreSQL exclusively</tool>
      </primary_tools>
    </tool_preferences>
  </backend_engineer>
</persona_overrides>
```

### Environment-Specific Configs
Create multiple configs:
- `PROJECT_CONFIG.dev.xml` - Development settings
- `PROJECT_CONFIG.prod.xml` - Production settings
- `PROJECT_CONFIG.ci.xml` - CI/CD settings

Load with: `/init --config PROJECT_CONFIG.dev.xml`

### Dynamic Values
Some values support dynamic resolution:
```xml
<build_directory>${BUILD_ENV:-dist}</build_directory>
<api_endpoint>${API_URL:-http://localhost:3000}</api_endpoint>
```

## Common Patterns

### Strict Quality Project
```xml
<quality_standards>
  <test_coverage>
    <threshold>100</threshold>
    <enforcement>BLOCKING</enforcement>
  </test_coverage>
  <code_quality>
    <linter>eslint</linter>
    <formatter>prettier</formatter>
    <type_checker>typescript</type_checker>
  </code_quality>
</quality_standards>
<framework_behavior>
  <test_first_enforcement>strict</test_first_enforcement>
</framework_behavior>
```

### Rapid Prototyping Project
```xml
<quality_standards>
  <test_coverage>
    <threshold>60</threshold>
    <enforcement>ADVISORY</enforcement>
  </test_coverage>
</quality_standards>
<framework_behavior>
  <file_creation_policy>liberal</file_creation_policy>
  <test_first_enforcement>advisory</test_first_enforcement>
</framework_behavior>
```

### Enterprise Project
```xml
<security_requirements>
  <authentication>oauth2</authentication>
  <compliance>SOC2,GDPR</compliance>
  <vulnerability_scanning>enabled</vulnerability_scanning>
</security_requirements>
<quality_standards>
  <test_coverage>
    <threshold>90</threshold>
    <enforcement>BLOCKING</enforcement>
  </test_coverage>
</quality_standards>
```

## Validation and Troubleshooting

### Validate Your Configuration
```bash
/init --validate
```

This will:
- Check XML syntax
- Verify all required fields
- Test placeholder resolution
- Report any issues

### Common Issues

**Issue**: "Configuration not found"
- **Solution**: Ensure PROJECT_CONFIG.xml is in project root
- **Check**: File permissions allow reading

**Issue**: "Invalid path: project_structure.soruce_directory"
- **Solution**: Fix typo - should be "source_directory"
- **Check**: Use dot notation for nested values

**Issue**: "Override not applying"
- **Solution**: Check override syntax matches exactly
- **Check**: Persona names use underscores (backend_engineer not backend-engineer)

### Debug Mode
```bash
/init --debug
```

Shows:
- Configuration loading process
- Placeholder resolution details
- Override application order
- Final resolved values

## Best Practices

1. **Start with defaults**: Only override what you need
2. **Document why**: Add comments explaining non-standard values
3. **Version control**: Commit PROJECT_CONFIG.xml with your code
4. **Team alignment**: Review configuration in team meetings
5. **Progressive enhancement**: Start simple, add complexity as needed

## Migration from Hardcoded Values

If you have existing projects:

1. Run `/init --wizard` to generate initial config
2. Review detected values and adjust as needed
3. Test thoroughly with new configuration
4. Remove any local framework modifications

## Getting Help

- Run `/init --help` for command options
- Check logs in `.claude/logs/` for detailed errors
- Framework adapts to YOUR project, not vice versa

Remember: The framework is now YOUR framework, customized for YOUR project's needs!