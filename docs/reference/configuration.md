# Configuration Reference

> **Quick Start**: See [Project Configuration](../user-guide/customization/project-config.md) for basic setup. This reference covers complete configuration options.

## 📋 Complete PROJECT_CONFIG.xml Reference

### Root Element Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0" type="project">
  <!-- All configuration sections go here -->
</project_configuration>
</?xml>
```

**Root Attributes**:
- `version` (required): Configuration schema version (currently "1.0.0")
- `type` (optional): Configuration type ("project", "team_base", "template")

## 🏷️ Project Information Section

### Basic Project Information

```xml
<project_info>
  <name>Your Project Name</name>
  <description>Brief project description for context</description>
  <domain>web-development</domain>
  <primary_language>typescript</primary_language>
  <framework_stack>react+nextjs+tailwind</framework_stack>
  <project_type>application</project_type>
  <team_size>small</team_size>
</project_info>
```

**Field Definitions**:

**name** (required):
- Project display name used in documentation and logs
- Example: `"E-commerce Platform"`, `"Mobile Banking App"`

**description** (optional):
- Brief description providing context for AI assistance
- Example: `"Customer-facing e-commerce platform with React frontend"`

**domain** (required):
- Primary domain determining module selection and patterns
- Values: `web-development`, `mobile-development`, `data-science`, `devops-platform`, `gaming`, `fintech`, `healthcare`, `education`

**primary_language** (required):
- Main programming language for code generation
- Values: `typescript`, `javascript`, `python`, `java`, `kotlin`, `swift`, `rust`, `go`, `csharp`, `php`, `ruby`

**framework_stack** (optional):
- Technology stack for framework adaptation
- Format: `primary+secondary+additional` (e.g., `react+nextjs+tailwind+prisma`)
- Special value: `auto-detect` for automatic detection

**project_type** (optional):
- Type of project for appropriate patterns
- Values: `application`, `library`, `framework`, `api`, `microservice`, `monolith`, `serverless`

**team_size** (optional):
- Team size for appropriate workflow patterns
- Values: `solo`, `small` (2-5), `medium` (6-15), `large` (16+)

## 📁 Project Structure Section

### Directory Configuration

```xml
<project_structure>
  <root_directory>.</root_directory>
  <source_directory>src</source_directory>
  <test_directory>tests</test_directory>
  <docs_directory>docs</docs_directory>
  <scripts_directory>scripts</scripts_directory>
  <config_directory>config</config_directory>
  <build_directory>build</build_directory>
  <assets_directory>assets</assets_directory>
  <public_directory>public</public_directory>
</project_structure>
```

**Directory Definitions**:

**root_directory** (required):
- Project root directory (usually ".")
- Used as base for all relative paths

**source_directory** (required):
- Main source code directory
- Common values: `src`, `lib`, `app`, `source`

**test_directory** (required):
- Test files directory
- Common values: `tests`, `test`, `__tests__`, `spec`

**docs_directory** (optional):
- Documentation directory
- Common values: `docs`, `documentation`, `wiki`

**scripts_directory** (optional):
- Build and utility scripts directory
- Common values: `scripts`, `tools`, `bin`

**config_directory** (optional):
- Configuration files directory
- Common values: `config`, `configs`, `settings`

**build_directory** (optional):
- Build output directory
- Common values: `build`, `dist`, `output`, `target`

### File Patterns

```xml
<file_patterns>
  <source_files>*.{ts,tsx,js,jsx}</source_files>
  <test_files>*.{test,spec}.{ts,tsx,js,jsx}</test_files>
  <config_files>*.{json,yaml,yml,toml}</config_files>
  <documentation_files>*.{md,mdx,rst}</documentation_files>
  <ignore_patterns>node_modules,*.log,*.tmp</ignore_patterns>
</file_patterns>
```

## 🎯 Quality Standards Section

### Test Coverage Configuration

```xml
<quality_standards>
  <test_coverage>
    <threshold>90</threshold>
    <enforcement>BLOCKING</enforcement>
    <tool>jest</tool>
    <exclude_patterns>*.config.js,*.test.js</exclude_patterns>
    <minimum_functions>85</minimum_functions>
    <minimum_lines>90</minimum_lines>
    <minimum_branches>85</minimum_branches>
  </test_coverage>
</quality_standards>
```

**Test Coverage Fields**:

**threshold** (required):
- Overall coverage threshold percentage
- Range: 0-100, recommended: 85-95

**enforcement** (required):
- Enforcement level for coverage requirements
- Values: `BLOCKING`, `WARNING`, `MONITORING`

**tool** (optional):
- Coverage measurement tool
- Values: `jest`, `nyc`, `c8`, `pytest-cov`, `jacoco`, `coverage.py`

**exclude_patterns** (optional):
- File patterns to exclude from coverage
- Comma-separated glob patterns

**minimum_functions** (optional):
- Function coverage threshold
- Range: 0-100

**minimum_lines** (optional):
- Line coverage threshold
- Range: 0-100

**minimum_branches** (optional):
- Branch coverage threshold
- Range: 0-100

### Performance Standards

```xml
<performance>
  <response_time_p95>200ms</response_time_p95>
  <response_time_p99>500ms</response_time_p99>
  <memory_limit>512MB</memory_limit>
  <cpu_limit>80%</cpu_limit>
  <bundle_size_limit>1MB</bundle_size_limit>
  <lighthouse_score>90</lighthouse_score>
</performance>
```

**Performance Fields**:

**response_time_p95** (optional):
- 95th percentile response time target
- Format: number with unit (ms, s)

**response_time_p99** (optional):
- 99th percentile response time target
- Format: number with unit (ms, s)

**memory_limit** (optional):
- Maximum memory usage
- Format: number with unit (MB, GB)

**cpu_limit** (optional):
- Maximum CPU utilization percentage
- Range: 0-100

**bundle_size_limit** (optional):
- Maximum bundle size for frontend applications
- Format: number with unit (KB, MB)

**lighthouse_score** (optional):
- Minimum Lighthouse performance score
- Range: 0-100

### Code Quality Standards

```xml
<code_quality>
  <linter>eslint</linter>
  <linter_config>.eslintrc.json</linter_config>
  <formatter>prettier</formatter>
  <formatter_config>.prettierrc</formatter_config>
  <type_checker>typescript</type_checker>
  <style_guide>airbnb</style_guide>
  <complexity_limit>10</complexity_limit>
</code_quality>
```

**Code Quality Fields**:

**linter** (optional):
- Code linting tool
- Values: `eslint`, `pylint`, `rubocop`, `golint`, `clippy`

**linter_config** (optional):
- Linter configuration file path
- Relative to project root

**formatter** (optional):
- Code formatting tool
- Values: `prettier`, `black`, `gofmt`, `rustfmt`

**formatter_config** (optional):
- Formatter configuration file path
- Relative to project root

**type_checker** (optional):
- Type checking tool
- Values: `typescript`, `mypy`, `flow`, `psalm`

**style_guide** (optional):
- Code style guide standard
- Values: `airbnb`, `google`, `standard`, `pep8`

**complexity_limit** (optional):
- Maximum cyclomatic complexity
- Range: 1-20, recommended: 10

## ⚙️ Development Workflow Section

### Command Configuration

```xml
<development_workflow>
  <commands>
    <install>npm install</install>
    <test>npm test</test>
    <test_watch>npm run test:watch</test_watch>
    <test_coverage>npm run test:coverage</test_coverage>
    <lint>npm run lint</lint>
    <lint_fix>npm run lint:fix</lint_fix>
    <format>npm run format</format>
    <format_check>npm run format:check</format_check>
    <build>npm run build</build>
    <dev>npm run dev</dev>
    <start>npm start</start>
    <clean>npm run clean</clean>
  </commands>
</development_workflow>
```

**Command Fields**:

**install** (optional):
- Package installation command
- Examples: `npm install`, `pip install -r requirements.txt`, `bundle install`

**test** (required):
- Test execution command
- Examples: `npm test`, `pytest`, `go test ./...`

**test_watch** (optional):
- Watch mode test command
- Examples: `npm run test:watch`, `pytest-watch`

**test_coverage** (optional):
- Test with coverage command
- Examples: `npm run test:coverage`, `pytest --cov`

**lint** (optional):
- Code linting command
- Examples: `npm run lint`, `pylint src/`

**lint_fix** (optional):
- Automatic lint fixing command
- Examples: `npm run lint:fix`, `autopep8 --in-place`

**format** (optional):
- Code formatting command
- Examples: `npm run format`, `black .`

**build** (optional):
- Build/compilation command
- Examples: `npm run build`, `cargo build`, `go build`

### Git Workflow Configuration

```xml
<git_workflow>
  <branch_pattern>feature/*</branch_pattern>
  <commit_style>conventional</commit_style>
  <pr_template>enabled</pr_template>
  <merge_strategy>squash</merge_strategy>
  <protected_branches>main,develop</protected_branches>
  <required_status_checks>ci,security-scan</required_status_checks>
</git_workflow>
```
<!-- BROKEN EXAMPLE: Unmatched closing tag: </project_configuration> - Agent V24 validation -->

**Git Workflow Fields**:

**branch_pattern** (optional):
- Branch naming convention
- Examples: `feature/*`, `feat/*`, `feature/JIRA-*`

**commit_style** (optional):
- Commit message convention
- Values: `conventional`, `angular`, `gitmoji`, `custom`

**pr_template** (optional):
- Pull request template usage
- Values: `enabled`, `disabled`, `custom`

**merge_strategy** (optional):
- Default merge strategy
- Values: `merge`, `squash`, `rebase`

**protected_branches** (optional):
- Comma-separated list of protected branches
- Examples: `main`, `main,develop`, `master,staging,production`

**required_status_checks** (optional):
- Required CI/CD checks before merge
- Comma-separated list of check names

## 🔧 Advanced Configuration Sections

### Environment-Specific Settings

```xml
<environments>
  <development>
    <debug_mode>true</debug_mode>
    <hot_reload>true</hot_reload>
    <source_maps>true</source_maps>
    <api_endpoint>http://localhost:3000</api_endpoint>
  </development>
  
  <staging>
    <debug_mode>false</debug_mode>
    <optimization>true</optimization>
    <api_endpoint>https://api-staging.example.com</api_endpoint>
  </staging>
  
  <production>
    <debug_mode>false</debug_mode>
    <optimization>true</optimization>
    <minification>true</minification>
    <api_endpoint>https://api.example.com</api_endpoint>
  </production>
</environments>
```

### AI and Framework Behavior

```xml
<ai_behavior>
  <temperature>
    <factual>0.2</factual>
    <analysis>0.3</analysis>
    <creative>0.7</creative>
  </temperature>
  
  <thinking_patterns>
    <critical_thinking_time>30s</critical_thinking_time>
    <complexity_threshold>medium</complexity_threshold>
    <uncertainty_handling>conservative</uncertainty_handling>
  </thinking_patterns>
  
  <code_generation>
    <verbosity>detailed</verbosity>
    <comment_style>comprehensive</comment_style>
    <error_handling>robust</error_handling>
  </code_generation>
</ai_behavior>
```

### Domain-Specific Extensions

```xml
<domain_extensions>
  <web_development>
    <responsive_design>true</responsive_design>
    <accessibility_level>WCAG_AA</accessibility_level>
    <browser_support>modern</browser_support>
    <seo_optimization>true</seo_optimization>
  </web_development>
  
  <mobile_development>
    <target_platforms>ios,android</target_platforms>
    <minimum_versions>ios_14,android_24</minimum_versions>
    <performance_priority>high</performance_priority>
  </mobile_development>
  
  <data_science>
    <notebook_integration>jupyter</notebook_integration>
    <visualization_library>matplotlib</visualization_library>
    <data_validation>strict</data_validation>
  </data_science>
</domain_extensions>
```

### Security Configuration

```xml
<security>
  <scan_dependencies>true</scan_dependencies>
  <secrets_detection>true</secrets_detection>
  <vulnerability_threshold>medium</vulnerability_threshold>
  <security_headers>true</security_headers>
  <encryption_requirements>AES-256</encryption_requirements>
  
  <compliance_frameworks>
    <framework>OWASP</framework>
    <framework>PCI-DSS</framework>
    <framework>GDPR</framework>
  </compliance_frameworks>
</security>
```

## 🔗 Configuration Resolution

### Placeholder Resolution System

The framework uses `[PROJECT_CONFIG: path | DEFAULT: value]` placeholders that resolve to configuration values:

**Resolution Examples**:
```xml
<!-- Configuration -->
<test_directory>spec</test_directory>
<test_coverage><threshold>85</threshold></test_coverage>

<!-- Framework rule -->
<rule>Tests go in [PROJECT_CONFIG: test_directory | DEFAULT: tests]</rule>
<!-- Resolves to: "Tests go in spec" -->

<rule>Coverage must be ≥[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%</rule>
<!-- Resolves to: "Coverage must be ≥85%" -->
```

**Resolution Priority**:
1. **Explicit Configuration**: Value specified in PROJECT_CONFIG.xml
2. **Environment Override**: Environment-specific value if applicable
3. **Team Standard**: Value from team configuration if extends team config
4. **Default Value**: DEFAULT value from placeholder
5. **Framework Default**: Hard-coded framework default

### Configuration Inheritance

**Team Configuration Inheritance**:
```xml
<!-- PROJECT_CONFIG.xml extends team standards -->
<project_configuration version="1.0.0" extends="PROJECT_CONFIG_TEAM.xml">
  <!-- Individual overrides to team standards -->
  <quality_standards>
    <test_coverage>
      <threshold>95</threshold>  <!-- Override team standard of 90% -->
    </test_coverage>
  </quality_standards>
</project_configuration>
```

**Environment Configuration Override**:
```xml
<!-- Environment-specific overrides -->
<environments>
  <development>
    <quality_standards>
      <test_coverage>
        <enforcement>WARNING</enforcement>  <!-- Relaxed for development -->
      </test_coverage>
    </quality_standards>
  </development>
</environments>
```

## 🔍 Configuration Validation

### Validation Tools

**Configuration Validator**:
```bash
# Validate configuration file
python scripts/framework/config_validator.py --config PROJECT_CONFIG.xml

# Validate with specific schema version
python scripts/framework/config_validator.py --config PROJECT_CONFIG.xml --schema 1.0.0

# Validate team configuration inheritance
python scripts/framework/config_validator.py --config PROJECT_CONFIG.xml --base PROJECT_CONFIG_TEAM.xml
```

**Template Resolution Tester**:
```bash
# Test placeholder resolution
python scripts/framework/template_resolver.py --config PROJECT_CONFIG.xml --text "Tests go in [PROJECT_CONFIG: test_directory | DEFAULT: tests]"

# Test all placeholders in framework
python scripts/framework/template_resolver.py --config PROJECT_CONFIG.xml --test-all
```

### Validation Rules

**Required Fields**:
- `project_info.name`
- `project_info.domain`
- `project_info.primary_language`
- `project_structure.source_directory`
- `project_structure.test_directory`
- `quality_standards.test_coverage.threshold`
- `quality_standards.test_coverage.enforcement`

**Validation Constraints**:
- Threshold values must be 0-100
- Directory paths must be valid and accessible
- Command strings must be executable
- Enforcement levels must be valid enum values
- Domain must be supported domain type

**Common Validation Errors**:
```bash
# Invalid threshold
<threshold>150</threshold>  # Error: Must be 0-100

# Invalid enforcement level
<enforcement>STRICT</enforcement>  # Error: Must be BLOCKING, WARNING, or MONITORING

# Invalid domain
<domain>custom-domain</domain>  # Error: Must be supported domain type

# Missing required field
<project_info>
  <!-- Missing required 'name' field -->
  <domain>web-development</domain>
</project_info>
```

## 📊 Configuration Examples

### Web Development Project

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0">
  <project_info>
    <name>E-commerce Platform</name>
    <domain>web-development</domain>
    <primary_language>typescript</primary_language>
    <framework_stack>react+nextjs+tailwind+prisma</framework_stack>
  </project_info>
  
  <project_structure>
    <source_directory>src</source_directory>
    <test_directory>__tests__</test_directory>
  </project_structure>
  
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>BLOCKING</enforcement>
      <tool>jest</tool>
    </test_coverage>
    <performance>
      <response_time_p95>200ms</response_time_p95>
      <lighthouse_score>90</lighthouse_score>
    </performance>
  </quality_standards>
  
  <development_workflow>
    <commands>
      <test>npm test</test>
      <lint>npm run lint</lint>
      <build>npm run build</build>
    </commands>
  </development_workflow>
</project_configuration>
```

### Data Science Project

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0">
  <project_info>
    <name>ML Pipeline</name>
    <domain>data-science</domain>
    <primary_language>python</primary_language>
    <framework_stack>pandas+scikit-learn+jupyter</framework_stack>
  </project_info>
  
  <project_structure>
    <source_directory>src</source_directory>
    <test_directory>tests</test_directory>
    <docs_directory>notebooks</docs_directory>
  </project_structure>
  
  <quality_standards>
    <test_coverage>
      <threshold>85</threshold>
      <enforcement>WARNING</enforcement>
      <tool>pytest-cov</tool>
    </test_coverage>
  </quality_standards>
  
  <development_workflow>
    <commands>
      <test>pytest</test>
      <lint>pylint src/</lint>
      <format>black .</format>
    </commands>
  </development_workflow>
  
  <domain_extensions>
    <data_science>
      <notebook_integration>jupyter</notebook_integration>
      <visualization_library>matplotlib</visualization_library>
      <data_validation>strict</data_validation>
    </data_science>
  </domain_extensions>
</project_configuration>
```

---

**Need help with configuration?** Use `/query "analyze my PROJECT_CONFIG.xml configuration"` for framework analysis of your current setup.

**Want examples for your domain?** Check the `examples/project-configs/` directory for domain-specific templates.